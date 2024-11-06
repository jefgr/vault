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
    
- Second, implement the ADT in the procedural style as a Scheme library.
    
- Third, write a procedure `=` that uses the ADT in order to verify whether or not two fractions are equal. You are not allowed to add `=` to your library.
    
- Fourth, reimplement the constructor such that rationals are always represented in reduced form. Does this reimplementation affect your code for `=`?
