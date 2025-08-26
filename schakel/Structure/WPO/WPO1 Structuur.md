#wpo #structuur
Mathijs Saey
scpi@dinf.vub.ac.be e-mail addres voor alle assistenten
2x per week
Niet verplicht
komen = opletten en meewerken
geen pauze, pak ze zelf
Eigen PC
[[R5RS]] tijdens de WPO's
Oefeningen:
- Dodona
- [oefeningenbundel](soft.vub.ac.be/SCPI) Oefeningen, extra oefeningen en oplossingen
# Dodona oefeningen
#dodona #oefeningen
## Eenvoudige Procedures
### Van infix- naar prefixnotatie
```scheme
(- (/ (+ a b) e) (/ (+ c d) f ))
(+ c (/ a (+ (* b c) (/ d (+ e (/f g))))))
(* (/ (+ a (/ b c)) d) (/ e (- (/ g i) h)))
```

### Voorspel het resultaat van eenvoudige expressies
1) 20
2) error
3) error
4) 110
5) error
6) void
7) 20
8) error
9) error
10) error
11) error
12) error
13) error
14) error
15) error
16) 3
17) \'#<procedure:/>

### Voorspel het resultaat van eenvoudige expressies a.d.h.v omgevingsmodellen
1) void, $ defined als /
2) 3, 6 $ 2 = 6 / 2
3) #<procedure:/>, $ is globaal gebonden aan de /-procedure
4) void, nieuwe procedure aangemaakt met name double die x als parameter heeft en (+x x) returned
5) 20, double aanroepen vanuit de global environment met parameter (double 5), nieuwe environment voor deze call en daar double opnieuw aanroepen met parameter 5, resultaat 10 wordt terug gestuurd naar eerste double call en die returned 20
6) void, nieuwe procedure aangemaakt met naam five zonder parameters die als procedure 5 heeft
7) void, variabele gedeclareerd met naam four en waarde 4
8) 4, lookup van de variabele four in global environment
9) '#<procedure:5>, lookup procedure five in global environment
10) error, lookup four, four is not a procedure
11) 5, lookup five, five is a procedure in global procedure and returns 5
### Fourth
```scheme
(define (square x) (* x x))
(define (fourth-* x) (* x x x x))
(define (fourth-square x) (square (square x)))
```

### sum-3-squares
```scheme
(define (square x) (* x x))
(define (sum-3-squares x y z) (+ (square x) (square y) (square z)))
```

### Celsius naar Fahrenheit
```scheme
(define (convert-C-to-F c) (- (* (+ c 40) 1.8) 40))
```

### Evaluatie van eenvoudige procedures

```scheme
;1)
(define (sphere-volume r)(* (/ 4 3) 3.14)(* r r r))
;te weinig haken rond procedure
(define (sphere-volume r)(* (* (/ 4 3) 3.14)(* r r r)))
;2)
(define (next x) (x + 1))
;foute syntax (+ x 1)
(define (next x) (+ x 1))
;3)
(define (square) (* x x))
;geen formele parameters in procedure definitie
(define (square x) (* x x))
;4)
(define (triangle-area triangle)(* 0.5 base height))
;formele parameters komen niet overeen in procedure definition and header
(define (triangle-area base height)(* 0.5 base height))
;5)
(define (sum-of-squares (square x) (square y))(+ (square x) (square y)))
;procedure call in definition header
(define (sum-of-squares x y)(+ (square x) (square y)))
```

### Omgevingsmodel met Atoma-schriftjes

### Omgevingsmodel met Atoma-schriftjes: "sum"

### Discount
```scheme
(define (discount prijs korting) (* prijs (/ (- 100 korting) 100)))
```

## Complexe Procedures
### Sign
```scheme
(define (sign number) (cond ((< number 0) -1)
                            ((> number 0) 1)
                            (else 0)))
```

### Leap-year?
```scheme
(define (leap-year? year) (cond ((= (modulo year 400) 0) #t)
                            ((= (modulo year 100) 0) #f)
                            ((= (modulo year 4) 0) #t)
                            (else #f)))
```

### Evaluatie van complexe procedures
1) 11
2) void, a = 3
3) void b = a + 1 = 4
4) 19, a + b + ab
5) '#f
6) 4
7) 4
8) 6
9) 16
10) 7

### Lokale definities

```scheme
(define (bereken x)
  (define a (- x 1))
  (define b (+ (* 2 x) 3))
  (+ (/ a b) (/ b a))
                   )
```

### Lokale definities: tangens

```scheme
(define (tangens-dubbel x)
  (define t (tan x))
  (/ (* 2 t) (- 1 (* t t)))
  )
```
