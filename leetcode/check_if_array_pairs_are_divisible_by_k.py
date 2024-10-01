# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulos = {}
        for val in arr:
            modulo = val % k
            modulos[modulo] = modulos.get(modulo, 0) + 1
        if modulos.get(0, 0) % 2 != 0:
            return False
        i = 1
        j = k - 1
        while i < j:
            if modulos.get(i, 0) != modulos.get(j, 0):
                return False
            i += 1
            j -= 1
        return True
