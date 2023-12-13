import os
from AES_Utils import get_hash_keys, encrypt_string_to_bytes_aes
from dotenv import load_dotenv

# .env 파일 업로드
load_dotenv()

# 환경 변수 사용
key = os.getenv("key")

hash_keys = get_hash_keys(key)

print("Hash Key : ", hash_keys[0])
print("Hash IV : ", hash_keys[1])


plain_text = input()

encrypt_text = encrypt_string_to_bytes_aes(
    plain_text, hash_keys[0], hash_keys[1])

print(encrypt_text)
