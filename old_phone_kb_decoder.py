import sys, getopt
import itertools

decoder_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

# gets the inpute file in command line
def main(argv):
   inputfile = str()
   outputfile = str()
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   return inputfile

lines = []
fobj = open(main(sys.argv[1:]), 'r+')
for line in fobj:
    lines.append(line)
fobj.close()

cryp_wds = []
for line in lines: # text treatment
    splited_list = line.split(' ')
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
    letters = []
    l = [(k, sum(1 for _ in v)) for k, v in itertools.groupby(a)] # list of tuples containing the key pressed and how many times it was pressed.
    for t in l: 
        k, v = t[0], t[1]
        letter = decoder_dict[k][v-1]
        letters.append(letter)
    word = ''.join(letters)
    print(word)
