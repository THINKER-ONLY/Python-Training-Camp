"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        if args:
            students.append(args[0])
    elif operation == "remove":
        if args:
            students.remove(args[0])
    elif operation == "update":
        if len(args) == 2 and args[0] in students: # 确保提供了两个名字且旧名字在列表中
            try:
                index = students.index(args[0])
                students[index] = args[1]
            except ValueError:
                # 虽然前面检查了 in students，但 index 仍然可能因为并发修改等原因失败（理论上）
                # 或者如果允许重名学生，只更新第一个找到的
                pass # 或者添加更详细的错误处理
                
    return students
    pass 