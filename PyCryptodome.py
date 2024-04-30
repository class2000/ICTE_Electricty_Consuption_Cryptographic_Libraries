from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from datetime import datetime, timedelta
import csv

def aes_encrypt(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return base64.b64encode(ciphertext).decode()

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext_bytes = base64.b64decode(ciphertext)
    decrypted_padded = cipher.decrypt(ciphertext_bytes)
    decrypted = unpad(decrypted_padded, AES.block_size)
    return decrypted.decode()

# Test parameters
plaintext = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ut malesuada urna. 1234567890 !@#$%^&*()_+-=[]{}|;:',.<>?/`~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
key = b'This is a key123'  # Convert key to bytes
iv = b'This is an IV456'  # Convert IV to bytes

# Run for 5 minutes
duration = 7200  # 2 hours in seconds
start_time = datetime.now()
end_time = start_time + timedelta(seconds=duration)

# Initialize counters
encryption_count = 0
decryption_count = 0

# Run encryption and decryption for 5 minutes
while datetime.now() < end_time:
    ciphertext = aes_encrypt(plaintext, key, iv)
    decrypted = aes_decrypt(ciphertext, key, iv)
    encryption_count += 1
    decryption_count += 1
    
# Calculate start and end dates
start_date = start_time.strftime("%Y-%m-%d %H:%M:%S")
end_date = end_time.strftime("%Y-%m-%d %H:%M:%S")

# Export results to CSV
csv_file = "encryption_results_pycryptodome.csv"
csv_columns = ['Start Date', 'End Date', 'Total Encryption Count', 'Total Decryption Count']

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerow({'Start Date': start_date, 'End Date': end_date, 'Total Encryption Count': encryption_count, 'Total Decryption Count': decryption_count})
except IOError:
    print("I/O error")

print("Test completed.")
