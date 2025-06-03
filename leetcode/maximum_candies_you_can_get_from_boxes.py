# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes_owned = set(initialBoxes)
        keys_owned = set()
        boxes_queued = set()
        candies_opened = 0
        boxes_to_open = []

        for box in boxes_owned:
            if status[box] == 1 or box in keys_owned:
                boxes_to_open.append(box)
                boxes_queued.add(box)

        while boxes_to_open:
            box = boxes_to_open.pop()

            keys_gotten = keys[box]
            boxes_gotten = containedBoxes[box]
            candies_gotten = candies[box]
            for box_gotten in boxes_gotten:
                if status[box_gotten] == 1 or box_gotten in keys_owned:
                    if box_gotten not in boxes_queued:
                        boxes_queued.add(box_gotten)
                        boxes_to_open.append(box_gotten)
                boxes_owned.add(box_gotten)
            for key_gotten in keys_gotten:
                if key_gotten in boxes_owned:
                    if key_gotten not in boxes_queued:
                        boxes_queued.add(key_gotten)
                        boxes_to_open.append(key_gotten)
                keys_owned.add(key_gotten)
            candies_opened += candies_gotten

        return candies_opened
