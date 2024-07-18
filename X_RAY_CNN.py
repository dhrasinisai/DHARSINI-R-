# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:28:24 2024

@author: dhras
"""

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#create batches
training_datagen=ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
training_set=training_datagen.flow_from_directory(r"D:\DL_Dataset\xray_dataset_covid19\train", target_size=(64,64), batch_size=32, class_mode='binary')

test_datagen=ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_set=test_datagen.flow_from_directory(r"D:\DL_Dataset\xray_dataset_covid19\test", target_size=(64,64), batch_size=32, class_mode='binary')

cnn=tf.keras.models.Sequential()
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu',input_shape=[64,64,3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
cnn.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
cnn.fit(training_set, validation_data=test_set, epochs=10)


import numpy as np
from keras.preprocessing import image
test_image=tf.keras.utils.load_img(r"D:\DL_Dataset\xray_dataset_covid19\single prediction\pneumoina_or_normal_1.jpg")
test_image=tf.keras.utils.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)

result=np.expand_dims(test_image,axis=-1)
if np.any(result[0][0]==1):
    prediction='Pneumonia'
else:
    prediction='normal'
    
    
print(prediction)

import matplotlib.pyplot as plt
history=cnn.fit(training_set,validation_data=test_set, epochs=10)
#evaluate model on test set
test_loss,test_acc=cnn.evaluate(test_set)
print("Test Loss:",test_loss)
print("Test Accuracy:", test_acc)

#plot the accuracy
plt.figure(dpi=300)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model Accuracy CNN')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Val'],loc='best')
plt.show()

#plot the loss
plt.figure(dpi=300)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss CNN')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Val'],loc='upper right')
plt.show()

































