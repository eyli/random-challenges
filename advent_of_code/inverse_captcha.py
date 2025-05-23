def inverse_captcha(s):
  sum = 0
  for i, c in enumerate(s):
    if c == s[(i+1) % len(s)]:
      sum += int(c)
  return sum

if __name__ == "__main__":
    with open("inverse_captcha.txt", "r") as f:
        s = f.read().strip()
    result = inverse_captcha(s)
    print(result)
