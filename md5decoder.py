#   Author : p1kxel
#   MD5 Multiple Decrypter
from hashlib import md5
import sys

check_argv = False


if len(sys.argv) == 3:
    check_argv = True
else:
    print(f'Usage : {sys.argv[0]} hash.txt wordlist.txt ')
    exit(0)

def decoder(hashfile,wordlist):
    try:
        with open(hashfile,"r") as hashf:
            for hashlines in hashf:
                hashline = hashlines.rstrip().encode("utf-8")
                with open(wordlist,"r") as wordf:
                    for wordlines in wordf:
                        wordline = wordlines.rstrip().encode("utf-8")
                        if hashline.decode("utf-8") == md5(wordline).hexdigest():
                            print(f'[+] Hash founed : {hashline.decode("utf-8")} => {wordline.decode("utf-8")} ')
    except Exception as e:
        print(e)
        exit(0)

if check_argv == True:
    decoder(sys.argv[1],sys.argv[2])
