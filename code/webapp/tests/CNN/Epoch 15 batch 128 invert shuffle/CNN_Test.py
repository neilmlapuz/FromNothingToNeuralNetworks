import numpy as np
from keras.datasets import mnist
import keras.models
from keras.models import model_from_json

#TESTING/TRAINING PURPOSES
import cv2


def testModel(loaded_model, imageFile):
    #read image in the file
    img_pred = cv2.imread(imageFile,0)

    #inverts the image 
    img_pred = np.invert(img_pred)

    #forces the image to have the input dimensions equal to those used in 
    #the training data (28x28)
    if img_pred.shape != [28,28]:
        img2 = cv2.resize(img_pred,(28,28))
        img_pred = img2.reshape(28,28,-1)
    else:
        img_pred = img_pred.reshape(28,28,-1)  
    
    #Reshapes the data to a 4d tensor
    img_pred = img_pred.reshape(1,1,28,28)
    
    #predict the number
    pred = loaded_model.predict_classes(img_pred)
    #Determine the probability of it
    pred_proba = loaded_model.predict_proba(img_pred)
    pred_proba = "%.2f%%" % (pred_proba[0][pred] * 100)
    #print("the number is " + pred[0])
    with open('results.txt', 'a') as results:
        results.write(  "%s predicted as %s\n" % (imageFile, pred[0]))


def main():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")

    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #images = open('image_file_names.txt', 'r')
    #for line in images:
    #    line = line.strip()
    testModel(loaded_model, "nine_1.png")

if __name__ == "__main__":
    main()