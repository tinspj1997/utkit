from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

from typing import NewType
import secrets


FernetKey = NewType("FernetKey", bytes)


async def generate_fernet_key() -> FernetKey:
    return Fernet.generate_key()


async def encrypt(content: str, fernet_key: FernetKey) -> str:
    if not isinstance(content, str):
        raise ValueError("content must by str format")
    try:
        fernet = Fernet(fernet_key)
        encrypted_content = fernet.encrypt(content.encode())
        return encrypted_content.decode("utf-8")
    except Exception as e:
        raise ValueError("Encryption failed.") from e


def decrypt(content: str, fernet_key: FernetKey) -> str:
    if not isinstance(content, str):
        raise ValueError("content must by str format")
    try:
        fernet = Fernet(fernet_key)
        return fernet.decrypt(bytes(content, "utf-8")).decode()
    except InvalidToken:
        raise ValueError("Decryption failed. Invalid key or corrupted data.")


def generate_rsa_keys(
    key_size=2048, private_key_path="private_key.pem", public_key_path="public_key.pem"
):
    # Generate private key

    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=int(key_size), backend=default_backend()
    )

    # Generate public key from private key
    public_key = private_key.public_key()

    # Serialize private key to PEM format
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    # Serialize public key to PEM format
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    # Save keys to files
    # private_key_path = 'private_key.pem'
    # public_key_path = 'public_key.pem'

    with open(private_key_path, "wb") as f:
        f.write(private_pem)

    with open(public_key_path, "wb") as f:
        f.write(public_pem)

    print("Keys generated successfully!")
    print(f"Private key saved to: {private_key_path}")
    print(f"Public key saved to: {public_key_path}")

    return private_key_path, public_key_path


def load_rsa_public_key(public_key_path):
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(), backend=default_backend()
        )
    return public_key


def load_rsa_private_key(private_key_path):
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend()
        )
    return private_key


def encrypt_rsa_content(content, public_key_path):
    # Convert string to bytes if necessary
    if isinstance(content, str):
        content = content.encode("utf-8")

    # Load public key
    public_key = load_rsa_public_key(public_key_path)

    # Encrypt the content
    encrypted = public_key.encrypt(
        content,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return encrypted


def decrypt_rsa_content(encrypted_content, private_key_path):
    # Load private key
    private_key = load_rsa_private_key(private_key_path)

    # Decrypt the content
    decrypted = private_key.decrypt(
        encrypted_content,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return decrypted.decode("utf-8")


def generate_secret_key(byte_length: int = 32) -> str:
    return secrets.token_hex(byte_length)