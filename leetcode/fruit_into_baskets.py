# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        initial_fruit = fruits[0]
        initial_fruit_start = 0
        other_fruit = None
        current_chain_fruit = initial_fruit
        current_chain_fruit_start = 0

        highest_seen = 0

        for i, fruit in enumerate(fruits):

            if fruit == current_chain_fruit:
                continue

            if other_fruit is None:
                other_fruit = fruit

            if fruit == initial_fruit or fruit == other_fruit:
                current_chain_fruit = fruit
                current_chain_fruit_start = i
            else: # New fruit
                highest_seen = max(highest_seen, i - initial_fruit_start)
                initial_fruit = current_chain_fruit
                initial_fruit_start = current_chain_fruit_start
                other_fruit = fruit
                current_chain_fruit = fruit
                current_chain_fruit_start = i

        return max(highest_seen, i - initial_fruit_start + 1)
