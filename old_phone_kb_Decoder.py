import sys, getopt
import itertools

decoder_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

# gets the input file in command line
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


with open(main(sys.argv[1:]), 'r+') as fobj:
   lines = [line for line in fobj]
         
cryp_wds = [cryp_wd.replace('\n', '') for line in lines for cryp_wd in line.split(' ')]


listed_nums = [list(cryp_wd) for cryp_wd in cryp_wds]
   
for a in listed_nums:
    for i in a:
        try:
            int(i)
        except ValueError:
            a.remove(i)

letters = [decoder_dict[t[0]][t[1]-1] for a in listed_nums for t in [(k, sum(1 for _ in v)) for k, v in itertools.groupby(a)]]

print(''.join(letters))
