from createcsv import *
from runMLmodel import *
from url_check import *

def main(url):
    getUrl(url)
    rootdir = "./downloads2/input.exe"
    output= "./output.csv"
    parseFile(rootdir, output)
    data = getData()
    #print(data)
    res = runMLAlg(data)
    return res
