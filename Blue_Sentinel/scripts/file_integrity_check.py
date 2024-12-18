from hash_funcs import *

def main(hash_type, valid_hash, path):
    try:
        if globals()[hash_type](path) == valid_hash:
            return True
        else:
            return False
    except:
        return False

#test
#print(main("md5", "54b0c58c7ce9f2a8b551351102ee0938", "C:\\Users\\mar71\\Google Drive\\CISS\\test.txt"))