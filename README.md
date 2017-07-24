# Origin
Originality in Logo Design - Computer Vision

Origin is a web application which identify the originality of a logo using machine learning algorithms.

In the first phase the model is trained. The SURF features of the class images are extracted, and based on them, the visual dictionary is formed (Bag of visual words).
For each class image, a histogram is generated using the visual dictionary, and based on them, the model is trained using neural network.

The web application can predict with which classes a logo look alike.

For training the model has been used:
- Train set: 56 classes with 6 images each
- Validation set: 56 classes with 3 images each
- Dictionary with 2240 visual words
- A neural network with input (Relu) and output (Softmax) layers. Linear problem.
- Batch: 6
- Optimization tool: Adam

For the validation set has been obtained an accuracy of 97.04%.
