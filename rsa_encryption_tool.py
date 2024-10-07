import random
from sympy import isprime, gcd

def generate_prime_candidate(length):
    """Generate an odd prime candidate."""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1  # Ensure it's odd and the right bit length
    return p

def generate_prime_number(length):
    """Generate a prime number of the specified bit length."""
    p = 4  # Not prime
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keypair(bits):
    """Generate a public and private key pair."""
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # Common choice for e
    # Calculate d
    d = pow(e, -1, phi)

    return ((e, n), (d, n))  # Public and private keys

def encrypt(public_key, plaintext):
    """Encrypt the plaintext with the public key."""
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext with the private key."""
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

def main():
    bits = 8  # You can increase this for stronger encryption
    public_key, private_key = generate_keypair(bits)

    message = "Hello"
    print(f"Original Message: {message}")

    # Encrypt the message
    ciphertext = encrypt(public_key, message)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the message
    decrypted_message = decrypt(private_key, ciphertext)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
