import numpy
import numpy as np
from keras.datasets import mnist
import keras.models
from keras.models import model_from_json


import cv2


def testModel(loaded_model, imageFile):
    #read image in the file
    img_pred = cv2.imread(imageFile,0)
    
    #forces the image to have the input dimensions equal to those used in 
    #the training data (28x28)
    if img_pred.shape != [28,28]:
        img2 = cv2.resize(img_pred,(28,28))
        img_pred = img2.reshape(28,28,-1)
    else:
        img_pred = img_pred.reshape(28,28 ,-1)  
    

    #Reshapes the data to a 4d tensor to feed our model
    img_pred = img_pred.reshape(1,1,28,28)
    #predict the number
    pred = loaded_model.predict_classes(img_pred)
    #Determine the probability of it
    pred_proba = loaded_model.predict_proba(img_pred)
    pred_proba = "%.2f%%" % (pred_proba[0][pred] * 100)
    with open('results.txt', 'w') as results:
        results.write(  "%s with probability of %s" % (pred_proba, pred[0]))


def main():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")

    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    images = open('image_file_names.txt', 'r')
    for line in images:
        print(line)
        testModel(loaded_model, line)
    """
    score = loaded_model.evaluate(X_test, y_test, verbose=0)
    print("%.2f%%" % (score[1]*100))
    """
if __name__ == "__main__":
    main()