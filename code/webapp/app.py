from flask import Flask, render_template, request,jsonify,Response
import random, copy
import numpy as np
import re
import base64

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering ( 'th' )

import keras.models
from keras.models import model_from_json
import cv2

app = Flask(__name__)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Reshapes our data to a suitable format to feed our network
#28x28 dim format in which we train our network -- 1 for greyscale
#cast data to float32 for precision
x_train = x_train.reshape(x_train.shape[0], 1, 28, 28).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 1, 28, 28).astype('float32')

#Normalize inputs to 0-1(from 0-255)
x_train = x_train / 255
x_test = x_test / 255

#convert into binary class matrix -- 0-10 classes
num_classes = 10
y_train = np_utils.to_categorical(y_train,num_classes)
y_test = np_utils.to_categorical(y_test,num_classes)


#Load our model
def loadModel():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into the model
    loaded_model.load_weights("model.h5")
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return loaded_model

#Saves the contents drawn in the canvas to the file (memory)
def saveImage(imgData):
    #taking the part of the image encoded in base64
    img = re.search(b'base64,(.*)',imgData).group(1)

    with open('imgData.png','wb') as output:
        #decodes base64 to raw binary data and saves it 
        output.write(base64.b64decode(img))


#converts image
def changeSizeImg(loadedImg):
    #resize image to a 28x28 pixel image
    img = cv2.resize(loadedImg,(28,28))

    #reshape to a 4d tensor (784 value) -- this is what we are going to feed our model
    img = img.reshape(1,1,28,28)

    return img
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit/",methods=["GET","POST"])
def predict():
    #-- js encodes it as base64
    #Gets data sent from index.html from "data"
    #This gets the raw data format of the img drawn in the canvas 
    canvasData = request.get_data()
    saveImage(canvasData)

    #Loads image data
    loadedImg = cv2.imread("imgData.png",0)
    #inverts colour of image
    loadedImg = np.invert(loadedImg)
    outputImg = changeSizeImg(loadedImg)


    #load our model
    model = loadModel()
    #Predict the image
    prediction = model.predict_classes(outputImg)

    #returns the prediction to client
    prediction = str(prediction[0])
    return "Recognized as: {}".format(prediction)

def randomize(questions):
    #Function to randomize the keys in the dictionary and returns the list of randomized keys
    lst = list(questions.keys())
    random.shuffle(lst)    
    return lst

@app.route("/retrieveAnswers",methods =["POST"])
def retrieveAnswers():
    quizAnswers = {
    "What is the difference between Supervised and Unsupervised learning?":"Supervised learning is trained on labeled data and Unsupervised learning is trained on unlabeled data",
    "With a Threshold of 4 what would a perceptron output, with two inputs x1 = 1, x2 = 0 and respective weights of 3 and 13:":"0",
    "Linear Combination is where we:":"Multiply inputs by their weights and sum together the results",
    "A weight’s purpose it to:":"Give value to individual neurons",
    "Training a network involves:":"Adjusting the weights based on the errors in the output produced by previous weights.",
    
    "Bias is:":"Negative threshold",
    "We change the threshold into bias to:":"Simplify the training process",
    "A large positive bias will make it:":"Easier for a neuron to “fire”",
    "The simplest activation function is:":"Heaviside Step",
    

    "Convolution is split up into 2 parts:":"Feature learning and Classification",
    "An image is equivalent to:":"A matrix of pixels",
    "In simple terms, Convolution is where:":"Two sources of information are combined",
    "The goal of Regularisation is to:":"Reduce Overfitting"
}
    correct = 0
    answerForm = request.form
    for query in quizAnswers.keys():
        #Checks if query in the form passed from client
        if query in answerForm:
            answer = request.form[query]
            if quizAnswers[query] == answer:
                correct +=1

    results = str(correct)
    return results

@app.route("/Intro/")
def Intro():
    perceptron_questions = {
    "What is the difference between Supervised and Unsupervised learning?":["Supervised learning takes longer to train a network","Unsupervised learning takes longer to train a network","Unsupervised learning is trained on labeled data and Supervised learning is trained on unlabeled data","Supervised learning is trained on labeled data and Unsupervised learning is trained on unlabeled data"],
    "A weight’s purpose it to:":["Speed the training process up","Make calculations less taxing","Give value to individual neurons","Give value to a layer in the network"],
    "Linear Combination is where we:":["Divide inputs by their weights and sum together the results","Multiply inputs by their weights and sum together the results","Add inputs to their weights and sum together the results","Subtract inputs from their weights and sum together the results"],
    "Training a network involves:":["Adjusting the weights based on the errors in the output produced by previous weights.","Adjusting the weights randomly and keeping weights that produce better results and discarding those that don’t."],
    "With a Threshold of 4 what would a perceptron output, with two inputs x1 = 1, x2 = 0 and respective weights of 3 and 13:":["20","4","1","0"]
}
    #A list of randomize keys
    lst_questionsKeys = randomize(perceptron_questions)
    #Randomized order of answers
    for query in lst_questionsKeys:
        random.shuffle(perceptron_questions[query])
    
    return render_template("Intro.html",lst_questionsKeys=lst_questionsKeys,questions=perceptron_questions)

@app.route("/activation/")
def activation():
    activation_questions = {
    "Bias is:":["Negative threshold","One over the threshold","Two times the threshold","Equal to the threshold"],
    "We change the threshold into bias to:":["Simplify the training process","Change the magnitude of our results","It’s just convention","Add dementionallity to our network"],
    "A large positive bias will make it:":["Easier for a neuron to “fire”","Harder for a neuron to “fire”","No different for a neuron to “fire”","Impossible for a neuron to “fire”"],
    "The simplest activation function is:":["ReLu","Sigmoid","Tahn","Softmax","Heaviside Step","Linear"]
}
    #A list of randomize keys
    lst_questionsKeys = randomize(activation_questions)
    #Randomized order of answers
    for query in lst_questionsKeys:
        random.shuffle(activation_questions[query])

    return render_template("activation.html",lst_questionsKeys=lst_questionsKeys,questions=activation_questions)
    
@app.route("/CNN/")
def CNN():
    CNN_questions = {
    "Convolution is split up into 2 parts:":["Feature learning and Classification","Classification and Feature learning","Regression and Weight Training","Weight Training and Regression"],
    "An image is equivalent to:":["An ordered list of pixels","A matrix of pixels","A matrix of matrices of pixels","A dictionary of pixels"],
    "In simple terms, Convolution is where:":["One source of information is transformed","Two sources of information are combined","Two sources of information are intersected","Any number of sources of information are combined"],
    "The goal of Regularisation is to:":["Reduce Overfitting","Reduce Underfitting","Reduce Underfitting and Overfitting","Increase Fitting"]
}
    #A list of randomize keys
    lst_questionsKeys = randomize(CNN_questions)
    #Randomized order of answers
    for query in lst_questionsKeys:
        random.shuffle(CNN_questions[query])
    
    return render_template("CNN.html",lst_questionsKeys=lst_questionsKeys,questions=CNN_questions)

@app.route("/CodeIt/")
def CodeIt():
	return render_template("CodeIt.html")


@app.route("/examineModel/")
def examineModel():
    return render_template("examineModel.html")

@app.route("/train",methods =["GET","POST"])
def train():
    #requests for the input sent from the client
    dataSize = int(request.form["dataSize"])
    activation = request.form["activation"]
    regularisation = float(request.form["regularisation"])
    batchSize = int(request.form["batchSize"])
    epoch = int(request.form["epoch"])

    #Builds the model
    model = build_model(activation,regularisation)

    #Trains the model with the data inputted
    train = model.fit(x_train[:dataSize], y_train[:dataSize], validation_data=(x_test, y_test), epochs=epoch, batch_size=batchSize)

    #Get the info of the model
    modelInfo,result_model = getEvaluation(train,epoch)

    return jsonify(result=modelInfo,result_model=result_model)


def getEvaluation(train,epoch):
    #Gets the evaluation of the data
    loss = train.history["loss"]
    val_loss = train.history["val_loss"]
    acc = train.history["acc"]
    val_acc = train.history["val_acc"]
    modelInfo = "loss {:.4f}\nval_loss {:.4f}\nacc {:.4f} val_acc {:.4f}".format(loss[-1],val_loss[-1],acc[-1],val_acc[-1])

    #Passed on to feed the line chart in the client
    epochs = [str(i) for i in range(0,epoch)]
    result_model = {
        "epochs":epochs,
        "loss":loss,
        "val_loss":val_loss,
        "acc":acc,
        "val_acc":val_acc
    }

    return modelInfo,result_model

def build_model(acti,regu):

    model = Sequential()
    #Perform Convolutional to get features  
    model.add(Conv2D(32,(5,5), input_shape = (1,28,28),activation=acti))
    #Pooling -- choose the best features of output matrix
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(64,(3,3),activation=acti))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    #Regularisation -- Dropout of 0.25
    model.add(Dropout(regu))
    model.add(Flatten())

    #Fully connected neurons
    model.add(Dense(128,activation=acti))
    model.add(Dense(50,activation=acti))

    #use softmax function to squash matrix to output probability value
    #determines which class does it belong to
    model.add(Dense(num_classes,activation='softmax'))

    #Compile our model
    #Adam for optimizer a method for Stochastic Optimization
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model




if __name__ == "__main__":
    app.run()