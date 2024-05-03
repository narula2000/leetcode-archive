class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver_1 = version1.split('.')
        ver_2 = version2.split('.')
        for i in range(max(len(ver_1), len(ver_2))):
            revision_1 = int(ver_1[i]) if i < len(ver_1) else 0
            revision_2 = int(ver_2[i]) if i < len(ver_2) else 0
            if revision_1 < revision_2:
                return -1
            elif revision_1 > revision_2:
                return 1
        return 0

