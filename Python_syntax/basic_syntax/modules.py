import os

# path of the directory to list down its contents 
dir_path='C:\Users\pandy\OneDrive\Desktop\sdl_project\python_SDL_tutorial\Python_syntax'

#function to list the directory contents 
contents=os.listdir(dir_path)

# print each file name and the directory name 
for item in contents:
    print(item)