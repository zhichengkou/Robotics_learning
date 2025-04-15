import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline, make_interp_spline

# 原始数据点
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 0, 1, 0])

# 插值用的更密的 x 值
xx = np.linspace(0, 4, 300)

# 各种插值方法
linear_interp = interp1d(x, y, kind='linear')
quadratic_interp = interp1d(x, y, kind='quadratic')
cubic_interp = CubicSpline(x, y)
bspline_interp = make_interp_spline(x, y)  # 默认是 cubic B-spline

# 计算插值结果
yy_linear = linear_interp(xx)
yy_quadratic = quadratic_interp(xx)
yy_cubic = cubic_interp(xx)
yy_bspline = bspline_interp(xx)

# 画图对比
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data Points', color='black')
plt.plot(xx, yy_linear, label='Linear Spline', linestyle='--')
plt.plot(xx, yy_quadratic, label='Quadratic Spline', linestyle='-.')
plt.plot(xx, yy_cubic, label='Cubic Spline', linestyle=':')
plt.plot(xx, yy_bspline, label='B-Spline', linewidth=2)

plt.title("Comparison of Spline Interpolation Methods")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
