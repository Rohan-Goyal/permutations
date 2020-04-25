# Permutations
For Bobble.ai Internship Challenge. 
Given an array of arrays, it returns a list of strings, each representing a way to choose one element from each row. In my implementation it sorts the strings alphabetically.

For instance, given a CSV containing

```
‘a’, ‘b’, ‘c’ 
‘i’, ‘j’
‘x’, ‘y’
```

It would ouput these 12 strings:
```aix, aiy, ajx, ajy, bix, biy, bjx, bjy, cix, ciy, cjx, cjy```

## Running:
- First mark the file as executable using chmod and run:
```
./permutations.py filename.csv 
```

- Alternatively, simply run:
```
python3 ./permutations.py filename.csv
```

- Relative or absolute paths from your CWD (not necessarily where the file is stored) for the CSV file should work
