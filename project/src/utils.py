def calculate_average(numbers):
    """计算一组数字的平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print("utils.py 模块加载成功！")
