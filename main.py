from createcsv import *
from runMLmodel import *

def main(directory):
    rootdir = "./" + directory +"/"
    output= "./output.csv"
    parseFile(rootdir, output)
    data = getData()
    print(data)
    res = runMLAlg(data)
    print(res)


input1 = input()
main(input1)