import os,zipfile,sys

def backup_zip(folder):
    
    if not os.path.exists(os.path.basename(folder)):
        print(f"Folder '{folder}' does not exist")
        return    
    zipfilename = os.path.basename(folder) + '.zip' #Overwrite caution
    backupzip = zipfile.ZipFile(zipfilename,'w')
    for foldername,subfolders,filenames in os.walk(folder):
        print("Writing folder '%s' to '%s'"%(foldername,zipfilename))
        backupzip.write(foldername) 
        for filename in filenames:
            if filename.startswith(os.path.basename(folder)) and filename.endswith('.zip'):
                continue
            print("Writing file '%s' to '%s'"%(filename,zipfilename))
            backupzip.write(os.path.join(foldername,filename))
    backupzip.close()

if len(sys.argv) >= 2:
    target_folder = sys.argv[1]
    backup_zip(target_folder)
else:
    print("Provide a valid folder name")
    
