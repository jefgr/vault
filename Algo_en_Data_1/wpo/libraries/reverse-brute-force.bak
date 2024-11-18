#lang r7rs
(define-library (reverse-brute-force)
  (export match)
  (import (scheme base))
  (begin
    (define (match t p)
      (define n-t (string-length t))
      (define n-p (string-length p))
      (let loop
        ((i-t n-t)
         (i-p n-p))
        (cond
          ((= i-p 0)
           (- i-t n-p))
          ((< i-t n-p)
           #f)
          ((eq? (string-ref t (- i-t i-p)) (string-ref p (- n-p i-p)))
           (loop i-t (- i-p 1)))
          (else
           (loop (- i-t 1) n-p))))
      )

    )
  )

(import (scheme base)
        (scheme write))

;; Test helper function to run and display test results
(define (run-test text pattern expected-result test-name)
  (let ((result (match text pattern)))
    (display test-name)
    (display ": ")
    (if (equal? result expected-result)
        (display "PASS")
        (begin
          (display "FAIL - Expected: ")
          (display expected-result)
          (display ", Got: ")
          (display result)))
    (newline)))

;; Basic matching tests
(run-test "hello world" "world" 6 "Basic match at end")        ; h=0,e=1,l=2,l=3,o=4,space=5,w=6
(run-test "world hello" "world" 0 "Basic match at start")      ; w=0
(run-test "hello world hello" "world" 6 "Basic match in middle")

;; Multiple occurrence tests
(run-test "worldworld" "world" 5 "Adjacent matches")           ; first w=0, second w=5
(run-test "world world" "world" 6 "Spaced matches")           ; first w=0, second w=6
(run-test "worldworldworld" "world" 10 "Multiple matches")    ; w=0,w=5,w=10

;; Edge cases
(run-test "" "" 0 "Empty text and pattern")
(run-test "hello" "" 5 "Empty pattern")                       ; Points to end of string
(run-test "" "world" #f "Empty text with pattern")
(run-test "hello" "hello world" #f "Pattern longer than text")

;; Partial matches and overlaps
(run-test "worlworld" "world" 4 "Partial match then full match")  ; w=0,w=4
(run-test "worworworld" "world" 6 "Multiple partial matches")     ; w=0,w=3,w=5
(run-test "wworldd" "world" 1 "Match with surrounding chars")     ; w=1

;; Case sensitivity tests
(run-test "Hello World" "world" #f "Case sensitivity - lowercase pattern")
(run-test "hello world" "World" #f "Case sensitivity - uppercase pattern")

;; Special character tests
(run-test "hello\nworld" "world" 6 "Newline in text")
(run-test "hello world!" "world" 6 "Punctuation after match")
(run-test "hello, world" "world" 7 "Punctuation before match")
(run-test "world." "world" 0 "Match with trailing punctuation")

;; Pattern length tests
(run-test "x" "x" 0 "Single character match")
(run-test "xy" "x" 0 "Single character at start")
(run-test "yx" "x" 1 "Single character at end")

;; Repeated character tests
(run-test "aaaaa" "aa" 3 "Repeated characters")               ; Last match starts at index 3
(run-test "aaaaaa" "aaa" 3 "Longer repeated characters")      ; Last match starts at index 3
(run-test "abababab" "abab" 4 "Repeated pattern")            ; Last match starts at index 4

;; Substring tests
(run-test "worldwide" "world" 0 "Pattern at start with suffix")
(run-test "helloworld" "world" 5 "Pattern at end with prefix")    ; h=0,e=1,l=2,l=3,o=4,w=5
(run-test "helloworldhello" "world" 5 "Pattern in middle with both")

;; Boundary tests
(run-test "worldx" "world" 0 "Match at start boundary")
(run-test "xworld" "world" 1 "Match at end boundary")
(run-test "world" "world" 0 "Exact match boundaries")

;; Complex pattern tests
(run-test "hello wonderful world" "wo" 16 "Multiple possible matches") ; Last 'wo' starts at 14
(run-test "mississippi" "issi" 4 "Overlapping possibilities")         ; Last 'issi' starts at 4
(run-test "testing 123 testing" "test" 12 "Numbers in text")         ; Last 'test' starts at 11

;; Expected failure cases
(run-test "hello" "world" #f "No match exists")
(run-test "wor" "world" #f "Partial pattern only")
(run-test "w o r l d" "world" #f "Spaced characters")

;; Additional edge cases
(run-test "worldworldworld" "worldx" #f "Almost matches")
(run-test "worldworldworld" "worldworld" 5 "Multi-character overlapping")  ; Last match starts at 5
(run-test "helloworld" "hello world" #f "Space in pattern")