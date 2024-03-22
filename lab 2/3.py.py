def chu_so_hang_chuc(n):
  return (n // 10) % 10
def chu_so_hang_don_vi(n):
  return n % 10
def doc_so(n):
  ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  if n < 10:
    return ones[n]
  elif n < 20:
    return teens[n - 10]
  elif n < 100:
    tens_digit = chu_so_hang_chuc(n)
    ones_digit = chu_so_hang_don_vi(n)
    if ones_digit == 0:
      return tens[tens_digit - 2]
    else:
      return tens[tens_digit - 2] + "-" + ones[ones_digit]
  else:
    return "hundred"
n = int(input("Nhập vào một số nguyên có ba chữ số: "))
print(f"Cách đọc của {n} là: {doc_so(n)}")