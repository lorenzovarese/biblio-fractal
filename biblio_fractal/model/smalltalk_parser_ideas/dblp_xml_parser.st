| xmlDoc rootNode |

"Read XML file"
xmlDoc := (XMLDOMParser onFileNamed: 'path/to/your/xml/file') parse.
rootNode := xmlDoc root.

"Initialize Publication objects and associate with Researchers"
rootNode elementsDo: [:eachNode |

    eachNode localName = 'www' ifFalse: [
        | publication year |
        publication := Publication new.
        publication setKey: (eachNode attributeAt: 'key').
        
        "Directly access single title and year."
        publication setTitle: (eachNode findElementNamed: 'title') content.
        year := (eachNode findElementNamed: 'year') content asInteger.
        publication setYear: year.

        "Add the publication to each Researcher's publicationsByYear dictionary"
        (eachNode findElementsNamed: 'author') do: [:each |
            | researcher authorName |
            authorName := each content.
            researcher := Researcher getOrCreateResearcher: authorName.
            
            "Associate the publication with the researcher and vice versa"
            researcher addPublication: publication forYear: year.
            publication addAuthor: researcher.
        ].
    ].
].
