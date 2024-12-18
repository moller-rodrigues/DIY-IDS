# Author: Moller.R 
# Email: greenorange103@gmail.com
# hash_funcs.py - returns the hash of the specified filename and given hash format.

import argparse
import hashlib

parser = argparse.ArgumentParser(description='Get the hash of a file Hash formats: md5, sha1, sha224, sha256, sha384, sha512')
parser.add_argument('-ft','--format', type=str, help='Hash type/format')
parser.add_argument('-f','--filename', type=str, help='path of file to hash')
args = parser.parse_args()

def md5(fname):
    hash_md5 = hashlib.md5()
    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except:
        return
    return hash_md5.hexdigest()

def sha1(fname):
    hash_md5 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha224(fname):
    hash_md5 = hashlib.sha224()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha256(fname):
    hash_md5 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha384(fname):
    hash_md5 = hashlib.sha384()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha512(fname):
    hash_md5 = hashlib.sha512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


if __name__ == '__main__':
    try:
        print(str(args.filename + " " + args.format + " hash: " + locals()[args.format](args.filename)))
    except:
        print("Please specify valid filename and hash format!")
