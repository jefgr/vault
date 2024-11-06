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

