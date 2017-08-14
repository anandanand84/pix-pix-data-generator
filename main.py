from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model, Sequential
from keras import backend as K
from keras.callbacks import TensorBoard

import numpy as np
import scipy.ndimage
import cv2
import os.path
<<<<<<< HEAD

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

=======
import sys
>>>>>>> 69191020aa7374ebaa0f9e9a5aa85c7c4a5fc5e0

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

<<<<<<< HEAD
model.compile(optimizer='adadelta', loss='binary_crossentropy')
=======
model.compile(optimizer='rmsprop', loss='binary_crossentropy',metrics=['accuracy'])
>>>>>>> 69191020aa7374ebaa0f9e9a5aa85c7c4a5fc5e0

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
image = []
image_noised = []
output = np.array([])
photo_count = 1
<<<<<<< HEAD
while photo_count < 5:
=======
while photo_count < 100:
>>>>>>> 69191020aa7374ebaa0f9e9a5aa85c7c4a5fc5e0
    photo_count = photo_count + 1
    if os.path.isfile('out/'+str(photo_count)+'.jpeg'):
        print 'loading file' + str(photo_count)
        original_image = img_to_array(load_img('out/'+str(photo_count)+'.jpeg', grayscale=True, target_size=(280, 280)))
<<<<<<< HEAD
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

=======
        original_image = original_image.astype('float32')/255.
        image.append(original_image)
        noised_image = img_to_array(load_img('out/noised/'+str(photo_count)+'.jpeg', grayscale=True, target_size=(280, 280)))
        noised_image = noised_image.astype('float32')/255.
        image_noised.append(noised_image)
    pass
print image_noised[5]
print np.asarray(image_noised).shape
print np.asarray(image).shape
scipy.misc.imsave('sample_train_data_expected_output.jpeg',image[3].reshape(280,280))
scipy.misc.imsave('sample_train_data_input.jpeg',image_noised[3].reshape(280,280))

model.fit(np.asarray(image),np.asarray(image),
                epochs=10,
                batch_size=16,
                verbose=1
                )
model.save('saved_model/saved.hd5')
>>>>>>> 69191020aa7374ebaa0f9e9a5aa85c7c4a5fc5e0
# autoencoder.f([noised, original]], 
#                 epochs=50,
#                 callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])
