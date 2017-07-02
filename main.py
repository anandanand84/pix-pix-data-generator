from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model, Sequential
from keras import backend as K
from keras.callbacks import TensorBoard

import numpy as np
import scipy.ndimage
import cv2
import os.path

# original_datagen = ImageDataGenerator(rescale=1./255)
# noised_datagen = ImageDataGenerator(rescale=1./255)

# original = original_datagen.flow_from_directory(
#         'data/original',
#         target_size=(280, 280),
#         batch_size=32,
#         seed=1,
#         class_mode=None)

# noised = noised_datagen.flow_from_directory(
#         'data/noised',
#         target_size=(280, 280),
#         batch_size=32,
#         seed=1,
#         class_mode=None)


model = Sequential()
model.add(Conv2D(160, (30, 30), activation='relu', padding='same', input_shape=(280,280,1)))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(80, (30, 30), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(80, (30, 30), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2), padding='same'))

# at this point the representation is (40, 40, 80) i.e. 128-dimensional

model.add(Conv2D(80, (30, 30), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(80, (30, 30), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(160, (30, 30), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(1, (30, 30), activation='sigmoid', padding='same'))
# (None, 7420, 7420, 10) but got array with shape (4, 280, 280, 1)

model.compile(optimizer='adadelta', loss='binary_crossentropy')

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
image = []
image_noised = []
output = np.array([])
photo_count = 1
while photo_count < 5:
    photo_count = photo_count + 1
    if os.path.isfile('out/'+str(photo_count)+'.jpeg'):
        print 'loading file' + str(photo_count)
        original_image = img_to_array(load_img('out/'+str(photo_count)+'.jpeg', grayscale=True, target_size=(280, 280)))
        image.append(original_image)
        noised_image = img_to_array(load_img('out/noised/'+str(photo_count)+'.jpeg', grayscale=True, target_size=(280, 280)))
        image_noised.append(noised_image)
    pass

print np.asarray(image_noised).shape
print np.asarray(image).shape

model.fit(np.asarray(image_noised),np.asarray(image),
                epochs=50,
                batch_size=128,
                verbose=1
                )

# autoencoder.f([noised, original]], 
#                 epochs=50,
#                 callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])
