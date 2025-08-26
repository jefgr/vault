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
	  <uitdrukkingen>)
;only one fundamental define, second define can be rewritten as follows and will be handled as such
(define <name> (lambda (<parameters>) <uitdrukkingen>))
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

### When
equivalent van (if (begin (...)))
### Unless
equivalent van (if (not (begin (...))))

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

## CONS, CAR, CDR
CONS word gebruikt om paren te definiëren. CAR (eerste element) en CDR (tweede element) worden gebruikt om de data uit een CONS te halen.
```scheme
> (define my-pair (cons a b))
> my-pair
(a . b)
> (car my-pair)
a
> (cdr my-pair)
b
```

## AND en OR
Evalueren de uitdrukkingen niet allemaal op voorhand (_lazy_). Werken van links naar rechts:
- and exit als er een false tegenkomt
- or exit als hij een true tegenkomt

> dus ook errors die achter true(or)/false(and) staan zullen niet doorkomen

```scheme
> (and <uitdrukking1> <uitdrukking2> … <uitdrukkingk>)
> (or <uitdrukking1> <uitdrukking2> … <uitdrukkingk>)
```

## Quote
Neemt één expressie en evalueerd die niet.

```scheme
> (quote <uitdrukking>)
> ; ex.:
> (quote #t)
#t 
> (quote (+ 1 2))
(+ 1 2)
> (quote (+ 1 (+ 2 3)))
(+ 1 (+ 2 3))
> (quote (fac 5))
(fac 5)
> (quote (oei (oei oei ((ai) ai) ai)))
(oei (oei oei ((ai) ai) ai))
; of afgekort door '
> '(1 2 3)
(1 2 3)
> '()
()
```

## Lambda
Anonieme procedures
Worden garbage collected na gebruik

```scheme
> (lambda (<naam1> <naam2> … <naamn>) <uitdrukking1> … <uitdrukkingm>)
;ex. square:
> ((lambda (x) (* 2 x)) 5)
25
```

## Let
> zoals "zij ..." in de wiskunde

```scheme
> (let (
 		(<naam1> <uitdrukking1>)
 		(<naam2> <uitdrukking2>)
 		…
 		(<naamn> <uitdrukkingn>)
 		)
 		<uitdrukking'1>
 		…
 		<uitdrukking’m> )
```

## Set
Variabelen aanpassen nadat ze gedeclareerd zijn. Type kan veranderen, vb. procedure kan een number worden.

```scheme
> (set! <naam> <uitdrukking>)
```

## Begin
Om meerdere expressies na elkaar te doen. De waarde van begin is de waarde van de laatste uitdrukking.

```scheme
> (begin <uitdrukking1> <uitdrukking2> … <uitdrukkingn>)
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

| Procedure      | ARGS                           | Description                                                                                                                                   |
| -------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| string-append  | string, string, ...            | string concatenation                                                                                                                          |
| substring      | string, number, number         | substring selectie                                                                                                                            |
| string->number | string                         | conversion                                                                                                                                    |
| string-length  | string                         | length                                                                                                                                        |
| sqrt           | number                         | squareroot                                                                                                                                    |
| abs            | number                         | absolute value                                                                                                                                |
| string         | char,...                       | van chars to string                                                                                                                           |
| string=?       | string, string, ...            | string vergelijking                                                                                                                           |
| newline        | _void_                         | /n, newline char in console                                                                                                                   |
| display        | string                         | print to console                                                                                                                              |
| read           | _void_                         | user input from console                                                                                                                       |
| list           | any, ...                       | make a list (linked pairs)                                                                                                                    |
| length         | list                           | length of a list                                                                                                                              |
| list-ref       | list, integer                  | get item at index, starts at 0                                                                                                                |
| list-tail      | list, integer                  | returns list without the first _integer_ elements                                                                                             |
| reverse        | list                           | reverses list                                                                                                                                 |
| append         | list, list, ...                | joins lists                                                                                                                                   |
| flatten        | list(list,...) _geneste lijst_ | flatten the list of lists to a single list                                                                                                    |
| eq?            | any, any                       | check equality in memory<br>warning: 5 not eq? 5.0<br>gaat checken op geheugen locatie                                                        |
| equal?         | any, any                       | check equality of content not location<br>warning: 5 not equal? 5.0                                                                           |
| memq           | any, list                      | looks for first element in the list<br>not found -> #f<br>else -> part of list starting from location<br>of search term inclusive search term |
| member         | any, list                      | same as memq, but uses _equal?_ instead of _eq?_                                                                                              |
| assq           | key, map*                      | looks for key in associatielijst<br>returns key-value pair                                                                                    |
| assoc          | key, map*                      | same as assq, but uses equals? instead of eq?                                                                                                 |
| set-car!       | cons, value                    |                                                                                                                                               |
| set-cdr!       | cons, value                    |                                                                                                                                               |
| make-vector    | number, any(optional)          | makes a vector (array) of length _number_ with value _any_ in each cell                                                                       |
| vector         | any, ...                       | makes a vector of the inputs                                                                                                                  |
| vector-ref     | vector, number                 | gets the value of index _number_ in _vector_                                                                                                  |
| vector-set!    | vector, number, any            | changes value of index _number_ to value _any_ in _vector_                                                                                    |
| vector-length  | vector                         | gets the length of _vector_ (O(1), because length is stored in memory)                                                                        |
| apply          | procedure, list                | applies procedure to elements of the list                                                                                                     |


# SRFI
Extra libraries voor scheme
## extra uit SRFI 60

| logior | number, number | logical inclusive or, bitwise |
| ------ | -------------- | ----------------------------- |
| logand | number, number | logical and, bitwise          |
| lognot | number         | logical not, bitwise          |
warning: for logical operators, 2's compliment