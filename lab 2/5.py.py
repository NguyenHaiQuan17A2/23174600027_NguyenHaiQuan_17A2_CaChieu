def tinh_gia_ve(n):
    gia_ve = 120000
    tong_tien = n * gia_ve  
    if 2 <= n <= 4:
        giam = 0.05
    elif 5 <= n <= 10:
        giam = 0.1
    elif n > 10:
        giam = 0.2
    else:
        giam = 0
    tien_giam = tong_tien - (tong_tien * giam)

    return tien_giam
try:
    n = int(input("Nhập số lượng người: "))
    if n > 0:
        tong_tien = tinh_gia_ve(n)
        print("Tổng số tiền phải trả là:", tong_tien, "đồng")
    else:
        print("Số lượng người phải là một số nguyên dương.")
except ValueError:
    print("Vui lòng nhập số nguyên dương.")