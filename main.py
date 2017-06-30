from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from keras.callbacks import TensorBoard

from keras.datasets import mnist
import numpy as np
import cv2



input_img = Input(shape=(28, 28, 1), dtype='int', name='noised_input')  # adapt this if using `channels_first` image data format
expected_img = Input(shape=(28, 28, 1), dtype='int', name='expected_output')

x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)

# at this point the representation is (4, 4, 8) i.e. 128-dimensional

x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(16, (3, 3), activation='relu')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(inputs=[input_img, expected_img],outputs=[decoded])
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

image = []
image_noised = []
output = []
photo_count = 100
while photo_count > 1:
    original_image = scipy.ndimage.imread('original/'+photo_count+'.jpg', flatten=True)
    cv2.resize(modified_image, (28, 28)).astype(np.float32)
    noised_image = scipy.ndimage.imread('noised/'+photo_count+'.jpg', flatten=True)
    photo_count++;
    pass

autoencoder.fit({noised_input : image_noised, expected_output:image}, output,
                epochs=50,
                batch_size=128,
                shuffle=True,
                validation_data=(x_test, x_test),
                callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])

autoencoder.predict(x=[{noised_input : image_noised[2]}],batch_size=10, verbose=1)


