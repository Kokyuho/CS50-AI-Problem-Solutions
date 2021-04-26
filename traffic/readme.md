CS50’s Introduction to Artificial Intelligence with Python
Neural Networks - Project 5 - Traffic

For this project, a TensorFlow neural network is built using Keras Sequential Model and then optimized for the task at hand.

First, I added a 2D convolutional layer (Conv2D) with 32 filters, a kernel size of 5 pixels, 2 strides and ReLU activation, followed by a MaxPooling2D with a pool size of 3 pixels. Then we add a flatten layer for input to the NN. Finally we add a Dense layer as output of the NN with softmax activation and the NUM_CATEGORIES nodes. We compile this NN using ADAM optimizer CategoricalCrossentropy losses and metrics for accuracy. The result is an accuracy of 75% on test data. Not bad, but could be improved.

Adding a hidden layer of 128 nodes, we manage to improve the accuracy on test data to 82%.

Then, I decided to reduce the kernel size of the convolution layer from 5 to 3 pixels and remove the 2 strides to have the default behaviour. The accuracy on test data improved to 92%. 

I tested without the hidden layer now, and the result was similar. However, leaving this layer and including a dropout layer after the convolution and max pool to avoid overfitting reached an accuracy of 94.5% on test data, which is already great.

Finally, adding a second convolution layer of kernel size 4 pixels and 32 filters after the first convolution results in an almost perfect test data accuracy, with around 98% accuracy!