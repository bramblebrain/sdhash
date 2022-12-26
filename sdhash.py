# cd to your model local repository
import os as os
import sys
os.getcwd()

ckpt_hashes = {}
other_hashes = {}
file_max_bytes = 500000000

def model_hash(pathed_filename): 
    import hashlib as hashlib
    m = hashlib.sha256()   
    file_split = os.path.splitext(pathed_filename)
    file_size = os.path.getsize(pathed_filename)
    file_name = os.path.basename(pathed_filename)
    file_ext = file_split[1]
    
    try:
        with open(pathed_filename, "rb") as file:
            # calculate full hash of non-model file if less than 500 and not a model file.
            if file_size < file_max_bytes and file_ext != ".ckpt" and file_ext != ".safetensors":
                buf = file.read(8192)
                while len(buf)> 0:
                    m.update(buf)
                    buf = file.read(8192)
                hash = m.hexdigest()[0:8]
                if hash in other_hashes.keys():
                    # duplicates
                    hash2 = hash + "+"
                    if hash2 in other_hashes.keys():
                        other_hashes[hash2] = other_hashes[hash2] + ", " + file_name
                    else:
                        other_hashes[hash + "+"] = file_name
                else:
                    # duplicate
                    other_hashes[hash] = file_name
            else:
                if file_size < file_max_bytes:
                    print("!" + file_name + " may be corrupt.")
                # calculate hash segment of model
                file.seek(0x100000)
                m.update(file.read(0x10000))
                hash = m.hexdigest()[0:8]
                
                if hash in ckpt_hashes.keys():
                    # duplicates
                    hash2 = hash + "+"
                    if hash2 in ckpt_hashes.keys():
                        ckpt_hashes[hash2] = ckpt_hashes[hash2] + ", " + file_name
                    else:
                        ckpt_hashes[hash + "+"] = file_name
                else:
                    # duplicate
                    ckpt_hashes[hash] = file_name
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
    try:
        with open('hashes.txt', 'w') as file:
            print("\n# Model Hashes")
            file.write("# Model Hashes\n")
            
            for hash in ckpt_hashes:
                output = "[" + hash + "] " + ckpt_hashes[hash]
                print(output)
                # write hashes to file
                file.write(output + "\n")
                
            print("\n# Other Hashes")
            file.write("\n# Other Hashes\n")
            
            for hash in other_hashes:
                output = "<" + hash + "> " + other_hashes[hash]
                print(output)
                # write hashes to file
                file.write(output + "\n")             
    except FileNotFoundError:
        print("error")
        
file.close()