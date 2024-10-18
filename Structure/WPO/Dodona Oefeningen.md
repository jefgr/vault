#dodona #oefeningen
# Eenvoudige Procedures
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

# Complexe Procedures
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

# Soorten Recursie

### Som: Recursie

```scheme
(define (1- x) (- x 1))
(define (1+ x) (+ 1 x))
(define (rec-add a b)
  (if (= b 0)
      a
      (1+ (rec-add a (1- b)))))

```

### Som: Iteratief d.m.v. staartrecursie

```scheme
(define (1- x) (- x 1))
(define (1+ x) (+ 1 x))
(define (iter-add a b) (if (= b 0) a (iter-add (1+ a) (1- b))))
```

### Som: Iteratief d.m.v. do

```scheme
(define (1- x) (- x 1))
(define (1+ x) (+ 1 x))
(define (do-add a b)
  (do ((counter b (1- counter))
        (result a (1+ result)))
        ((= counter 0) result)
    )
  )
```

### Multiply: Linear proces (Recursief & Iteratief)

```scheme
(define (rec-multiply a b)
  (if (= b 0)
      0
      (+ (rec-multiply a (- b 1)) a)))

(define (iter-multiply a b)
  (define (hulp b c)
     (if (= b 0)
         c
         (hulp (- b 1) (+ c a))))
  (hulp b 0))
```

###   Multiply: Logaritmisch proces (Recursief & Iteratief)

```scheme
(define (double a) (* a 2))
(define (halve a) (/ a 2))

(define (rec-fast-multiply a b)
  (cond ((= b 0) 0)
        ((even? b) (double (rec-fast-multiply a (halve b))))
        (else (+ a (rec-fast-multiply a (- b 1))))))

(define (iter-fast-multiply a b)
  (define (hulp a b result)
     (cond 
       ((= b 0) result)
          ((even? b) (hulp (double a) (halve b) result))
          (else (hulp a (- b 1) (+ result a)))
    ))
  (hulp a b 0))
```

**Pseudocode for iterative variant from chatgpt:**
```
function logMultiplication(a, b, result):
    # Base case: if b is 0, return the accumulated result
    if b == 0:
        return result

    # If b is even, use the property a * b = (2 * a) * (b // 2)
    if b is even:
        return logMultiplication(2 * a, b // 2, result)

    # If b is odd, reduce b by 1 and accumulate a into result
    else:
        return logMultiplication(a, b - 1, result + a)

# Wrapper function for ease of calling
function multiply(a, b):
    return logMultiplication(a, b, 0)

```
**Explanation:**

- The function `logMultiplication` works by dividing the multiplication problem into smaller subproblems.
- If `b` is even, it doubles `a` and halves `b` (reducing the problem size).
- If `b` is odd, it decreases `b` by 1 and adds `a` to the result, and continues reducing the problem.
- The base case is when `b` becomes 0, in which case the accumulated `result` is returned.
- The `multiply` function serves as a wrapper to initialize the recursion with a `result` of 0.

**Time complexity:**

- The function operates in O(log⁡b)O(\log b)O(logb) time because the value of `b` is halved in each recursive step.

This technique minimizes the number of multiplication operations.
### Mutuele recursie: De Hofstadter-reeksen

```scheme
(define (hofstadter-V n)
  (if (= n 0) 1 (- n (hofstadter-M (hofstadter-V (- n 1))))))

(define (hofstadter-M n)
  (if (= n 0) 0 (- n (hofstadter-V (hofstadter-M (- n 1))))))
```

### Mutuele recursie: De Hofstadter-reeksen printen d.m.v. do

```scheme
(define (hofstadter-V n)
  (if (= n 0) 1 (- n (hofstadter-M (hofstadter-V (- n 1))))))

(define (hofstadter-M n)
  (if (= n 0) 0 (- n (hofstadter-V (hofstadter-M (- n 1))))))

(define (hofstadter-reeksen n)
  (do ((counter 0 (+ counter 1)))
       ((= counter n) ) 
       (display (hofstadter-V counter))
       (display " ")
       (display (hofstadter-M counter))
       (newline)
  ))
```

### Reeksen: Het getal van Euler
```scheme
;optimisation by removing recursion, but not used in new calc-e procedure
(define (factorial n)
  (do ((count 1 (+ count 1))
       (result 1 (* result count)))
       ((< n count) result)
       ))

(define (calc-e n)
  (define (help i prev-fac acc)
    (if (> i n)
        acc
        (help (+ i 1) (* prev-fac i) (+ acc (/ 1 (* prev-fac i))))))
  (help 1 1 1))
```

### Reeksen: Het getal van Euler d.m.v. do

```scheme
(define (calc-e n)
  (do (
       (count 1 (+ count 1))
       (next-fac 1 (* next-fac count))
       (result 0 (+ result (/ 1 next-fac))))
    ((> count (+ n 1)) result)))
```

### Recursiediepte: Implementeer de procedure "weird"
De opdracht is niet juist geschreven, er word gezocht naar de procedure die weird blijft aanroepen tot resultaat 1 is
```scheme
;call weird once
(define (weird-one x)
  (cond ((= x 1) 1)
        ((even? x) (/ x 2))
        (else (+ 1 (* x 3)))))
; call weird until result is 1
(define (weird x)
  (cond ((= x 1) 1)
        ((even? x) (weird(/ x 2)))
        (else (weird (+ 1 (* x 3))))))
```

### Recursiediepte: Bereken de recursiediepte van "weird"

```scheme
(define (weird-one x)
  (cond ((= x 1) 1)
        ((even? x) (/ x 2))
        (else (+ 1 (* x 3)))))

(define (weird x)
  (cond ((= x 1) 1)
        ((even? x) (weird(/ x 2)))
        (else (weird (+ 1 (* x 3))))))

(define (depth-weird x)
  (do ((count 0 (+ count 1))
       (xn x (weird-one xn)))
    ((= xn 1) count)
    )
  )
```

### Terugkeerpunten: Binaire vormen

```scheme
(define (display-as-binary n)
  (if (= n 0) (display "0"))
  (define output "")
  (do ((remainer n (quotient remainer 2))
       )
    ((= remainer 0) (display output))
    (if (even? remainer) (set! output (string-append "0" output)) (set! output (string-append "1" output)))
    )
  )
```

### display-n met do

```scheme
(define (display-n x n)
  (do (
       (count 0 (+ count 1))
       )
    ((= count n))
    (display x)
  )
  )
```

### display-n: parasol met do

```scheme
(define (display-n x n)
  (do (
       (count 0 (+ count 1))
       )
    ((= count n))
    (display x)
  )
  )

(define (display-stem n)
  (do (
       (count 0 (+ count 1))
       )
    ((= count 3))
    (display-n " " (- n 1))
    (display "*")
    (newline)
    )
  )

(define (parasol n)
  (do (
       (row 0 (+ row 1))
       (treewidth 1 (+ treewidth 2))
       )
    ((= row n) (display-stem n))
    (display-n " " (- n row 1))
    (display-n "*" treewidth)
    (newline)
    )
  )
```

# Lijsten en Symbolische Data

## Modeloplossing

```scheme
(define (list-procedure-rec lst)
  (if (null? lst)
      base-result
      (combine-car/res (do-something-with (car lst))
                       (list-procedure-rec (cdr lst)))))
 
(define (list-procedure-it lst)
  (define (iter lst res)
    (if (null? lst)
        res
        (iter (cdr lst)
              (combine-car/res (do-something-with (car lst))
                               res))))
  (iter lst base-result))
```

## Element toevoegen achteraan een lijst: add-to-end

```scheme
; kan ook recursief zonder de reverse
(define (add-to-end e l)
  (define (iter l res)
    (if (null? l)
        (cons e res)
        (iter (cdr l)
              (cons (car l) res))))
  (reverse (iter l '())))
; recursief
(define (add-to-end e lst)
  (if (null? lst)
	  (cons e '())
	  (cons (car lst)
			  (add-to-end e (cdr lst))
			  )
			)
		)
```

## Lijsten aaneen plakken: my-append (iteratief)

```scheme
(define (my-append lst1 lst2)
  (define (iter lst res)
    (if (null? lst)
        res
        (iter (cdr lst)
              (cons (car lst) res))))
  (reverse (iter lst2 (iter lst1 '()))))
```

## Lijsten omdraaien 

```scheme
(define (iter-reverse l)
  (define (iter l res)
    (if (null? l)
        res
        (iter (cdr l)
              (cons (car l) res))))
  (iter l '()))

(define (rec-reverse l)
  (if (null? l)
      '()
      (append (rec-reverse (cdr l)) (list (car l)))
      )
    )
```

## Laatste element van een lijst bepalen: last

```scheme
(define (last lst)
  (define (iter lst res)
    (if (null? lst)
        res
        (iter (cdr lst) (car lst))
        )
    )
  (iter lst #f)
  )
```

## Elementen in een lijst vervangen: replace

```scheme
(define (replace e1 e2 l)
    (if (null? l)
        '()
        (cons (if (eq? (car l) e1) e2 (car l)) (replace e1 e2 (cdr l)))
        )
    )
```

## Gelijkheid van twee lijsten bepalen: my-equal?

```scheme
(define (my-equal? l1 l2)
    (cond ((and (null? l1) (null? l2)) #t)
        ((or (null? l1) (null? l2)) #f)
        (else (and (eq? (car l1) (car l2)) (my-equal? (cdr l1) (cdr l2))))
        )
    )
```

## Element tussenvoegen in een lijst: intersperse

```scheme
(define (intersperse e l)
    (if (null? l)
        '()
        (cons (car l) (if (null? (cdr l))
				        (intersperse e (cdr l))
				        (cons e (intersperse e (cdr l)))
				        )
			)
        )
    )
```

## Sommatie van elementen in lijsten: sum-lists (Recursief)
```scheme
(define (rec-sum-lists l1 l2)
  (cond ((and (null? l1) (null? l2)) '())
        ((null? l2) (cons (car l1) (rec-sum-lists (cdr l1) '())))
        ((null? l1)(cons (car l2) (rec-sum-lists '() (cdr l2))))
        (else (cons (+ (car l1) (car l2)) (rec-sum-lists (cdr l1) (cdr l2))))
        )
  )
```

## Sommatie van elementen in lijsten: sum-lists (Iteratief)

```scheme
(define (iter-sum-lists l1 l2)
  (define (iter lst1 lst2 res)
  (cond ((and (null? lst1) (null? lst2)) res)
        ((null? lst2) (iter (cdr lst1) '() (cons (car lst1) res)))
        ((null? lst1) (iter '() (cdr lst2) (cons (car lst2) res)))
        (else  (iter (cdr lst1) (cdr lst2) (cons (+ (car lst1) (car lst2)) res)))
        )
    )
  (reverse (iter l1 l2 '()))
  )
```

## Samenvoegen van twee lijsten: merge-n

```scheme

```

## Samenvoegen van een willekeurig aantal lijsten: super-merge-n

```scheme

```

# Taak

## Fibonacci van de Derde Orde

```scheme
(define (fib-3 n)
  (cond ((< n 2) 0)
        ((= n 2) 1)
        (else (+ (fib-3 (- n 1)) (fib-3 (- n 2)) (fib-3 (- n 3)))) 
         )
  )
```

## Fibonacci van de Vijfde Orde

```scheme
(define (fib-5 n)
  (cond ((< n 4) 0)
        ((= n 4) 1)
        (else (+ (fib-5 (- n 1)) (fib-5 (- n 2)) (fib-5 (- n 3)) (fib-5 (- n 4)) (fib-5 (- n 5)))) 
         )
  )
```

## Veralgemeende Fibonacci Procedure

```scheme

```