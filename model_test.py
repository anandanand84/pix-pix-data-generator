from keras.models import load_model
import os
import numpy as np
import scipy
model = load_model('saved_model/saved.hd5')
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
image_noised = []
photo_count = 1
while photo_count < 10:
    photo_count = photo_count + 1
    if os.path.isfile('out/'+str(photo_count)+'.jpeg'):
        noised_image = img_to_array(load_img('out/noised/'+str(photo_count)+'.jpeg', grayscale=True, target_size=(280, 280)))
        noised_image = noised_image.astype('float32')/255.
        image_noised.append(noised_image)
    pass
x_test = np.asarray(image_noised)
decoded_imgs = model.predict(x_test)

import matplotlib.pyplot as plt

n = 10  # how many digits we will display
x_test = x_test * 255
decoded_imgs = decoded_imgs * 255 
print x_test.shape
print decoded_imgs.shape
print decoded_imgs[3].reshape(280,280)
scipy.misc.imsave('noised_input.jpeg',x_test[3].reshape(280,280))
scipy.misc.imsave('decoded_output.jpeg',decoded_imgs[3].reshape(280,280))
# plt.figure(figsize=(20, 4))
# for i in range(n):
#     # display original
#     ax = plt.subplot(2, n, i + 1)
#     plt.imshow(x_test[i])
#     plt.gray()
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)

#     # display reconstruction
#     ax = plt.subplot(2, n, i + 1 + n)
#     plt.imshow(decoded_imgs[i])
#     plt.gray()
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
# plt.show()