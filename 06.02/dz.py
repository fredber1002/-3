import os

path = "C:/Users/Users/Downloads"

os.mkdir(path + "/Images")
os.mkdir(path + "/Documents")
os.mkdir(path + "/Archives")
os.mkdir(path + "/Other")

files = os.listdir(path)

for file in files:
    full_path = path + "/" + file

    if os.path.isfile(full_path):

        if file.endswith(".jpg") or file.endswith(".png"):
            os.rename(full_path, path + "/Images/" + file)
        elif file.endswith(".pdf") or file.endswith(".docx"):
            os.rename(full_path, path + "/Documents/" + file)
        elif file.endswith(".zip"):
            os.rename(full_path, path + "/Archives/" + file)
        else:
            os.rename(full_path, path + "/Other/" + file)
