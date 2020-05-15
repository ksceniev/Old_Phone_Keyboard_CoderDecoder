import os

os.chdir('/home/annie/Downloads')
lines = []

fobj = open('bank_heist_message.txt', 'r+')
for line in fobj:
    lines.append(line)
fobj.close()

cryp_wds = []
for line in lines:
    splited_list = (line.split(' '))
    for cryp_wd in splited_list:
        cryp_wd.replace('\n', '')
        cryp_wds.append(cryp_wd)
       
print(cryp_wds)

