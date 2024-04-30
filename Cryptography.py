from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from datetime import datetime, timedelta
import csv

def aes_encrypt(message, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message + b"\0" * (algorithms.AES.block_size - len(message) % algorithms.AES.block_size)
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode()

def aes_decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()
    return decrypted_padded.rstrip(b"\0").decode()

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
csv_file = "encryption_results_cryptography.csv"
csv_columns = ['Start Date', 'End Date', 'Total Encryption Count', 'Total Decryption Count']

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerow({'Start Date': start_date, 'End Date': end_date, 'Total Encryption Count': encryption_count, 'Total Decryption Count': decryption_count})
except IOError:
    print("I/O error")

print("Test completed.")
