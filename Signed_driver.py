import os
import shutil
src = r'C:\Users\suwe\Desktop\driver\WHQL_Signed'
dst1 = r'C:\Users\suwe\Desktop\driver\Signed_Win8'
Signed_Win8 = []
for dirpath,dirnames,filenames in os.walk(src):
	if 'Win8' in dirpath:
		for filename in filenames:
			Signed_Win8.append(os.path.join(dirpath,filename))
print(Signed_Win8)


for line in Signed_Win8:
	shutil.copy(line, dst1)

dst2 = r'C:\Users\suwe\Desktop\driver\Signed_Win7'
Signed_Win7 = []
for dirpath,dirnames,filenames in os.walk(src):
	if 'Win7' in dirpath:
		for filename in filenames:
			Signed_Win7.append(os.path.join(dirpath,filename))
print(Signed_Win7)


for line in Signed_Win7:
	shutil.copy(line, dst2)

dst3 = r'C:\Users\suwe\Desktop\driver\Signed_Win10'
Signed_Win10 = []
for dirpath,dirnames,filenames in os.walk(src):
	if 'Win10' in dirpath:
		for filename in filenames:
			Signed_Win10.append(os.path.join(dirpath,filename))
print(Signed_Win10)


for line in Signed_Win10:
	shutil.copy(line, dst3)


