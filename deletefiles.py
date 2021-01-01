import os
import shutil

os.chdir('D:\Desktop Backup Dec 20 2020')
print(f'we are in: {os.getcwd()}')

items=os.listdir()
print(f'items on list: {items}')

os.chdir(r'C:\Users\nabee\Desktop')
print(f'we are in: {os.getcwd()}')

for i in items:
    if os.path.isdir(i):
        print(f'{i} is a path')
        # removedirs(i)
        shutil.rmtree(i)
        print(f'{i} has been successfully deleted')
    elif os.path.isfile(i):
        # os.remove(i)
        print(f'{i} is a file')