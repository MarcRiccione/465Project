from createcsv import *
from runMLmodel import *
from url_check import *

def main(url):
    getUrl(url)
    rootdir = "./downloads2/input.exe"
    output= "./output.csv"
    x = parseFile(rootdir, output)
    if x == 1:
        return "Benign"
    data = getData()
    #print(data)
    res = runMLAlg(data)
    return res
