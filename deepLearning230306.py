# import tensorflow as tf
#
# print(tf.test.is_built_with_cuda())
# print(tf.test.gpu_device_name())


num = 0.0
for idx in range(0,100):
    num += 0.1
print(num)
print(f'{num: .18f}')