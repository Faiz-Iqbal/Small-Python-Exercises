I deprecate code like this:
```
if <test>:
   return <val1>
return <val2>
```

This is better 
```
if <test>:
   return <val1>
else:
   return <Val2>
```
because it clearly signals the intended logical structure. 
