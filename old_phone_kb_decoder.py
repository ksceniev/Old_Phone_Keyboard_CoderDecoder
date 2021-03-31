import os
import itertools

decoder_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
os.chdir('/home/annie/Documents/htb/boxes')

lines = []
fobj = open('bank_heist_message.txt', 'r+')
for line in fobj:
    lines.append(line)
fobj.close()

cryp_wds = []
for line in lines: # text treatment
    splited_list = (line.split(' '))
    for cryp_wd in splited_list:
        cryp_wd.replace('\n', '')
        cryp_wds.append(cryp_wd)

listed_nums = [] # nested list of cryp_wds for further counting
for cryp_wd in cryp_wds:
    a = list(cryp_wd)
    listed_nums.append(a)
for a in listed_nums:
    for i in a:
        try:
            int(i)
        except ValueError:
            a.remove(i)

for a in listed_nums:
        l = [(k, sum(1 for _ in v)) for k, v in itertools.groupby(a)] # list of tuples containing the key pressed and how many times it was pressed.
        for t in l:
            k, v = t[0], t[1]
            letter = decoder_dict[k][v-1]
