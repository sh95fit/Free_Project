import array
import hashlib

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode


def adjust_iv_size(iv):
    if len(iv) < 16:
        # IV가 16바이트 미만인 경우 나머지 부분을 0으로 채움
        adjusted_iv = iv.ljust(16, b'\0')
    elif len(iv) > 16:
        # IV가 16바이트보다 긴 경우 처음 16바이트만 사용
        adjusted_iv = iv[:16]
    else:
        # 이미 16바이트인 경우 그대로 사용
        adjusted_iv = iv

    return adjusted_iv

# def resize_array(arr, new_size):
#     if len(arr) < new_size:
#         # 배열이 작을 경우 나머지 부분을 0으로 채워서 크기를 조절합니다.
#         return arr.ljust(new_size, b'\0')
#     elif len(arr) > new_size:
#         # 배열이 클 경우 처음부터 new_size까지만 사용합니다.
#         return arr[:new_size]
#     else:
#         # 이미 원하는 크기일 경우 그대로 반환합니다.
#         return arr


def get_hash_keys(key):
    enc = 'utf-8'
    sha2 = hashlib.sha256()

    raw_key = key.encode(enc)
    raw_iv = key.encode(enc)

    sha2.update(raw_key)
    hash_key = sha2.digest()

    sha2.update(raw_iv)
    hash_iv = sha2.digest()

    adjusted_iv = adjust_iv_size(hash_iv)
    # adjusted_iv = resize_array(hash_iv,16)

    return hash_key, adjusted_iv


def encrypt_string_to_bytes_aes(plain_text, key, iv):
    if plain_text is None or len(plain_text) <= 0:
        raise ValueError("plain_text cannot be null or empty")
    if key is None or len(key) <= 0:
        raise ValueError("Key cannot be null or empty")
    if iv is None or len(iv) <= 0:
        raise ValueError("IV cannot be null or empty")

    plain_text_bytes = plain_text.encode('utf-8')

    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv),
                    backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_bytes = encryptor.update(plain_text_bytes) + encryptor.finalize()

    return b64encode(encrypted_bytes).decode('utf-8')
