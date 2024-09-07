#--------------------- Imports -----------------------
import os
from os import listdir
from os.path import isfile, join

#---------------------  List all files from Desktop Directory -----------------------
def locatefiles(mypath):

    if os.path.exists(mypath):
        print(f"The location '{mypath}' exists")
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  
    else:
        print(f"{mypath} location doesn't exist")
        
    return onlyfiles


    

#---------------------  List all folders from Desktop Directory -----------------------
def locatefolders(mypath):

    if os.path.exists(mypath):
        print(f"The location '{mypath}' exists")
        onlyfolders = [d for d in listdir(mypath) if os.path.isdir(join(mypath, d))]
        
    else:
        print(f"{mypath} location doesn't exist")

    return onlyfolders


    


#---------------------  Create New Folder To Place All Files in -----------------------
def createFolder(mypath):
    newpath = f"{mypath}\\All_Files"

    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print(f"{newpath} created successfully!")
    else:
        print(f"Folder already exist")
        
    return newpath
    
#---------------------  Move Existing Folders To All Files Folder -----------------------



def moveFolder(onlyfolders,newpath):
    
    count1 = 0
    total_folders = 0
    remove_All_FilesFolder = onlyfolders.remove("All_Files")
    
    
    if remove_All_FilesFolder == None:
        
        for folder in onlyfolders:
            
            count1 += 1
            total_folders += 1
            
            
            movefolder = f"{mypath}\\{folder}"
            # print(f"Src: {movefolder}")
            destination = f"{newpath}\\{folder}"
            # print(f"Destination: {destination}")
            
            
            
            try:
                if os.path.isdir(destination):
                        print(f"This folder already exisit")
                else:
                        os.replace(movefolder ,destination)
                        print(f"{movefolder} was moved")
            except FileNotFoundError:
                    print(f"{movefolder} was not found")

        return total_folders, print(f"Total folders moved: {total_folders}")
#---------------------  Create New Folder with File Extension and Move File to src destination -----------------------


def movefile(newpath,onlyfiles):
    
    count2 = 0
    total_files = 0
    

    
    for file in onlyfiles:
        
        count2 += 1
        total_files += 1
        
        #split Filename and Extension
        index = file.index(".")
        filename = file[:index]
        file_ext = file[index + 1:]
        print(f"Filename: {filename} \nFile Extention: {file_ext}")
        
        
        #create new folder with File Extension and move File to src destination
        new_folderpath = f"{newpath}\\{file_ext.upper()}"
        if not os.path.exists(new_folderpath):
            os.makedirs(new_folderpath)
            print(f"{new_folderpath} created successfully!")
        # else:
        #     print(f"Folder already exist ")
            
        # move file to destination folder
        if file_ext == file_ext:
            movefile = f"{mypath}\\{file}"
            # print(f"Src: {movefile}")
            destination = f"{new_folderpath}\\{file}"
            # print(f"Destination: {destination}")
            
            try:
                if os.path.exists(destination):
                    print(f"There is already a file there")
                else:
                    os.replace(movefile,destination)
                    # print(f"{movefile} was moved")
            except FileNotFoundError:
                print(f"{movefile} was not found")
            
    return total_files, print(f"Total files moved: {total_files}")
    

    
        


if __name__ == "__main__":
    
    rt_dir = f"C:\\Users" # root directory
    pc_name = ""
    desktop = "Desktop"
    mypath = f"{rt_dir}\\{pc_name}\\{desktop}"
    
    
    files = locatefiles(mypath)
    folders = locatefolders(mypath)
    newpath = createFolder(mypath)


    moveFolder(folders,newpath)
    movefile(newpath,files)
    
   
    
    
    


