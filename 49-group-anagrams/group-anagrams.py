class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # обычный словарь

        for s in strs:
            key = ''.join(sorted(s))  # каноническая форма
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())