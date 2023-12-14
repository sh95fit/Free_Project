import os
from AES_Utils import get_hash_keys, encrypt_string_to_bytes_aes, encrypt_string_to_bytes_aes_1, encrypt_string_to_bytes_aes_2, encrypt_string_to_bytes_aes_3, encrypt_string_to_bytes_aes_4, encrypt_string_to_bytes_aes_5
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

encrypt_text2 = encrypt_string_to_bytes_aes_1(
    plain_text, hash_keys[0], hash_keys[1])

encrypt_text3 = encrypt_string_to_bytes_aes_2(
    plain_text, hash_keys[0], hash_keys[1])

encrypt_text4 = encrypt_string_to_bytes_aes_3(
    plain_text, hash_keys[0], hash_keys[1])

encrypt_text5 = encrypt_string_to_bytes_aes_4(
    plain_text, hash_keys[0], hash_keys[1])

encrypt_text6 = encrypt_string_to_bytes_aes_5(
    plain_text, hash_keys[0], hash_keys[1])

print(encrypt_text, "\n", encrypt_text2, "\n",
      encrypt_text3, "\n", encrypt_text4, "\n", encrypt_text5, "\n", encrypt_text6)
