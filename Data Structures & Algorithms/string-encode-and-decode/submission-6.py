class Solution:

    def encode(self, strs):
        if len(strs) == 0:
            return 'empty'
        return '_space_'.join(strs)

    def decode(self, s):
        if s == 'empty':
            return []
        return s.split('_space_')