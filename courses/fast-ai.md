[go back](https://github.com/pkardas/learning)

## Practical Deep Learning for Coders
Course -> https://course.fast.ai/

[TOC]

#### Lesson 1

Truth, to start with Deep Learning:

- high school math is sufficient
- there is no need for enormous amounts of data
- no need for expensive hardware for basic usage



1961 first machine built on top of mathematical model from 1943. Heavily criticised by Minsky - example that artificial neural network could not learn simple XOR. Global academic gave up on neural networks.

1986 MIT released a paper defining requirements for building and using neural networks. Later researchers proved, that adding additional layers of neural networks is enough to approximate any mathematical model. But in fact these models were too slow and too big to be useful.



**What is ML?** Like regular programming, a way to get computers to complete a specific task. Instead of telling the computer the exact steps to solve a problem, show it examples fo the problem to solve and let it figure out how to solve it itself.



Neural network - parametrised function that can solve any problem to any level of accuracy (in theory - *universal approximation theorem)*.



What does it mean to train neural network? It means finding good weights. This is called **SDG**. SDG - Stochastic Gradient Descent.



Neural Networks work using patterns, need labeled data and create PREDICTIONS not recommended actions. 



You need to be super careful what is the input data (initial bias, stereotypic data) will produce biased results. Eg. marihuana consumption is equal amon whites and blacks, but black people are mor often arrested for marihuana possession. Given biased input data will produce biased predictions, eg. send more police officers to black neighbourhoods. 



Segmentation - marking areas on images (trees, cars, ...)

