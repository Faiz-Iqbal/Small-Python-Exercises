Suppose you've written code like this:
```
def sumsquare_less_nice(n):
   counter = 0
   l = range(1,n)
   for i in l:
      counter += i*i
   return counter
```
In this example, it's to calculate a sum of the squares, but clearly it generalises to many lists.
 
It might be better to write something like this:
```
def sumsquare_nice(n):
   return sum(map(lambda x : x * x, range(1,n)))
```

(Don't use this in Q2 of the coursework!  The `sum` precisely contains the iterative loop which that simple question wants you to make explicit.  Thanks to a very sharp student for pointing this out.)

What's going on here?

* `sum` sums a list: this saves you that for loop.
* `map` and `lambda x : x * x` are a succinct way to say "square the elements in the list"

Pro tip: you can use `zip` to zip two lists together, as in:
```
zip([1,2],["one","two"])
```
this calculates (lazily)
```
[(1, "one"), (2, "two")]
```
