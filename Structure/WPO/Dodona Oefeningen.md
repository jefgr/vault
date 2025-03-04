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

```python
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
        ((null? l1) (cons (car l2) (rec-sum-lists '() (cdr l2))))
        (else (cons (+ (car l1) (car l2)) (rec-sum-lists (cdr l1) (cdr l2))))
        )
  )
; oplossing uit de les
(define (rec-sum-lists l1 l2)
  (cond ((null? l2) l1)
        ((null? l1) l2)
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
;recursief
(define (rec-merge-n lst1 lst2 n)
  (define (hulp lst1 lst2 n i)
    (cond ((null? lst2) lst1)
          ((null? lst1) lst2)
          ((= i n) (hulp lst2 lst1 n 0))
          (else (cons (car lst1) (hulp (cdr lst1) lst2 n (+ i 1))))
          )
    )
  (hulp lst1 lst2 n 0)
  )
;iteratief
(define (iter-merge-n lst1 lst2 n)
  (define (hulp lst1 lst2 n i res)
    (cond ((null? lst2) (append (reverse res) lst1))
          ((null? lst1) (append (reverse res) lst2))
          ((= i n) (hulp lst2 lst1 n 0 res))
          (else (hulp (cdr lst1) lst2 n (+ i 1) (cons (car lst1) res)))
          )
    )
  (hulp lst1 lst2 n 0 '())
  )
```

## Samenvoegen van een willekeurig aantal lijsten: super-merge-n

```scheme
(define (super-merge-n lsts n)
  (define (replace-list lsts new-list index)
    (define (replace-helper lsts index current-index)
      (cond
        ((null? lsts) '())
        ((= current-index index)
         (cons new-list (cdr lsts)))
        (else
         (cons (car lsts)
               (replace-helper (cdr lsts) index (+ current-index 1)))))
      )
    (replace-helper lsts index 0)
    )
  (define (all-empty? lsts)
    (cond
      ((null? lsts) #t)
      ((not (null? (car lsts))) #f)
      (else (all-empty? (cdr lsts))))
    )
  (define (lift-index index len)
    (if (= (+ index 1) len) 0 (+ index 1))
    )
  (define (hulp lsts lst len n i lstindex)
    (cond ((null? lst) (if (all-empty? lsts) '() (hulp lsts (list-ref lsts (lift-index lstindex len)) len n 0 (lift-index lstindex len))))
          ((= i n) (hulp lsts (list-ref lsts (lift-index lstindex len)) len n 0 (lift-index lstindex len)))
          (else (cons (car lst) (hulp (replace-list lsts (cdr lst) lstindex) (cdr lst) len n (+ i 1) lstindex)))
          )
    )
  (trace hulp)
  (hulp lsts (list-ref lsts 0) (length lsts) n 0 0)
  )
;modeloplossing
(define (super-merge-n-opl lsts n)
  (define (hulp curr rest i)
    (cond ((and (null? curr) (null? rest)) '())
          ((null? curr) (hulp (car rest) (cdr rest) 0))
          ((= i n) (hulp (car rest) (append (cdr rest) (list curr)) 0))
          (else (cons (car curr) (hulp (cdr curr) rest (+ i 1))))
          )
    )
  (hulp (car lsts) (cdr lsts) 0)
  )
```

# Interludium: Lazy Special Forms

## my-and

```scheme
(define (my-and a b)
  (if a (if b #t #f) #f)
  )
```

## my-and: my-or

```scheme
(define (my-or a b)
  (if a #t (if b #t #f))
  )
```

## my-if

```scheme
(define (my-if a b c)
  (cond (a b)
        (else c)
  )
  )
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
(define (fib-p n p)
  (define (sum-p n p)
    (do ((i 0 (+ i 1))
         (sum 0 (+ sum (fib-p (- n i 1) p))))
      ((= i p) sum)))
  (cond ((< n (- p 1)) 0)
        ((= n (- p 1)) 1)
        (else (sum-p n p)) 
      )
  )
```

# Hogere Orde Procedures

## Product

```scheme
(define (product term a next b)
  (if (> a b)
      1
      (* (term a) (product term (next a) next b))))
```

## Product: staartrecursie

```scheme
(define (iter-product term a next b)
  (define (hulp a res)
    (if (> a b)
        res
        (hulp (next a) (* res (term a))))
    )
  (hulp a 1)
  )
```

## Product: factorial

```scheme
; zelfde als hiervoor, maar wordt gebruikt door de rest
(define (product term a next b)
  (if (> a b)
      1
      (* (term a) (product term (next a) next b))))

(define (factorial x)
  (product (lambda (a) a) 1 (lambda (b) (+ b 1) ) x)
  )
```

## Accumulate

```scheme
(define (accumulate combiner null-value term a next b)
  (define (iter a res) 
    (if (> a b)
        res
        (iter (next a) (combiner res (term a))))
    )
  (iter a null-value)
  )
```

## Accumulate: Product en Sum

```scheme(define (accumulate combiner null-value term a next b)
  (define (iter a res) 
    (if (> a b)
        res
        (iter (next a) (combiner res (term a))))
    )
  (iter a null-value)
  )

(define (sum term a next b)
  (accumulate + 0 term a next b)
  )

(define (product term a next b)
  (accumulate * 1 term a next b)
  )
```

## Accumulate: Add en Multiply

```scheme
(define (accumulate combiner null-value term a next b)
  (define (iter a res) 
    (if (> a b)
        res
        (iter (next a) (combiner res (term a))))
    )
  (iter a null-value)
  )

(define (add a b)
  (accumulate + b (lambda (x) x) a (lambda (y) (+ y 1)) a)
  )

(define (multiply a b)
  (accumulate * b (lambda (x) x) a (lambda (y) (+ y 1)) a)
  )
```

## Filtered-Accumulate

```scheme
(define (filtered-accumulate combiner filter? null-value term a next b)
  (define (iter a res) 
    (if (> a b)
        res
        (iter (next a) (if (filter? (term a)) (combiner res (term a)) res)))
    )
  (iter a null-value)
  )
```

## Filtered-Accumulate: grootste gemene deler

```scheme
(define (filtered-accumulate combiner filter? null-value term a next b)
  (define (iter a res) 
    (if (> a b)
        res
        (iter (next a) (if (filter? (term a)) (combiner res (term a)) res)))
    )
  (iter a null-value)
  )

(define (product-gcd n)
  (filtered-accumulate * (lambda (i) (= (gcd i n) 1)) 1 (lambda (x) x) 1 (lambda (y) (+ y 1)) n)
  )
```

## Syntactische Suiker: define met lambda-notatie

```scheme
(define f1 5)

(define f2 (lambda () 5))

(define f3 (lambda (x) 5))

(define f4 (lambda () (lambda () 5)))

(define f5 (lambda () (lambda () (lambda (x) 5))))
```

## Het verschil tussen let en let*: Lambda-notatie

```scheme
(let* ((x 2) (y (+ x 8)) (z (/ y x))) (+ x y z))
;herschreven a.d.h.v. lambda's
((lambda (x)
   ((lambda (y)
      ((lambda (z)
         (+ x y z))
       (/ y x)))
    (+ x 8)))
   2)
```
## Procedures die procedures maken: Compose

```scheme
(define (compose f g)
  (lambda (x) (f (g x)))
  )
```

## Procedures die procedures maken: make-do-n d.m.v. do

```scheme
(#%require racket/trace)
(define (make-do-n f n)
  (lambda () (do ((i 0 (+ i 1)))
               ((= n i) )
               (f)
               ))
  )
```

## Hogere Orde Procedures op lijsten: replace d.m.v. map

```scheme
(define (replace-dmv-map e1 e2 l)
  (map (lambda (x) (if (eq? x e1) e2 x)) l)
  )
```

## Hogere Orde Procedures op lijsten: All?

```Scheme
(define (all? pred l)
  (cond ((null? l) #t)
    ((pred (car l)) (all? pred (cdr l)))
    (else #f))
  )
```

## Hogere Orde Procedures op lijsten: zip

```scheme
(define (zip lst1 lst2 combine)
  (map combine lst1 lst2)
  )
; zonder gebruik van map
(define (zip lst1 lst2 combine)
  (if (null? lst1)
      '()
      (cons (combine (car lst1) (car lst2)) (zi
      
      p (cdr lst1) (cdr lst2) combine)))
  )
```

## Hogere Orde Procedures op lijsten: sum-of-squares d.m.v. zip

```scheme
(define (zip lst1 lst2 combine)
  (map combine lst1 lst2)
  )

(define (sum-of-squares lst1 lst2)
  (zip lst1 lst2 (lambda (x y) (+ (* x x) (* y y))))
  )
```

# Imperatief Programmeren

## Vectoren transformeren: vector-map!

```scheme
(define (vector-map! f vec)
  (do ((i 0 (+ i 1)))
    ((= i (vector-length vec)))
    (vector-set! vec i (f (vector-ref vec i)))))
```

## Vectoren transformeren: vector-map

```scheme
(define (vector-map f vec)
  (define new-v (make-vector (vector-length vec)))
  (do ((i 0 (+ i 1)))
    ((= i (vector-length vec)) new-v)
    (vector-set! new-v i (f (vector-ref vec i)))))
```

## Stukken uit een vector selecteren: vector-slice

```scheme
(define (vector-slice begin end vect)
  (define slice (make-vector (- end begin -1)))
  (do ((i begin (+ i 1)))
    ((> i end) slice)
    (vector-set! slice (- i begin) (vector-ref vect i))))
```

## Vectoren aaneen plakken: vector-append

```scheme
(define (vector-append v1 v2)
  (define vout (make-vector (+ (vector-length v1) (vector-length v2))))
  (do ((i 0 (+ i 1)))
    ((= i (vector-length v1)))
    (vector-set! vout i (vector-ref v1 i)))
  (do ((j 0 (+ j 1)))
    ((= j (vector-length v2)) vout)
    (vector-set! vout (+ j (vector-length v1)) (vector-ref v2 j))))
```

## Circulaire Datastructuren: make-ring!

```scheme
(define (make-ring! n)
  (define lst
    (let make-list
      ((current n))
      (if (< current 0) '()
          (cons current (make-list (- current 1))))))
  (set-cdr! (list-tail lst n) lst)
  l)

(define (print-ring r)
  (define (aux l)
    (if (not (null? l))
        (cond ((eq? (cdr l) r) (display " ")
                               (display (car l))
                               (display "..."))
              (else (display " ")
                    (display (car l))
                    (aux (cdr l))))))
  (aux r))
```

## Circulaire Datastructuren: shift-forward

```scheme
(define (make-ring! n)
  (define lst
    (let make-list
      ((current n))
      (if (< current 0) '()
          (cons current (make-list (- current 1))))))
  (set-cdr! (list-tail lst n) lst)
  lst)

(define (print-ring r)
  (define (aux l)
    (if (not (null? l))
        (cond ((eq? (cdr l) r) (display " ")
                               (display (car l))
                               (display "..."))
              (else (display " ")
                    (display (car l))
                    (aux (cdr l))))))
  (aux r))

(define (shift-forward r)
  (set! r (cdr r))
  r)
```

## Circulaire Datastructuren: shift-backward

```scheme
(define (make-ring! n)
  (define lst
    (let make-list
      ((current n))
      (if (< current 0) '()
          (cons current (make-list (- current 1))))))
  (set-cdr! (list-tail lst n) lst)
  lst)

(define (print-ring r)
  (define (aux l)
    (if (not (null? l))
        (cond ((eq? (cdr l) r) (display " ")
                               (display (car l))
                               (display "..."))
              (else (display " ")
                    (display (car l))
                    (aux (cdr l))))))
  (aux r))

(define (shift-backward r)
  (define (aux l)
    (if (eq? (cdr l) r) (set! r l)
        (aux (cdr l))))
  (aux r)
  r)
```

## Destructieve Procedures: map!

```scheme
(define (map! f lst)
  (if (not (null? lst))
      (begin
      (set-car! lst (f (car lst)))
      (map! f (cdr lst)))))
```

## Destructieve Procedures: schuif-in!

```scheme
(define (schuif-in! lst1 lst2)
  (if (null? lst1) "ok"
      (let
          ((l1 (cdr lst1)))
        (set-cdr! lst1 lst2)
        (schuif-in! lst2 l1))))
```

## Destructieve Procedures: merge! (Implementatie)

```scheme
(define (merge! b1 b2)
  (define res (if (symbol<? (caar b1) (caar b2)) b1 b2))
  (let aux
    ((best1 b1)
     (best2 b2))
    (cond ((or (null? best1) (null? best2)))
          ((element=? (car best1) (car best2))
           (aux best1 (cdr best2)))
          ((symbol<? (caar best2) (caar best1))
           (aux best2 best1))
          ((null? (cdr best1))
           (set-cdr! best1 best2))
          ((symbol<? (caadr best1) (caar best2))
           (aux (cdr best1) best2))
          (else
           (let
               ((l1 (cdr best1)))
             (set-cdr! best1 best2)
             (aux best2 l1)))))
  res)

(define (symbol<? s1 s2)
  (string<? (symbol->string s1) (symbol->string s2)))
 
(define (element=? el1 el2)
  (equal? el1 el2))

```

# Closures en Omgevingsdiagrammen

## sum & add-c

omgevingsmodel:

| Global |                    |
| ------ | ------------------ |
| c      | 3                  |
| add-c  | pointer naar add-c |
| sum    | pointer naar sum   |

| add-c                    |                     |
| ------------------------ | ------------------- |
| pointer naar definitions | pointer naar global |
| definitions:             |                     |
| (x y)                    | (+x y c)            |

| sum                      |                     |
| ------------------------ | ------------------- |
| pointer naar definitions | pointer naar global |
| (x y c)                  | (add-c x y)         |

## let naar lambda

```scheme
(let ((x 1)
      (y (+ 1 x)))
  (+ x y))
; omgezet naar lambda
((lambda (x y) (+ x y)) 1 (+ 1 x))
```
__error x: undefined; cannot reference an identifier before its definition__
 
Omgevingsdiagram van de lambda

| global |                     |
| ------ | ------------------- |
| lambda | pointer naar lambda |

| lambda                  |                                |
| ----------------------- | ------------------------------ |
| pointer naar definition | pointer naar global            |
| x                       | 1                              |
| y                       | ((+ 1 x) =>) error x undefined |
| definition              |                                |
| (x y)                   | (+ x y)                        |
Lambda word opgeroepen in de globale omgeving en er wordt in de oproep x aangeroepen die niet bestaat in die omgeving

## Omgevingsmodel let

```scheme
(define (print-abc a b c)
  (display a) (display " ")
  (display b) (display " ")
  (display c) (newline))
 
(define (foo a b c)
  (print-abc a b c)
  (let ((a 4) ; 1
        (c 5)
        (b c))
    (print-abc a b c)
    (let ((b 6) ; 2
          (c a))
      (print-abc a b c))
    (let ((a b) ; 3
          (c a))
      (print-abc a b c)))
  (print-abc a b c))
```

omgevings model tijdens (foo 1 2 3)
output:
>1 2 3
>4 3 5
>4 6 4
>3 3 4
>1 2 3 

![[omgevingsmodelLet.png]]
## let* naar lambda

```scheme
(let* ((x 1)
       (y (+ 1 x)))
  (+ x y))
; omgezet naar lambda
((lambda (x)
   ((lambda (y)
      (+ x y)) (+ 1 x)))
 1)
```

Omgevingsdiagram van de lambda

| global |                     |
| ------ | ------------------- |
| lambda | pointer naar lambda |

| lambda 1                |                                         |
| ----------------------- | --------------------------------------- |
| pointer naar definition | pointer naar global                     |
| x                       | 1                                       |
| definition              |                                         |
| (x)                     | ((lambda (y)<br>      (+ x y)) (+ 1 x)) |

| lambda 2                |                       |
| ----------------------- | --------------------- |
| pointer naar definition | pointer naar lambda 1 |
| y                       | ((+ 1 x) =>) 2        |
| definition              |                       |
| (y)                     | (+ x y)               |

Lambda 2 word opgeroepen in de lambda 1 omgeving en er wordt in de oproep x aangeroepen die nu wel bestaat in die omgeving

## Omgevingsmodel let*

![[omgevingsmodelLetSter.png]]
## Twice: omgevingsmodel

![[omgevingsmodelTwice.png]]

## Examen Informatica Partieel januari 1995

![[omgevingsmodelExamen1995.png]]
## sum & add-c: dynamische scoping

> 9

## Dynamische scoping: Voorspel

> 1: 'global
> 2: 'local

## Flip

```scheme
(define flip 
  (let ((state #f))
    (lambda ()
       (set! state (not state))
       (if state 1 0))))
```

## Flip: Omgevingsmodel-diagram

![[omgevingsmodelFlip.png]]
## Flip: Make-flip

```scheme
(define (make-flip)
  (let ((state #f))
    (lambda ()
       (set! state (not state))
       (if state 1 0))))
(define flip (make-flip))
```

## Flip: Voorspel

```scheme
(define flip (make-flip))
(define flap1 (flip))
(define (flap2) (flip))
(define flap3 flip)
(define (flap4) flip)
```
1. `flap1`: 1
2. `flap2`: procedure
3. `flap3`: procedure
4. `flap4`: procedure
5. `(flap1)`: error not a procedure
6. `(flap2)`: 0
7. `(flap3)`: 1
8. `(flap4)`: procedure
9. `flap1`: 1
10. `(flap3)`: 0
11. `(flap2)`: 1

# Objectgebaseerd Programmeren

## Random: Simpele Generator

```scheme
(define (make-random m a seed)
  (let ((xi seed))
    (lambda ()
      (set! xi (modulo (* xi a) m))
      (exact->inexact (/ xi m)))))
```

## Random: Generator met berichten

```scheme
(define (make-random m a seed)
  (let ((xi seed))
    (lambda (args)
      (cond ((eq? 'generate args)
             (lambda ()
               (set! xi (modulo (* xi a) m))
               (exact->inexact (/ xi m))))
            ((eq?  args 'reset)
             (lambda (new-seed)
               (set! xi seed)))))))
```

## Examen Wiskunde Partieel januari 1995

```scheme
(define (make-counter initial)
  (define (increase!)
    (set! initial (+ initial 1)))
 
  (define (decrease!)
    (set! initial (- initial 1)))
 
  (define (dispatch m)
    (cond ((eq? m 'increase!) increase!)
          ((eq? m 'decrease!) decrease!)
          ((eq? m 'read) initial)
          (else (display "wrong message"))))
 
  dispatch)

(define (make-parking capacity1 capacity2)
  (let ((cars1 0)
        (cars2 0))
    (define (full?)
      (if (and (= cars1 capacity1) (= cars2 capacity2)) #t #f))

    (define (empty?)
      (if (and (= cars1 0) (= cars2 0)) #t #f))

    (define (level)
      (if (= cars1 capacity1) 2 1))

    (define (car-enters!)
      (cond ((< cars1 capacity1) (set! cars1 (+ cars1 1)))
            ((< cars2 capacity2) (set! cars2 (+ cars2 1)))
            (else #f)))

    (define (car-leaves!)
      (cond ((> cars1 0) (set! cars1 (- cars1 1)))
            ((> cars2 0) (set! cars2 (- cars2 1)))
            (else #f)))

    (define (dispatch m)
      (cond ((eq? m 'full?) (full?))
            ((eq? m 'empty?) (empty?))
            ((eq? m 'level) (level))
            ((eq? m 'car-enters!) car-enters!)
            ((eq? m 'car-leaves!) car-leaves!)))
    dispatch))
```

## Examen januari 2018

### Laadpaal

```scheme
(define (maak-laadstation)
  (let ((auto #f)
        (stroom 0))
    (define (withdraw! number)
      (set! stroom (+ stroom number)))
    (define (koppel! new-auto)
      (set! auto new-auto))
    (define (ontkoppel!)
      (set! auto #f))
    (define (vrij?)
      (not auto))
    (define (dispatch m . args)
      (cond ((eq? m 'withdraw!) (withdraw! (car args)))
            ((eq? m 'koppel!) (koppel! (car args)))
            ((eq? m 'ontkoppel!) (ontkoppel!))
            ((eq? m 'vrij?) (vrij?))))
    dispatch))
```

### Auto

```scheme
(define (maak-auto capaciteit)
  (let ((current-battery capaciteit)
        (laadpaal #f))
    (define (charge)
      current-battery)
    (define (charge!)
      (set! current-battery capaciteit))
    (define (koppel! laadstation)
      (set! laadpaal laadstation)
      (laadstation 'koppel! dispatch))
    (define (ontkoppel!)
      (laadpaal 'ontkoppel!)
      (set! laadpaal #f))
    (define (dispatch m . args)
      (cond ((eq? m 'charge) (charge))
            ((eq? m 'charge!) (charge!))
            ((eq? m 'koppel!) (koppel! (car args)))
            ((eq? m 'ontkoppel!) (ontkoppel!))
            (else (display "Wrong message"))))
    dispatch))
```

### Laadpark

```scheme
(define (maak-laadpark n)
  (let ((laadpalen (make-vector n)))
    (define (full?)
      (not (find-empty)))
    (define (find-empty)
      (let loop ((i 0))
        (cond ((= i n) #f)
              (((vector-ref laadpalen i) 'vrij?)
               i)
              (else
               (loop (+ i 1))))))
    (define (enter! auto)
      (cond ((full?) #f)
            (else
             (let ((id (find-empty)))
               (auto 'koppel! (vector-ref laadpalen id)))
             #t)))
    (define (dispatch m . args)
      (cond ((eq? m 'full?) (full?))
            ((eq? m 'enter!) (enter! (car args)))
            (else (display "wrong message"))))
    (let loop ((i 0))
        (cond ((= i n))
              (else
               (vector-set! laadpalen i (maak-laadstation))
               (loop (+ i 1)))))
    dispatch
    ))
```

### Gebruik van objecten
Volledige code samen
```scheme
(define (maak-laadstation)
  (let ((auto #f)
        (stroom 0))
    (define (withdraw! number)
      (set! stroom (+ stroom number)))
    (define (koppel! new-auto)
      (set! auto new-auto))
    (define (ontkoppel!)
      (set! auto #f))
    (define (vrij?)
      (not auto))
    (define (dispatch m . args)
      (cond ((eq? m 'withdraw!) (withdraw! (car args)))
            ((eq? m 'koppel!) (koppel! (car args)))
            ((eq? m 'ontkoppel!) (ontkoppel!))
            ((eq? m 'vrij?) (vrij?))))
    dispatch))

(define (maak-auto capaciteit)
  (let ((current-battery capaciteit)
        (laadpaal #f))
    (define (charge)
      current-battery)
    (define (charge!)
      (set! current-battery capaciteit))
    (define (koppel! laadstation)
      (set! laadpaal laadstation)
      (laadstation 'koppel! dispatch))
    (define (ontkoppel!)
      (laadpaal 'ontkoppel!)
      (set! laadpaal #f))
    (define (dispatch m . args)
      (cond ((eq? m 'charge) (charge))
            ((eq? m 'charge!) (charge!))
            ((eq? m 'koppel!) (koppel! (car args)))
            ((eq? m 'ontkoppel!) (ontkoppel!))
            (else (display "Wrong message"))))
    dispatch))

(define (maak-laadpark n)
  (let ((laadpalen (make-vector n)))
    (define (full?)
      (not (find-empty)))
    (define (find-empty)
      (let loop ((i 0))
        (cond ((= i n) #f)
              (((vector-ref laadpalen i) 'vrij?)
               i)
              (else
               (loop (+ i 1))))))
    (define (enter! auto)
      (cond ((full?) #f)
            (else
             (let ((id (find-empty)))
               (auto 'koppel! (vector-ref laadpalen id)))
             #t)))
    (define (dispatch m . args)
      (cond ((eq? m 'full?) (full?))
            ((eq? m 'enter!) (enter! (car args)))
            (else (display "wrong message"))))
    (let loop ((i 0))
        (cond ((= i n))
              (else
               (vector-set! laadpalen i (maak-laadstation))
               (loop (+ i 1)))))
    dispatch
    ))

(define auto1 (maak-auto 10))
(define auto2 (maak-auto 10))
(define auto3 (maak-auto 10))
(define laadpark (maak-laadpark 2))

(laadpark 'enter! auto1)
(laadpark 'enter! auto2)
(laadpark 'enter! auto3)
(auto1 'ontkoppel!)
(laadpark 'enter! auto2)
```

# Bomen en operaties op bomen: Boominterpretatie van Geneste Lijsten

## Recursie/iteratie op geneste lijsten: modeloplossing

```scheme
(define (atom? x)
    (not (pair? x)))
    
(define (tree-procedure-rec lst)
    (cond ((null? lst) base-result)
           ((atom? lst) atom-result)
           (else (combine-branches (tree-procedure-rec (car lst))
                                   (tree-procedure-rec (cdr lst))))))
```

## Diepte en bladeren van een boom: Aantal elementen

```scheme
(define (atom? x)
  (not (pair? x)))
(define (leaf-count lst)
  (cond ((null? lst) 0)
        ((atom? lst) 1)
        (else (+ (leaf-count (car lst))
                 (leaf-count (cdr lst))))))
```

## Diepte en bladeren van een boom: Diepte

```scheme
(define (atom? x)
  (not (pair? x)))
(define (depth lst)
  (cond ((null? lst) 0)
        ((atom? lst) 0)
        (else (max (+ 1 (depth (car lst)))
                   (depth (cdr lst))))))
```

## Diepte en bladeren van een boom: Combinatie

```scheme
(define (atom? x)
  (not (pair? x)))
(define (depth-and-leaf-count tree)
  (define count 0)
  (cons
   (let loop
     ((lst tree))
     (cond ((null? lst)
            0)
           ((atom? lst)
            (set! count (+ count 1))
            0)
           (else
            (max (+ 1 (loop (car lst)))
                 (loop (cdr lst))))))
   count))
```

## Fringe

```scheme
(define (atom? x)
  (not (pair? x)))
(define (fringe tree)
  (define out '())
  (let loop ((lst tree))
    (cond ((null? lst))
          ((atom? lst) (set! out (cons lst out)))
          (else (loop (car lst))
                (loop (cdr lst)))))
  (reverse out))
; Alternatieve versie
(define (fringe2 lst)
  (cond ((null? lst) '())
        ((atom? lst) (list lst))
        (else (append (fringe2 (car lst))
                      (fringe2 (cdr lst))))))
```


## Structuur vergelijken

```scheme
(define (atom? x)
  (not (pair? x)))
(define (same-structure? l1 l2)
  (cond ((and (null? l1) (null? l2) #t))
        ((and (atom? l1) (atom? l2) #t))
        ((or (null? l1) (null? l2) (atom? l1) (atom? l2)) #f)
        (else (and (same-structure? (car l1) (car l2))
                   (same-structure? (cdr l1) (cdr l2))))))
```

## Hogere Orde: deep-combine

```scheme
(define (atom? x)
  (not (pair? x)))
(define (deep-combine f neutral lst)
  (cond ((null? lst) neutral)
        ((atom? lst) lst)
        (else (f (deep-combine f neutral (car lst))
                 (deep-combine f neutral (cdr lst))))))
```

## Hogere Orde: deep-map

```scheme
(define (atom? x)
  (not (pair? x)))
(define (deep-map f lst)
  (cond ((null? lst) '())
        ((atom? lst) (f lst))
        (else (cons (deep-map f (car lst))
                 (deep-map f (cdr lst))))))
```

## Hogere Orde: deep-change

```scheme
; utils
(define (atom? x)
  (not (pair? x)))
(define (deep-map f lst)
  (cond ((null? lst) '())
        ((atom? lst) (f lst))
        (else (cons (deep-map f (car lst))
                    (deep-map f (cdr lst))))))

(define (deep-change e1 e2 lst)
  (deep-map (lambda (x) (if (eq? x e1) e2 x)) lst)
  )
```
## Hogere Orde: deep-atom-member?

```scheme
;utils
(define (deep-map f lst)
  (cond ((null? lst) '())
        ((atom? lst) (f lst))
        (else (cons (deep-map f (car lst))
                    (deep-map f (cdr lst))))))
(define (deep-combine f neutral lst)
  (cond ((null? lst) neutral)
        ((atom? lst) lst)
        (else (f (deep-combine f neutral (car lst))
                 (deep-combine f neutral (cdr lst))))))
(define (atom? x)
  (not (pair? x)))

(define (deep-atom-member? e lst)
  (let ((new (deep-map (lambda (x) (if (= e x) #t #f)) lst)))
    (deep-combine (lambda (x y) (if (or x y) #t #f)) #f new)))
```
## Hogere Orde: count-atoms

```scheme
;utils
(define (deep-map f lst)
  (cond ((null? lst) '())
        ((atom? lst) (f lst))
        (else (cons (deep-map f (car lst))
                    (deep-map f (cdr lst))))))
(define (deep-combine f neutral lst)
  (cond ((null? lst) neutral)
        ((atom? lst) lst)
        (else (f (deep-combine f neutral (car lst))
                 (deep-combine f neutral (cdr lst))))))
(define (atom? x)
  (not (pair? x)))

(define (count-atoms lst)
  (let ((new (deep-map (lambda (x) 1) lst)))
    (deep-combine (lambda (x y) (+ x y)) 0 new)))
```

## Examen Informatica Partieel januari 1995

```scheme
(define (deep-map f lst)
  (cond ((null? lst) '())
        ((atom? lst) (f lst))
        (else (cons (deep-map f (car lst))
                    (deep-map f (cdr lst))))))
(define (deep-combine f neutral lst)
  (cond ((null? lst) neutral)
        ((atom? lst) lst)
        (else (f (deep-combine f neutral (car lst))
                 (deep-combine f neutral (cdr lst))))))
(define (atom? x)
  (not (pair? x)))

(define boom
  '((blad (appel . golden))
    (blad (appel . granny))
    (((appel . golden) blad) blad (appel . cox))))
```
### Tel bladeren

```scheme
(define (leafs lst)
  (let ((new (deep-map (lambda (x) (if (eq? x 'blad) 1 0)) lst)))
    (deep-combine (lambda (x y) (+ x y)) 0 new)))
```

### Zoek alle appels

```scheme
(define (all-apples lst)
  (cond ((null? lst) '())
        ((atom? lst) (if (not (or (eq? lst 'appel) (eq? lst 'blad))) (list lst) '()))
        (else (append (all-apples (car lst))
                      (all-apples (cdr lst))))))
```

### Geef de verschillende soorten appels

```scheme
(define (apple-types lst)
  (let loop ((all (all-apples lst)))
    (cond ((null? all)'())
          ((null? (cdr all))
           all)
          ((not (member (car all) (cdr all)))
           (cons (car all) (loop (cdr all))))
          (else
           (loop (cdr all))))))
```

### Procedure om de bomen te bewerken

```scheme
(define (bewerk-boom boom doe-blad doe-appel combiner init)
  (cond ((null? boom) init)
        ((atom? boom) (doe-blad boom))
        ((eq? (car boom) 'appel) (doe-appel boom))
        (else (combiner (bewerk-boom (car boom) doe-blad doe-appel combiner init)
                        (bewerk-boom (cdr boom) doe-blad doe-appel combiner init)))))
```

### Tel bladeren (hogere orde)

```scheme
(define (leafs-dmv-bewerk boom)
  (bewerk-boom boom (lambda (x) 1) (lambda (x) 0) + 0))
```

### Geef alle appels (hogere orde)

```scheme
(define (all-apples-dmv-bewerk boom)
  (bewerk-boom boom (lambda (x) '()) (lambda (x) (list (cdr x))) append '()))
```

## Circulaire Datastructuren: cycles?
> Note: we are only looking at cycles in cdr
```scheme
(define (atom? x)
  (not (pair? x)))
(define (cycles? r)
  (define (loop visited r)
    (cond ((null? r)
           #f)
          ((atom? r)
           #f)
          ((member r visited) #t)
          (else           
           (loop (cons r visited) (cdr r)))))
  (loop '() r))
```
## Correcte versie count-pairs

```scheme
(define (atom? x)
  (not (pair? x)))

(define (count-pairs xin)
  (define (loop visited x)
    (cond ((not (pair? x))
           0)
          ((member x visited)
          0)
          (else
           (+ (loop (cons x visited) (cdr x))
              1))))
  (loop '() xin))
```

# Bomen en procedures op bomen: Familiebomen & Hiërarchische Relaties

## Modeloplossing

```scheme
(define (parent tree)   ...)
(define (children tree) ...)
 
(define (tree-proc tree ...)
  (cond ((test-parent (parent tree)) ...)
        (else (tree-proc-in (children tree) ...))))
 
(define (tree-proc-in lst ...)
  (cond ((null? lst) ...)
        (else (combine-res (tree-proc (car lst) ...)
                           (tree-proc-in (cdr lst) ...)))))
```

## Examen Informatica 2e Zit 1995

![[examen-informatica-2e-zit-1995-organigram.png]]
```scheme
(define organigram
  '(directeur
    (hoofd-verkoop (verkoopsleider-vlaanderen)
                   (verkoopsleider-brussel))
    (hoofd-productie (hoofd-inkoop (bediende1)
                                   (bediende2)
                                   (bediende3))
                     (hoofd-fakturen))
    (hoofd-administratie (hoofd-personeel)
                         (hoofd-boekhouding))))
```

### Bazen

```scheme
(define (bazen-van organigram employee)
  (define (parent tree) (car tree))
  (define (children tree) (cdr tree))
  (define (tree-proc tree result)
    (display result)(newline)
    (cond ((eq? (parent tree) employee) result)
          ((null? (children tree)) #f)
          (else (tree-proc-in (children tree) (cons (parent tree) result)))))
  (define (tree-proc-in lst result)
    (cond ((null? lst) #f)
          (else
           (or (tree-proc (car lst) result)
           (tree-proc-in (cdr lst) result))
           )))
  (tree-proc organigram '()))
```

### Hiërarchie

```scheme
(define (hierarchisch? p1 p2 organigram)
  (define (parent tree) (car tree))
  (define (children tree) (cdr tree))

  (define (tree-proc tree b1 b2)
    (cond ((eq? (parent tree) p1) (tree-proc-in (children tree) #t b2))
          ((eq? (parent tree) p2) (tree-proc-in (children tree) b1 #t))
          (else (tree-proc-in (children tree) b1 b2))))
  
  (define (tree-proc-in lst b1 b2)
    (cond ((and b1 b2) #t)
          ((null? lst) #f)
          (else
           (or (tree-proc (car lst) b1 b2)
           (tree-proc-in (cdr lst) b1 b2))
           )))
  (tree-proc organigram #f #f))
```

### Collega's

```scheme
(define (collegas employee organigram)
  (define (flatten lst)
  (cond
    ((null? lst) '())
    ((not (pair? lst)) (list lst)) 
    (else (append (flatten (car lst))      
                  (flatten (cdr lst))))))
  (define (parent tree) (car tree))
  (define (children tree) (cdr tree))
  (define (tree-proc tree result)
    (display result)(newline)
    (cond ((eq? (parent tree) employee) (append result (flatten (children tree))))
          ((null? (children tree)) #f)
          (else (tree-proc-in (children tree) (cons (parent tree) result)))))
  (define (tree-proc-in lst result)
    (cond ((null? lst) #f)
          (else
           (or (tree-proc (car lst) result)
           (tree-proc-in (cdr lst) result))
           )))
  (tree-proc organigram '()))
```

## Examen Informatica januari 2010

```scheme
(define VUBOrganigram
  '(VUB (academisch (rectoraat)
                    (faculteiten
                     (rechten (bachelor (ba-rechten)
                                        (ba-criminologie))
                              (master (ma-rechten)
                                      (ma-criminologie)))
                     (economie)
                     (wetenschappen (bachelor (ba-wiskunde)
                                              (ba-fysica)
                                              (ba-cw))
                                    (master (ma-wiskunde)
                                            (ma-fysica)
                                            (ma-cw)))))
        (administratief (personeel) (financien))))
```

![[examen-informatica-2010-organigram.png]]

```scheme
(define (display-n n d)
  (cond ((> n 0) (display d)
                 (display-n (- n 1) d))))
(define (print-lijn aantalblanco tekst)
  (display-n aantalblanco " ")
  (display tekst)
  (newline))
```

### Print-vanaf

```scheme
(define VUBOrganigram
  '(VUB (academisch (rectoraat)
                    (faculteiten
                     (rechten (bachelor (ba-rechten)
                                        (ba-criminologie))
                              (master (ma-rechten)
                                      (ma-criminologie)))
                     (economie)
                     (wetenschappen (bachelor (ba-wiskunde)
                                              (ba-fysica)
                                              (ba-cw))
                                    (master (ma-wiskunde)
                                            (ma-fysica)
                                            (ma-cw)))))
        (administratief (personeel) (financien))))
(define (display-n n d)
  (cond ((> n 0) (display d)
                 (display-n (- n 1) d))))
(define (print-lijn aantalblanco tekst)
  (display-n aantalblanco " ")
  (display tekst)
  (newline))

(define (print-vanaf organigram label)
  (define (parent tree) (car tree))
  (define (children tree) (cdr tree))
  (define (print-boom boom)
    (define (tree-proc tree level)
      (print-lijn level (parent tree))
      (tree-proc-in (children tree) (+ level 1)))
    (define (tree-proc-in lst level)
      (cond ((null? lst))
            (else
             (tree-proc (car lst) level)
             (tree-proc-in (cdr lst) level))
            ))
    (tree-proc boom 0))
  (define (tree-proc tree)
    (cond ((eq? (parent tree) label)
           (print-boom tree))
          ((null? (children tree)))
          (else (tree-proc-in (children tree)))))
  (define (tree-proc-in lst)
    (cond ((null? lst))
          (else
           (tree-proc (car lst))
           (tree-proc-in (cdr lst))
          )))
  (tree-proc organigram))
```

### Print-tot

```scheme
(define (print-tot organigram niveau)
  (define (parent tree) (car tree))
  (define (children tree) (cdr tree))
  
    (define (tree-proc tree level)
      (print-lijn level (parent tree))
      (tree-proc-in (children tree) (+ level 1)))
    (define (tree-proc-in lst level)
      (cond ((null? lst))
            ((> level niveau))
            (else
             (tree-proc (car lst) level)
             (tree-proc-in (cdr lst) level))
            ))
  (tree-proc organigram 0))
```

## Examen Informatica januari 2008
### Verdeel democratisch

```scheme
(define (atom? x)
  (not (pair? x)))
(define (leaf-count lst)
  (cond ((null? lst) 0)
        ((atom? lst) 1)
        (else (+ (leaf-count (car lst))
                 (leaf-count (cdr lst))))))
(define (verdeel-democratisch familieboom budget)
  (/ budget (- (leaf-count familieboom) 1))
  )
```
### Bereken budget

```scheme
(define (budget familieboom lst)
  (define parent car)
  (define children cdr)
  (define (tree-proc tree verdeling)
    (+ (car verdeling) (tree-proc-in (children tree) (cdr verdeling))))
  (define (tree-proc-in lst verdeling)
    (cond ((null? lst) 0)
          ((null? verdeling) 0)
          (else (+ (tree-proc (car lst) verdeling)
                   (tree-proc-in (cdr lst) verdeling)))))
  (tree-proc-in (children familieboom) lst))
```

### Verdeel budget onder kinderen zonder nakomelingen

```scheme
(define (verdeel familieboom budget)
  (define parent car)
  (define children cdr)
  (define (tree-proc tree budget)
    (cond ((null? (children tree)) (list (list (parent tree) budget)))
          (else (tree-proc-in (children tree) (/ budget (length (children tree)))))))
  (define (tree-proc-in lst budget)
    (cond ((null? lst) '())
          (else (append (tree-proc (car lst) budget)
                   (tree-proc-in (cdr lst) budget)))))
  (tree-proc familieboom budget))
```

# Stromen en uitgestelde evaluatie

## Introductie
> **See Also WPO/streams.rkt & WPO/dodona-streams.rkt**
```scheme
(load "streams.rkt")
```
**Let op!** Je moet er wel voor zorgen dat het bestand met je code en het streams.rkt bestand in dezelfde directory opgeslagen zijn.

In dit bestand zijn de volgende procedures gedefinieerd: `cons-stream`, `head`, `tail`, `empty-stream?`, `stream-accumulate`, `stream-accumulate-n`, `stream-map`, `stream-filter`, `stream-for-each`, `stream-append`, `enumerate-int`, `enumerate-tree`, `stream-print`, `take`, `pairs`, `stream-flatten`, `stream-interleave`, `stream-flatten/interleaved`, `stream-accumulate-delayed`, `stream-interleave-delayed` en `stream-values`. Ook `the-empty-stream` is in dit bestand gedefinieerd.

## Reeksontwikkelingen

```scheme
(load "streams.rkt")
(define (factorial n)
  (do ((count 1 (+ count 1))
       (result 1 (* result count)))
    ((< n count) result)
    ))
(define (calc-e n)
  (stream-accumulate
   + 0
   (stream-map
    (lambda (x) (/ 1 (factorial x)))
    (enumerate-int 0 n))))
(define (sinus x n)
  (stream-accumulate
   + 0
   (stream-map
    (lambda (a) (let ((b (+ (* a 2) 1)))
                  (if (even? a)
                    (/ (expt x b) (factorial b))
                    (- 0 (/ (expt x b) (factorial b))))))
      (enumerate-int 0 (- n 1)))))
```

## som-kwadraten-oneven-elementen

```scheme
(load "streams.rkt")
(define (sum-odd-squares stream)
  (stream-accumulate
   + 0
   (stream-map
    (lambda (x) (* x x))
    (stream-filter
     odd?
     stream))))
```

## triples

```scheme
(define (odd-sum-triples max)
  (stream-flatten
   (stream-map
    (lambda (y)
      (stream-map
       (lambda (x) (list x  y (+ x y)))
       (stream-filter odd? (enumerate-int 1 (- max 1)))))
    (stream-filter odd? (enumerate-int 1 (- max 1))))))
```

## integers

```scheme
(define integers (cons-stream 1 (stream-map (lambda (x) (+ x 1)) integers)))
```

## Stream-filter

```scheme
(define integers (cons-stream 1 (stream-map (lambda (x) (+ x 1)) integers)))
(define (integers-special integers)
   (stream-filter
    (lambda (y) (not (or (= (modulo y 2) 0)
                         (= (modulo y 3) 0)
                         (= (modulo y 5) 0))))
    integers))
```

## triplets

```scheme
(define (triplets)
  (stream-map
   (lambda (l) (car l))
   (stream-flatten/interleaved
    (stream-map
     (lambda (x)
       (stream-map
        (lambda (y)
          (stream-map
           (lambda (k) (list x y k))
           (enumerate-int 1 (+ x y))))
        integers))
     integers))))
```

## Examen Informatica eerste zit 1997
> **See Also WPO/examen-informatica-1997-streams.rkt**
### Cuts
```scheme
(define (cut stream)
  (if (empty-stream? stream)
      the-empty-stream
      (let ((current (head stream)))
        (let ((current-group (stream-filter (lambda (x) (= x current)) stream)))
          (cons-stream
           current-group
           (cut (stream-filter (lambda (x) (> x current)) (tail stream))))))))
```

### Merge

```scheme
(define (merge str1 str2)
  (cond
    ((empty-stream? str1) str2) 
    ((empty-stream? str2) str1)
    (else
     (let ((head1 (head str1))
           (head2 (head str2)))
       (if (< head1 head2)
           (cons-stream head1 (merge (tail str1) str2))
           (cons-stream head2 (merge str1 (tail str2))))))))
```

### Merge-n

```scheme
(define (merge str1 str2)
  (cond
    ((empty-stream? str1) str2) 
    ((empty-stream? str2) str1)
    (else
     (let ((head1 (head str1))
           (head2 (head str2)))
       (if (< head1 head2)
           (cons-stream head1 (merge (tail str1) str2))
           (cons-stream head2 (merge str1 (tail str2))))))))
(define (merge-n strs)
  (if (empty-stream? (tail strs))
      (head strs)
      (let* ((h1 (head strs))
            (h2 (head (tail strs)))
            (rest (tail (tail strs))))
        (display h1)(newline)
        (display h2)(newline)
        (display strs)(newline)
        (merge-n (cons-stream (merge h1 h2) rest))
      )))
```

### Traffiek in een pretpark

```scheme
(define (pretpark-traffiek strs)
  (stream-map
   (lambda (str)
     (cons
      (head str)
      (stream-accumulate
       + 0 (stream-map (lambda (x) 1) str))))
   (cut
    (merge-n strs))))
```

## Examen Januari 2008
> **See Also WPO/examen-informatica-januari-2008-streams.rkt**
### Prune

```scheme
(define (prune str n)
  (define i -1)
  (stream-filter
   (lambda (x)
     (set! i (+ i 1))
     (even? (quotient i n)))
   str))
```

### Split

```scheme
(define (split str n)
  (define (helper stream curr count)
    (if (empty-stream? stream)
        (if (empty-stream? curr)
            the-empty-stream
            (cons-stream curr the-empty-stream))
        (let ((x (head stream)))
          (if (= count n)
              (cons-stream curr (helper (tail stream) (cons-stream x the-empty-stream) 1))
              (helper (tail stream) (stream-append curr (cons-stream x the-empty-stream)) (+ count 1))))))
  (helper str the-empty-stream 0))
```

### Daggemiddelden

```scheme
(define (daggemiddelden str)
  (stream-map
   (lambda (x)
     (/ x 12))
   (stream-map
    (lambda (x)
      (stream-accumulate + 0 x))
    (split (prune str 12) 12))))
```

### Nachtgemiddelden

```scheme
; Alternative version that starts with pruning instead of starting with streaming
(define (prune-alt str n)
  (define i -1)
  (stream-filter
   (lambda (x)
     (set! i (+ i 1))
     (odd? (quotient i n)))
   str))
; Dodona expects inexact numbers here in contrast with previous exercise
(define (nachtgemiddelden str)
  (stream-map
   (lambda (x)
     (exact->inexact (/ x 12)))
   (stream-map
    (lambda (x)
      (stream-accumulate + 0 x))
    (split (prune-alt str 12) 12))))
```