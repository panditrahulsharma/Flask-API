#load model pickle file
import pickle
import cv2
from keras.preprocessing import image
import numpy as np


print("***********************start*********************************")


def getKeysByValues(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] in listOfValues:
            listOfKeys.append(item[0])
    return  listOfKeys[0] 


def blood_cell_classification(img):

	print("***********************load pkl*********************************")

	classifier_pkl=open('static/model/Blood_cell.pkl','rb')
	model= pickle.load(classifier_pkl)

	img=cv2.resize(img,(28,28))
	img= np.reshape(img,(1,28,28,1))

	result = model.predict(img)
	pred=result.argmax(axis=1)

	print("***********************result*********************************")

	print(pred[0])

	classes={'EOSINOPHIL': 0, 'LYMPHOCYTE': 1, 'MONOCYTE': 2, 'NEUTROPHIL': 3}


	label_pred = getKeysByValues(classes, [pred] )

	return label_pred


#img=cv2.imread('a.jpeg',0)
#blood_cell_classification(img)
