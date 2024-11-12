# Samengestelde uitdrukkingen
Aftrekking met meer dan 2 argumenten, 1e argument - som(rest argumenten):
```scheme
> (- 15 5 5 5)
0
```

# Define
variabele defineren
```scheme
> (define x 5)
> x
5
> (define y (* x 2))
> y
10
```
procedures aanmaken
```scheme
> (define (f x)
	(+ (* x x x) 17.3)) ; f(x) = x**3 + 17.3
> (f 13)

```
# Math
```scheme
> (sqrt 9)
3
> (abs -5)
5
...
```

# Ariteit
Unaire (1), Binaire (2) en ternaire (3) procedures.
vb: (abs 1), (modulo 17 3), if x then y else z
Variabele ariteit (vb: + in scheme)

# Booleans
```scheme
> #t ;true
> #f ;false
> (not #f)
#t
> (and #t #f)
#f
> (or #t #f #f)
#t
```
# Relational Operators
```scheme
> (= 10 10)
#t
> (>= 23 24)
#f
```
# Types
You can check for types using the following format:
```scheme
> (number? 10)
> #t
> (real? 10)
> #t
> (integer? 10.0)
> #t
> (procedure? abs)
> #t
```
## Predicaten:
eindigen meestal op '?' en geven aan of iets klopt, vb: number?
Predicaat is elke procedure die true of false teruggeeft


**formele parameters** en **actuele parameters**, aka parameters en argumenten
formele parameters in definitie van procedure, actuele in de aanroep

# Modellen
## Substitutie-model
[Racket's substitution model](https://www.cs.uni.edu/~wallingf/teaching/cs3540/readings/substitution-model.html)
Enkel voor simpele programma's
Inspritatie uit de wiskunde:
Deel-expressies eerst uitrekenen, dan verder rekenen 
## Omgevingsmodel
### Metafoor met atoma-schriftje
Dichter bij de realiteit, maar niet exact
- **Definitie van een procedure**: Wanneer je een procedure definieert met bijvoorbeeld `define`, wordt de naam van de procedure gekoppeld aan een procedure-object. Dit object bewaart informatie zoals de parameters en de code van de procedure (de "body"). Deze binding wordt toegevoegd aan de huidige omgeving.
- **Oproep van een procedure**: Tijdens het aanroepen van een procedure word een extra omgeving aangemaakt. Daarin worden de waarden van de actuele parameters berekend en vervolgens gebonden aan de formele parameters. Deze nieuwe omgeving bevat de variabelen van de procedure.
- **Evaluatie in de omgeving**: Wanneer de body van de procedure wordt uitgevoerd, gebeurt dit in de context van deze tijdelijk uitgebreide omgeving. De berekeningen binnen de procedure kunnen gebruik maken van de gebonden waarden in de nieuwe en de oude omgeving.
- **Omgevingsstructuur**: Wanneer een variabele nodig is tijdens een berekening (bijvoorbeeld de waarde van `x` in een expressie `(* x x)`), zoekt de evaluator in de huidige omgeving en gaat omhoog door eerdere omgevingen totdat de waarde gevonden wordt.
- Als de procedure afgelopen is worden de resultaten terug gegeven en de uitgebreide omgeving wordt vernietigd door de **garbage collector**
Dit gebeurt recursief voor geneste operaties.
### Omgevingsdiagrammen
Echte werking van Scheme, zie [[H9 Closures en omgevingsmodellen]]


# Programmeerstijl & Abstractie
## Procedurele Abstractie
Als je een procedure oproept hoef/wil je de body niet kennen
Procedure --> Zwarte doos: Implementatie van een procedure maakt niet uit voor het gebruik

# Strings and Characters
Characters in deze vorm: \#\\f is 'f'
Van chars naar string: 
```scheme
> (string #\o #\n #\e)
"one"
```

# R5RS vs Racket
[[Racket]] is een dialect van Scheme met meer bibliotheken en meer mogelijkheden ingebouwd.

## images
2htdp/image library

| commands     | args                           |                            |
| ------------ | ------------------------------ | -------------------------- |
| circle       | number, string, string         | size, fill, color          |
| rectangle    | number, number, string, string | width, height, fill, color |
| image-width  | image                          |                            |
| image-height | image                          |                            |
| above        | image, image, ...              |                            |
| beside       | image, image, ...              |                            |
| overlay      | image, image, ...              |                            |
