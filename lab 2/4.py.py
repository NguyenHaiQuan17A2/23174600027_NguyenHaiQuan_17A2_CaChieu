def phan_loai_diem(n):
    if 0 <= n < 5:
        return "Điểm kém"
    elif 5 <= n < 7:
        return "Điểm trung bình"
    elif 7 <= n < 8.5:
        return "Điểm khá"
    elif 8.5 <= n <= 10:
        return "Điểm tốt"
    else:
        return "Điểm không hợp lệ"
try:
    n = float(input("Nhập điểm số của bài kiểm tra: "))
    result = phan_loai_diem(n)
    print("Kết quả phân loại:", result)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")