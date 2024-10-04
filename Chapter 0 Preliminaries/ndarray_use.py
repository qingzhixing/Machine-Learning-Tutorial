import torch

# 我们可以使用 arange 创建一个行向量 x。
# 这个行向量包含以0开始的前12个整数，它们默认创建为整数。
# 也可指定创建类型为浮点数。
# 张量中的每个值都称为张量的 元素（element）。
# 例如，张量 x 中有 12 个元素。除非额外指定，新的张量将存储在内存中，并采用基于CPU的计算。

x = torch.arange(12)
print(x, "\n")  # tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

print(x.shape, "\n")  # torch.Size([12])

reshaped_x = x.reshape(2, -1)  # 重新排列张量的形状。
print(reshaped_x, "\n")  # tensor([[ 0,  1,  2,  3,  4,  5],[ 6,  7,  8,  9, 10, 11]])

# tensor(
#     [
#         [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
#         [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
#         [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
#     ]
# )
print(torch.zeros((3, 3, 3), dtype=torch.float32), "\n")

# tensor(
#     [
#         [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]],
#         [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]],
#         [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]],
#     ]
# )
print(torch.ones((3, 3, 3), dtype=torch.float32), "\n")

y = torch.arange(66, 78)

# tensor([66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88])
print(x + y, "\n")

z = torch.arange(5, 13)

# print(x + z, "\n")
#       ^^^^^
# Traceback (most recent call last):
#   File "xxx\Machine-Learning-Tutorial\Chapter 0 Preliminaries\ndarray\pytorch.py", line 42, in <module>
#     print(x + z, "\n")
# RuntimeError: The size of tensor a (12) must match the size of tensor b (8) at non-singleton dimension 0

#    tensor([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
#            [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
#            [ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13],
#            [ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
#            [ 4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
#            [ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16],
#            [ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17],
#            [ 7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
#            [ 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
#            [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
#            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]])
print(x.reshape(-1, 1) + x, "\n")


# Practice
X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
print("X:\n", X, "\n")

Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print("Y:\n", Y, "\n")

catted_dim0, catted_dim1 = torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)
print("Catted_dim0:\n", catted_dim0, "\n")
print("Catted_dim1:\n", catted_dim1, "\n")

print("X==Y:\n", X == Y, "\n")

print("X<Y:\n", X < Y, "\n")

print("X>Y:\n", X > Y, "\n")

tensor_3d = torch.zeros((2, 2, 2), dtype=torch.float32)
print("tensor_3d:\n", tensor_3d, "\n")

tensor_3d[0, 1, 1] = 1
print("tensor_3d:\n", tensor_3d, "\n")

tensor_2d = torch.randn((2, 3), dtype=torch.float32)
print("tensor_2d:\n", tensor_2d, "\n")

# 张量的运算
# print("tensor_2d + tensor_3d:\n", tensor_2d + tensor_3d, "\n")
#                                   ^^^^^^^^^^^^^^^^^^^
# Traceback (most recent call last):
#   File "x\Machine-Learning-Tutorial\Chapter 0 Preliminaries\ndarray_use.py", line 91, in <module>
#     print("tensor_2d + tensor_3d:\n", tensor_2d + tensor_3d, "\n")
# RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 2
