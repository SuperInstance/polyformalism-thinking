;;; LISP: What homoiconicity reveals about conservation
;;; Forces you to think about: Code IS data. The formula is a tree you can transform.
;;; Broken assumption: That operators are primitive — (/ 1 (sqrt n)) is a first-class node.
;;; Novel insight: S-expressions ARE ASTs. δ(n) written as an S-expression is the parse
;;;   tree of the formula — language and math share the same representation.

(defun delta (n)
  "Compute the CLT correction δ(n) = (1/√n)(1 − 3/(2n))"
  (* (/ 1 (sqrt n))
     (- 1 (/ 3 (* 2 n)))))

(defun ccr (n)
  "Conservation cancellation ratio as percentage"
  (* (delta n) 100))

(defun conservation-table (&optional (max 100))
  "Print conservation table from n=1 to MAX"
  (format t "~5T~10T~8T~%" "n" "δ(n)" "CCR%")
  (format t "~A~%" (make-string 28 :initial-element #\-))
  (loop for n from 1 to max
        do (format t "~5D  ~10,6F  ~7,2F%~%" n (delta n) (ccr n))))

;; Run it
(conservation-table)
