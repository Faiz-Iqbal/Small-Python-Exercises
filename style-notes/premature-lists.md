If your code looks like this:
```
l = list(range(x))
for i in l:
   [stuff]
```
consider rewriting to
```
l = range(x)
for i in l:
   [stuff]
```
or to
```
for i in range(x):
   [stuff]
```

Only trigger evaluation with `list` if this is required. 

Bottom line: if you've written `list(range(x))` and didn't *intend* to force evaluation at that point, then something may be wrong.


If your code looks like this:
```
l = list(range(x))
for i in l:
   [stuff]  x[i]   [stuff]
```
then you may mean
```
for i in x:
   [stuff]  i  [stuff]
```

Bottom line: only iterate over a list by *numerical index* if you can't directly use the list as an *iterator object*. 
