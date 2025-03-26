## Delen
> zie wpo/les5.2.rkt
```scheme
(define deel-machine
  (make-machine
    '(cont res v1 v2)
    ops
    '(start
       (assign cont (label stop))
       (assign res (const 0))
       (goto (label delen))
      delen
       ; Jouw code komt hier
       (test (op <) (reg v1) (reg v2))
       (branch (label stop))
       (assign res (op +) (reg res) (const 1))
       (assign v1 (op -) (reg v1) (reg v2))
       (goto (label delen))
      stop)))
```

## Machtsverheffing (iteratief)
> zie wpo/les5.2.rkt
```scheme
(define expt-machine
  (make-machine
    '(cont res v1 v2)
    ops
    '(start
       (assign cont (label stop))
       (assign res (const 1))
       (goto (label expt))
       expt
       ; Jouw code komt hier
       (test (op =) (reg v2) (const 0))
       (branch (label expt-exit))
       (assign v2 (op -) (reg v2) (const 1))
       (assign res (op *) (reg res) (reg v1))
       (goto (label expt))
      expt-exit
       (goto (reg cont))
      stop)))
```

## Machtsverheffing (recursief)
> zie wpo/les5.2.rkt
```scheme
(define expt-machine
  (make-machine
   '(cont res v1 v2)
   ops
   '(start
     (assign cont (label stop))
     (goto (label expt))

     expt
     ; Jouw code komt hier
     (assign res (const 1))
     (test (op =) (reg v2) (const 0))
     (branch (label expt-exit))
     (save cont)
     (assign cont (label expt-loop-up))
     (goto (label expt-loop-down))

     
     expt-loop-down
     (test (op =) (reg v2) (const 1))
     (branch (label expt-loop-up))
     (assign v2 (op -) (reg v2) (const 1))
     (save cont)
     (goto (label expt-loop-down))

     expt-loop-up
     (assign res (op *) (reg res) (reg v1))
     (restore cont)
     (goto (reg cont))

     expt-exit
     (goto (reg cont))

     stop)))
```

## Fibonacci
>zie wpo/les6.rkt
```scheme
(define fib-machine
  (make-machine
    '(cont res v1)
    ops
    '(start
       (assign cont (label stop))
       (goto (label fib-start))
       ; Jouw code komt hier
       fib-start
       (test (op <) (reg v1) (const 2))
       (branch (label fib-end))

       fib-min-1 ; label overbodig
       (save cont)
       (save v1)
       (assign v1 (op -) (reg v1) (const 1))
       (assign cont (label fib-min-2))
       (goto (label fib-start))

       fib-min-2
       (restore v1)
       (save res)
       (assign v1 (op -) (reg v1) (const 2))
       (assign cont (label fib-plus))
       (goto (label fib-start))

       fib-plus
       (restore v1)
       (assign res (op +) (reg v1) (reg res))
       (restore cont)
       (goto (reg cont))

       fib-end
       (assign res (reg v1))
       (goto (reg cont))
       
      stop)))
```

## Examenvraag: Gelukkige Getallen
> zie wpo/les6.2.rkt
```scheme
(define (laatste-cijfer x)
  (modulo x 10))
(define (verwijder-laatste-cijfer x)
  (floor (/ x 10)))
(define geluk-machine
  (make-machine
    '(cont res v1)
    `(,@ops
      (laatste-cijfer ,laatste-cijfer)
      (verwijder-laatste-cijfer ,verwijder-laatste-cijfer))
    '(start
       (assign cont (label stop))
       (goto (label geluk))

       geluk
       ; Jouw code komt hier
       (save cont)
       (assign res (reg v1))
       
       geluk-iter
       (assign v1 (reg res))
       (test (op =) (reg v1) (const 1))
       (branch (label lucky))
       (assign cont (label geluk-iter))
       (goto (label kwadraat))
       
       lucky
       (assign res (const #t))
       (restore cont)
       (goto (reg cont))

       kwadraat
       (assign res (const 0))
       
       kwadraat-iter
       (test (op <) (reg v1) (const 10))
       (branch (label kwadraat-end))
       (save v1)
       (assign v1 (op laatste-cijfer) (reg v1))
       (assign v1 (op *) (reg v1) (reg v1))
       (assign res (op +) (reg res) (reg v1))
       (restore v1)
       (assign v1 (op verwijder-laatste-cijfer) (reg v1))
       (goto (label kwadraat-iter))
       
       kwadraat-end
       (assign v1 (op *) (reg v1) (reg v1))
       (assign res (op +) (reg res) (reg v1))
       (goto (reg cont))
       
      stop)))
```

## Examenvraag: fietsvakantie
> zie wpo/les6.3.rkt

Eerste oplossing, maar som is iteratief en niet recursief zoals in de vraag
```scheme
(define helling-machine
       (make-machine
         '(cont v1 v2 res)
         `((null? ,null?) (car ,car) (cdr ,cdr) (+ ,+) (* ,*) (/ ,/))
         '(start
          (assign v1 (const ( 228   52   72   43   64   53   67   72  194))) ; hoogtes
          (assign v2 (const (3000 1000 3000 1000 1000 1000 1000 2000 2800))) ; lengtes
          (assign cont (label stop))
          (goto (label hellingsgraad))

          ;;; <jouw code hier>

          hellingsgraad
          (save cont)
          (assign cont (label after-hoogtes))
          (goto (label som))
          
          after-hoogtes
          (assign v1 (reg v2))
          (assign v2 (reg res))
          (assign cont (label after-lengtes))
          (goto (label som))
          
          after-lengtes
          (assign v1 (reg v2))
          (assign v2 (reg res))
          (restore cont)
                  
          (assign res (op /) (reg v1) (reg v2))
          (assign res (op *) (reg res) (const 100))
          (goto (reg cont))

          som
          (assign res (const 0))
          som-iter
          (test (op null?) (reg v1))
          (branch (label som-base))
          (save v1)
          (assign v1 (op car) (reg v1))
          (assign res (op +) (reg res) (reg v1))
          (restore v1)
          (assign v1 (op cdr) (reg v1))
          (goto (label som-iter))

          som-base
          (goto (reg cont))
          
          stop)))
```