[go back](https://github.com/pkardas/learning)

## Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition
Book by Daniel Jurafsky and James H. Martin (December 2020 draft)



[TOC]

#### Chapter 2: Regular Expressions, Text Normalization, Edit Distance

##### Regular Expressions

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



##### Words

Fragment - broken-off word, "I do main- mainly", "main-" is a fragment here

Filler - "um, uh" - used in spoken language, problem: should be treated as a word? Fragment and fillers are 2 kinds of disfluencies.

Type - number of distinct words in a corpus. When we speak about number of words in the language, we are generally referring to word types.



Herdan's Law/Heap's Law - relationship between number of types (`|V|`) and number of tokens (`N`) in the corpora:
$$
|V| = kN^{\beta}
$$
(k and 0 < B < 1 are constants)



##### Corpora

Writers, speakers have specific styles of communicating, use specific dialects, text can vary by time, place, function, race, gender, age, socioeconomic class.



Code switching - common practice for speakers and writers to use multiple languages in single communicative act



When preparing a computational models for language processing it is useful to prepare datasheet, document answering questions like: Who produced the text? In what context? For what purpose? In what language? What was race, gender, ... of the authors? How data was annotated?



##### Text Normalisation

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



#### Chapter 2: N-gram Language Models

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

PP for short, metric used for evaluating language model. Perplexity on a test set ts the inverse probability od the test set, normalised by the number of words. Minimising perplexity is equivalent to maximising the test set probability according to the language model. 

Another way of thinking about perplexity: weighted average branching factor (branching factor - number of possible next words that can follow any words).

The more information the n-gram gives us about the word sequence, the lower the perplexity (unigram: 962, bigram: 170, trigram: 109).

An intrinsic improvement in perplexity does not guarantee an extrinsic improvement in the performance. In other words: because some metric shows your model is great, it does not mean it will do so great in real life. Perplexity should be confirmed by an end-to-end evaluation of a real task.

