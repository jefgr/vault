#lang r7rs
(import (scheme base)
        (scheme write)
        (prefix (a-d positional-list double-linked-positional-list) adlp:)
        (prefix (a-d pattern-matching quicksearch) quick:))

; 3.6.1
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

; 3.6.2
; part 1
(define (plist-display l)
  (adlp:for-each l (lambda (element)
                     (display element)
                     (display #\space)))
  (newline))


(define my-list (adlp:new string=?))

(adlp:add-before! my-list "and")
(adlp:add-after! my-list "me")
(adlp:add-after! my-list "to" (adlp:first my-list))
(adlp:add-after! my-list "goodday" (adlp:first my-list))
(adlp:add-before! my-list "hello")
(adlp:add-after! my-list "world" (adlp:first my-list))
; part 2
(define (find-e plist)
  (let ((count 0))
    (adlp:for-each plist (lambda (element)
                           (if (quick:match element (string #\e))
                               (set! count (+ count 1)))))
    count))

; 3.6.3
(define (pair-eq? x y)
  (equal? (cdr x) (cdr y)))

   
(define pair-list (adlp:map my-list
                            (lambda (x) (cons x (string-length x)))
                            pair-eq?))


