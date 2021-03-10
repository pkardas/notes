[go back](https://github.com/pkardas/learning)

## Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition
Book by Daniel Jurafsky and James H. Martin (December 2020 draft)



[TOC]

#### Chapter 2: Regular Expressions, Text Normalization, Edit Distance

*Regular Expressions*

Regular expression is an algebraic notation for characterising a set of strings. 



Kleene * (cleany star) - zero or more occurrences. 

Kleene + - at least one



Anchors - special characters that *anchor* regular expressions to particular places in a string (`^` - start, `$` - end of a string).

`^` has multiple meanings:

1. match start of the line
2. negation inside square brackets `[^Ss]` - neither `S` nor `s`



Pipe symbol `|` also known as "disjunction". Logical OR. `cat|dog` match either `cat` or `dog`.



Operator precedence hierarchy:

1. Parenthesis: `()`
2. Counters: `* + ? {}`, `{}` - explicit counter
3. Sequences and anchors: `sequence ^the end$`
4. Disjunction: `|`



Regular expressions are greedy, however there is a way to enforce non-greedy behaviour -> `*?` - Kleene star that matches as little text as possible, `+?` - Kleene plus that matches as little text as possible.



Fixing RE errors might require following efforts:

- Increasing precision (minimising false positives - incorrectly matched)

- Increasing recall (minimising false negatives - incorrectly missed)

  

*Substitution* - easiest to explain with an example:

```
the (.*)er they were, the \1er they will be
--- will match ---
the bigger they were, the bigger they will be
```

Number operator, eg.: `\1` allows to repeat matched group. So parenthesis operator not only allows to group but also store in a numbered registe. It is possible to disable register and use non-capturing group, eg.: `(:?some: a few) (people|cats) like some \1`. Famous chatbot ELIZA used a series of regular expressions substitutions.

```
I'M (depressed|sad) -> I AM SORRY TO HEAR YOU ARE \1
```



Look ahead - look ahead in the text to see if some pattern matches BUT not advance the match cursor.

Negative lookahead - used for ruling out special cases, eg. rule out strings starting with word Volcano: `(?!Volcano)[A-Za-z]+`

*Words*

Fragment - broken-off word, "I do main- mainly", "main-" is a fragment here

Filler - "um, uh" - used in spoken language, problem: should be treated as a word? Fragment and fillers are 2 kinds of disfluencies.

Type - number of distinct words in a corpus. When we speak about number of words in the language, we are generally referring to word types.



Herdan's Law/Heap's Law - relationship between number of types (`|V|`) and number of tokens (`N`) in the corpora:
$$
|V| = kN^{\beta}
$$
(k and 0 < B < 1 are constants)

*Corpora*

Writers, speakers have specific styles of communicating, use specific dialects, text can vary by time, place, function, race, gender, age, socioeconomic class.

Code switching - common practice for speakers and writers to use multiple languages in single communicative act

When preparing a computational models for language processing it is useful to prepare datasheet, document answering questions like: Who produced the text? In what context? For what purpose? In what language? What was race, gender, ... of the authors? How data was annotated?

*Text Normalisation*

1. Tokenisation (segmentation)
2. Normalising word formats
3. Segmenting sentences



*Tokenisation*

UNIX's `tr` command can be used for quick tokenisation of English texts.



Problem: Keep specific words together: `2020/02/02`, `km/h`, `$65`, `www.github.com`, `100 000`, `I'm`, `New York`



Tokeniser can be used to expand clitic contractions: `we're -> we are`. Tokenisation is tied up with Named Entity Recognition. Tokenisation needs to be fast, hence often uses deterministic algorithms based on regular expressions compiled into efficient finite state automata. Tokenisation is more complex for eg.: Chinese or Japanese (languages not using spaces for separating words). For Japanese algorithms like words segmentation work better. Also it is possible to use neural networks for the task of tokenisation.



Penn Treebank Tokeniser

- separates clitics (`deosn't -> does n't`)
- keeps hyphenated words together (`close-up`, `Bielsko-Biała`)
- separates out all punctuation



Byte-Pair Encoding

- begins with a vocabulary that is set of all individual characters
- examines training corpus, chooses the two symbols that are most frequently adjacent (A, B -> AB)
- continues to count and merge, creating longer and longer character strings, until k merges (parameter of the algorithm)
- most words will be represented as full symbols, few rare will have to be represented by their parts



*Normalisation*

Task of putting words in a standard format, choosing a single normal form for words with multiple forms like USA/US. Valuable proces despite spelling information is lost.



Case folding - mapping everything to lower/upper case. However might give wrong results, eg.: US (country) -> us (people, we)



*Lemmatisation*

Task of determining that two words have the same root (am, are, is -> be). Useful for web search - usually we want all forms to be found. Requires morphological parsing of the word. Morphology is the study of the way words are built up from smaller meaning-bearing units called morphemes. Morphemes have 2 classes: stems - central part of the word and affixes - (prefixes and suffixes).



The Porter Stemmer

Lemmatisation is hard, that's why sometimes we use stemming.

```
This -> Thi, was -> wa, Bone's -> Bone s, ...
```

Stemming is based on series of rules, eg.: `ATIONAL -> ATE` (relational -> relate). They do make errors, but are fast and deterministic.



Sentence Segmentation

`?`, `!` are unambiguous, `.` is unfortunately ambiguous, it doesn't need to mean sentence end. Rule-based approach or machine learning.



*MInimum Edit Distance* - minimum number of editing operations (add, delete, substitution) needed to transform one string into another.

How to find Minimal Edit Distance? This can be think of as a shortest path problem. Shortest sequence of edits from one string to another. This can be solved using dynamic programming (table-driven method for solving problems by combining solutions to sub-problems). 



#### Chapter 3: N-gram Language Models

Assigning probabilities of upcoming words in a sentence is a very important task in speech recognition, spelling correction, machine translation and AAC systems. Systems that assign probabilities to sequences of models are called **language models**. Simplest model is a n-gram.



*P(w|h)* - the probability of a word *w* given some history *h*.
$$
P(the|its\ water\ is\ so\ transparent\ that) = \dfrac{count(its\ water\ is\ so\ transparent\ that\ the)}{count(its\ water\ is\ so\ transparent\ that)}
$$
You can compute these probabilities for a large corpus, eg. wikipedia. This method works fine in many cases, but it turned out even the web can not give us good estimates in most cases - language is dynamic, you are not able to count ALL the possible sentences. Hence, there is a need for introducing more clever way for estimating the probability *P(w|h)*.

Instead of computing the probability of a word given its entire history, we can approximate the history by just the last few words. The bigram model approximates the probability by taking the last word, so for the example we had earlier (so in general: n-gram takes *n - 1* words into the past, trigrams are most commonly used, 4/5-grams are used when there is sufficient training data):
$$
P(the|its\ water\ is\ so\ transparent\ that) \approx P(the|that)
$$
This assumption, that next word depends on the previous one is called a **Markov** assumption.

Probability of a sentence can be calculated using chain rule of probability:
$$
P(<s>\ i\ want\ english\ food\ </s>) = P(i|<s>)P(want|i)P(english|want)P(food|english)P(</s>|food) =\ ...
$$
Such technique is able to capture eg. cultural things - people more often look for Chinese food than English. Language models are always computed in log format - log probabilities. Why? Probability always fall between 0 and 1, multiplying small float numbers - you end up with numerical underflow, using logarithms you get numbers that are not as small.

*Evaluating Language Models*

Best way to evaluate the performance of a language model is to embed it in an application and measure how much the application improves - **extrinsic evaluation**. However this technique requires running multiple models in order to measure the improvement. Better approach is to use  **intrinsic evaluation** - standard approach from ML, training set and validation (unseen) set. So the better predictions on the test set, the better model you got. Sample from test set can not appear in training set - this introduces bias - probabilities gets too high (unreliable) - huge inaccuracies in perplexity - probability based metric. If a particular test set is used too often, we implicitly tune to its characteristics. 

*Perplexity*

PP for short, metric used for evaluating language model. Perplexity on a test set is the inverse probability of the test set, normalised by the number of words. Minimising perplexity is equivalent to maximising the test set probability according to the language model. 

Another way of thinking about perplexity: weighted average branching factor (branching factor - number of possible next words that can follow any words).

The more information the n-gram gives us about the word sequence, the lower the perplexity (unigram: 962, bigram: 170, trigram: 109).

An intrinsic improvement in perplexity does not guarantee an extrinsic improvement in the performance. In other words: because some metric shows your model is great, it does not mean it will do so great in real life. Perplexity should be confirmed by an end-to-end evaluation of a real task.

*Generalisation and zeros*

N-gram model is highly dependant on the training model, also it does better job as we increase *n*. You need to use similar genres for the training - Shakespearian English is far different from WSJ's English. To build model for translating legal documents you need to train it on legal documents, you need to build a questions answering system, you need to use questions for training. It is important to use appropriate dialects and variety (African American Language, Nigerian English, ...).

Zeros: Imagine you trained a model on a corpus, "denied the: allegations, speculation, rumours, report", but for the test you check phrases like "denied the: offer, loan", model would estimate probability as 0:
$$
P(offer|denied\ the) = 0
$$
This is bad... if you want to calculate perplexity, you would need to divide by zero. Which is kinda problematic. 

So what about words we haven't seen before (open vocabulary -> out of vocabulary words / unknown words)? Add pseudo word `<UNK>`. You can use this tag to replace all the words that occur fewer than some small number *n*.

*Smoothing* (discounting) - process of shaving off a bit of probability mass from some more frequent events and give it to the events we have never seen. There are variety of ways to do smoothing:

- Laplace Smoothing (add-one smoothing) - adds 1 to all bigram counts before we normalise them into probabilities. So all the counts that uses do be 0, becomes 1, 1 will be 2, ... This method is not used in state-of-the-art solutions. Can be treated as a baseline. 
- Add-k smoothing - Instead of adding 1, we add a fractional count eg. 0.5, 0.05, 0.01, ... Useful for some of the applications but still, does not perform perfectly.

Backoff - we can use available knowledge, if you need to computer trigram, maybe bigram can help you with that, or even unigram. Sometimes, this might be sufficient.

Interpolation - mix the probability estimates form all the n-gram estimators

*Kneser-Ney Smoothing* - most commonly used method. It uses following observation: "words that have appeared in more contexts in the past are more likely to appear in some new context as well". The best performing method is a modified Kneser-Ney Smoothing. 

*Huge Language Models and Stupid Backoff*

Google open-sourced their The Web 1 Trillion 5-gram corpus, they released also Google Books Ngrams. There is also COCA. 

Stupid backoff - algorithm for a language model, gives up idea of making the idea of trying to make the model a true probability distribution, no discounting. If a higher-order n-gram has zero count, we simply backoff to a lower order n-gram, this algorithm does not produce a probability distribution. 

#### Chapter 4: Naive Bayes and Sentiment Classification

Many problems can be viewed as classification problems: text categorisation, sentiment analysis, language identification, authorship attribution, period disambiguation, tokenisation, and many more. Goal is to take a sample, extract features and classify the observation. 

*Naive Bayes Classifiers*

Classifiers that make simplified (naive) assumption about how the features interact.

Binary Multinomial Naive Bayes (binary NB) - used for sentiment analysis, clip the word counts in each document at 1 (extract unique words from the documents and count occurrence).

How to deal with negations? I really like this movie (positive), I don't like this movie (negative). Very simple baseline, commonly used is: during text normalisation prepend the prefix *NOT_* to every word after a token of logical negation.

````
i didn't like this movie , but ... -> i didn't NOT_like NOT_this NOT_movie , but ...
````

Chapter 16 will tell more about parsing and relationship between negations.

Sentiment lexicons - lists of words that are pre-annotated with positive or negative sentiment. Popular lexicon: General Inquirer or LIWC. For Naive Bayes you can add a feature "this word occurs in the positive lexicon" instead of counting each words separately. Chapter 20 will tell how lexicons can be learned automatically and other use cases besides sentiment analysis will be shown. 

Spam detection - Naive Bayes + regex + HTML scan

Language identification - Naive Byes but not on the words! Used Character n-grams.

Naive Bayes can be viewed as a language model. 

*Evaluation*

Confusion matrix - table for visualising how an algorithm performs with respect to the human *gold label* (human labeled data - gold labels). Has 2 dimensions - system output and gold labels.

Accuracy - what percentage of all observations our system labelled correctly, doesn't work well for unbalanced classes - eg. 80 negative classes, 20 *positive*, learn to always answer *negative* and you have 80% *accuracy*.

Precision - percentage of the items that the system detected that are in fact positive.

Recall - percentage of the items actually present in the input that were correctly identified by the system.

F-measure - combines both metrics - weighted harmonic mean of precision and recall - conservative metric, closer to the minimum of the two values (comparing to the arithmetic mean).

*Evaluating with more than two classes*

Macro-averaging - compute the performance of each class and then average over classes. Can be dominated by the more frequent class.

Micro-averaging - collect decisions for all classes into a single confusion matrix and then computer precision and recall from that table. Reflects better the statistics for the smaller classes, more appropriate when the performance on all the classes is equally important.

*Test sets and Cross-validation*

Cross validation - when your dataset is not large enough, you can use it all for training and validating by using cross-validation. Process of selecting random training and validation sets, training the classifier, computing the error and the repeating it once again. Usually 10 times.

*Statistical Significance Testing*

We often need to compare the performance of two systems. How can we know one system is better than the another?

*Effect size* - difference between F1-scores.

*Null hypothesis* - we suppose *delta > 0*, we would like to know if we can confidentially rule out this hypothesis. In order to do this, create random variable *X* ranging over all test sets, we ask: how likely is it if the null hypothesis is correct that among these test sets we would encounter the value of *delta* that we found. This likelihood is called *p-value*. We select the threshold - usually small, if we can reject the *null hypothesis* we can tell A is better than B - is *statistically significant*.

*Avoiding harms in classification*

Representational harms - system perpetuating negative stereotypes about social groups.

Toxicity detection - hate speech, abuse, harassment detection. These systems make harm themselves, for example: mark sentences mentioning minorities.

System based on stereotypes can lead to censorship. Also human labeled data can be biased.

It is important to include *model card* when releasing a system. Model card includes: training algorithms and parameters, data sources, intended users and use, model performance across different groups.

#### Chapter 5: Logistic Regression

Logistic regression - one of the most important analytic tools in the social and natural sciences. Baseline supervised machine learning algorithm for classification. Neural network can be seen as a series of logistic regression classifiers stacked on top of each other. This is a discriminative classifier (unlike Naive Bayes - generative classifier - you can literally as such model how for example dog or cat looks like, discriminative model learns only how to distinguish the classes, eg. training set with dogs with collars and cats - when you ask a model what does it know about cats it would respond: it doesn't wear a collar).

Classification: *The Sigmoid*

Sigmoid function - takes a real value (even x -> infinity) and maps it to the range [0, 1].Nearly linear near 0. This is extremely useful for calculating eg. *P(y=1|x)* - belonging to the class.
$$
z = weights\ of \ feature\ vector\ *\ x + bias
$$

$$
P(y=1) = \sigma(z)
$$

*z* - ranges from *-inf* to *+inf*.

Logistic regression can be used for all sorts of NLP tasks, eg. period  disambiguation (deciding if a period is the end of a sentence or part of a word).

*Designing features* - features are generally designed by examining the training set with an eye to linguistic intuitions. 

*Representation learning* - ways to learn features automatically in an unsupervised way from the input.

*Choosing a classifier* - Logistic Regression great at finding correlations.

*Loss / cost function* -  The distance between the system output and the gold output. Gradient descent - optimisation algorithm for updating the weights. It is a method that finds a minimum of a function by figuring out in which direction the function's slope is rising the most steeply.
$$
\theta\ -\ weights,\ in\ the\ case\ of\ logistic\ regression\ \theta = weights,\ bias
$$
*Convex function* - function with one minimum. No local minima to get stuck. Local minima is a problem in training neural networks - non-convex functions.

*Learning rate* - the magnitude of the amount to move in gradient descent (hyper-parameter).

*Hyper-parameters* - special parameters chosen by the algorithm designer that affect how the algorithm works. 

*Batch training* - we compute gradient over the entire dataset, quite expensive to compute. Possibility to use *mini-batch* training, we train on a group of *m* examples (512 or 1024).

*Regularisation* - a good model should generalise well, there is a problem of overfitting it model fits the data too perfectly. There is a possibility to add a regularisation - L1 (lasso regression) and L2 (ridge regression) regularisation. 