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


**formele parameters** en **actuele parameters**, aka parameters en argumenten
formele parameters in definitie van procedure, actuele in de aanroep
