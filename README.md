# CommonSubsequenceCounter
Count the occurrence of common subsequence in a corpus.

# Example
```python
sentences = [
    ['0', '1', '2', '3', '4', '5'],
    ['0', '1', '2', '3', '4', '5'],
    ['0', '1', '2', '3', '4', '5']
]

csc = CommonSubsequenceCounter(ngram=3, max_skip=2, min_count=1)
csc.fit(sentences)
result = csc.traverser(csc.tree)

for sub_seq, count in result:
    print(sub_seq, count)

```
output:
```python
('0',) 3
('0', '1') 3
('0', '1', '2') 3
('0', '1', '3') 3
('0', '2') 3
('0', '2', '3') 3
('0', '2', '4') 3
('1',) 3
('1', '2') 3
('1', '2', '3') 3
('1', '2', '4') 3
('1', '3') 3
('1', '3', '4') 3
('1', '3', '5') 3
('2',) 3
('2', '3') 3
('2', '3', '4') 3
('2', '3', '5') 3
('2', '4') 3
('2', '4', '5') 3
('3',) 3
('3', '4') 3
('3', '4', '5') 3
('3', '5') 3
('4',) 3
('4', '5') 3
('5',) 3
```
