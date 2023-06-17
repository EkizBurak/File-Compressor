import os
import argparse
import subprocess
#Adem
parser = argparse.ArgumentParser()
parser.add_argument("--path","-p" ,required=True, help="Please Entry file loacation")
parser.add_argument("--winrar", "-w", required=True, help="Entry winrar.exe path")
parser.add_argument("--remove","-r" ,required=False, help="If you want it to delete files after compression --remove 1")
parser.add_argument("--exception", "-e", required=False, help="If there is a type in your files that you do not want to compress, you can use this parameter")
parser.add_argument("--targetpath", "-t", required=False, help="the path where you want the compressed files to be saved.")
parser.add_argument("--filesize", "-s", required=False, help="If you want to split by GB while your files are compressed, you can use the --filesize parameter.")
args = parser.parse_args()

location_PATH = args.path
file_size = f"{args.filesize}M"
exceptionFileType = str(args.exception).split(",")
target_PATH = args.targetpath
winrar_PATH = args.winrar

print(exceptionFileType)

if args.path[-1] != "\\":
    location_PATH = args.path + "\\"

if target_PATH == None or target_PATH == "":
    target_PATH = location_PATH

else:
    if args.targetpath[-1] != "\\":
        target_PATH = args.targetpath + "\\"

for i in os.listdir(location_PATH):
    status = True
    for x in exceptionFileType:
        if x in i:
            status = False
    if status == True:
        
        command = [
            winrar_PATH,
            'a', '-r', '-ep']
        if file_size != None or file_size == "M" or file_size == "":
            command.append('-v90M')
        
        command.append(target_PATH + str(i).split(".")[0] + ".rar")
        command.append(location_PATH + i)        

        subprocess.run(command, shell=True)

        if args.remove == "1":
            try:
                os.remove(location_PATH + i)
            except BaseException as err:
                print(err)
