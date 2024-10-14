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

## Atom
In Scheme, an **atom** is an indivisible unit of data, such as:

- **Numbers**: `42`, `3.14`
- **Symbols**: `x`, `foo`
- **Booleans**: `#t`, `#f`
- **Strings**: `"hello"`

### Defining `atom?` in Scheme

Scheme doesn’t have a built-in `atom?` function (common in Lisp), but you can define it:

```scheme
(define (atom? x)
  (not (pair? x)))
```

This returns `#t` if `x` is an atom and `#f` if not.

### Atoms vs. Lists

- **Atoms**: indivisible data (e.g., numbers, symbols).
- **Non-atoms**: pairs or lists, like `(cons 1 2)` or `(list 1 2 3)`.

Atoms are the simplest data elements in Scheme.

## Destructief vs niet-Destructief

- **Destructieve procedures** veranderen de originele data of structuur. De oorspronkelijke waarde wordt overschreven of verloren, en kan niet worden hersteld zonder een aparte back-up. Een voorbeeld is wanneer je een lijst sorteert en de oorspronkelijke volgorde verdwijnt.

- **Niet-destructieve procedures** laten de originele data intact en maken vaak een kopie om de bewerkingen op uit te voeren. Hierdoor blijft de originele waarde behouden. Bijvoorbeeld, bij het sorteren van een lijst zonder de originele volgorde te veranderen, maak je een nieuwe gesorteerde lijst.

## Homoiconisch
**Homoiconisch** betekent dat de code van een programmeertaal dezelfde structuur heeft als de data waarmee het werkt. Dit houdt in dat programma's in die taal kunnen worden gemanipuleerd als data door het programma zelf.

In homoiconische talen, zoals Lisp, is de code zelf data (vaak lijsten), en dit maakt het eenvoudig om programma's te schrijven die hun eigen code kunnen aanpassen of genereren.

Kort gezegd: bij een homoiconische taal is er geen onderscheid tussen code en data, waardoor code gemanipuleerd kan worden als data.

## Symbols

In **Scheme** (een dialect van Lisp) is een **symbol** een primitief datatype dat wordt gebruikt om namen of identifiers weer te geven. Een symbol is een unieke, onveranderlijke string van tekens die niet aan een waarde hoeft te zijn gekoppeld, hoewel dat wel kan. Symbols worden vaak gebruikt om variabelen of functies te benoemen.

Een belangrijk kenmerk van symbols is dat ze vergeleken worden op identiteit, niet op de stringinhoud. Als je twee keer dezelfde naam invoert, is dat dezelfde symbol.

```scheme
`(define x 'apple)  ; 'apple is een symbol`
;Hier is `'apple` een symbol, en niet de string "apple".
```

## Meta programmeren

**Metaprogrammeren** is het schrijven van programma's die andere programma's kunnen manipuleren of genereren. Dit betekent dat het programma niet alleen zijn taken uitvoert, maar ook de code kan aanpassen of nieuwe code kan maken tijdens de uitvoering.

Metaprogrammeren stelt je in staat om flexibeler en dynamischer te programmeren, bijvoorbeeld door templates of codegeneratie te gebruiken, of zelfs programma's te laten reageren op hun eigen structuur (zoals bij homoiconische talen zoals Lisp).

