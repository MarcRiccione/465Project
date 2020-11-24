import pickle
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split

def getData():
    data = pd.read_csv("output.csv")
    data_in = data.filter(['Machine', 'SizeOfOptionalHeader', 'Characteristics', 'ImageBase', 'MajorOperatingSystemVersion', 'MajorSubsystemVersion', 'Subsystem', 'DllCharacteristics'])
    #print(data_in)
    return data_in.values

def runMLAlg(data):
    filename='final_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(data)
    if result[0] == 1:
        return 'Benign'
    else:
        return 'Malignant'