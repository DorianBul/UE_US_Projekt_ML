import sys, os
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

checkpointPath = './checkpoints/my_checkpoint'
cnn = tf.keras.models.load_model(checkpointPath)

try:
    predicImageName = sys.argv[1]
    predicImagePath = "<SERVER_PATH>" + predicImageName
    
    predictImage = image.img_to_array(image.load_img(predicImagePath, target_size = (64, 64)))
    predictImage = np.expand_dims(predictImage, axis = 0)

    prediction = cnn.predict(predictImage)

    print('dog' if prediction[0][0] == 1 else 'cat')
    exit(0)
except IndexError:
    print('error')
    exit(666)


