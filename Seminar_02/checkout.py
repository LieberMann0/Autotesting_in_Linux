import subprocess
from zlib import crc32


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def calc_crc32(data, value):
    hash_crc = crc32(b'path_arch')
    return hash_crc
    