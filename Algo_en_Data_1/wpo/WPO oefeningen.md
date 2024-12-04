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

## 2.7.7
Suppose that we allow patterns to contain “holes” indicated by `*`. E.g., the pattern `"hel*skel"` will match any text that contains the fragments `"hel"` and `"skel"` separated by zero or more irrelevant characters. In other words, every such hole (usually called a wildcard) is allowed to correspond to any number of characters. Implement a variant of the brute-force algorithm that enables matching patterns with holes. What is the performance characteristic of your algorithm?

```scheme
(define (wild-match t p)
  (define (count-non-* str)
    (let count
      ((c 0)
       (i 0))
      (cond ((= i (string-length str))
             c)
            ((char=? #\* (string-ref str i))
             (count c (+ i 1)))
            (else 
             (count (+ c 1) (+ i 1))))))
  (define n-t (string-length t))
  (define n-p (count-non-* p))
  (let loop
    ((i-t 0)
     (i-p 0))
    (cond
      ((> i-p (- n-p 1))
       i-t)
      ((> i-t (- n-t n-p))
       #f)
      ((eq? (string-ref p i-p) #\*)
       (if (wild-match (substring t i-t) (substring p (+ i-p 1)))
           i-t (loop (+ i-t 1) 0)))
      ((eq? (string-ref t (+ i-t i-p)) (string-ref p i-p))
       (loop i-t (+ i-p 1)))
      (else
       (loop (+ i-t 1) 0)))))
```

## 2.7.8
Find 2 common words in your mother tongue that contain repetitions of at least 2 characters. In some languages, entire words can occur several times as constituents of a composite word.
> Papa, mama, ...

## 2.7.9
Study the application of the KMP algorithm for the pattern `"ABCDABD"` and the text `"ABC ABCDAB ABCDABCDABDE"`. Extend the code of the algorithm with `display` instructions in order to display it and ip throughout the iterations. Use the generated trace to graphically show the consecutive alignments of the pattern against the text.

```scheme
; print function that must be added to the algorithm in match before the cond in the named let
(define (print-t-p t p i-t)
  (begin
    (display t)
    (newline)
    (display (make-string i-t #\space))
    (display p)
    (newline)
    (display "---")
    (newline)))
```

## 2.7.10
What is the procedure type of the `compute-failure-function` procedure?

```scheme
(string -> (number -> number))
```

## 2.7.11
Manually work out the `sigma-table` used in σ for the pattern `"abracadabra"`. Verify your answer using the procedure `compute-failure-function`.

> sigma-table

| a   | b   | r   | a   | c   | a   | d   | a   | b   | r   | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -1  | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 2   | 3   |
## 2.7.12
Manually work out the `sigma-table` used in σ for the pattern `"haahiihaahaahii"`. Verify your answer using the procedure `compute-failure-function`.

> sigma-table

| h   | a   | a   | h   | i   | i   | h   | a   | a   | h   | a   | a   | h   | i   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -1  | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 2   | 3   | 4   | 2   | 3   | 4   | 5   |

## 2.7.13
Find an example which illustrates that the worst-case performance characteristic of the QuickSearch algorithm is in O(nt.np).
> in de tekst "aaaaaaaaaaaaaaa{...}a" en met het patroon "aaa{...}aza" zal alle posities in de tekst moeten checken dus nt keer en zal altijd tot aan bijna het einde van het patroon moeten doorlopen dus np keer, dit geeft tijdcomplexiteit O(nt.np)
## 2.7.14
The QuickSearch algorithm works better for some kinds of inputs than others. Modify the QuickSearch algorithm and explore for _which kinds of inputs_ this is the case.
    1. Extend the QuickSearch algorithm so that it logs the positions to which the algorithm shifts after a mismatch (i.e. the new value of `i-t`) in a list. The modified algorithm returns a vector of 2 values: (1) the original result of the algorithm, and (2) the accumulated list of positions.
    2. Run your modified algorithm with the following two inputs of similar length.
        - Input 1   
            - Text: `"GGCAGCACGATCGCATGTCCCACGTGAACCATTGGTAAACCCTGTGGCCTGTGAGCGACAAAAGCTTTAATGGGAAATTCGCGCCCATAACTTGGTCCGAATACGGGTCCTAGCAACGTTCGTCTGAGTTTGATCTATATAATACGGGCGGTATGTCTGCTTTGATCAACCTCCAATAGCTCGTATGATAGTGCACCCGCTGGTGATCACTCAATGATCTGGGCTCCCCGTTGCAACTACGGGGATTTTTCGAGACCGACCTGCGTTCGGCATTGTGGGCACAGTGAAGTATTAGCAAACGTTAAGTCCCGAACTAGATGTGACCTAACGGTAAGAGAATTTCATAATACGTCCTGCCGCACGCGCAAGGTACATTTGGAAGTATTGAATGGACTCTGATCAACCTTCACACCGATCTAGAATCGAATGCGTAGATCAGCCAGGTGCAAACCAAAAATTCTAGGTTACTAGAAGTTTTGCGACGTTCTAAGTGTTGGACGAAATGATTCGCGACCCAGGATGAGGTCGCCCTAAAAAATAGATTTCTGCAACTCTCCTCGTGAGCAGTCTGGTGTATCGAAAGTACAGGACTAGCCTTCCTAGCAACCGCGGGCTGGGAGTCTGAGACATCACTCAAGATATATGCTCGGTAACGTATGCTCTAGCCATCTAACTATTCCCTATGTCTTATAGGGGCCTACGTTATCTGCCTGTCGAACCATAGGATTCGCGTCAGCGCGCAGGCTTGGATCGAGATGAAATCTCCGGAGCCTAAGACCACGAGCGTCTGGCGTCTTGGCTAATCCCCCTACATGTTGTTATAAACAATCAGTGGAAACTCAGTGCTAGAGGGTGGAGTGACCTTAAATCAAGGACGATATTAATCGGAAGGAGTATTCAACGCAATGAAGTCGCAGGGTTGACGTGGGAATGGTGCTTCTGTCCAAACAGGTAAGGGTATGAGGCCGCAACCGTCCCCCAAGCGTACAGGGTGCACTT"`  
            - Pattern: `"GCAACCGTCCCCCAAGCGTACA"`
        - Input 2
            - Text: `"Once upon a time, in a quaint village nestled between rolling hills and lush forests, there was a small community of artisans and farmers. The villagers were known for their craft and the quality of their produce. Every morning, the marketplace bustled with activity as people exchanged goods, shared stories, and formed bonds over the freshest bread, the ripest fruits, and the most intricate handcrafted items. Among them was a young blacksmith named Eric, whose reputation for creating the finest tools had spread far and wide. Eric was not only skilled in his craft but also known for his kindness and willingness to help anyone in need. One summer, as the village prepared for the annual harvest festival, Eric found himself particularly busy, fulfilling orders and repairing tools to ensure everything was ready for the celebrations. The festival was a time for joy, gratitude, and a showcase of the village's talents, drawing visitors from neighboring towns and far-off places."`      
            - Pattern: `"drawing visitors"`
    3. Based on your findings, can you determine for which kind of input QuickSearch works better, and why?

> 1.
> See also a-d/patternmatching/quicksearch.rkt
```scheme
(define (quickmatch t p) ;quicksearch with shift position output
  (define n-t (string-length t))
  (define n-p (string-length p))
  (define shift (compute-shift-function p))
  (define pos-list '()) ; empty list define
  (let loop
    ((i-t 0)
     (i-p 0))
    (cond 
      ((> i-p (- n-p 1))
       (vector i-t (reverse pos-list))) ; return with the reversed list
      ((> i-t (- n-t n-p))
       (vector #f (reverse pos-list))) ; return with the reversed list
      ((eq? (string-ref t (+ i-t i-p)) (string-ref p i-p))
       (loop i-t (+ i-p 1)))
      (else
       (let ((c-t (string-ref t (modulo (+ i-t n-p) n-t))))
         (set! pos-list (cons (+ i-t (shift c-t)) pos-list)) ; fill the list 
         (loop (+ i-t (shift c-t)) 0))))))))
```
> 2.
> Output 1:
> _(967 (2 6 8 9 13 17 19 21 26 28 33 35 36 38 39 40 41 46 47 48 52 53 54 55 59 61 63 65 69 73 77 78 79 83 88 92 93 94 96 100 104 105 110 111 115 119 120 124 129 133 137 139 143 147 149 153 154 158 162 163 167 168 173 175 177 179 184 188 192 196 198 203 205 207 212 213 214 216 217 219 224 228 230 231 236 237 239 243 247 252 257 259 261 266 271 272 277 279 283 288 293 294 299 304 305 306 308 313 314 319 323 324 325 329 333 338 339 341 343 345 346 351 352 356 361 362 366 367 371 373 375 380 381 383 387 389 391 396 397 402 407 409 413 417 419 420 425 426 427 428 430 431 432 433 434 435 439 440 445 447 448 453 457 459 460 462 466 467 468 473 478 479 480 481 485 489 494 495 500 501 506 508 510 511 512 513 514 515 516 520 524 528 529 531 533 535 539 544 549 554 558 559 560 565 570 571 576 578 582 583 584 586 591 593 598 602 603 608 610 612 614 615 620 621 625 627 632 637 639 641 642 647 649 650 651 653 654 658 660 661 665 669 670 675 677 678 680 684 686 691 695 696 698 699 703 704 708 710 714 716 718 720 725 730 735 740 742 744 749 751 752 753 758 760 761 766 770 775 780 781 785 787 791 795 800 801 802 803 805 806 810 814 815 816 818 820 825 826 831 835 840 842 846 850 855 856 860 861 862 866 867 868 873 874 878 879 881 883 884 888 893 894 899 904 909 913 918 922 924 925 926 928 933 938 942 947 948 949 951 956 958 959 960 965 967))_
> Output 2:
>_(925 (17 34 51 60 69 78 79 88 105 106 120 121 138 155 160 174 188 197 206 208 213 217 234 251 265 279 296 312 320 337 354 363 380 391 395 412 426 443 456 461 464 481 482 486 489 498 512 529 540 549 551 568 577 594 599 600 601 610 624 641 645 653 670 684 693 710 727 744 747 764 773 782 790 800 817 821 822 839 840 849 852 869 880 881 898 899 908 917 925))_
>3.
>Quicksearch works best for texts and patterns without a lot of repeated characters. This is the case in written english but is not the case when analysing DNA-sequences (a lot of repeating characters in both pattern and text)


# Hoofdstuk 3

**See also wpo/libraries/wpo_h3.rkt**
## 3.6.1
Write Scheme expressions for the headed lists and headed vectors shown in Figure 3.5. Based on the drawings, try to distill a meaningful semantics for the extra information stored.
Figure 3.5:
![[figure3_5AD1.png|400]]
```scheme
(define-record-type exercise-c
  (new a b c)
  exercise-c?
  (a get-a set-a!)
  (b get-b set-b!)
  (c get-c set-c!))


(define ex-c (let ((the-last-cell (list 7))
                   (the-list (list -5 -8 -1 6 2 0)))
               (new the-last-cell
                    3
                    (append the-list the-last-cell))))
```

## 3.6.2
- Pick any implementation of the positional-list ADT (i.e. deciding on P is up to you) and use the operations of the ADT to construct the list `'("hello" "world" "and" "goodday" "to" "me")` by adding the words in the following order: `"and"`, `"me"`, `"to"`, `"goodday"`, `"hello"`, `"world"`.
- Write a procedure which runs over the elements of the list and which counts the number of words that contain an `#\e`. Use a pattern matching algorithm of [Chapter 2](https://soft.vub.ac.be/~jnicolay/courses/ad1/html-dynamic/index.html#stringprocessing).

```scheme
#lang r7rs
(import (scheme base)
        (scheme write)
        (prefix (a-d positional-list augmented-double-linked-positional-list) adlp:)
        (prefix (a-d pattern-matching quicksearch) quick:)) ; part 2

(define (plist-display l)
  (adlp:for-each l (lambda (element)
                     (display element)
                     (display #\space)))
  (newline))


(define list (adlp:new string=?))

(adlp:add-before! list "and")
(adlp:add-after! list "me")
(adlp:add-after! list "to" (adlp:first list))
(adlp:add-after! list "goodday" (adlp:first list))
(adlp:add-before! list "hello")
(adlp:add-after! list "world" (adlp:first list))

(define (find-e plist) ; part 2
  (let ((count 0))
    (adlp:for-each plist (lambda (element)
                           (if (quick:match element (string #\e))
                               (set! count (+ count 1)))))
    count))
```

## 3.6.3
Use your positional list of the previous exercise. Use `map` to generate a positional list of pairs (i.e. V=pair) that consists of a string and its length. In order to do so, define your own procedure `pair-eq?` that declares two pairs equal whenever they store the same number in their cdr. Subsequently , apply `find` in order to locate the word whose length is 7.

```scheme
(define (pair-eq? x y)
  (equal? (cdr x) (cdr y)))

   
(define pair-list (adlp:map my-list
                            (lambda (x) (cons x (string-length x)))
                            pair-eq?))
; REPL
> (adlp:find pair-list (cons " " 7))
```

## 3.6.4
The implementation of the positional-list ADT as a double-linked list defines a list-node record. Replace this record with ordinary Scheme functions that have the same functionality as the original list-node record. In other words, after removing the list-node record, all other code works the same as before.
> **See also a-d/positional-list/double-linked-list.rkt**
```scheme
; alternative with vectors instead of records
(define (make-list-node v p n) (vector 'node v p n))
(define (list-node? node) (eq? (vector-ref node 0) 'node))
(define (list-node-val node) (vector-ref node 1))
(define (list-node-val! node v) (vector-set! node 1 v))
(define (list-node-prev node) (vector-ref node 2))
(define (list-node-prev! node v) (vector-set! node 2 v))
(define (list-node-next node) (vector-ref node 3))
(define (list-node-next! node v) (vector-set! node 3 v))

; original:
(define-record-type list-node
  (make-list-node v p n)
  list-node?
  (v list-node-val list-node-val!)
  (p list-node-prev list-node-prev!)
  (n list-node-next list-node-next!))
```

## 3.6.5
Write a procedure which takes two positional-list arguments and which returns a positional-list that only contains the data elements contained by both argument lists (i.e. the intersection of both input lists).
> **See also libraries/wpo_h3.rkt**
```scheme
(define (intersect plist1 plist2)
  (define pout (dlp:new =))
  (dlp:for-each plist1 (lambda (el) (if (dlp:find plist2 el) (dlp:add-after! pout el))))
  pout)
```

## 3.6.7
Implement a procedure `ternary-search` that resembles binary search except that it divides a sorted list in three instead of two parts in every phase of the iteration. What is the worst-case performance characteristic of your procedure? Can you identify the price to pay for the improvement? (_hint:_ what does the implementation look like for 4-ary, 5-ary, 6-ary, ... searching?)
> **See also libraries/wpo_h3.rkt
> 		a-d/sorted-list/vectorial.rkt**

```scheme
; binary
(define (find! slst key)
      (define ==? (equality slst))
      (define <<? (lesser slst))
      (define vect (storage slst))
      (define leng (size slst))
      (let binary-search
        ((left 0)
         (right (- leng 1)))
        (if (<= left right)
            (let ((mid (quotient (+ left right 1) 2)))
              (cond
                ((==? (vector-ref vect mid) key)
                 (current! slst mid))
                ((<<? (vector-ref vect mid) key)
                 (binary-search (+ mid 1) right))
                (else
                 (binary-search left (- mid 1)))))
            (current! slst -1)))
      slst)

; ex 3.6.7
(define (find-ternary! slst key)
	(define ==? (equality slst))
	(define <<? (lesser slst))
	(define vect (storage slst))
	(define leng (size slst))
	(let ternary-search
		((left 0)
		 (right (- leng 1)))
		(if (<= left right)
			(let ((fmid (+ left (quotient (- right left) 3)))
				  (smid (+ left (* (quotient (- right left) 3) 2))))
			  (cond
				((==? (vector-ref vect fmid) key)
				 (current! slst fmid))
				((==? (vector-ref vect smid) key)
				 (current! slst smid))
				((<<? (vector-ref vect smid) key)
				 (ternary-search (+ smid 1) right))
				((<<? key (vector-ref vect fmid))
				 (ternary-search left (- fmid 1)))
				(else
				 (ternary-search (+ fmid 1) (- smid 1)))))
			(current! slst -1)))
	  slst)
```

> [geeksforgeeks explaination](https://www.geeksforgeeks.org/binary-search-preferred-ternary-search/)
>  It looks like the performance will improve, but the amount of comparisons will increase faster than that the recursion reduces.
>  In AD3 we will see an exception where there will be improvements.

## 3.6.8
Write a procedure `sort` which takes a plain Scheme list and which returns a new list that consists of the same elements but in sorted order. Use the sorted-list ADT to implement your procedure. What is the worst-case performance characteristic of your implementation?
> **See also wpo/libraries/wpo_h3.rkt**
```scheme
(define (sort list <<? ==?)
  (let* ((>>? (lambda (x y) (not (<<? x y))))
         (slist (sorted:from-scheme-list list >>? ==?)))
    (sorted:set-current-to-first! slist)
    (let loop
      ((element (sorted:peek slist))
       (current-result '()))
      (let ((new-result (cons element current-result)))
        (cond ((sorted:current-has-next? slist)
               (sorted:set-current-to-next! slist)
               (loop (sorted:peek slist) new-result))
              (else new-result))))))
```

# Hoofdstuk 4

## 4.5.1
Implement a procedure `postfix-eval` that evaluates a Scheme list representing expressions in postfix notation. For example, `(postfix-eval '(5 6 +))` should return 11 and `(postfix-eval '(5 6 + 7 -))` should return 4. You can use the predicate `number?` to test whether or not a Scheme value is a number.
> **See also wpo/libraries/wpo_h4.rkt**
```scheme
(define (postfix-eval args)
  (define stk (stack:new))
  (let loop
    ((arg args))
    (cond ((number? (car arg))
           (stack:push! stk (car arg)))
          (else
           (let empty-stack ((lst '()))
             (cond ((stack:empty? stk)
                    (stack:push! stk (apply (car arg) lst)))
                   (else
                    (empty-stack (cons (stack:pop! stk) lst)))))))
    (if (null? (cdr arg))
        (stack:pop! stk)
        (loop (cdr arg)))))
```

## 4.5.2
XML is a language that allows one to represent documents by including data it in arbitrarily deep nestings of “parentheses”. Instead of using real parentheses like `(` and `)` or `[` and `]`, XML allows us to define our own parentheses. Every string that is included in angular brackets `<` and `>` is considered to be an “opening” parenthesis. The corresponding closing parenthesis uses an additional slash in front of the string. For example, `<open>` is an opening parenthesis. Its corresponding closing parenthesis is `</open>`. For example, the list `'(<html> <head> This is the head </head> <body> And this is the body </body> </html>)` could be a valid XML document. Notice that we can nest these “parentheses” in an arbitrarily deep way. Write a procedure `(valid? lst)` that takes a list of Scheme symbols and that checks whether or not the list constitutes a valid XML document. You will need `symbol->string` to convert the symbols to strings which you can further investigate using `string-length` and `string-ref`. Write auxiliary procedures `opening-parenthesis?` and `closing-parenthesis?` that check whether or not a given symbol is an opening or closing parenthesis. Also write a procedure `matches?` that takes two symbols and that checks whether they both represent an opening parenthesis and its matching closing parenthesis. The `substring` procedure, explained in [Chapter 2](https://soft.vub.ac.be/~jnicolay/courses/ad1/html-dynamic/index.html#stringprocessing), may simplify your procedures.
> **See also wpo/libraries/wpo_h4.rkt**
```scheme
(define (opening-parenthesis? symbol)
  (let ((str (symbol->string symbol)))
    (if (and (eq? #\< (string-ref str 0))
             (not (eq? #\/ (string-ref str 1)))
             (eq? #\> (string-ref str (- (string-length str) 1))))
        #t
        #f)))

(define (closing-parenthesis? symbol)
  (let ((str (symbol->string symbol)))
    (if (and (eq? #\< (string-ref str 0))
             (eq? #\/ (string-ref str 1))
             (eq? #\> (string-ref str (- (string-length str) 1))))
        #t
        #f)))

(define (matches? sopen sclose)
  (let ((strO (symbol->string sopen))
        (strC (symbol->string sclose)))
    (if (equal? (substring strO 1)
             (substring strC 2))
        #t
        #f)))

(define (valid? lst)
  (define stk (stack:new))
  (let loop
    ((current-lst lst))
    (if (null? current-lst)
        (stack:empty? stk)
        (let ((tag (car current-lst)))
          (cond ((opening-parenthesis? tag)
                 (stack:push! stk tag)
                 (loop (cdr current-lst)))
                ((closing-parenthesis? tag)
                 (if (matches? (stack:pop! stk) tag)
                     (loop (cdr current-lst))
                     #f))
                 (else
                  (loop (cdr current-lst))))))))
```

## 4.5.3
The Josephus Problem for a given number m is a mathematical problem where n people, numbered 1 to n sit in a circle. Starting at person 1, we count m people in a circular way. The last person in the count is removed from the circle[2](https://soft.vub.ac.be/~jnicolay/courses/ad1/html-dynamic/index.html#auto:69) after which we start counting m people again starting at the person sitting next to the person that was removed. And so on. The circle is getting smaller and smaller and the person that remains wins[3](https://soft.vub.ac.be/~jnicolay/courses/ad1/html-dynamic/index.html#auto:71). It is possible to solve the Josephus problem in a mathematical way. However, in this exercise we will write a simulation procedure `josephus` that takes n and m and which sets up an iterative process to simulate the flow of events and which returns the number of the winning person. Use the queue ADT to formulate the procedure.
> **See also wpo/libraries/wpo_h4.rkt**
```scheme
(define (josephus n m)
  (define q (queue:new))
  (let loop
    ((current 1))
    (queue:enqueue! q current)
    (if (< current n)
        (loop (+ current 1))))
  (let loopm
    ((currentm 1))
    (cond ((= currentm m)
           (let ((maybelast (queue:serve! q)))
             (display maybelast) (newline)
             (if (queue:empty? q)
                 maybelast
                 (loopm 1))))
          (else
           (queue:enqueue! q (queue:serve! q))
           (loopm (+ currentm 1))))))
```

## 4.5.8
Manually perform the steps executed by the following algorithm to transform an arbitrary vector into a valid heap (in other words, do it on paper): `(from-scheme-vector (vector 25 2 17 20 84 5 7 12) <)`.
    - What is the parent of the element sitting at index 3?
    - Which element in the heap does not have a parent?
    - Which element in the heap does not have a left child? Which element only has a left child?
    - What is the formula to calculate the height of the heap?
    - Is the following statement true or false? ``The value sitting at the root of a subheap of a heap is always the smallest element of all values contained by that subheap.''
> - Element at index 3 = 20 with parent at index 1 = 12
> - Element at index 0 = 2 has no parent
> - Only leaves have no left child so, from index 4-7 (second half of the vector) (84 17 7 25), Element at index 3 = 20 has only a left child, because 4x2 = 8 (length of heap) but 4x2 + 1 = 9 (out of bounds)
> - h = log(n) => h = int(log(8)) + 1 = 4
> - True
  ![[ad1-exercise-4-5-8.png|500]]
## 4.5.9
What can you say about the location of the greatest element of a heap?
> It is located in a leaf, so in a vectorial representation in the last half of the vector.

## 4.5.10
Assume you have an empty heap with comparator `<`. Using `insert!`, we add the elements 5,2,3,1,2,1 in that order. Draw every phase of the heap during the construction. Now remove two elements from the heap and redraw the result. In all phases of the exercise, draw the heap as a complete binary tree and draw the underlying vector as well.
> ![[ad1-exercise-4-5-10.png|500]]