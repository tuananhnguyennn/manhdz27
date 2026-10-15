#1 Tạo DataFrame.
import pandas as pd

# Dữ liệu mẫu cho 10 sinh viên
data = {
    'Họ và tên': [
        'Châu', 'Chi', 'Phượng', 
        'Đạt', 'Khánh', 'Thùy', 
        'Băng', 'Minh', ' Mạnh', 'Nguyễn'
    ],
    'Điểm chuyên cần': [9.0, 8.5, 7.0, 10.0, 6.5, 9.5, 8.0, 7.5, 9.0, 8.5],
    'Điểm giữa kỳ': [8.5, 7.0, 6.5, 9.0, 5.0, 8.0, 7.5, 8.0, 9.5, 8.5],
    'Điểm cuối kỳ': [8.0, 9.0, 7.5, 9.5, 6.0, 8.5, 8.0, 7.0, 9.0, 8.5]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Hiển thị bảng dữ liệu
print(df)
#2. Tính điểm tổng kết
import pandas as pd

# Dữ liệu gốc
data = {
    'Họ và tên': [
        'Châu', 'Thùy', 'Phượng', 
        'Minh', 'Mạnh', 'Đạt', 
        'Khánh', 'Nguyên','Chi', 'Băng'
    ],
    'Điểm chuyên cần': [9.0, 8.5, 7.0, 10.0, 6.5, 9.5, 8.0, 7.5, 9.0, 8.5],
    'Điểm giữa kỳ': [8.5, 7.0, 6.5, 9.0, 5.0, 8.0, 7.5, 8.0, 9.5, 8.5],
    'Điểm cuối kỳ': [8.0, 9.0, 7.5, 9.5, 6.0, 8.5, 8.0, 7.0, 9.0, 8.5]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết theo công thức
df['Tong_ket'] = (0.2 * df['Điểm chuyên cần']) + (0.3 * df['Điểm giữa kỳ']) + (0.5 * df['Điểm cuối kỳ'])
df['Tong_ket'] = df['Tong_ket'].round(2)

# Hiển thị bảng dữ liệu
print(df)
#3. Xếp loại sinh viên.
import pandas as pd

# (Tiếp tục từ DataFrame hiện tại có cột 'Tong_ket')
# Định nghĩa hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

# Thêm cột Xep_loai vào DataFrame
df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Hiển thị bảng dữ liệu
print(df)
#4 Thống kê.
import pandas as pd

# (Tiếp tục từ DataFrame df đã có các cột Tong_ket và Xep_loai)

# 1. Tính điểm tổng kết trung bình của lớp
dtk_tb_lop = df['Tong_ket'].mean()
print(f"Điểm tổng kết trung bình của lớp: {dtk_tb_lop:.2f}")

# 2. Tìm sinh viên có điểm tổng kết cao nhất
sv_max = df.loc[df['Tong_ket'].idxmax()]
print(f"Sinh viên điểm cao nhất: {sv_max['Họ và tên']} với {sv_max['Tong_ket']} điểm")

# 3. Tìm sinh viên có điểm tổng kết thấp nhất
sv_min = df.loc[df['Tong_ket'].idxmin()]
print(f"Sinh viên điểm thấp nhất: {sv_min['Họ và tên']} với {sv_min['Tong_ket']} điểm")

# 4. Đếm số sinh viên đạt (điểm tổng kết >= 5)
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()
print(f"Số sinh viên đạt (>= 5 điểm): {so_sv_dat}")
#5. Thực quan hóa.
import matplotlib.pyplot as plt
import pandas as pd

# Dữ liệu từ các bước trước
data = {
    'Họ và tên': [
        'Châu', 'Minh', 'Mạnh', 
        'Thùy', 'Đạt', 'Khánh', 
        'Băng', 'Chi', 'Nguyên', 'Phượng'
    ],
'Điểm chuyên cần': [9.0, 8.5, 7.0, 10.0, 6.5, 9.5, 8.0, 7.5, 9.0, 8.5],
    'Điểm giữa kỳ': [8.5, 7.0, 6.5, 9.0, 5.0, 8.0, 7.5, 8.0, 9.5, 8.5],
    'Điểm cuối kỳ': [8.0, 9.0, 7.5, 9.5, 6.0, 8.5, 8.0, 7.0, 9.0, 8.5]
}

df = pd.DataFrame(data)
df['Tong_ket'] = (0.2 * df['Điểm chuyên cần']) + (0.3 * df['Điểm giữa kỳ']) + (0.5 * df['Điểm cuối kỳ'])
df['Tong_ket'] = df['Tong_ket'].round(2)

# Thiết lập biểu đồ cột ngang
plt.figure(figsize=(10, 6))
plt.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue')

# Thêm tiêu đề và nhãn các trục
plt.xlabel('Điểm tổng kết', fontsize=12)
plt.ylabel('Họ và tên sinh viên', fontsize=12)
plt.title('Biểu đồ thể hiện điểm tổng kết của 10 sinh viên', fontsize=14, fontweight='bold')

# Giới hạn trục x từ 0 đến 10
plt.xlim(0, 10)

# Hiển thị lưới mờ ở trục x
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Đảo ngược trục y để sinh viên đầu tiên hiển thị lên trên cùng
plt.gca().invert_yaxis()

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()