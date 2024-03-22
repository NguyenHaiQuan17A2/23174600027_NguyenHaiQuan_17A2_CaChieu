def so_hang_nghin(n):
    if n< 1000:
        return 0 
    else:
        return (n//1000) % 10
n = int(input("Nhap so nguyen n: "))
print(f"Chữ số hàng nghìn của {n} là: {so_hang_nghin(n)}")


    
