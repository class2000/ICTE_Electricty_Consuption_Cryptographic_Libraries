import nacl.secret
import nacl.utils
import base64
from datetime import datetime, timedelta
import csv

def nacl_encrypt(message, key):
    box = nacl.secret.SecretBox(key)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    ciphertext = box.encrypt(message, nonce)
    return base64.b64encode(ciphertext).decode()

def nacl_decrypt(ciphertext, key):
    box = nacl.secret.SecretBox(key)
    decrypted = box.decrypt(base64.b64decode(ciphertext))
    return decrypted.decode()

# Test parameters
plaintext = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ut malesuada urna. 1234567890 !@#$%^&*()_+-=[]{}|;:',.<>?/`~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# Run for 5 minutes
duration = 7200  # 2 hours in seconds
start_time = datetime.now()
end_time = start_time + timedelta(seconds=duration)

# Initialize counters
encryption_count = 0
decryption_count = 0

# Run encryption and decryption for 5 minutes
while datetime.now() < end_time:
    ciphertext = nacl_encrypt(plaintext, key)
    decrypted = nacl_decrypt(ciphertext, key)
    encryption_count += 1
    decryption_count += 1

# Calculate start and end dates
start_date = start_time.strftime("%Y-%m-%d %H:%M:%S")
end_date = end_time.strftime("%Y-%m-%d %H:%M:%S")

# Export results to CSV
csv_file = "encryption_results_pynacl.csv"
csv_columns = ['Start Date', 'End Date', 'Total Encryption Count', 'Total Decryption Count']
csv_data = [{'Start Date': start_date, 'End Date': end_date, 'Total Encryption Count': encryption_count, 'Total Decryption Count': decryption_count}]

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in csv_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

print("Test completed.")
