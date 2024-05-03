BitcoinKeyBalanceChecker is a Python project that generates Bitcoin private keys and checks their corresponding addresses for balances on the Bitcoin blockchain. generate_private_keys.py and check_balance.py.

generate_private_keys.py: This script generates a specified number of random Bitcoin private keys using cryptographic-strength randomization and writes them to a text file named keys.txt.
check_balance.py: This script reads the private keys from the keys.txt file, derives the corresponding Bitcoin addresses, and queries the blockchain to check their balances. If a non-zero balance is found, it displays a pop-up window indicating the address associated with the private key.
The project aims to provide a simple tool for users to generate Bitcoin private keys and verify the balances associated with them, enhancing their understanding of Bitcoin and blockchain technology.

I plan to move this project to Assembly language for faster speed and more control over CPU and GPU memory.

Probability of gussing the genesis Block private keys is 1.1579209×10e-77

Chances of guessing a private key if a billion keys are checked per second: 3.67×10e60 years.

Chanced of guessing a private key if used a 442 petaFLOPS super computer: 5.797786825×10 −16seconds


Since finding collision on the SHA256 functions is harder. It makes the problem much easier if we followed the secp256k1 elliptic curve
