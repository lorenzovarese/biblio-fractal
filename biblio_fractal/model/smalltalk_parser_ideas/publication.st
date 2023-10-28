Object subclass: #Publication
    instanceVariableNames: 'key title year authors'

Publication>>initialize
    key := ''.
    title := ''.
    year := 0.
    authors := OrderedCollection new.

Publication>>addAuthor: aResearcher
    authors add: aResearcher.
