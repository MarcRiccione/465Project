from createcsv import *
from runMLmodel import *
from url_check import *

def main(directory):
    rootdir = "./downloads2/" + directory
    output= "./output.csv"
    parseFile(rootdir, output)
    data = getData()
    #print(data)
    res = runMLAlg(data)
    print(res)

getUrl()
input1 = input()
main(input1)