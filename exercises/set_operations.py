"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    # 请在下方编写代码
    if operation == "union":
        # 计算并集：包含 set1 和 set2 中所有不重复的元素
        return set1.union(set2) # 或者使用 set1 | set2
    elif operation == "intersection":
        # 计算交集：同时存在于 set1 和 set2 中的元素
        return set1.intersection(set2) # 或者使用 set1 & set2
    elif operation == "difference":
        # 计算差集：存在于 set1 但不存在于 set2 中的元素
        return set1.difference(set2) # 或者使用 set1 - set2
    else:
        # 无效的操作类型
        print(f"错误: 未知的操作类型 '{operation}'。支持的操作有 'union', 'intersection', 'difference'。")
        return None
    pass