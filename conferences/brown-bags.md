[go back](https://github.com/pkardas/learning)

- [NLP - State fo the Art](#nlp---state-fo-the-art)
- [Kanban Training](#kanban-training)

## NLP - State fo the Art

*By Michał Jakóbczyk*

Turing Test - are you able to distinguish if you are talking to a computer or a person? It determined the direction of
development of NLP.

> The Man Who Mistook His Wife For a Hat - Olivier Sacks - book recommendation.

Analyse sentence:

```python
from spacy import displacy

displacy.render(nlp("Some sentence"))
```

"They ate the pizza with anchovies" - context matters (with fishes or using fishes?).

"They ate the pizza with hands"

"I shot an elephant in my pyjamas" - model will refer pyjama to the elephant.

"I shot an elephant, in my pyjamas" - model will refer pyjama to the person.

We know about these differences! Models have difficulties.

40-50 years ago, NLP was mostly about POS tags analysis, recently is more about machine learning.

Python code -> Assembler <- Machine learning model. In the end everything is Assembly.

*playground.tensorflow.org* - 1 square = 1 neuron that is basically checking one if / one line.

Text to number:

- document vectorisation - if document contains word - 1, 0 otherwise
- one-hot encoding - you can use it for encoding word position (2D matrix) - a lot of memory
- word embeddings - place word in a multidimensional space
    - adding vectors - drawing a multidimensional sphere containing multiple words
    - *projector.tensorflow.org*

We can compare sentences using embeddings.

```python
nlp("Gave a research talk in Boston").similarity(nlp("Had a science lecture in Seattle"))
```

Training is done using input text, then every word is removed (word by word) and machine is supposed to guess missing
word.

GPT-3 - the biggest transformer, almost 5M$ spent on training this model

## Kanban Training

*By Marcin Lelek*

https://tools.kaiten.io/featureban

KANBAN - card + signal, name of the board, method for implementing improvements requested by client. Created by Toyota.

3 rules:

- stat with what you do now
- gain agreement to evolutionary change (don't make changes against people, agree on change)
- encourage acts of leadership at all levels (independent teams)

General practices:

- you need to have a board to visualise progress
- number of items in Work In Progress is limited
- manage flow - work flow management, not people optimisation
- make policies explicit - define policy how to treat a card in a column, e.g. when card moves from one column to
  another
- implement feedback loops
- improve collaboratively
- evolve experimentally

Different levels of Kanban boards - e.g. 1 WIP per person.
