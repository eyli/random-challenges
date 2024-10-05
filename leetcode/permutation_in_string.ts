// https://leetcode.com/problems/permutation-in-string/

function checkInclusion(s1: string, s2: string): boolean {
  const len1 = s1.length;
  const len2 = s2.length;

  if (len1 > len2) return false;

  const count1 = new Array(26).fill(0);
  const windowCount = new Array(26).fill(0);

  for (let i = 0; i < len1; i++) {
      count1[getCharIndex(s1[i])]++;
      windowCount[getCharIndex(s2[i])]++;
  }

  let matches = 0;
  for (let i = 0; i < 26; i++) {
      if (count1[i] === windowCount[i]) {
          matches++;
      }
  }

  for (let right = len1; right < len2; right++) {
      if (matches === 26) return true;

      const left = right - len1;

      const indexNew = getCharIndex(s2[right]);
      const indexOld = getCharIndex(s2[left]);

      windowCount[indexNew]++;
      if (windowCount[indexNew] === count1[indexNew]) {
          matches++;
      } else if (windowCount[indexNew] === count1[indexNew] + 1) {
          matches--;
      }

      windowCount[indexOld]--;
      if (windowCount[indexOld] === count1[indexOld]) {
          matches++;
      } else if (windowCount[indexOld] === count1[indexOld] - 1) {
          matches--;
      }
  }

  return matches === 26;
}

function getCharIndex(c: string): number {
  return c.charCodeAt(0) - 'a'.charCodeAt(0);
}
