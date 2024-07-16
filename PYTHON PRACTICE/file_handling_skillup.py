from os import path
def create_file(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write('welcome in python')
        f.close()

dest='C:\\Users\\mhava\\OneDrive\\Desktop\\PYTHON PRACTICE\\sample.txt'
create_file(dest)
print('file is created')