# Hoofdstuk 1
## 1.4.3
Analogous to the complex ADT, let's define the fraction ADT. Here are the procedures that should be supported by the ADT:

- `(new n d)` returns the rational number whose numerator is the number `n` and whose denominator is the number `d`.
- `(numer f)` returns the numerator of the fraction `f`.
- `(denom f)` returns the denominator of the fraction `f`.
- `(fraction? v)` checks whether or not a Scheme value `v` is a fraction.
- `(+ f1 f2)` adds two fractions `f1` and `f2`.
- `(- f1 f2)` a fraction `f2` from `f1`.
- `(/ f1 f2)` divides a fraction `f1` by the fraction `f2`.
- `(* f1 f2)` multiplies two fractions `f1` and `f2`.
Given this description:
- First, formulate the ADT itself. I.e., specify all procedures along with their procedural type.
> new: (number number -> fraction)
> numer: (fraction -> number)
> denom: (fraction -> number)
> fraction?: (any -> boolean)
> +, -, /, *: (fraction fraction -> fraction)
- Second, implement the ADT in the procedural style as a Scheme library.
> Zie fraction.rkt in libraries
```scheme
(define-library (fraction)
  (export new numer denom fraction? + - * /)
  (import (rename (scheme base) (* base:*) (+ base:+) (- base:-) (/ base:/))
          (scheme write))
  (begin

    (define-record-type fraction
      (new n d)
      fraction?
      (n numer)
      (d denom))

    (define (+ f1 f2)
      (new (base:+ (base:* (numer f1) (denom f2))
                   (base:* (numer f2) (denom f1)))
           (base:* (denom f1) (denom f2)))
      )

    (define (- f1 f2)
      (new (base:- (base:* (numer f1) (denom f2))
                   (base:* (numer f2) (denom f1)))
           (base:* (denom f1) (denom f2)))
      )

    (define (/ f1 f2)
      (new (base:* (numer f1) (denom f2))
           (base:* (denom f1) (numer f2)))
      )

    (define (* f1 f2)
      (new (base:* (numer f1) (numer f2))
           (base:* (denom f1) (denom f2)))
      )

    ))
```
- Third, write a procedure `=` that uses the ADT in order to verify whether or not two fractions are equal. You are not allowed to add `=` to your library.
```scheme
(define (frac:= frac1 frac2)
  (= (/ (frac:numer frac1) (frac:denom frac1)
     (/ (frac:numer frac1) (frac:denom frac1)))))
```
- Fourth, reimplement the constructor such that rationals are always represented in reduced form. Does this reimplementation affect your code for `=`?
> nu moeten we de deling niet meer uitvoeren, kunnen gewoon gelijkheid van teller en noemer

## 1.4.1
Specify the procedural type of the following built-in Scheme procedures: `cons`, `car`, `cdr`, `vector-ref`, `vector-set!`, `member`. You can use the following data types: any, pair, vector, number, boolean and ∅. You can also use singleton sets such as {`#f`}.

```scheme
cons
	(any, any -> pair)
car
	(pair -> any)
cdr
	(pair -> any)
vector-ref
	(vector, number -> any)
vector-set!
	(vector, number, number -> ∅)
member
	(any, pair -> pair U {#f})
```

## 1.4.5
Consider the ADT dictionary and suppose that we want to use an implementation of the ADT in the following applications. Formally specify K and V for all cases.
- A dictionary Dutch-English that maps a Dutch word onto its only translation in English.
> dict<string, string>
- A dictionary Dutch-English that maps a Dutch word onto a series of possible translations in English.
> dict<string, pair>
- A list of students that associates a student's name with the number of credits he (or she) still has to collect in order to get a bachelor degree.
> dict<string, number>
- A list of students that associates a student's name with the fact whether or not the student is male.
> dict<string, bool>
- A list of students that associates a student with his or her study program. The study program is a mapping that associates course names with the mark obtained by the student for that particular course.
> dict<string, dict<string, number>>

Uit de slides h1 p32
```scheme
ADT dictionary< K V >
new
	( ( K K -> boolean ) -> dictionary< K V > )
dictionary?
	( any -> boolean )
insert!
	( dictionary< K V > K V -> dictionary< K V > )
delete!
	( dictionary< K V > K -> dictionary< K V > )
find
	( dictionary< K V > K -> V ∪ {#f} )
empty?
	( dictionary< K V > -> boolean )
full?
	( dictionary< K V > -> boolean )
```

## 1.4.6
Consider two procedures to retrieve the last element from a data structure. Their procedural type looks as follows:
- `last-of-list`  
	(pair → number)
- `last-of-vector`  
	(vector → number)
Given these types,
- Implement both procedures.
- What is the wort-case performance characteristic of these procedures?
- What is the best-case performance characteristic of the procedures?
```scheme
(define (last-of-list lst)
  (cond ((null? l) #f)
	    ((null? (cdr lst)) (car lst)
        (else (last-of-list (cdr lst)))))
; worst-case O(n)
; best-case Omega(n)
; dus ook Theta(n)

(define (last-of-vector vct)
  (vector-ref vct (- (vector-length vct) 1)))
; worst-case O(1)
; best-case Omega(1)
; dus ook Theta(1)
```

## 1.4.2
Specify the procedural type of the following higher-order procedures. You can use the same data types as in the previous exercise.
- `(map f l)` applies a procedure `f` to all elements of a list `l`. The result is a new list.
> ((any -> any) pair -> pair)

- `(sum a b term next)` begins at `a` and perpetually adds `(term a)` to the number that corresponds to `(sum (next a) b term next)`. It does this as long as `a` is smaller than `b`.
```scheme
(define (sum a b term next)
	(if (> a b)
	    0
        (+ (term a) (sum (next a) b term next))))
```
> (number number (number -> number) (number -> number) -> number>)

- `(compose f g)` takes two one-argument procedures `f` and `g` and it returns their mathematical composition.
```scheme
(define (compose f g)
	(lambda (x) (f (g x))))
```
> ((any -> any) (any -> any) -> (any -> any))

## 1.4.8
Consider the following Scheme procedure.
```scheme
(define (all-but-first-n l n)
  (let iterate
    ((current l)
     (counter n))
    (if (or (= counter 0)
            (null? current))
      current
      (iterate (cdr current) (- counter 1)))))
```
Convert it to an equivalent procedure that does not use a named let.
```scheme
(define (all-but-first-n-no-let l n)
  (define (iterate current counter)
    (if (or (= counter 0)
            (null? current))
      current
      (iterate (cdr current) (- counter 1))))
  (iterate l n))
```

## 1.4.9
What is the worst-case performance characteristic of the following two-argument procedures?
A procedure to compute $n −m$:
```scheme
(define (subtract n m)
  (if (= m 0)
    n
    (subtract (- n 1) (- m 1))))
```
> b = O(1) rec = O(m) -> O(m)

A procedure that zips two lists in a pairwise fashion:
```scheme
(define (zip l1 l2)
  (if (or (null? l1) (null? l2))
    '()
    (cons (cons (car l1)
                (car l2))
          (zip (cdr l1) (cdr l2)))))
```
> b = O(1) r = O(min (l1, l2)) -> O(min(l1, l2))

## 1.4.10
What is the worst-case performance characteristic of the following procedure?
```scheme
(define (all-i-to-j n)
  (define (i-to-j i j)
    (if (= j 0)
      1
      (* i (i-to-j i (- j 1)))))
  (define (sum i)
    (if (= i 0)
      0
      (+ (sum (- i 1)) (i-to-j i i))))
  (sum n))
```
> i-to-j: b = O(1) r = O(j) -> O(j)
> sum: b = O(i) r = O(i) -> O(i²)
> all-i-to-j: O(n²)

# Hoofdstuk 2

## 2.7.1
Determine the range of ASCII-values that correspond to the characters `#\0` to `#\9`, `#\a` to `#\z` and `#\A` to `#\Z`. What is the Scheme procedure to use?
> 0 -> 48
> {...}
> 9 -> 57
> a -> 97
> {...}
> z -> 122
> A -> 65
> {...}
> Z -> 90
```scheme
>(char->integer #\A)
65
```

## 2.7.2
Write a procedure of type (string → number) that converts a string containing any combination of numeric characters (i.e., characters between `#\0` and `#\9`) to the corresponding number. Determine Ω(f(n)) for your algorithm:
- when n is the length of the string.
> Omega(n)
- when n is the value of the number.
> Omega(log(n))

```scheme
(define (convert str)
  (let conv
    (
     (v 0)
     (i 0))
    (if (= (string-length str) i) v
    (conv (+ (* v 10) (- (char->integer (string-ref str i)) 48)) (+ i 1)))))
```

## 2.7.3
Consider the text t="helterskelter" and the pattern p="elter". Consider the fragments v="helter" and w="ter". Fill in the blanks:
   - v is a _prefix_ of t.
   - w is a _suffix_ of t.     
   - Is v a proper prefix of t? Yes/No because _yes, not equal to the entire string or the empty string_

## 2.7.4
Consider the string `"Hello"`. Enumerate all prefixes, all suffixes, all proper prefixes and all proper suffixes.
> (proper) prefixes: 
> h, he, hel, hell (non proper: "" and hello)
> (proper) suffixes:
> o, lo, llo, ello (non proper: "" hello)

## 2.7.5
Write the procedure type for the `match` procedures discussed in this chapter.
```scheme
Match:
(string string -> number U {#f})
```

## 2.7.6
Adapt the original brute-force algorithm such that it can be used to find multiple occurrences of a pattern in the text. Instead of returning the shift of just one match, the modified procedure returns a list of shifts of all matches. Bear in mind however that patterns with repetitions can cause several matches to overlap. For example, the text `"bababxzy"` contains two occurrences of the pattern `"bab"`; one at shift 0 and another one at shift 2. Your algorithm should return `'(0 2)`.

```scheme
(define (multi-match t p)
  (define n-t (string-length t))
  (define n-p (string-length p))
  (let loop
    ((i-t 0)
     (i-p 0)
     (res '())) ; aangepast
    (cond
      ((> i-p (- n-p 1))
       (loop (+ i-t 1) 0 (cons i-t res))) ; aangepast
      ((> i-t (- n-t n-p))
       (reverse res)) ; aangepast
      ((eq? (string-ref t (+ i-t i-p)) (string-ref p i-p))
       (loop i-t (+ i-p 1) res))
      (else
       (loop (+ i-t 1) 0 res)))))
```

