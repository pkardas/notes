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





