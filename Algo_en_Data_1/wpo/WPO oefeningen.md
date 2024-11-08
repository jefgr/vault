# 1.4.3
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

# 1.4.1
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

# 1.4.5
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

# 1.4.6
Consider two procedures to retrieve the last element from a data structure. Their procedural type looks as follows:
- `last-of-list`  
	(pair → number)
- `last-of-vector`  
	(vector → number)
Given these types,
- Implement both procedures.
- What is the wort-case performance characteristic of these procedures?
- What is the best-case performance characteristic of the procedures?