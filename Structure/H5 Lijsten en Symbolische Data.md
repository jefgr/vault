## CONS, CAR, CDR
Gebruikt voor het maken van paren.
CONStruct
CAR: Contents of Address Register (eerste element)
CDR: Contents of Decrement Register (tweede element)

## Box-and-Pointer Diagrams
vb: linked list using CONS
![[boxAndPointDiagramLinkedList.png]]
binary tree using CONS
![[boxAndPointDiagramBinaryTree.png]]

## Lijsten
De Lege Lijst: '()
```scheme
> '()
'()
> (null? '())
#t 
> (null? (cons 1 2))
#f 
```

Lijsten geen apart type in Scheme, gewoon paren die aan elkaar hangen (linked-list)

> Definitie van lijst:
> - De lege lijst is een lijst
> - Elke reeks paren die (via cdrs) aan mekaar hangen en die eindigen met een lege-lijst is ook een lijst

Om door geneste lijsten te navigeren zijn er extra procedures gebaseerd op car en cdr, met variabele hoeveelheden a/d's (tot 4).


