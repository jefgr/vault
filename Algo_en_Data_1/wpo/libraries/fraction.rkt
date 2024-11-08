#lang r7rs
(define-library (fraction)
  (export new numer denom fraction? + - * /)
  (import (rename (scheme base) (* base:*) (+ base:+) (- base:-) (/ base:/))
          (scheme write))
  (begin

    (define-record-type fraction
      (make-frac n d)
      fraction?
      (n numer)
      (d denom))

    (define (new n d)
      (make-frac (base:/ n (gcd n d))
                 (base:/ d (gcd n d))))

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
