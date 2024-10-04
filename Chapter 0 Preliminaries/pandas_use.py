import os
import pandas as pd

os.makedirs(os.path.join(".", "data"), exist_ok=True)
data_file = os.path.join(".", "data", "house_tiny.csv")

with open(data_file, "w") as f:
    f.write("NumRooms,Alley,Price\n")  # 列名
    f.write("NA,Pave,127500\n")  # 每行表示一个数据样本
    f.write("2,NA,106000\n")
    f.write("4,NA,178100\n")
    f.write("NA,NA,140000\n")

data = pd.read_csv(data_file)  # 读取数据
print(data, "\n")
#    NumRooms Alley   Price
# 0       NaN  Pave  127500
# 1       2.0   NaN  106000
# 2       4.0   NaN  178100
# 3       NaN   NaN  140000

inputs_NumRooms, inputs_Alley, ourputs = (
    data.iloc[:, 0],
    data.iloc[:, 1],
    data.iloc[:, 2],
)  # 切分输入输出

print(inputs_NumRooms, "\n")

inputs_NumRooms = inputs_NumRooms.fillna(inputs_NumRooms.mean())  # 用平均值填充缺失值

print(inputs_NumRooms, "\n")

os.remove(data_file)  # 删除文件
os.removedirs(os.path.join(".", "data"))  # 删除文件夹
