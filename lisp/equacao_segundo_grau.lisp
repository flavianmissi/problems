(defun delta(a b c)
    (- (expt b 2) (* 4 a c))
)

(defun square_roots(a b c factor)
    (- b (+ (* (sqrt (delta a b c)) factor) ))
)

(defun quadratic_equation(a b c)
    (princ (square_roots a b c (- 1)))
    (princ (square_roots a b c 1))
)
