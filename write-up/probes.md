Carry forward sentence length and word content from Conneau et al. (2018).
Current assumption is that all of these tasks are carried out in English.

Syntax

-Is noun n singular or plural in sentence s?

Proposed probing task 1: Internal vs. external argument subject on main clause verb
(i.e. unaccusative vs. unergative verbs, or agent vs. experiencer theta-roles for intransitive subjects)

Example: “Todd runs” (external argument) vs. “Todd burns” (internal argument)

Justification: a change occurs to the subject. “Todd burns” has more in common with “the fire burns Todd” than “Todd runs”, in terms of Todd undergoing a change as a result of the first versus Todd performing an action. This is fundamental property of intransitive verbs which indicates the deep syntactic structure of seemingly simple intransitive constructions. People may not be able to explain this, but they can sense it. 

Formal probing statement: For a sentence embedding s, with a verb v and a subject e of v, does e stand in agent or experiencer theta-role to v?


Proposed probing task 2: Number of arguments on main clause verb

Example: “Todd gives” vs. “Todd gives money” vs. “Todd gives Howard money”

Justification: This information is readily apparent to an observer with a basic definition of “argument” and “verb”. This probing task tests whether the neural network or other model in question is correctly forming dependencies/associations between the main clause verb and the DPs in the same clause.

Formal probing statement: For a sentence embedding s, with a verb v, what is the number n of arguments that v has?


Proposed probing task 3: Number on main clause verb

Example: “Todd goes to the store” vs. “Todd and Howard go to the store”; “Todd went to the store” vs. “Todd and Howard went to the store”.

Justification: For present tense verbs, this is a straightforward test as in Conneau et al. (2018) and Linzen et al. (2016). For past tense verbs in English (where number is unmarked), if the results of this task are at chance, then the tested model is detecting verb number solely based on the information the model gleans from the verb. If above chance, then the model integrates information from the subject to determine the number on the main clause verb as well.

Formal probing statement: For a sentence embedding s and a verb v in s, is v singular or plural?


Proposed probing task 4: Word-level “complement” vs. “adjunct” (structural necessity)

Example: “Lovely” in “Todd is lovely” vs. “Todd owns a lovely house”; is “lovely” structurally essential for the sentence to be grammatical and parseable?

Justification: This task probes for the model’s understanding of whether a word is necessary for a sentence to make sense or merely provides additional information. Is this word a necessary part of the structure of the sentence? This is something that people have an intuitive grasp of, and taps into the recursive power of language.

Formal probing statement: For a sentence embedding s and a word embedding w, is w a complement or adjunct in s?


Proposed probing task 5: Syntactic odd man out

Example: “The professor helps the student” vs. “The professor *help the student”; “The professor in the truck likes noodles” vs. “The professor *for the truck likes noodles”.

Justification: The syntactic analogue of Conneau et al. (2018)’s semantic odd man out for syntactic testing. The goal is to compare two embeddings that differ only by swapping one word for another semantically similar but syntactically unacceptable form of the word. This is like a grammaticality judgment, but working with minimal pairs of sentences instead of expecting the network to judge grammaticality for an independent sentence.

Formal probing statement: For two sentence embeddings s1 and s2, is s1 the original (grammatical) sentence?









Semantics

-Truth value of the sentence given a narrative
-Word content but with lemmas, not just exact word embeddings
-Synonyms (does a synonym for this word appear in the embedding), should be really easy for co-occurrence word embedding models
-Clause content (word content but use a sentence vector output by the same model, where the sentence is a subordinate clause)


Proposed probing task:

Example:

Justification:

Formal Probing Statement:



-- Template --
Proposed probing task:

Example:

Justification:

Formal Probing Statement:
