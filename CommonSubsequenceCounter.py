# python3

class CommonSubsequenceCounter(object):
    def __init__(self, ngram=3, max_skip=2, min_count=5):
        # paras
        self.ngram = ngram
        self.max_skip = max_skip
        self.min_count = min_count

        # sequence tree
        self.tree = {}
            
    def counter(self, root, seg, curr_deep, target_deep):
        max_skip = self.max_skip if curr_deep != 0 else None
        if curr_deep == target_deep:
            for w in seg[0:max_skip]:
                root.setdefault( w, [0, {}] )
                root[w][0] += 1
        else:
            for i, w in enumerate(seg[0:max_skip]):
                if w in root and root[w][0] > self.min_count:
                    self.counter(root[w][1], seg[i+1:], curr_deep+1, target_deep)

    def leaf_node_cleaner(self, root):
        for w in list(root.keys()):
            if root[w][0] > self.min_count:
                self.leaf_node_cleaner( root[w][1] )
            else:
                root.pop(w)

    def fit(self, sentences):
        for target_deep in range(self.ngram):
            for seg in sentences:
                self.counter(self.tree, seg, 0, target_deep)
            self.leaf_node_cleaner(self.tree)

    def traverser(self, root, chain=(), min_len=0):
        result = []
        for w, c in root.items():
            new_chain = chain+(w,)
            if len(new_chain) >= min_len:
                result.append( (new_chain, c[0]) )
            if c[1] != {}:
                result += self.traverser(c[1], new_chain)
        return result


if __name__ == '__main__':
    sentences = [
        ['0', '1', '2', '3', '4', '5', '6', '7'],
        ['0', '1', '2', '3', '4', '5', '6', '7'],
        ['0', '1', '2', '3', '4', '5', '6', '7']
    ]

    csc = CommonSubsequenceCounter(ngram=3, max_skip=2, min_count=1)
    csc.fit(sentences)
    result = csc.traverser(csc.tree)

    for sub_seq, count in result:
        print(sub_seq, count)
