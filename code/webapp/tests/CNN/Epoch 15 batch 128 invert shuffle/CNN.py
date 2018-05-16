import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering ( 'th' )

from keras.models import model_from_json

#read/load image
import cv2

#Loads the dataset from mnist
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

#Build the network now
def build_model():
    model = Sequential()
    #Perform Convolutional to get features
    model.add(Conv2D(32,(5,5), input_shape = (1,28,28),activation='relu'))
    #Pooling -- choose the best features of output matrix
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(64,(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    #Regularisation -- Dropout of 0.25
    model.add(Dropout(0.25))
    model.add(Flatten())

    #Fully connected neurons
    model.add(Dense(128,activation='relu'))
    model.add(Dense(50,activation='relu'))


    #use softmax function to squash matrix to output probability value
    #determines which class does it belong to
    model.add(Dense(num_classes,activation='softmax'))

    #Compile our model
    #Adam for optimizer a method for Stochastic Optimization
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

def main():
    model = build_model()

    #Trains the model
    #evaluates the loss
    #number of samples per gradient update
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=15, batch_size=128,shuffle=True)
    scores = model.evaluate(x_test, y_test, verbose=0)
    print("Accuracy: %.2f%%" % (scores[1]*100))
    
    model_json = model.to_json()
    with open("model.json","w") as json_file:
        json_file.write(model_json)
    model.save_weights("model.h5")
    print("SAVED")

if __name__ == "__main__":
    main()