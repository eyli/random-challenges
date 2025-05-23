def corruption_checksum(doc):
  checksum = 0
  for line in doc:
    low = None
    high = None
    for value in line:
      value = int(value)
      if low is None:
        low = value
      if high is None:
        high = value
      low = min(low, value)
      high = max(high, value)
    checksum += high - low
  return checksum




if __name__ == "__main__":
    with open("corruption_checksum.txt", "r") as f:
        s = f.read().strip()
    doc = [line.split() for line in s.splitlines()]
    result = corruption_checksum(doc)
    print(result)
