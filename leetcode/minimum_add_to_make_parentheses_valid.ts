// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

function minAddToMakeValid(s: string): number {
  let unmatchedCloses = 0;
  let unmatchedOpens = 0;

  for (const char of s) {
      if (char === '(') {
          unmatchedOpens++;
      } else if (char === ')') {
          if (unmatchedOpens > 0) {
              unmatchedOpens--;
          } else {
              unmatchedCloses++;
          }
      }
  }

  return unmatchedCloses + unmatchedOpens;
};
