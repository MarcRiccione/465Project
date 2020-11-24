import pickle
import pandas as pd


def getData():
    data = pd.read_csv("output.csv")
    result = data.filter(['DllCharacteristics', 'Characteristics', 'Machine', 'Subsystem', 'MajorSubsystemVersion', 'ImageBase', 'SizeOfOptionalHeader', 'MajorOperatingSystemVersion'])
    return result.values

def runMLAlg(data):
    filename='final_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(data)
    if result[0] == 1:
        return 'Benign'
    else:
        return 'Malignant'