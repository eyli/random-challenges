// https://leetcode.com/problems/minimum-string-length-after-removing-substrings

function minLength(s: string): number {
  const stack: string[] = [];
  let numRemoved = 0;

  for (const c of s) {
      if (c === 'A' || c === 'C') {
          stack.push(c);
      } else if (
          c === 'B' && stack[stack.length - 1] === 'A' ||
          c === 'D' && stack[stack.length - 1] === 'C'
      ) {
          stack.pop();
          numRemoved += 2;
      } else {
          stack.length = 0;
      }
  }
  return s.length - numRemoved;
};
