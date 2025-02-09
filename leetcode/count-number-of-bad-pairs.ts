// https://leetcode.com/problems/count-number-of-bad-pairs/

function countBadPairs(nums: number[]): number {
  const offsetCounts = new Map<number, number>();

  let goodPairs = 0;
  for (let i = 0; i < nums.length; i++) {
    const offset = nums[i] - i;
    const goodMatches = offsetCounts.get(offset) ?? 0;
    goodPairs += goodMatches;
    offsetCounts.set(offset, goodMatches + 1);
  }

  const n = nums.length;
  const totalPairs = (n * (n - 1)) / 2;

  return totalPairs - goodPairs;
}
