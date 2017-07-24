import pickle
import numpy as np
from keras.models import load_model

class DataManage:
    def loadDataNp(self, name):
        return np.load(name)

    def loadDataPkl(self, name):
        with open(name, "rb") as f:
            return pickle.load(f)

    def loadModel(self, name):
        try:
            self.model = load_model(name)

            return self.model
        except Exception as e:
            print(e)