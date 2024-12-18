import string
import argparse

parser = argparse.ArgumentParser(description='Unix strings implementation in Python for Windows')
parser.add_argument('-m','--min', type=int, help='min number of characters in a distinguisable word')
parser.add_argument('-f','--filename', type=str, help='path of file')
args = parser.parse_args()



def strings(filename, min):
    with open(filename, errors="ignore") as f:  # Python 3.x          
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
        if len(result) >= min:  # catch result at EOF
            yield result

if __name__ == '__main__':
    strings_list = strings(args.filename, args.min)
    
    for s in strings_list:
        print(s)