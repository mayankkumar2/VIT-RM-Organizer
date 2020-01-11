import os
import sys
import re
import shutil

flag = 0
for i,s in enumerate(sys.argv):
    if re.match('.*vtool\.py',s):
        flag = i
        break
if len(sys.argv)-1 == i:
    basepath = "."
else:    
 if not os.path.isdir(sys.argv[flag+1]):
    print("%s doesn't exist." % (sys.argv[flag+1]))
    print("Exiting")
    exit(1)
 else:
    basepath = sys.argv[flag+1]


for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        if re.match('.*\.zip',(entry)):
            continue
        lee = entry.split('_')
        if len(lee) > 4:
            file_name = " ".join(lee[4:])
            sem = lee[0]
            course = lee[1]
            course_type = lee[2]
            class_code = lee[3]
            try:
             if not os.path.isdir(os.path.join(basepath,sem,course,course_type,class_code)):
                os.makedirs(os.path.join(basepath,sem,course,course_type,class_code))
            except:
                print("%s can't be created" % os.path.join(basepath,sem,course,course_type,class_code) )
            if not (os.path.isfile(os.path.join(basepath,sem,course,course_type,class_code,entry))):
            
                dest = shutil.move(os.path.join(basepath,entry),os.path.join(basepath,sem,course,course_type,class_code),copy_function = shutil.copytree)
            else:
                print("%s already exists. Replacing with the new file." % os.path.join(basepath,sem,course,course_type,class_code,entry))
                os.remove(os.path.join(basepath,sem,course,course_type,class_code,entry))
                dest = shutil.move(os.path.join(basepath,entry),os.path.join(basepath,sem,course,course_type,class_code),copy_function = shutil.copytree)
