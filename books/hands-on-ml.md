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