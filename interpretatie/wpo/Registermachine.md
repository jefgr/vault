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
