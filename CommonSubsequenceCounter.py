# python3

class CommonSubsequenceCounter(object):
    def __init__(self, ngram=3, max_skip=2, min_count=5):
        self.ngram = ngram
        self.max_skip = max_skip
        self.min_count = min_count

        # tree structure: { 'word1':[count_num, children], 'word2': ... }
        self.tree = {}
            
    def counter(self, root, seg, curr_deep, target_deep):
        ''' create the count tree. '''
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
        ''' deletes leaf nodes that occur less than min_count times. '''
        for w in list(root.keys()):
            if root[w][0] > self.min_count:
                self.leaf_node_cleaner( root[w][1] )
            else:
                root.pop(w)

    def fit(self, sentences):
        ''' the subsequence counter. '''
        for target_deep in range(self.ngram):
            for seg in sentences:
                self.counter(self.tree, seg, 0, target_deep)
            self.leaf_node_cleaner(self.tree)

    def traverser(self, root, hist_seq=(), min_gram=0):
        ''' traverse the tree to get sub_seq count results (sub_seq length big than min_gram). '''
        result = []
        for w, data in root.items():
        	# data[0]: count num, data[1]: children
            curr_seq = hist_seq + (w,)
            if len(curr_seq) >= min_gram:
                result.append( (curr_seq, data[0]) )
            if data[1] != {}:
                result += self.traverser(data[1], curr_seq, min_gram)
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
