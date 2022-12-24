# cd to your model local repository
import os as os
import sys
import re
os.getcwd()
hash_list = {}

def model_hash(pathed_filename):
    try:
        with open(pathed_filename, "rb") as file:
            import hashlib as hashlib
            m = hashlib.sha256()
            file.seek(0x100000)
            m.update(file.read(0x10000))
            hash = m.hexdigest()[0:8]
            filename = os.path.basename(pathed_filename)
            
            if hash in hash_list.keys():
                # duplicates
                hash2 = hash + "+"
                if hash2 in hash_list.keys():
                    hash_list[hash2] = hash_list[hash2] + ", " + filename
                else:
                    hash_list[hash + "+"] = filename
            else:
                # duplicate
                hash_list[hash] = filename
        return 1
    except FileNotFoundError:
        print('NOFILE')
        return 0

args = len(sys.argv)

if(args < 2):
    print("Explorer: Drag and Drop files onto sdhash.bat")
    print("CMD: sdhash.bat model1, model2, etc...")
else:
    # process files
    for arg in range(len(sys.argv)):
        if(arg == 0):
            continue    
        model_hash(sys.argv[arg])

    # print hashes and write
    file = open(r"hashes.txt", "w")
    for hash in hash_list:
        output = "[" + hash + "] " + hash_list[hash]
        print(output)
        # write hashes to file
        file.write(output + "\n")
        
file.close()