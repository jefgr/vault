Case Insensitive
_Void_ wordt niet geprint, maar bestaat wel als hidden object

---
# Special Forms
Een _special form_ is een samengestelde uitdrukking waarvan de component die in de eerste positie staat een gereserveerd "sleutelwoord" is
## Define
```scheme
;declare a variable:
(define <naam> <uitdrukking>)
;declare a procedure:
(define (<naam> <parameters>)
	  <uitdrukking>)
```
## If
If fungeert als een if-else blok
```scheme
> (if <test> <consequent> <alternatief>)
;in python: if (test): consequent else alternatief
```
ex. absolute value
```scheme
> (define (abs2 x)
  	(if (< x 0)
 	(- x)
 	x))
```
\<alternatief> kan je weglaten, dan wordt _void_ gereturned
## Cond
conditional (switch-case)
Bestaat uit verschillende test-consequent koppels, ook wel clausules genoemd.
Clausules worden afgegaan van boven naar onder en exit bij de eerste true test.
Als er geen clausule true test word er _void_ gereturned.
Er kan een "catch-all" toegevoegd worden met else, deze clausule moet de laatste zijn.
```scheme
> (cond (<test1> <consequent1>)
> 		(<test2> <consequent2>)
> 		(<test3> <consequent3>)
> 		<...>
> 		(else <alternatief>))
```

---
# Trace
Als we tracen laat elk begin+einde van een procedure-oproep een spoor op het scherm achter
```scheme
;Inladen van de tracing infrastructuur
> (#%require racket/trace)
;Tracing aanzetten procedure per procedure
> (trace <procedure-name>)
```

# Conversions
```scheme
> (string->number "23")
23
> (string->number "two")
#f
```

# Build in Procedures

| Procedure      | ARGS                   | Description          |
| -------------- | ---------------------- | -------------------- |
| string-append  | string, string, ...    | string concatenation |
| substring      | string, number, number | substring selectie   |
| string->number | string                 | conversion           |
| string-length  | string                 | length               |
| sqrt           | number                 | squareroot           |
| abs            | number                 | absolute value       |
| string         | char,...               | van chars to string  |
| string=?       | string, string, ...    | string vergelijking  |
