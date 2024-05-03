import requests
import binascii
from hashlib import sha256
import tkinter as tk
from tkinter import messagebox

def generate_address_from_private_key(private_key):
    # Derive the corresponding Bitcoin address from the private key
    # This requires additional cryptographic operations
    # This is a simplified version, actual derivation requires more steps
    # Replace this with your actual address derivation method
    public_key = binascii.hexlify(sha256(private_key).digest()).decode()
    address = public_key[:34]  # Dummy address, replace with actual derivation
    return address

def check_balance(address):
    url = f"https://blockchain.info/rawaddr/{address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('final_balance', 0) / 100000000  # Convert satoshis to BTC
        else:
            print(f"Failed to retrieve balance for address: {address}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return 0

def read_private_keys():
    with open("keys.txt", "r") as file:
        private_keys = [bytes.fromhex(line.strip()) for line in file if line.strip()]
    return private_keys

def show_message(private_key):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Address Found", f"Address Found on {private_key}")

def main():
    private_keys = read_private_keys()

    for i, private_key in enumerate(private_keys, start=1):
        address = generate_address_from_private_key(private_key)
        balance = check_balance(address)
        print(f"Balance for Private Key {i}: {balance} BTC")
        
        if balance != 0:
            show_message(private_key.hex())

if __name__ == "__main__":
    main()
