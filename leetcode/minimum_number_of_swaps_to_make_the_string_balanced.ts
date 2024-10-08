// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

function minSwaps(s: string): number {
  let count = 0;
  let maxCount = 0;
  for (const c of s) {
      if (c === '[') {
          count--;
      } else if (c === ']') {
          count++;
          maxCount = Math.max(count, maxCount);
      }
  }

  return Math.ceil(maxCount / 2) + maxCount % 2;
};
