# Decompilatie a

```scheme
(define antwoord
(compile
  ; Door jou in te vullen
 '(begin (define oef-a 100) oef-a)
 'resultaat
 'next
  )
  )
```

# Decompilatie b

```scheme
(define antwoord
(compile
  ; Door jou in te vullen
 '(if (= 10 (+ 1 2)) 100 200)
 'een-getal
 'return
  )
  )

```

# Decompilatie c

```scheme
(define antwoord
(compile
  ; Door jou in te vullen
 '(begin (define x 20)(if (> x 10) 5 15))
 'z
 'label-10
  )
  )
```

# Decompilatie d

```scheme
(define antwoord
(compile
  ; Door jou in te vullen
 '(begin
    (define (f n)
      (if (< n 2)
          1
          (* n (f (- n 1)))))
    (f 11)
      )
 's
 'next
  )
  )
```