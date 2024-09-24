# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        int_prefix_trie = {}
        for value in arr1:
            current_value = str(value)
            current_node = int_prefix_trie
            while current_value:
                current_digit = current_value[0]
                if current_digit in current_node:
                    current_node = current_node[current_digit]
                else:
                    new_node = {}
                    current_node[current_digit] = new_node
                    current_node = new_node
                current_value = current_value[1:]

        output = 0
        for value in arr2:
            current_output = 0
            current_value = str(value)
            current_node = int_prefix_trie
            while current_value:
                current_digit = current_value[0]
                if current_digit in current_node:
                    current_value = current_value[1:]
                    current_node = current_node[current_digit]
                    current_output += 1
                else:
                    break
            output = max(output, current_output)
        return output
