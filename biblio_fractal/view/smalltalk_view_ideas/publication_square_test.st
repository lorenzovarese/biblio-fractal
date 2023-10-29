| view shape publicationsCount |
"Get the number of publications for the selected researcher"
publicationsCount := selectedResearcher totalPublicationsCount. "Assume totalPublicationsCount returns the total number of publications"

"Initialize the Roassal view"
view := RSCanvas new.

"Create a square shape, 10 pixels per publication"
shape := RSShapeBuilder rectangle
    size: (publicationsCount * 10); "Size in pixels, 10 pixels for each publication"
    color: Color blue;
    build.

"Add the shape to the view"
view add: shape.

"Open the view"
view open.
