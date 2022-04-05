[go back](https://github.com/pkardas/learning)

# Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition

Book by Daniel Jurafsky and James H. Martin (December 2020 draft)

- [Chapter 2: Regular Expressions, Text Normalization, Edit Distance](#chapter-2-regular-expressions-text-normalization-edit-distance)
- [Chapter 3: N-gram Language Models](#chapter-3-n-gram-language-models)
- [Chapter 4: Naive Bayes and Sentiment Classification](#chapter-4-naive-bayes-and-sentiment-classification)
- [Chapter 5: Logistic Regression](#chapter-5-logistic-regression)
- [Chapter 6: Vector Semantics and Embeddings](#chapter-6-vector-semantics-and-embeddings)
- [Chapter 7: Neural Networks and Neural Language Models](#chapter-7-neural-networks-and-neural-language-models)
- [Chapter 8: Sequence Labeling for Parts of Speech and Named Entities](#chapter-8-sequence-labeling-for-parts-of-speech-and-named-entities)
- [Chapter 9: Deep Learning Architectures for Sequence Processing](#chapter-9-deep-learning-architectures-for-sequence-processing)
- [Chapter 10](#chapter-10)
- [Chapter 11: Machine Translation and Encode-Decoder Models](#chapter-11-machine-translation-and-encode-decoder-models)
- [Chapter 12: Constituency Grammars](#chapter-12-constituency-grammars)
- [Chapter 13-16](#chapter-13-16)
- [Chapter 17: Information Extraction](#chapter-17-information-extraction)
- [Chapter 18: Word Senses and WordNet](#chapter-18-word-senses-and-wordnet)
- [Chapter 19](#chapter-19)
- [Chapter 20: Lexicons for Sentiment, Affect and Connotation](#chapter-20-lexicons-for-sentiment-affect-and-connotation)
- [Chapter 21-22](#chapter-21-22)
- [Chapter 23: Question Answering](#chapter-23-question-answering)
- [Chapter 24: Chatbots & Dialogue Systems](#chapter-24-chatbots--dialogue-systems)
- [Chapter 25: Phonetics](#chapter-25-phonetics)
- [Chapter 26: Automatic Speech Recognition and Text-to-speech](#chapter-26-automatic-speech-recognition-and-text-to-speech)

## Chapter 2: Regular Expressions, Text Normalization, Edit Distance

*Regular Expressions*

Regular expression is an algebraic notation for characterising a set of strings.

Kleene * (cleany star) - zero or more occurrences.

Kleene + - at least one

Anchors - special characters that *anchor* regular expressions to particular places in a string (`^` - start, `$` - end
of a string).

`^` has multiple meanings:

1. match start of the line
2. negation inside square brackets `[^Ss]` - neither `S` nor `s`

Pipe symbol `|` also known as "disjunction". Logical OR. `cat|dog` match either `cat` or `dog`.

Operator precedence hierarchy:

1. Parenthesis: `()`
2. Counters: `* + ? {}`, `{}` - explicit counter
3. Sequences and anchors: `sequence ^the end$`
4. Disjunction: `|`

Regular expressions are greedy, however there is a way to enforce non-greedy behaviour -> `*?` - Kleene star that
matches as little text as possible, `+?` - Kleene plus that matches as little text as possible.

Fixing RE errors might require following efforts:

- Increasing precision (minimising false positives - incorrectly matched)

- Increasing recall (minimising false negatives - incorrectly missed)

*Substitution* - easiest to explain with an example:

```
the (.*)er they were, the \1er they will be
--- will match ---
the bigger they were, the bigger they will be
```

Number operator, e.g.: `\1` allows repeating matched group. So parenthesis operator not only allows to group but also
store in a numbered register. It is possible to disable register and use non-capturing group,
e.g.: `(:?some: a few) (people|cats) like some \1`. Famous chatbot ELIZA used a series of regular expressions
substitutions.

```
I'M (depressed|sad) -> I AM SORRY TO HEAR YOU ARE \1
```

Look ahead - look ahead in the text to see if some pattern matches BUT not advance the match cursor.

Negative lookahead - used for ruling out special cases, e.g. rule out strings starting with word
Volcano: `(?!Volcano)[A-Za-z]+`

*Words*

Fragment - broken-off word, "I do main- mainly", "main-" is a fragment here

Filler - "um, uh" - used in spoken language, problem: should be treated as a word? Fragment and fillers are 2 kinds of
disfluencies.

Type - number of distinct words in a corpus. When we speak about number of words in the language, we are generally
referring to word types.

Herdan's Law/Heap's Law - relationship between number of types (`|V|`) and number of tokens (`N`) in the corpora:
$$ |V| = kN^{\beta} $$
(k and 0 < B < 1 are constants)

*Corpora*

Writers, speakers have specific styles of communicating, use specific dialects, text can vary by time, place, function,
race, gender, age, socioeconomic class.

Code switching - common practice for speakers and writers to use multiple languages in single communicative act

When preparing a computational models for language processing it is useful to prepare data-sheet, document answering
questions like: Who produced the text? In what context? For what purpose? In what language? What was race, gender, ...
of the authors? How data was annotated?

*Text Normalisation*

1. Tokenisation (segmentation)
2. Normalising word formats
3. Segmenting sentences

*Tokenisation*

UNIX's `tr` command can be used for quick tokenisation of English texts.

Problem: Keep specific words together: `2020/02/02`, `km/h`, `$65`, `www.github.com`, `100 000`, `I'm`, `New York`

Tokeniser can be used to expand clitic contractions: `we're -> we are`. Tokenisation is tied up with Named Entity
Recognition. Tokenisation needs to be fast, hence often uses deterministic algorithms based on regular expressions
compiled into efficient finite state automata. Tokenisation is more complex for e.g.: Chinese or Japanese (languages not
using spaces for separating words). For Japanese algorithms like words segmentation work better. Also, it is possible to
use neural networks for the task of tokenisation.

Penn Treebank Tokeniser

- separates clitics (`doesn't -> does n't`)
- keeps hyphenated words together (`close-up`, `Bielsko-Biała`)
- separates out all punctuation

Byte-Pair Encoding

- begins with a vocabulary that is set of all individual characters
- examines training corpus, chooses the two symbols that are most frequently adjacent (A, B -> AB)
- continues to count and merge, creating longer and longer character strings, until k merges (parameter of the
  algorithm)
- most words will be represented as full symbols, few rare will have to be represented by their parts

*Normalisation*

Task of putting words in a standard format, choosing a single normal form for words with multiple forms like the USA/US.
Valuable proces despite spelling information is lost.

Case folding - mapping everything to lower/upper case. However, might give wrong results, e.g.: US (country) -> us (
people, we)

*Lemmatisation*

Task of determining that two words have the same root (am, are, is -> be). Useful for web search - usually we want all
forms to be found. Requires morphological parsing of the word. Morphology is the study of the way words are built up
from smaller meaning-bearing units called morphemes. Morphemes have 2 classes: stems - central part of the word and
affixes - (prefixes and suffixes).

The Porter Stemmer

Lemmatisation is hard, that's why sometimes we use stemming.

```
This -> Thi, was -> wa, Bone's -> Bone s, ...
```

Stemming is based on series of rules, e.g.: `ATIONAL -> ATE` (relational -> relate). They do make errors, but are fast
and deterministic.

Sentence Segmentation

`?`, `!` are unambiguous, `.` is unfortunately ambiguous, it doesn't need to mean sentence end. Rule-based approach or
machine learning.

*Minimum Edit Distance* - minimum number of editing operations (add, delete, substitution) needed to transform one
string into another.

How to find Minimal Edit Distance? This can be thought of as the shortest path problem. Shortest sequence of edits from
one string to another. This can be solved using dynamic programming (table-driven method for solving problems by
combining solutions to sub-problems).

## Chapter 3: N-gram Language Models

Assigning probabilities of upcoming words in a sentence is a very important task in speech recognition, spelling
correction, machine translation and AAC systems. Systems that assign probabilities to sequences of models are called **
language models**. Simplest model is an n-gram.

*P(w|h)* - the probability of a word *w* given some history *h*. $$ P(the|its\ water\ is\ so\ transparent\ that) =
\dfrac{count(its\ water\ is\ so\ transparent\ that\ the)}{count(its\ water\ is\ so\ transparent\ that)} $$ You can
compute these probabilities for a large corpus, e.g. wikipedia. This method works fine in many cases, but it turned out
even the web can not give us good estimates in most cases - language is dynamic, you are not able to count ALL the
possible sentences. Hence, there is a need for introducing more clever way for estimating the probability *P(w|h)*.

Instead of computing the probability of a word given its entire history, we can approximate the history by just the last
few words. The bigram model approximates the probability by taking the last word, so for the example we had earlier (so
in general: n-gram takes *n - 1* words into the past, trigrams are most commonly used, 4/5-grams are used when there is
sufficient training data):
$$ P(the|its\ water\ is\ so\ transparent\ that) \approx P(the|that)
$$ This assumption, that next word depends on the previous one is called a **Markov** assumption.

Probability of a sentence can be calculated using chain rule of probability:
$$ P(<s>\ i\ want\ english\ food\ </s>) = P(i|<s>)P(want|i)P(english|want)P(food|english)P(</s>|food) =\ ... $$ Such
technique is able to capture e.g. cultural things - people more often look for Chinese food than English. Language
models are always computed in log format - log probabilities. Why? Probability always fall between 0 and 1, multiplying
small float numbers - you end up with numerical underflow, using logarithms you get numbers that are not as small.

*Evaluating Language Models*

Best way to evaluate the performance of a language model is to embed it in an application and measure how much the
application improves - **extrinsic evaluation**. However, this technique requires running multiple models in order to
measure the improvement. Better approach is to use  **intrinsic evaluation** - standard approach from ML, training set
and validation (unseen) set. So the better predictions on the test set, the better model you got. Sample from test set
can not appear in training set - this introduces bias - probabilities gets too high (unreliable) - huge inaccuracies in
perplexity - probability based metric. If a particular test set is used too often, we implicitly tune to its
characteristics.

*Perplexity*

PP for short, metric used for evaluating language model. Perplexity on a test set is the inverse probability of the test
set, normalised by the number of words. Minimising perplexity is equivalent to maximising the test set probability
according to the language model.

Another way of thinking about perplexity: weighted average branching factor (branching factor - number of possible next
words that can follow any words).

The more information the n-gram gives us about the word sequence, the lower the perplexity (unigram: 962, bigram: 170,
trigram: 109).

An intrinsic improvement in perplexity does not guarantee an extrinsic improvement in the performance. In other words:
because some metric shows your model is great, it does not mean it will do so great in real life. Perplexity should be
confirmed by an end-to-end evaluation of a real task.

*Generalisation and zeros*

N-gram model is highly dependant on the training model, also it does better job as we increase *n*. You need to use
similar genres for the training - Shakespearian English is far different from WSJ's English. To build model for
translating legal documents you need to train it on legal documents, you need to build a questions answering system, you
need to use questions for training. It is important to use appropriate dialects and variety (African American Language,
Nigerian English, ...).

Zeros: Imagine you trained a model on a corpus, "denied the: allegations, speculation, rumours, report", but for the
test you check phrases like "denied the: offer, loan", model would estimate probability as 0:
$$ P(offer|denied\ the) = 0 $$ This is bad... if you want to calculate perplexity, you would need to divide by zero.
Which is kinda problematic.

So what about words we haven't seen before (open vocabulary -> out of vocabulary words / unknown words)? Add pseudo
word `<UNK>`. You can use this tag to replace all the words that occur fewer than some small number *n*.

*Smoothing* (discounting) - process of shaving off a bit of probability mass from some more frequent events and give it
to the events we have never seen. There are variety of ways to do smoothing:

- Laplace Smoothing (add-one smoothing) - adds 1 to all bigram counts before we normalise them into probabilities. So
  all the counts that uses do be 0, becomes 1, 1 will be 2, ... This method is not used in state-of-the-art solutions.
  Can be treated as a baseline.
- Add-k smoothing - Instead of adding 1, we add a fractional count e.g. 0.5, 0.05, 0.01, ... Useful for some of the
  applications but still, does not perform perfectly.

Backoff - we can use available knowledge, if you need to computer trigram, maybe bigram can help you with that, or even
unigram. Sometimes, this might be sufficient.

Interpolation - mix the probability estimates form all the n-gram estimators

*Kneser-Ney Smoothing* - most commonly used method. It uses following observation: "words that have appeared in more
contexts in the past are more likely to appear in some new context as well". The best performing method is a modified
Kneser-Ney Smoothing.

*Huge Language Models and Stupid Backoff*

Google open-sourced their The Web 1 Trillion 5-gram corpus, they released also Google Books Ngrams. There is also COCA.

Stupid backoff - algorithm for a language model, gives up idea of making the idea of trying to make the model a true
probability distribution, no discounting. If a higher-order n-gram has zero count, we simply backoff to a lower order
n-gram, this algorithm does not produce a probability distribution.

## Chapter 4: Naive Bayes and Sentiment Classification

Many problems can be viewed as classification problems: text categorisation, sentiment analysis, language
identification, authorship attribution, period disambiguation, tokenisation, and many more. Goal is to take a sample,
extract features and classify the observation.

*Naive Bayes Classifiers*

Classifiers that make simplified (naive) assumption about how the features interact.

Binary Multinomial Naive Bayes (binary NB) - used for sentiment analysis, clip the word counts in each document at 1 (
extract unique words from the documents and count occurrence).

How to deal with negations? I really like this movie (positive), I don't like this movie (negative). Very simple
baseline, commonly used is: during text normalisation prepend the prefix *NOT_* to every word after a token of logical
negation.

````
i didn't like this movie , but ... -> i didn't NOT_like NOT_this NOT_movie , but ...
````

Chapter 16 will tell more about parsing and relationship between negations.

Sentiment lexicons - lists of words that are pre-annotated with positive or negative sentiment. Popular lexicon: General
Inquirer or LIWC. For Naive Bayes you can add a feature "this word occurs in the positive lexicon" instead of counting
each words separately. Chapter 20 will tell how lexicons can be learned automatically and other use cases besides
sentiment analysis will be shown.

Spam detection - Naive Bayes + regex + HTML scan

Language identification - Naive Byes but not on the words! Used Character n-grams.

Naive Bayes can be viewed as a language model.

*Evaluation*

Confusion matrix - table for visualising how an algorithm performs with respect to the human *gold label* (human labeled
data - gold labels). Has 2 dimensions - system output and gold labels.

Accuracy - what percentage of all observations our system labelled correctly, doesn't work well for unbalanced classes -
e.g. 80 negative classes, 20 *positive*, learn to always answer *negative* and you have 80% *accuracy*.

Precision - percentage of the items that the system detected that are in fact positive.

Recall - percentage of the items actually present in the input that were correctly identified by the system.

F-measure - combines both metrics - weighted harmonic mean of precision and recall - conservative metric, closer to the
minimum of the two values (comparing to the arithmetic mean).

*Evaluating with more than two classes*

Macro-averaging - compute the performance of each class and then average over classes. Can be dominated by the more
frequent class.

Micro-averaging - collect decisions for all classes into a single confusion matrix and then computer precision and
recall from that table. Reflects better the statistics for the smaller classes, more appropriate when the performance on
all the classes is equally important.

*Test sets and Cross-validation*

Cross validation - when your dataset is not large enough, you can use it all for training and validating by using
cross-validation. Process of selecting random training and validation sets, training the classifier, computing the error
and the repeating it once again. Usually 10 times.

*Statistical Significance Testing*

We often need to compare the performance of two systems. How can we know one system is better than the another?

*Effect size* - difference between F1-scores.

*Null hypothesis* - we suppose *delta > 0*, we would like to know if we can confidentially rule out this hypothesis. In
order to do this, create random variable *X* ranging over all test sets, we ask: how likely is it if the null hypothesis
is correct that among these test sets we would encounter the value of *delta* that we found. This likelihood is called *
p-value*. We select the threshold - usually small, if we can reject the *null hypothesis* we can tell A is better than B

- is *statistically significant*.

*Avoiding harms in classification*

Representational harms - system perpetuating negative stereotypes about social groups.

Toxicity detection - hate speech, abuse, harassment detection. These systems make harm themselves, for example: mark
sentences mentioning minorities.

System based on stereotypes can lead to censorship. Also, human labeled data can be biased.

It is important to include *model card* when releasing a system. Model card includes: training algorithms and
parameters, data sources, intended users and use, model performance across different groups.

## Chapter 5: Logistic Regression

Logistic regression - one of the most important analytic tools in the social and natural sciences. Baseline supervised
machine learning algorithm for classification. Neural network can be seen as a series of logistic regression classifiers
stacked on top of each other. This is a discriminative classifier (unlike Naive Bayes - generative classifier - you can
literally as such model how for example dog or cat looks like, discriminative model learns only how to distinguish the
classes, e.g. training set with dogs with collars and cats - when you ask a model what does it know about cats it would
respond: it doesn't wear a collar).

Classification: *The Sigmoid*

Sigmoid function - takes a real value (even x -> infinity) and maps it to the range [0, 1]. Nearly linear near 0. This
is extremely useful for calculating e.g. *P(y=1|x)* - belonging to the class. $$ z = weights\ of \ feature\ vector\ *\ x

+ bias $$

$$ P(y=1) = \sigma(z)
$$

*z* - ranges from *-inf* to *+inf*.

Logistic regression can be used for all sorts of NLP tasks, e.g. period disambiguation (deciding if a period is the end
of a sentence or part of a word).

*Designing features* - features are generally designed by examining the training set with an eye to linguistic
intuitions.

*Representation learning* - ways to learn features automatically in an unsupervised way from the input.

*Choosing a classifier* - Logistic Regression great at finding correlations.

*Loss / cost function* - The distance between the system output and the gold output. Gradient descent - optimisation
algorithm for updating the weights. It is a method that finds a minimum of a function by figuring out in which direction
the function's slope is rising the most steeply. $$ \theta\ -\ weights,\ in\ the\ case\ of\ logistic\ regression\ \theta
= weights,\ bias $$
*Convex function* - function with one minimum. No local minima to get stuck. Local minima is a problem in training
neural networks - non-convex functions.

*Learning rate* - the magnitude of the amount to move in gradient descent (hyper-parameter).

*Hyper-parameters* - special parameters chosen by the algorithm designer that affect how the algorithm works.

*Batch training* - we compute gradient over the entire dataset, quite expensive to compute. Possibility to use *
mini-batch* training, we train on a group of *m* examples (512 or 1024).

*Regularisation* - a good model should generalise well, there is a problem of overfitting it model fits the data too
perfectly. There is a possibility to add a regularisation - L1 (lasso regression) and L2 (ridge regression)
regularisation.

*Multinomial logistic regression* (*softmax* regression) - for classification problems with more than 2 classes. The
multinomial logistic classifier uses a generalisation of the sigmoid function called softmax function.

*Model interpretation* - Often we want to know more than just the result of classification, we want to know why
classifier made certain decision. Logistic regression is interpretable.

## Chapter 6: Vector Semantics and Embeddings

*Distributional hypothesis* - the link between similarity in how words are distributed and similarity.

*Lemma / citation* form - basic form of a word. *Wordform* - inflected lemma. Lemma can have multiple meanings, e.g.
mouse might refer to a rodent or to a pointer, each of these are called word senses. Lemmas can be polysemous (have
multiple senses), this makes interpretation difficult. Word sense disambiguation - the task of determining which sense
of a word is being used in particular context.

*Synonyms* - two words are synonymous if they are substitutable - have the same propositional meaning.

*Principle of contrast* - a difference in linguistic form is always associated with some difference in meaning, e.g.:
water / H2O, H2O - rather used in scientific context.

*Word similarity* - *cat* is not a synonym of a *dog*, but these are 2 similar words. There are many human-labelled
datasets for this.

*Word relatedness* - (or association) e.g.: *coffee* is not similar to *cup*, they shave ro similar features, but they
are very related - associated, they co-exist. Very common kind of relatedness is semantic field, e.g.: *surgeon,
scalpel, nurse, hospital*. Semantic fields are related to topic models like LDa - Latent Dirichlet Allocation -
unsupervised learning on large sets of texts to induce sets of associated words from text. There are more relations
between words:
hypernymy, antonymy or meronymy.

*Semantic Frames and Roles* - a set of words that denote perspectives or participants in a particular type of event,
e.g.: *Ling sold the book to Sam* - seller / buyer relation. Important problem in question answering.

*Connotation* - affective meaning - emotions, sentiment, opinions or evaluations.

*Sentiment* - valence - the pleasantness of the stimulus, arousal - the intensity of emotion provoked by the stimulus,
dominance - the degree of control exerted by the stimulus. In 1957 Osgood used these 2 values to represent a word -
revolutionary idea! Word embedded in 3D space.

*Vectors semantics*. Word's meaning can be defined by its distribution in language - use neighbouring words. Idea of
vector semantics is to represent a word as a point in a multidimensional semantic space (word embedding) that is derived
from the distributions of word neighbours.

*Information retrieval* - the task of finding the document *d* from the *D* documents in some collection that best
matches a query *q*.

*Cosine* - similarity metric between 2 words (angle between 2 vectors)

*TF-IDF* - Raw frequencies - not the best way to measure association between words (a lot of noise from words like *the,
it, they, ...*). Term Frequency - the frequency of a word *t* in document *d*. The second factor gives higher weights to
words that occur only in a few documents.

*PMI* - Point-wise Mutual Information - measure how often 2 events occur, compared with what we would expect if they
were independent. A useful tool whenever we need to find words that are strongly associated. It is more common to use
PPMI. Very rare words tend to have very high PMI.

*Word2vec* - dense word embedding, the intuition of word2vec is that instead of counting how often each word *w* occurs
near word *u*, we train a classifier on a binary classification task: "Is word *w* likely to show up near word *u*?". We
can use running text as supervised training data. - this is called self-supervised training data.

Visualising embeddings - visualise the meaning of a word embedded in space by listing the most similar words, clustering
algorithms and the most important method - dimensionality projection, e.g. t-SNE.

*First-order co-occurrence / Syntagmatic association* - if words are near each other, e.g. *wrote* and *book*.

*Second-order co-occurrence / Paradigmatic association* - if words have similar neighbours, e.g. *wrote*, *said*

*Representational harm*. Embeddings are capable of capturing bias and stereotypes. More, they are capable of amplifying
bias.

## Chapter 7: Neural Networks and Neural Language Models

Neural network share much of the same mathematics as logistic regression, but NNs are more powerful classifier than
logistic regression. Neural networks can automatically learn useful representations of the input.

*Unit* - takes a set of real values numbers as input, performs some computations on them and produces an output. Is
taking weighted sum of inputs + bias. Output of this function is called an activation. $$ y = a = f(z) = f(w \cdot x +
b)
$$
*f* - e.g. sigmoid, tanh, ReLU. Sigmoid most commonly used for teaching. Tanh is almost always better than sigmoid.
ReLU (rectified linear unit) - most commonly used and the simplest.

*The (famous) XOR problem* - Minsky proved it is not possible to build a perceptron (very simple neural unit that has a
binary output and does not have a non-linear activation function) to compute logical XOR. However, it can be computed
using a layered neural network.

*Feed-Forward Neural Network*. Multi-layer network, units are connected without cycles. Sometimes called multi-layer
perceptrons for historical reasons, modern networks aren't perceptrons (aren't linear). Simple FFNN have 3 types of
nodes: input units, hidden units and output units. The core of the neural network is the hidden layer formed of hidden
units. Standard architecture is that each layer is fully connected - each unit in each layer takes all the outputs from
the previous layer.

Purpose of learning is to learn weights and bias on each layer. *Loss function* - the distance between the system output
and the gold output, e.g. cross-entropy loss. To find the parameters that minimise this loss function, we use for
example *gradient descent*. Gradient descent requires knowing the gradient of the loss function with respect to each of
the parameters. Solution for computing this gradient is error back-propagation.

Language modeling - predicting upcoming words from prior word context - neural networks are perfect at this task. Much
better than *n-gram* models - better generalisation, higher accuracy, on the other hand - much slower to train.

## Chapter 8: Sequence Labeling for Parts of Speech and Named Entities

*Named entity* - e.g. Marie Curie, New York City, Stanford University, ... important for many natural language
understanding tasks (e.g. sentiment towards specific product, question answering). Generally speaking, anything that can
be referred to with a proper name (person, location, organisation). Possible output tags: PER (person), LOC (location),
ORG (organisation) and GPE (geopolitical entity).

*POS/Part of Speech* - knowing if a word is noun or verb tells us about likely neighbouring words. They fall into 2
categories: closed class and open class. POS-tagging is the process of assigning a part-of-speech to each word in a
text. Tagging is a disambiguation task. Words are ambiguous, one can have more than one POS e.g. book flight, hand me
that book, ... The goal is to resolve these ambiguities. The accuracy of POS tagging algorithms is very high +97%. Most
Frequent Class Baseline - effective, baseline method, assign token to the class that occurs most often in the training
set.

Markov chain - a model that tells about the probabilities of sequences of random variables. A Markov chain makes a very
strong assumption - if you want to predict future sentence, all that matters is the current state. Formally a Markov
chain is specified by: set of *N* states, a transition probability matrix and initial probability distribution.

The Hidden Markov Model - allows talking about both observed events (words seen in the input) and hidden events (
part-of-speech tags). Formally HMM is specified by: set of *N* states, a transition probability, observations,
observation likelihoods / emission probabilities (probability of an observation begin generated from a state *q*) and
initial probability distribution.

HMM is a useful and powerful model, but needs a number of augmentations to achieve high accuracy. CFR is a log-linear
model that assigns a probability to an entire output sequence. We can think of a CRF as like a giant version of what
multinomial logistic regression does for a single token.

Gazetteer - list of place names, millions of entries for locations with detailed geographical and political information,
e.g. https://www.geonames.org/

POS tags are evaluated by accuracy. NERs are evaluated using recall, precision and F1.

Named Entity Recognition is often based on rule based approaches.

## Chapter 9: Deep Learning Architectures for Sequence Processing

Language is inherently temporal phenomenon. This is hard to capture using standard machine learning models.

*Perplexity* - a measure of model quality, perplexity of a model with respect to an unseen test set is the probability
the model assigns to it, normalised by its length.

*RNN - Recurrent Neural Network* - any network that contains a cycle within its network connections. Any network where
the value of a unit is directly or indirectly dependent on its own earlier outputs as an input. Within RNNs there are
constrained architectures that have proven to be extremely effective.

*Elman Networks / Simple Recurrent Networks* - very useful architecture, also serves as the basis for more complex
approaches like LSTM (Long Short-Term Memory). RNN can be illustrated as a feedforward network. New set of weights that
connect the hidden layer from the previous time step to the current hidden layer determine how the network makes the use
of past context in calculating the output for the current input.

RNN-based language models process sequences a word at a time, attempting to predict the next word in a sequence by using
the current word and the previous hidden state as inputs.

RNNs can be used for many other tasks:

- sequence labeling - task is to assign a label chosen from a small fixed set of labels to each element of a sequence (
  e.g. POS tagging or named entity recognition). Inputs for RNN are word embeddings and the outputs are tag
  probabilities generated by softmax layer.
- sequence classification - e.g. sentiment analysis, spam detection, message routing for customer support applications.

Stacked RNN - multiple networks where the output of one layer serves as the input to a subsequent layer. They very often
outperform single-layer networks, mainly because stacked layers are able to have different level of abstractions across
layers. Optimal number of layers is application-dependant.

Bidirectional RNN = forward and backward networks combined. In these 2 independent networks input is processed form the
start to the end and from the end to the start. Also, very effective for sequence classification.

It is difficult to train RNNs for tasks that require a network to make use of information distant from the current point
of processing. RNNs can not carry forward critical information because of hidden layers and because they are fairly
local.

LSTM - Long Short-Term Memory - divide the context management problem into two sub-problems:

- removing information no longer needed from the context
- adding information likely to be needed for later decision-making

LSTM is capable of mitigating the loss of distant information. However, there are still RNNs, so relevant information
can be lost.

Transformers - approach to sequence processing that eliminates recurrent connections and returns to architectures
reminiscent of the fully connected networks. Transformers are made up of stacks of networks of the same length of simple
linear layers, feedforward networks and custom connections.

Transformers use *self-attention layers* - they allow network to directly extract and use information from arbitrarily
large contexts without the need to pass it through intermediate recurrent connections as in RNNs.

At the core of an attention-based approach is the ability to compare an item of the interest to a collection of other
items in way that reveals their relevance in the current context.

It turns out, language models can generate toxic language. Many models are trained on data from Reddit (majority of
young, males - not representative). Language model can also leak information about training data - meaning it can be
attacked.

## Chapter 10

Missing chapter.

## Chapter 11: Machine Translation and Encode-Decoder Models

Machine translation - the use of computers to translate from one language to another. The most common use of machine
translation is information access - when you want to for example translate some instructions on the web. Also, often
used in CAT - Computer-Aided Translation, where computer produces draft translation and then human fixes it in
post-editing. Last but not least, useful in human communication needs.

Standard algorithm for MT is encoder-decoder network (can be implemented with RNNs or with Transformers). They are
extremely successful in catching small differences between languages.

Some aspects of human language seem to be universal - true for every or almost every language, for example every
language have words for referring to people, eating or drinking. However, many languages differ what causes translation
divergences.

German, French, English and Mandarin are all SVO (Subject-Verb-Object) languages. Hindi and Japanese are SOV languages.
Irish and Arabic are VSO languages. VO languages generally have prepositions, OV languages generally have postpositions.

Machine Translation and Words Sense Disambiguation problems are closely linked.

Encode-decoder (sequence-to-sequence) networks are models capable of generating contextually appropriate, arbitrary
length, output sequences. Encoder (LSTM, GRU, convolutional networks, Transformers) takes an input sequence and creates
a contextualised representation of it, then representation is passed to decoder (any kind of sequence architecture)
which generates a task-specific output sequence.

Machine translation raises many ethical of the same issues that we have discussed previously. MT systems often assign
gender according to culture stereotypes. Some reaserch found that MY systems perform worse when they are asked to
translate sentences that describe people with non-stereotypical gender roles.

## Chapter 12: Constituency Grammars

Syntactic constituency is the idea that groups of words can behave as single units.

The most widely used formal system for modeling constituent structure in English is Context-Free Grammar, also called
Phrase-Structure Grammars, and the formalism is equivalent to Backus-Naur Form (BNF). A context-free grammar consist of
a set of rules or productions, each of which expresses the ways that symbols of the language can be grouped and ordered
together.

Treebank - parse tree.

## Chapter 13-16

Skipped for now.

## Chapter 17: Information Extraction

Information extraction - turns the unstructured information embedded in texts into structured data - e.g. relational
database to enable further processing.

Relation extraction - finding and classifying semantic relations among the text entities. These are often binary
relations - child of, employment, part-whole. Task of NER is extremely useful here. Wikipedia also offers large supply
of relations.

RDF - Resource Description Framework - tuple of entry-relation-entry. DBPedia was derived from Wikipedia and contains
over 2 bilion RDF triples. Freebase - part of Wikidata, has relations between people and their nationality or locations.

There are 5 main classes of algorithms for relation extraction:

- handwritten patterns - high-precision and can be tailored to specific domains, however low recall and a lot of work
- supervised machine learning - for all entity pairs determine if are in relation
- semi-supervised machine learning (bootstrapping and via distant supervision) - bootstrapping proceeds by taking the
  entities in the seed pair and then finding sentences that contain both entities.
- unsupervised

For unsupervised and semi-supervised approaches it is possible to calculate estimated metrics (like estimated precision)
.

Knowledge graphs - dataset of structured relational knowledge.

Event extraction - task of identification mentions of events in texts. In English most events correspond to verbs and
most verbs introduce events (United Airlines SAID, prices INCREASED, ...). Some noun phrases can also denote events (
the increase, the move, ...).

With extracted events and extracted temporal expressions, events from text can be put on a timeline. Determining
ordering can be viewed as a binary relation detection and classification task.

Event coreference - is needed to figure out which event mentions in a text refer to the same event.

Extracting time - temporal expressions are used to determine when the events in a text happened. Dates in text need to
be normalised.

- relative: yesterday, next semester
- absolute: date
- durations

Temporal expressions task consists of finding the start and the end of all the text spans that correspond to such
temporal expressions. Such task can use rule-based approach.

Temporal Normalisation - process of mapping a temporal expressions to either a specific point in time or to a duration.

Template filling - the task of describing stereotypical or recurring events.

## Chapter 18: Word Senses and WordNet

Ambiguity - the same word can be used to mean different things. Words can be polysemous - have many meanings.

Word sense is a discrete representation of one aspect of the meaning of a word. Meaning can be expressed as an
embedding, for example embedding that represents the meaning of a word in its textual context. Alternative for
embeddings are glosses - written for people, a gloss is just a sentence, sentence can be embedded. Other way of defining
a sense is through relationships ("right" is opposite to "left").

Relations between senses:

- synonymy - when two senses of two different words are (almost) identical - couch / sofa, vomit / throw up
- antonymy - when two words have an opposite meaning - long / short, fast / slow
- hyponym / subordinate - when one word is more specific than the other word - car (hyponym) -> vehicle
- hypernym / superordinate- when one word is more general than the other word - vehicle (hypernym) -> car
- meronymy - when one word describes part of the other word - wheel (meronym) -> car
- holonym - opposite to meronym - car (holonym) -> wheel
- metonymy - the use of one aspect of a concept to refer to other aspects of the entity - Jane Austen wrote Emma (
  author) <-> I really love Jane Austen (works of author),

WordNet - a large online thesaurus, a database that represents word senses. WordNet also represents relations between
senses (is-a, part-whole). The relation between two senses is important in language understanding, for example -
antonymy - words with opposite meaning.

English WordNet has 3 separate databases (nouns, verbs, adjectives and adverbs).

Synset - (Synonym Set) - the set of near-synonyms for a WordNet sense. Glosses are properties of a synset.

Word Sense Disambiguation - the task of determining which sense of a word is being used in a particular context. WSD
algorithms take as input some word and context and output the correct word sense.

Lexical sample tasks - small pre-selected set of target words and an inventory of senses. All-words task (harder
problem) - the system is given an entire texts and a lexicon with an inventory of senses for each entry, and we have
disambiguate every word in the text.

The best WSD algorithm is simple 1-nearest-neighbour algorithm using contextual word embeddings.

There are also feature-based algorithms for WSD - POS-tags, n-grams (3-gram most commonly used), weighted average of
embeddings - passed to SVM classifier

The Lesk algorithm - the oldest and the most powerful knowledge-based WSD metod and useful baseline. Lest is a family of
algorithms that choose the sense whose dictionary gloss or definition shares the most words with the target word's
neighbourhood.

BERT - uses contextual embeddings.

Word Sense Induction - unsupervised approach, we don't use human-defined word senses, instead, the set of senses of each
word is created automatically from the instances of each word in the training set.

## Chapter 19

Skipped for now.

## Chapter 20: Lexicons for Sentiment, Affect and Connotation

Connotation - the aspect of word's meaning that are related to a writer or reader's emotions, sentiment, opinions or
evaluations.

Emotion - (by Scherer) relatively brief episode of response to the evaluation of an external or internal event as being
of major significance. Detecting emotions has the potential to improve a number of language processing tasks - detecting
emotions in reviews, improve conversation systems, depression detection.

Basic emotions proposed by Ekman - surprise, happiness, anger, fear, disgust, sadness

Basic emotions proposed by Plutchik - joy-sadness, anger-fear, trust-disgust, anticipation-surprise.

Most models include 2-3 dimensions:

- valence - the pleasantness of the stimulus
- arousal - the intensity of emotion provoked by stimulus
- dominance - the degree of control exerted by the stimulus

The General Inquirer - the oldest lexicon of 1915 positive words and 2291 negative words. The NRC Valence, Arousal and
Dominance scores 20 000 words (this model assigns valence, arousal and dominance). The NC WordEmotion Association
Lexicon uses Plutchik's basic emotions to describe 14 000 words. There are many more lexicons.

Best-worst scaling - method used in crowdsourcing, annotators are given N items and are asked which item is the best and
which item is the worst.

Detecting peron's personality from their language can be useful for dialog systems. Many theories of human personality
are based around a small number of dimensions:

- extroversion vs introversion - sociable, assertive vs aloof, reserved, shy
- emotional stability vs neurocriticism - calm, unemotional vs insecure, anxious
- agreeableness vs disagreeableness - friendly, cooperative vs antagonistic, fault-finding
- conscientiousness vs unconscientiousness - self-disciplined, organised vs inefficient, careless
- openness to experience - intellectual, insightful s shallow, unimaginative

Connotation frames - express richer relations ot affective meaning that a predicate encodes about its arguments -
Country A violated the sovereignty of Country B.

## Chapter 21-22

Skipped for now.

## Chapter 23: Question Answering

Two major paradigms of question answering:

- information retrieval
- knowledge-based

Factoid questions - questions that can be answered with simple facts expressed in short texts, like: Where is the Louvre
Museum located?

Information retrieval. The resulting IR system is often called a search engine. Ad hoc retrieval, user poses a query to
a retrieval system, which then returns an ordered set of documents from some collection.

Basic IR system architecture uses the vector space, queries and documents are mapped to vector, then cosine similarity
is being used to rank potential documents answering the query. This is an example of the bag-of-words model. However, we
don't use raw word counts in IR, instead we use TD-IDF.

TD-IDF - The term frequency tells us how frequent the word is, words that occur more often are likely to be informative
about the document's contest. However, terms that occur across all documents aren't useful. In such case inverse
document frequency comes handy.

Documents scoring - we score document d by the cosine of its vector d with the query vector q. $$ score(q, d) = cos(q *
d) = \frac{q*d}{|q|*|d|} $$ More commonly used version of the score (because queries are usually short):
$$ score(q, d) =\sum \frac{tf-idf(t,d)}{|d|} $$ Slightly more complex version of TF-IDF is called BM25.

In the past it was common to remove high-frequency words from query and the document. The list of such high-frequency
words to be removed is called a stop list (the, a, to, ...). Worth to know, however not commonly used recently because
of much better mechanisms.

Inverted index - given a query term, gives a list of documents that contain the term.

TF-IDF / BM25 have conceptual flaw - they work only if there is exact overlap of words between the query and document -
vocabulary mismatch problem. Solution to this is to use synonymy - instead of using word-count, use embeddings. Modern
methods use encoders like BERT.

The goal of IR-based QA (open domain QA) is to answer a user's question by finding short text segments from the web or
some document collection.

Datasets:

- SQuAD - Stanford Question Answering Dataset - contains passages form Wikipedia and associated questions.

- HotpotQA - is the dataset that was created by showing crowd workers multiple context documents and asked to come up
  with questions that require reasoning about all the documents.

- TriviaQA - questions written by trivia enthusiasts, question-answer-evidence triples
- The Natural Questions - real anonymised queries to the Google search engine, annotators were presented a query along
  with Wikipedia page from the top 5 results
- TyDi QA - questions from diverse languages

Entity linking - the task of associating a mention in text with the representation of some real-word entity in an
ontology (e.g. Wikipedia).

Knowledge-based question answering - idea of answering a question by mapping it to a query over a structured database.

RDF triples - a tuple of 3 elements: subject, predicate and object, e.g. (Ada Lovelace, birth-year, 1815). This can be
used to perform queries: "When was Ada Lovelace born?" - birth-year(Ada Lovelace, ?).

Second kind uses a semantic parser to map the question to a structured program to produce an answer.

Another alternative is to query a pretrained model, forcing model to answer a question solely from information stored in
its parameters.

T5 is an encoder-decoder architecture, in pretraining it learns to fill in masked spans of task by generating missing
spans in the decoder. It is then fine-tuned on QA datasets, given the question without adding any additional context or
passages.

Watson DeepQA - system from IBM that won the Jeopardy - main stages - Question processing, Candidate Answer Generation,
Candidate Answer Scoring, Answer Merging and Confidence Scoring.

MRR - mean reciprocal rank - a common evaluation metric for factoid question answering

## Chapter 24: Chatbots & Dialogue Systems

Properties of Human Conversation:

- turns - a dialogue is a sequence of turns, turn structure have important implications for spoken dialogue - a system
  needs to know when to stop talking and also needs to know when user is done speaking.
- speech acts :
    - constatives - committing the speaker to something's being the case (answering, claiming, denying, confirming,
      disagreeing)
    - directives - attempts by the speaker to get the addressee to do something (advising, asking, forbidding, inviting,
      ordering, requesting)
    - commissives - committing the speaker to some future course of action (promising, planning, vowing, betting,
      opposing)
    - acknowledgments - express the speaker's attitude regarding the hearer with respect to some social action (
      apologising, greeting, thanking, accepting, thanking)
- grounding - this means acknowledging that the hearer has understood the speaker (like ACK in TCP), humans do this all
  the time for example using OK
- sub-dialogues and dialogue structure:
    - questions set up an expectation for an answer, proposals are followed by acceptance / rejection, ...
    - dialogue systems aren't always followed immediately by their second pair part, they can be separated by a side
      sequence (or sub-dialogue) - correction sub-dialogue, clarification question or presequence (Can you make a train
      reservations? Yes I can. Please, do ...)
- initiative - sometimes a conversation is completely controlled by one participant, for humans it is more natural that
  initiative shifts from one person to another
- inference - speaker uses provides some information and another information needs to be derived from that information (
  When in May do you want to travel? I have a meeting from 12th to 15th.)

Because of characteristics of human conversations it is difficult to build dialogue systems that can carry on natural
conversations.

Chatbots - the simplest form of dialogue systems. Chatbots have 3 categories:

- rule based chatbots - for example ELIZA based on psychological research, created in 1966, the most important chatbot.
  Few years later PARRY was created - this chatbot had model of its own mental state (fear, anger, ...) - first known
  system to pass the Turing test (1972) - psychiatrists couldn't distinguish text transcripts of interviews with PARRY
  from transcripts of interviews with real paranoids (!!!)
- corpus-based chatbots - instead of using hand-built rules, mine conversations of human-human conversations. Requires
  enormous data for training. Most methods use retrieval methods (grab response from some document) or generation
  methods (language model or encoder-decoder to generate the response given the dialogue context).
- hybrid of 2 above

Task-based dialogue - a dialogue system has the goal of helping a user solve some task like making an airplane
reservation or buying a product. GUS - influential architecture form 1977 for travel planning.

The control architecture for frame-based (frame - kind of knowledge structure representing the kinds of intentions the
system can extract from user sentences) dialogues systems is used in various modern systems like Siri, Google Assistant
or Alexa. The system's goal is to fill the slots in the frame with the fillers the user intends and the preform relevant
action for the user. To do this system asks questions associated with frames. This is heavily rule-based approach.

Slot-filling - task of domain and intent classification.

If dialogue system misrecognizes or misunderstands an utterance, the user will generally correct the error by repeating
or reformulating the utterance.

Modern systems often ask for confirmation or rejection if input data is correct. The explicit confirmation eliminates
risk of mistakes, but awkward and increases the length of conversation.

System might as clarification questions.

Dialogue systems might be evaluated using different metrics, e.g. engagingness, avoiding repetition, making sense.
Commonly used high-level metric is called acute-eval - annotator looks at two conversations and choose the one in which
the dialogue system participant performed better. Automatic metrics are generally not used for chatbots. However, there
are some attempts to train a Turing-like evaluator classifier to distinguish a human-generated responses and
machine-generated responses.

The study of dialogue systems is closely liked with the field of Human-Computer Interaction. Ethical issues also need to
be taken into consideration when designing system - famous example Microsoft's Tay chatbot (adversarial attacks). ML
models amplify stereotypes and also raise privacy concerns.

## Chapter 25: Phonetics

## Chapter 26: Automatic Speech Recognition and Text-to-speech
