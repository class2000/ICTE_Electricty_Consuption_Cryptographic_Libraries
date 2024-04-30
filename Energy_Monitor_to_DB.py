from datetime import datetime, timezone
import sys
import subprocess
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Configuration for InfluxDB connection
token = "" #Fill with token
org = "" #Fill with org name
bucket = "" #Fill with bucket name
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Powermetrics process for CPU power
process = subprocess.Popen("/usr/bin/powermetrics -i 300 --samplers cpu_power -a --hide-cpu-duty-cycle", 
                           shell=True, stdout=subprocess.PIPE, bufsize=3)

while True:
    out = process.stdout.readline().decode()
    if out == '' and process.poll() is not None:
        break
    if out != '':
        if 'Combined Power' in out:
            # Handling combined power metrics
            metric, value = out.split(': ')
            power_value = int(value.replace(' mW', ''))
            point = Point("Combined Power") \
                .tag("host", "host1") \
                .field("power", power_value) \
                .time(datetime.now(timezone.utc), WritePrecision.NS)
            write_api.write(bucket, org, point)
        elif ' Power: ' in out:
            # Handling individual component power metrics
            metrics = out.split(' Power: ')
            point = Point(metrics[0]) \
                .tag("host", "host1") \
                .field("power", int(metrics[1].replace('mW', ''))) \
                .time(datetime.now(timezone.utc), WritePrecision.NS)
            write_api.write(bucket, org, point)

        sys.stdout.flush()

with subprocess.Popen("/usr/bin/powermetrics -i 300 --samplers cpu_power -a --hide-cpu-duty-cycle | grep -B 2 'GPU Power'", 
                      shell=True, stdout=subprocess.PIPE, bufsize=3) as p:
    for c in iter(lambda: p.stdout.readline(), b''):
        sys.stdout.write(c)
    for line in p.stdout.read():
        metrics = line.split(' Power: ')
        print(line)