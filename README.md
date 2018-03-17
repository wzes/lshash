# lshash for python3.x


#### USE

- Enter the lshash folder

- Run
```
$ python setup.py install
```
- Congratulate! You can use it by python3!


## TEST

```
from lshash import LSHash

lsh = LSHash(6, 8)
lsh.index([1,0,1,0,0,0,0,0])
lsh.index([1,1,1,0,0,0,0,0])
lsh.index([1,0,0,1,1,1,1,1])
print(lsh.query([1,0,1,1,1,1,1,1], 3, "hamming"))
```

