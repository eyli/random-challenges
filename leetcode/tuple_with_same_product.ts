// https://leetcode.com/problems/tuple-with-same-product/
function tupleSameProduct(nums: number[]): number {
  const unique = Array.from(new Set(nums));
  const sorted = unique.sort((a, b) => a - b);

  let products: Record<number, number> = {};

  for (let i=0; i<sorted.length; i++) {
    for (let j=i+1; j<sorted.length; j++) {
      const currProduct = sorted[i] * sorted[j];
      products[currProduct] ??= 0;
      products[currProduct] += 1;
    }
  }

  let numTuples = 0;

  for (const [product, pairs] of Object.entries(products)) {
    if (pairs >= 2) {
      const numChoices = pairs * (pairs - 1) / 2;
      numTuples += numChoices * 8;
    }
  }

  return numTuples;
};
