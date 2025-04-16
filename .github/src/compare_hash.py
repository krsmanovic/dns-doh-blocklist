import hashlib
import os.path

def get_sha256_hash(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

if __name__ == '__main__':
    path_tmp = './doh_tmp.txt'
    path_hash = '../../hash'
    github_env_file = os.getenv('GITHUB_OUTPUT', 'WAS_EMPTY=true\n')
    temp_exists = os.path.isfile(path_tmp)
    hash_exists = os.path.isfile(path_hash)
    if temp_exists:
        hash_temp = get_sha256_hash(path_tmp)
        with open(github_env_file, "a") as ghe:
            print("HASH_TEMP=" + hash_temp)
            ghe.write("HASH_TEMP=" + hash_temp + "\n")
    else:
        sys.exit('Error: temporary file "doh_tmp.txt" does not exist.')
    if hash_exists:
        with open(path_hash, 'r') as file:
            hash_existing = file.read()
            print("HASH_EXISTING=" + hash_existing)
            with open(github_env_file, "a") as ghe:
                ghe.write("HASH_EXISTING=" + hash_existing + "\n")
        if hash_existing == hash_temp:
            print("Old and new hash match. No need to run update.")
            with open(github_env_file, "a") as ghe:
                ghe.write("REQUIRES_UPDATE=false\n")
        else:
            print("New hash match does not match old one. Runnning update...")
            with open(github_env_file, "a") as ghe:
                ghe.write("REQUIRES_UPDATE=true\n")
    else:
        print("Old hash does not exist. Runnning update...")
        with open(github_env_file, "a") as ghe:
            ghe.write("REQUIRES_UPDATE=true\n")
