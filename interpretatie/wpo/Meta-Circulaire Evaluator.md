# Dodona

## Primaire functies toevoegen
lijnen toegevoegd hier
```scheme
(define primitive-procedures
  (list (list 'car car)
	(list 'cdr cdr)
	(list 'cons cons)
	(list 'null? null?)
	(list '+ +)
	(list '* *)
	(list '/ /)
	(list '= =)
	(list '- -)
	(list '< <)
	(list '> >)
	(list 'symbol? symbol?)
	(list 'pair? pair?)
	(list 'display display)
	(list 'newline newline)
	(list 'number->string number->string)
	;; more primitives
	))
```

# Logische And toevoegen aan de evaluator
## Stap 1
and to if veranderaar
```scheme
(define (and? exp)
  (tagged-list? exp 'and))

(define (and-args exp) (cdr exp))

(define (and->if exp)
  (define (and-args->if exps)
    (cond
      ((null? exps) 'true)
      ((null? (cdr exps)) (car exps))
      (else (make-if
             (car exps)
             (and-args->if (cdr exps))
             'false))))
  (and-args->if (and-args exp)))
```

## Stap 2
Toevoegen aan eval

```scheme
(define (eval exp env)
  (cond ((self-evaluating? exp) exp)
        ((variable? exp) (lookup-variable-value exp env))
        ((quoted? exp) (text-of-quotation exp))
        ((assignment? exp) (eval-assignment exp env))
        ((definition? exp) (eval-definition exp env))
        ((if? exp) (eval-if exp env))
        ((lambda? exp)
         (make-procedure (lambda-parameters exp)
                         (lambda-body exp)
                         env))
        ((begin? exp) 
         (eval-sequence (begin-actions exp) env))
        ((cond? exp) (eval (cond->if exp) env))
        ((and? exp) (eval (and->if exp) env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))
        (else
         (error "Unknown expression type -- EVAL" exp))))
```

## Stap 3
eval-and ipv rewrite as if
```scheme
(define (eval-and exp env)
  (define (eval-and-hulp exp)
  (cond ((null? exp) #t)
        ((null? (cdr exp)) (eval (car exp) env))
        ((false? (eval (car exp) env))
         'false)
        (else (eval-and-hulp (cdr exp)))))
  (eval-and-hulp (and-args exp)))
```

# Logische Or toevoegen aan de evaluator

## Stap 1
or->if

```scheme
(define (or? exp)
  (tagged-list? exp 'or))

(define (or-args exp) (cdr exp))

(define (or->if exp)
  (define (or-args->if exps)
    (cond
      ((null? exps) 'false)
      ((null? (cdr exps)) (car exps))
      (else (make-if
             (car exps)
             (car exps)
             (or-args->if (cdr exps))))))
  (or-args->if (or-args exp)))
```
and add to eval

```scheme
(define (eval exp env)
  (cond ((self-evaluating? exp) exp)
        ((variable? exp) (lookup-variable-value exp env))
        ((quoted? exp) (text-of-quotation exp))
        ((assignment? exp) (eval-assignment exp env))
        ((definition? exp) (eval-definition exp env))
        ((if? exp) (eval-if exp env))
        ((lambda? exp)
         (make-procedure (lambda-parameters exp)
                         (lambda-body exp)
                         env))
        ((begin? exp) 
         (eval-sequence (begin-actions exp) env))
        ((cond? exp) (eval (cond->if exp) env))
        ((and? exp) (eval-and exp env))
        ((or? exp) (eval (or->if exp) env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))
        (else
         (error "Unknown expression type -- EVAL" exp))))
```

## Deel 2
eval-or maken
```scheme
(define (eval-or exp env)
  (define (eval-or-hulp exps)
    (cond ((null? exps) #false)
          ((true? (eval (car exps) env))
           (eval (car exps) env))
          (else (eval-or-hulp (cdr exps)))))
  (eval-or-hulp (or-args exp)))
```

