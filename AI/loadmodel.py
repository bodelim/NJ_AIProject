import tensorflow as tf
from tensorflow import keras
import numpy as np

new_model = tf.keras.models.load_model('model.h5') # 모델 불러오기

a_test = np.array([0,1,2,3,4,5, 10])

# 모델 구조를 출력합니다
new_model.summary()

learn_Result = new_model.predict(a_test)
print(learn_Result)