def tinh_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi
def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi < 25.0:
        return "Bình thường"
    elif 25.0 <= bmi < 30.0:
        return "Hơi béo"
    else:
        return "Béo"
try:
    height = float(input("Nhập chiều cao của bạn (cm): "))
    weight = float(input("Nhập cân nặng của bạn (kg): "))
    if height > 0 and weight > 0:
        bmi = tinh_bmi(height, weight)
        phan_loai = phan_loai_bmi(bmi)
        print("Chỉ số BMI của bạn là:", bmi)
        print("Phân loại BMI của bạn là:", phan_loai)
    else:
        print("Chiều cao và cân nặng phải là số dương.")
except ValueError:
    print("Vui lòng nhập số dương cho chiều cao và cân nặng.")