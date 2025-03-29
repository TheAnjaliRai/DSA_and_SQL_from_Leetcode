class Solution(object):
    def groupAnagrams(self, strs):
        sorted_key = ()
        group = {}
        for word in strs:
            sorted_key = tuple(sorted(word))
            if sorted_key in group:
                group[sorted_key].append(word)
            else:
                group[sorted_key] = [word]
        return list(group.values())

        