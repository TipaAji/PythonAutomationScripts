import os, shutil, easygui

PATH = r"C:/Users/tipaa/Downloads/"

folderNames = ["Images", "ZIPs", "EXEs", "PDFs", "Text"]

for folder in folderNames:
    if not os.path.exists(PATH +folder):
        os.makedirs(PATH + folder)

files = os.listdir(PATH)
notAllMoved = True

for file in files:
    if ".exe" in file and not os.path.exists(PATH + "EXEs/" + file):
        shutil.move(PATH + file, PATH + "EXEs/" + file)

    elif ".png" in file or ".jpg" in file or ".JPG" in file or ".webp" in file and not os.path.exists(PATH + "Images/" + file):
        shutil.move(PATH + file, PATH + "Images/" + file)

    elif ".zip" in file and not os.path.exists(PATH + "ZIPs/" + file):
        shutil.move(PATH + file, PATH + "ZIPs/" + file)

    elif ".docx" in file or ".txt" in file and not os.path.exists(PATH + "Text/" + file):
        shutil.move(PATH + file, PATH + "Text/" + file)

    elif ".pdf" in file and not os.path.exists(PATH + "PDFs/" + file):
        shutil.move(PATH + file, PATH + "PDFs/" + file)

    else:
        notAllMoved = False

if not notAllMoved:
    easygui.msgbox("Not all files were moved.")