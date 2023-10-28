Object subclass: #Researcher
    instanceVariableNames: 'key name publicationsByYear'

Researcher>>initialize
    key := ''.
    name := ''.
    publicationsByYear := Dictionary new.

Researcher>>setKey: aKey
    key := aKey.

Researcher>>setName: aName
    name := aName.

Researcher>>addPublication: aPublication forYear: aYear
    | publicationsForYear |
    publicationsForYear := publicationsByYear at: aYear ifAbsentPut: [OrderedCollection new].
    publicationsForYear add: aPublication.

Researcher class>>getOrCreateResearcher: name
    ^allResearchers at: name ifAbsentPut: [Researcher new name: name].


