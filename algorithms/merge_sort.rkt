#lang racket

(define (merge-sort l)
  (define (merge as bs)
    (match* (as bs)
      [((list) bs) bs]
      [(as (list)) as]
      [((list a as ...) (list b bs ...))
       (if (< a b)
           (cons a (merge as (cons b bs)))
           (cons b (merge (cons a as) bs)))]))

        
  (match l
    ;empty list
    [(list) l]
    ;list with single element
    [(list a) l]
    ;else
    [_ (define-values (ll rl)
         (split-at l (quotient (length l) 2)))
         (merge (merge-sort ll) (merge-sort rl))]))

