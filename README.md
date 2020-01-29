# CommonSubsequenceCounter
Count the occurrence of common subsequence in a corpus.

# Example
```python
sentences = [
  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
  ['a', '1', 'c', '2', 'e', '3', 'g'],
  ['a', 'b', '1', 'd', 'e', '2', 'g']
]

csc = CommonSubsequenceCounter(ngram=3, max_skip=2, min_count=1)
csc.fit(sentences)
result = csc.traverser(csc.tree)

for x in result:
  print(x)

```
output:
```python
(('a',), 3)
(('a', 'b'), 2)
(('a', 'b', 'd'), 2)
(('a', 'c'), 2)
(('a', 'c', 'e'), 2)
(('a', '1'), 2)
(('b',), 2)
(('b', 'd'), 2)
(('b', 'd', 'e'), 2)
(('c',), 2)
(('c', 'e'), 2)
(('c', 'e', 'g'), 2)
(('d',), 2)
(('d', 'e'), 2)
(('d', 'e', 'g'), 2)
(('e',), 3)
(('e', 'g'), 3)
(('g',), 3)
(('1',), 2)
(('2',), 2)
```
