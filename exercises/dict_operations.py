"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    if operation == "add":
        # 添加操作：需要姓名和成绩两个参数
        if len(args) == 2:
            name, score = args
            students_dict[name] = score
            return students_dict
        else:
            print("错误: 'add' 操作需要姓名和成绩两个参数。")
            return None # 参数数量不符

    elif operation == "remove":
        # 删除操作：需要姓名一个参数
        if len(args) == 1:
            name = args[0]
            # 使用 pop 方法删除，如果键不存在也不会报错（返回 None）
            students_dict.pop(name, None) 
            return students_dict
        else:
            print("错误: 'remove' 操作需要姓名一个参数。")
            return None # 参数数量不符

    elif operation == "update":
        # 更新操作：需要姓名和新成绩两个参数
        if len(args) == 2:
            name, new_score = args
            # 只有当学生存在时才更新
            if name in students_dict:
                students_dict[name] = new_score
            else:
                print(f"警告: 学生 '{name}' 不存在，无法更新。")
            return students_dict
        else:
            print("错误: 'update' 操作需要姓名和新成绩两个参数。")
            return None # 参数数量不符

    elif operation == "get":
        # 查询操作：需要姓名一个参数
        if len(args) == 1:
            name = args[0]
            # 使用 get 方法获取成绩，如果键不存在则返回 None
            return students_dict.get(name)
        else:
            print("错误: 'get' 操作需要姓名一个参数。")
            return None # 参数数量不符
            
    else:
        # 无效的操作类型
        print(f"错误: 未知的操作类型 '{operation}'。")
        return None
    pass 