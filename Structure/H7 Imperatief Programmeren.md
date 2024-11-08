In procedures die geheugen aanpast eindigen op ! ("bang"), vb. set! ("set bang")

## List vs. Vector
List gedraagd zich als een linked list, vector gedraagt zich als een array

Imperatief programmeren is vaak destructief

Headed-list: oplossing om te voorkomen dat de verwijzing naar het eerste element deel is van de omgeving

Earmuffs rond globale mutable variabelen
```scheme
(define *x* '())

```