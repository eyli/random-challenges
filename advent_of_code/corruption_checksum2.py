def corruption_checksum(doc):
  checksum = 0
  for line in doc:
    checksum += find_evenly_disible(line)
  return checksum

def find_evenly_disible(line):
  for i in range(len(line)):
    for j in range(len(line)):
      if i != j:
          a, b = int(line[i]), int(line[j])
          if a % b == 0:
            print (a, b, a // b)
            return a // b


if __name__ == "__main__":
    with open("corruption_checksum.txt", "r") as f:
        s = f.read().strip()
    doc = [line.split() for line in s.splitlines()]
    result = corruption_checksum(doc)
    print(result)
