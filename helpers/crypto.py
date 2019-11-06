from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import codecs
import os


# generate a new password
def generate_password():
    randomness = os.urandom(64)
    return codecs.encode(randomness, 'base64').decode()


# generate a private key
def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )


# generate private key pem
def generate_private_pem(private_key, password):
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password=password)
    )


# loads private key from a private_pem
def load_private_key(private_pem, password):
    return serialization.load_pem_private_key(
        private_pem,
        password=password,
        backend=default_backend()
    )


# generate a private pem string
def generate_private_pem_string(private_key, password):
    private_pem = generate_private_pem(private_key, password.encode('utf-8'))
    return private_pem.decode()


# generate public key
def generate_public_key(private_key):
    return private_key.public_key()


# generate public pem
def generate_public_pem(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


# load public key from public pem
def load_public_key(public_pem):
    return serialization.load_pem_public_key(
        public_pem,
        backend=default_backend()
    )


# generate a string for the public pem
def generate_public_pem_string(private_pem_string, password):
    private_key = load_private_key(
        private_pem_string.encode('utf-8'),
        password.encode('utf-8')
    )
    public_key = generate_public_key(private_key)
    return generate_private_pem(private_key).decode()


# sign a message
def sign(private_pem_string, password, message):
    private_key = load_private_key(
        private_pem_string.encode('utf-8'),
        password.encode('utf-8')
    )
    signature = sign_binary(private_key, message.encode('utf-8'))
    return codecs.encode(signature, 'base64').decode()


# verify a signature
def verify_signature(public_pem_string, signature, message):
    public_key = load_public_key(public_pem_string.encode('utf-8'))
    signature_binary = codecs.decode(signature.encode('utf-8'), 'base64')
    return verify_binary(public_key, signature_binary, message.encode('utf-8'))


def sign_binary(private_key, message_binary):
    type(message_binary)
    signature = private_key.sign(
        message_binary,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA3_256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA3_256()
    )
    return signature


def verify_binary(public_key, signature, message_binary):
    try:
        verify = public_key.verify(
            signature,
            message_binary,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA3_256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA3_256()
        )
    except InvalidSignature:
        return False
    return True
