[go back](https://github.com/pkardas/learning)

# Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems
Book by Aurelien Geron

[TOC]

TODO: *Re-read Part I.*

## Chapter 10: Introduction to Artificial Neural Networks with Keras

ANNs - Artificial Neural Networks - inspired by by the networks of biological neurons, have gradually become quite different from their biological cousins,.

ANNs introduced in 1943 by McCulloch and Pitts - a simplified computational model of how biological neurons might work together in animal brains to perform complex computation using propositional logic.

McCulloch and Pitts proposed an artificial neuron that has one or more binary inputs (on/off) and one binary output. The artificial neuron activates its output when more than a certain number of its inputs are active. They showed that even such simplified model is possible capable of performing various logical computations.

The Perceptron - is one of the simplest ANN architectures, invented in 1957. It is based on slightly different artificial neuron - threshold logic unit or linear threshold unit. The inputs and outputs are numbers (instead of binary on/off values) and each input connection is associated with a weight. The TLU computes a weighted sum of its inputs, then applies a step function to that sum and outputs the result. Most commonly used step function is the Heaviside step function.

A single TLU can be used for simple linear binary classification.

A perceptron is composed of a single layer of TLUs, each TLU connected to all inputs (when all the neurons are connected to every neuron in the previous layer, the layer is called a fully connected layer). The inputs of the Perceptron are fed to special passthrough neurons from the input layer. Extra bias feature is generally added (neuron that always output 1). A Perceptron with 2 inputs and three outputs can classify instances simultaneously into three different binary classes - multi-output classifier. 

How perceptron is trained? "Cells that fire together, wire together" - the connection between weight between 2 neurons tend to increase when they fire simultaneously (Hebb's rule). The perceptron is fed one example at a time, when it outputs wrong answer, it reinforces the connection weights from the inputs that would have contributed to the correct answer.  

In fact single Perceptron is similar to SDGClassifier. 

Back-propagation training algorithm - it is Gradient Descent using an efficient technique for computing the gradients automatically in just 2 passes through network - one forward, one backward. It can find out how each connection weight and each bias term should be tweaked in order to reduce the error. 

In other words: for each training instance, the back propagation algorithm first makes a prediction (forward pass) and measures the error, then goes through each layer in reverse to measure the error contribution from each connection (reverse pass) and finally tweaks the connection weights to reduce error (Gradient Descent step).

When building MLP for regression you don't want to use any activation function for the output neurons, so they are free to output any range of values. If output needs to be always positive ReLU can be used in the output layer. 

The loss function function to use during training is typically the mean squared error, but if there are many outliers in the training set, mean absolute error might be a better choice. 

MLP can be used also for classification.

Tensorflow 2 adopted Keras' high API + introduced some additional functionalities.

Sequental API - simplest kind of Keras model for neural networks that are just composed of a single stack of layers connected sequentially. Flatten - preprocessing layer whose role is to convert each input into 1D array. Once model is defined it needs to be compiled - you need to specify loss function and optimiser to use, optionally list of metrics can be passed. Then model can be trained.  

