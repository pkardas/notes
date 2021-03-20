[go back](https://github.com/pkardas/learning)

# Practical Deep Learning for Coders
Course -> https://course.fast.ai/

[TOC]

## Lesson 1

Truth, to start with Deep Learning:

- high school math is sufficient
- there is no need for enormous amounts of data
- no need for expensive hardware for basic usage



1961 first machine built on top of mathematical model from 1943. Heavily criticised by Minsky - example that artificial neural network could not learn simple XOR. Global academic gave up on neural networks.

1986 MIT released a paper defining requirements for building and using neural networks. Later researchers proved, that adding additional layers of neural networks is enough to approximate any mathematical model. But in fact these models were too slow and too big to be useful.

**What is ML?** Like regular programming, a way to get computers to complete a specific task. Instead of telling the computer the exact steps to solve a problem, show it examples fo the problem to solve and let it figure out how to solve it itself.

*Neural network* - parametrised function that can solve any problem to any level of accuracy (in theory - *universal approximation theorem)*.

What does it mean to train neural network? It means finding good weights. This is called **SDG**. SDG - Stochastic Gradient Descent.

Neural Networks work using patterns, need labeled data and create PREDICTIONS not recommended actions. 

You need to be super careful what is the input data (initial bias, stereotypic data) will produce biased results. Eg. marihuana consumption is equal amon whites and blacks, but black people are mor often arrested for marihuana possession. Given biased input data will produce biased predictions, eg. send more police officers to black neighbourhoods. 

Segmentation - marking areas on images (trees, cars, ...)

## Lesson 2

When you want to predict a category you are facing a classification problem. Whenever you want to predict a number you are dealing with regression problem.

```python
learn = cnn_learner(data, architecture, metric)
```

Architecture - eg. *resnet32, resnet64* - name of the architecture (64 layers) - function that we are optimising.

Epoch - eg. looking at every image in the training set = 1 epoch, 1 loop

Metric - function measuring quality of the model's predictions (*error_rate, accuracy*), we care about it.

Loss != Metric, loss - computer uses this to update parameters, computer cares about it. For example tweaking parameters just a little might not change accuracy or error rate.

Model might cheat - "I have seen this image, this is a cat", we don't want model to memorise images. That is why we need splitting into training and validation. For validating time-series, you should not removed eg. 20% of the data, instead, drop off the end and let the model predict eg. next 2 weeks.

*Transfer learning* - using a pretrained model for a task different to what it was originally trained for. Take pretrained (initial weights), add more epochs on your specific dataset and you will end up with way more better model.

*Fine tuning* - transfer learning technique where the weights of pretrained model are updated by training for additional epochs using different task to that used for pretraining.

You can take advantage of pretrained feature - eg. dog faces, patterns, etc.

Computer Vision can be used for variety of problems, eg. sound, virus analysis (data transformed into images). 

![fast-ai-1](../_images/fast-ai-1.png)

Set of pretrained models: https://modelzoo.co/

*How to decide if there is a relationship?*

*Null hypothesis* - eg. "no relationship between X and Y" -> gather data -> how often do we see a relationship?

*P-Value* - probability of an observed result assuming that the null hypothesis is true.



