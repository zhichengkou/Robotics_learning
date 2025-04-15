import numpy as np

def rot_z(theta_deg):
    """绕 Z 轴旋转 theta（度）"""
    theta = np.deg2rad(theta_deg)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])

def make_transform(R, t):
    """构建 4x4 齐次变换矩阵"""
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T

def transform_point(T, p):
    """将点 p 进行齐次变换"""
    p_h = np.append(p, 1)  # 转为齐次坐标
    return (T @ p_h)[:3]

# 1️⃣ 坐标系 A 到 B 的变换
R_ab = rot_z(90)                    # 绕 Z 轴旋转 90°
t_ab = np.array([1, 0, 0])          # 平移 1m 到 X 方向
T_ab = make_transform(R_ab, t_ab)  # 坐标变换矩阵

# 2️⃣ 点在 A 系的坐标
p_a = np.array([1, 1, 0])

# 3️⃣ 点在 B 系的坐标
p_b = transform_point(T_ab, p_a)
print("点在 B 坐标系下的坐标：", p_b)

# 4️⃣ 组合两个变换（比如机械臂多关节）
T_bc = make_transform(np.eye(3), np.array([0, 2, 0]))
T_ac = T_ab @ T_bc
print("\n组合变换 T_ac：\n", T_ac)

# 5️⃣ 求逆变换（从 B 回到 A）
T_ba = np.linalg.inv(T_ab)
p_a_recovered = transform_point(T_ba, p_b)
print("\n变换回 A 坐标系：", p_a_recovered)
