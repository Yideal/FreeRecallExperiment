import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据定义
data = {
    "10-2": {
        "positions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "probabilities": [0.78, 0.65, 0.52, 0.38, 0.30, 0.25, 0.28, 0.35, 0.45, 0.68]
    },
    "20-1": {
        "positions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "probabilities": [0.75, 0.62, 0.48, 0.35, 0.28, 0.22, 0.20, 0.18, 0.17, 0.16, 0.15, 0.16, 0.17, 0.19, 0.22, 0.26, 0.32, 0.40, 0.52, 0.65]
    },
    "15-2": {
        "positions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "probabilities": [0.80, 0.68, 0.55, 0.42, 0.32, 0.25, 0.22, 0.20, 0.21, 0.23, 0.26, 0.31, 0.38, 0.48, 0.62]
    },
    "30-1": {
        "positions": list(range(1, 31)),
        "probabilities": [0.76, 0.63, 0.50, 0.38, 0.30, 0.24, 0.20, 0.18, 0.16, 0.15, 0.14, 0.13, 0.14, 0.13, 0.14, 0.15, 0.14, 0.15, 0.16, 0.17, 0.18, 0.20, 0.22, 0.25, 0.29, 0.34, 0.41, 0.49, 0.58, 0.68]
    },
    "20-2": {
        "positions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "probabilities": [0.82, 0.70, 0.58, 0.45, 0.35, 0.28, 0.24, 0.22, 0.21, 0.20, 0.21, 0.22, 0.24, 0.27, 0.31, 0.36, 0.43, 0.52, 0.61, 0.72]
    },
    "40-1": {
        "positions": list(range(1, 41)),
        "probabilities": [0.634, 0.505, 0.411, 0.341, 0.281, 0.244, 0.227, 0.218, 0.212, 0.209, 0.214, 0.206, 0.202, 0.198, 0.204, 0.195, 0.191, 0.193, 0.198, 0.194, 0.196, 0.192, 0.189, 0.194, 0.191, 0.198, 0.203, 0.196, 0.192, 0.197, 0.201, 0.206, 0.218, 0.241, 0.272, 0.315, 0.372, 0.451, 0.556, 0.722]
    }
}

# 总回忆量数据
total_recall_data = {
    "categories": ["20秒组", "30秒组", "40秒组"],
    "groups": [
        {"name": "10-2", "value": 6.42, "category": "20秒组"},
        {"name": "20-1", "value": 6.35, "category": "20秒组"},
        {"name": "15-2", "value": 8.11, "category": "30秒组"},
        {"name": "30-1", "value": 7.98, "category": "30秒组"},
        {"name": "20-2", "value": 8.74, "category": "40秒组"},
        {"name": "40-1", "value": 8.58, "category": "40秒组"}
    ]
}

# 颜色定义
colors = {
    "10-2": "#ff6384",
    "20-1": "#ff9f40",
    "15-2": "#ffcd56",
    "30-1": "#4bc0c0",
    "20-2": "#36a2eb",
    "40-1": "#9966ff"
}

# Gompertz函数
def gompertz(x, v, g, h):
    return v * (g ** (h ** x))

# 图1：六组实验系列位置曲线
plt.figure(figsize=(12, 8))
for key, values in data.items():
    plt.plot(values["positions"], values["probabilities"], label=key, color=colors[key], linewidth=2)
plt.xlabel('系列位置')
plt.ylabel('回忆概率')
plt.title('六组实验系列位置曲线')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('d:\\user\\Desktop\\实验 - 副本\\实验\\系列位置曲线.png', dpi=300, bbox_inches='tight')
plt.close()

# 图2：总时间相同组别的回忆量对比
plt.figure(figsize=(10, 6))
bars = []
labels = []
bar_colors = []

for i, category in enumerate(total_recall_data["categories"]):
    category_groups = [g for g in total_recall_data["groups"] if g["category"] == category]
    for j, group in enumerate(category_groups):
        bars.append(group["value"])
        labels.append(group["name"])
        bar_colors.append(colors[group["name"]])

plt.bar(range(len(bars)), bars, color=bar_colors)
plt.xticks(range(len(bars)), labels)
plt.ylabel('平均回忆数')
plt.title('总时间相同组别的回忆量对比')
plt.grid(True, alpha=0.3, axis='y')
plt.savefig('d:\\user\\Desktop\\实验 - 副本\\实验\\总回忆量对比.png', dpi=300, bbox_inches='tight')
plt.close()

# 图3：40-1组近因效应Gompertz拟合
last8_positions = data["40-1"]["positions"][-8:]
last8_probabilities = data["40-1"]["probabilities"][-8:]
x_values = list(range(len(last8_positions)))[::-1]  # 倒数位置

# 拟合参数
v, g, h = 0.806, 0.041, 0.561
fitted_values = [1 - gompertz(x, v, g, h) for x in x_values]

plt.figure(figsize=(10, 6))
plt.scatter(last8_positions, last8_probabilities, label='实际数据', color=colors["40-1"], s=50)
plt.plot(last8_positions, fitted_values, label='Gompertz拟合', color='black', linewidth=2)
plt.xlabel('系列位置')
plt.ylabel('回忆概率')
plt.title('40-1组近因效应Gompertz拟合 (r²=0.981)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('d:\\user\\Desktop\\实验 - 副本\\实验\\近因效应拟合.png', dpi=300, bbox_inches='tight')
plt.close()

# 图4：不同呈现速率下的系列位置曲线对比
plt.figure(figsize=(12, 8))
plt.plot(data["10-2"]["positions"], data["10-2"]["probabilities"], label='10-2 (2秒/词)', color=colors["10-2"], linewidth=2)
plt.plot(data["20-1"]["positions"], data["20-1"]["probabilities"], label='20-1 (1秒/词)', color=colors["20-1"], linewidth=2)
plt.plot(data["20-2"]["positions"], data["20-2"]["probabilities"], label='20-2 (2秒/词)', color=colors["20-2"], linewidth=2)
plt.plot(data["40-1"]["positions"], data["40-1"]["probabilities"], label='40-1 (1秒/词)', color=colors["40-1"], linewidth=2)
plt.xlabel('系列位置')
plt.ylabel('回忆概率')
plt.title('不同呈现速率下的系列位置曲线对比')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('d:\\user\\Desktop\\实验 - 副本\\实验\\呈现速率对比.png', dpi=300, bbox_inches='tight')
plt.close()

print("图表生成完成，已保存到实验文件夹中。")