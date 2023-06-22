from os import system,listdir
from argparse import ArgumentParser
from subprocess import run, call
import ctypes
try:
    try:
        parser = ArgumentParser()
        parser.add_argument("--path","-p" ,required=True, help="Please Entry file loacation")
        parser.add_argument("--winrar", "-w", required=True, help="Entry winrar.exe path")
        parser.add_argument("--remove","-r" ,required=False, help="If you want it to delete files after compression --remove 1")
        parser.add_argument("--exception", "-e", required=False, help="If there is a type in your files that you do not want to compress, you can use this parameter")
        parser.add_argument("--targetpath", "-t", required=False, help="the path where you want the compressed files to be saved.")
        parser.add_argument("--filesize", "-s", required=False, help="If you want to split by GB while your files are compressed, you can use the --filesize parameter.")
        args = parser.parse_args()

    except BaseException as err:
        ICON_STOP = 0x00000010
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(0, err, "Error", 0 | ICON_STOP)

    file_size = f"{args.filesize}M"
    exceptionFileType = str(args.exception).split(",")
    target_PATH = args.targetpath
    winrar_PATH = args.winrar

    if args.path[-1] != "\\":
        location_PATH = args.path + "\\"

    if target_PATH == None or target_PATH == "":
        target_PATH = location_PATH

    else:
        if args.targetpath[-1] != "\\":
            target_PATH = args.targetpath + "\\"
    
    for i in listdir(location_PATH):
        status = True
        for x in exceptionFileType:
            print(x)
            print(i)
            if x in i and x != "":
                status = False
                
        if status == True:
            command = [
                winrar_PATH,
                'a', '-r', '-ep']
            if file_size != None or file_size == "M" or file_size == "":
                command.append(f'-v{file_size}M')
            
            command.append(target_PATH + str(i).split(".")[0] + ".rar")
            command.append(location_PATH + i)        

            run(command, shell=True)

            if args.remove == "1":
                try:
                    #remove(location_PATH + i)
                    system("del " + location_PATH + i)
                except BaseException as err:
                    print(err)
                    ICON_STOP = 0x00000010
                    MessageBox = ctypes.windll.user32.MessageBoxW
                    MessageBox(0, err, "Başlık", 0 | ICON_STOP)
                    
except BaseException as err:
    ICON_STOP = 0x00000010
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(0, err, "Error", 0 | ICON_STOP)
    