import zipfile
import os.path
import time

target = input("TargetFile:")
extractTo = input("TargetDirectory:")

exist = os.path.isfile(target)

if exist == False:
    print("")
    print("[File does not exist]")
    time.sleep(0.5)
    
    print("")
    print("Open.file('" + target + "') |ERROR|")
    time.sleep(1.0)
    
    print("Extract.toPath('" + extractTo + "') |ERROR|")
    time.sleep(0.3)
    
    print("Close.file('" + target + "') |ERROR|")
    pass
elif exist == True:
    print("")
    print("[File does exist]")
    time.sleep(1.0)
    
    print("")
    print("Open.file('" + target + "')")
    time.sleep(2.0)
    
    print("Extract.toPath('" + extractTo + "')")
    time.sleep(0.5)
    
    print("Close.file('" + target + "')")
    
    handle = zipfile.ZipFile(target)
    handle.extractall(extractTo)
    handle.close()

print("")
print("[Exit]")