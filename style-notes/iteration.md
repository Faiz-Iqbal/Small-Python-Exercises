If you write code that looks like this:
```
l = 0
while (l < 10):
   [some action]
   l = l + 1
```
then correct it to this:
```
for i in range(10):
   [some action]
```
Similarly for e.g.
```
l = 10
while (l > 10):
   [some action]
   l = l - 1
```
which would use
```
for i in range(10,0,-1):
```
and so forth.

Using an explicit counter in the idiom of C, is unidiomatic in Python (and also ugly in absolute terms).  You might lose marks for this, even if your program passes some tests.  

You should use a range, an iterator, or some other similar object, as appropriate.
