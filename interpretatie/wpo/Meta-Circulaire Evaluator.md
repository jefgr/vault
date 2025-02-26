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
          ((true? (eval (car exps) env)) ; fout moet in een let, anders words expressie 2 keer geevalueerd (side effects)
           (eval (car exps) env))
          (else (eval-or-hulp (cdr exps)))))
  (eval-or-hulp (or-args exp)))
```
Oplossing uit de les:
```scheme
(define (eval-or exp env)
  (define (evaluate-arguments args)
	(if (null? args)
      false
      (let ((res (eval (car args) env)))
        (if (true? res)
          res
          (evaluate-arguments (cdr args))))))
  (evaluate-arguments (car exp)))
```
# Let Toevoegen aan de evaluator
Niet vergeten values ook te evalueren voor ze in de nieuwe environment te steken
```scheme
;; Oefening Let
(define (let? exp) (tagged-list? exp 'let))

(define (let-var-val-list exp) (cadr exp))
(define (let-body exp) (cddr exp))
(define (let-vars exp) (map car (let-var-val-list exp) ))
(define (let-vals exp) (map cadr (let-var-val-list exp) ))

(define (eval-let exp env)
  (define new-env (extend-environment (let-vars exp) (list-of-values (let-vals exp) env) env))
  (eval-sequence (let-body exp) new-env))

; Also:
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
>       ((let? exp)
>        (eval-let exp env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))
        (else
         (error "Unknown expression type -- EVAL" exp))))
```

gebruik maken van lambda
```scheme
(define (make-application procedure arguments)
  (cons procedure arguments))

(define (let->applied-lambda exp)
  (make-application (make-lambda (let-vars exp) (let-body exp))
                    (let-vals exp)))

(define (eval-let exp env)
  (eval (let->applied-lambda exp) env))
```

# Toevoegen let*
Gebruik maken van let
```scheme
(define (let*? exp) (tagged-list? exp 'let*))

(define (make-let var-val-list body)
  (cons 'let (cons var-val-list body)))

(define (let*->lets exp)
  (let loop ((var-val-list (let-var-val-list exp)))
    (if (or (null? var-val-list) (null? (cdr var-val-list)))
        (make-let var-val-list (let-body exp))
        (make-let (list (car var-val-list)) (list (loop (cdr var-val-list)))))))

; also
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
        ((let? exp)
         (eval-let exp env))
>       ((let*? exp)
>        (eval (let*->lets exp) env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))
        (else
         (error "Unknown expression type -- EVAL" exp))))
```

Eigen eval-let*
```scheme
(define (extend-environment* env var-val-list)
  (if (null? var-val-list)
      env
      (let ((var (caar var-val-list))
            (val (cadar var-val-list)))
        (extend-environment* (extend-environment (list var) (list (eval val env)) env)
                             (cdr var-val-list)))))
(define (eval-let* exp env)
  (eval-sequence (let-body exp)
                 (extend-environment* env
                                      (let-var-val-list exp))))

; Also
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
        ((let? exp)
         (eval-let exp env))
>       ((let*? exp)
>        (eval-let* exp env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))
        (else
         (error "Unknown expression type -- EVAL" exp))))

```