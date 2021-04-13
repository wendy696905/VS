import os

def file(path,filename):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for dirpath,dirnames,filenames in os.walk(path):
            for filename in filenames:
                f.write(os.path.join(dirpath,filename) + '\n')


file(r'C:\Users\suwe\Desktop\driver\Signed_Win7','Signed_Win7.csv')
file(r'C:\Users\suwe\Desktop\driver\Onedrive_Win 7 64bits  WHQL Driver','onedrive_win7.csv')
file(r'C:\Users\suwe\Desktop\driver\Onedrive_Win10 64bits WHQL Driver','onedrive_win10.csv')