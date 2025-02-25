import hashlib

user_hash_dict = {}

with open('password.txt', 'r') as f:
    passwords = f.read().splitlines()

with open('username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]

        user_hash_dict[username] = hash

for passwd in passwords:
    hashed_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dict.items():
        if hashed_passwd == hash:
            print(f"HASH FOUND\n{username}:{passwd}")




