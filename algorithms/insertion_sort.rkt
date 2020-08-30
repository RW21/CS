#lang racket

(define test-list '(1 4 2 3 0))

(define (insertion-sort l)
  (define (insert x ls)
    (match ls
      [(list) (list x)]
      [(cons y rst) (cond
                      [(< x y) (cons x ls)]
                      [else (cons y (insert x rst))])]))
  (foldl insert '() l))

