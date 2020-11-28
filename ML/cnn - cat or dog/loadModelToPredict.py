import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

cnn = tf.keras.models.load_model('./checkpoints/my_checkpoint')

# Part 4 - Making a single prediction
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/michal.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)

if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'
print(prediction)