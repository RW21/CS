#lang racket

(define sample-graph
  '(a (b) (c))
  )

(define (dfs queue target-node)
  (if (not (empty? queue))
      (let ([node (first queue)])
        (if (eq? (first node) target-node)
            node
            (dfs (append (rest node) (rest queue)) target-node)))
      (list)))

