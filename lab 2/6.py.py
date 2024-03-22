def tim_so_lon_thu_hai(a, b, c):
    so_lon_nhat = max(a, b, c)
    if so_lon_nhat == a:
        so_lon_thu_hai = max(b, c)
    elif so_lon_nhat == b:
        so_lon_thu_hai = max(a, c)
    else:
        so_lon_thu_hai = max(a, b)
    return so_lon_thu_hai
try:
    num1 = int(input("Nhập số nguyên thứ nhất: "))
    num2 = int(input("Nhập số nguyên thứ hai: "))
    num3 = int(input("Nhập số nguyên thứ ba: "))
    if num1 > 0 and num2 > 0 and num3 > 0:
        result = tim_so_lon_thu_hai(num1, num2, num3)
        print("Số lớn thứ hai trong các số là:", result)
    else:
        print("Cần nhập các số nguyên dương.")
except ValueError:
    print("Vui lòng nhập số nguyên dương.")