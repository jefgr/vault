# 2 Prolog Syntax
1)  Empty body
2)  Predicate with a capital
3)  Ending a statement with a comma instead of full stop
4)  ' not allowed
5)  % not allowed
6)  starting with a number not allowed
7) missing full stop
8) space in head name

# 3 List Processing
## 3.1 Joining lists together
1)  False
2) X = [a, b] 
3) X = [a] 
4) X = [a|b] 
5) Y = [a|X]
6) X = [], Y = [b,c] ?
   X = [A], Y = [A, b, c] ?
   X = [A, B], Y = [A, B, b, c] ?
   .... infinite amounts of added variables
7) X = [], Y = [a, b, c] ?
   X = [a], Y = [b, c] ?
   X = [a, b], Y = [c] ?
   X = [a, b, c], Y = [] ?
   False
## 3.2 Unifying lists
