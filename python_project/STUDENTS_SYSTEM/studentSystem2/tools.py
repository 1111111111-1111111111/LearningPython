from file import *
def display():
    """
    打印菜单
    :return:
    """
    print("""
    =====================================
                学生信息管理系统
    1. 添加学生信息            2. 查看学生信息
    3. 修改学生信息            4. 删除学生信息
    5. 退出
    =====================================
    """)
def add():
    """
    添加学生信息
    :return:
    """
    cid = input("请输入需要添加的学生学号：")
    if exists(cid):
        print("该学号已存在！")
    else:
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        message = f"{cid}    {name}    {age}\n"
        file_write(message)
        print("学生信息添加成功！")



def show():
    """
    展示学生信息
    :return:
    """
    print("当前学生信息：")
    for data in file_read():
        print(data.decode("utf-8"), end="")



def modify():
    """
    修改学生信息
    :return:
    """
    cid = input("请输入要修改的学生学号：")
    index = exists(cid)
    if index:
        data = file_read()
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        message = f"{cid}    {name}    {age}\n"
        data[index] = message.encode("utf-8")
        file_overwrite(data)
        print("学生信息修改成功！")
    else:
        print("该学号不存在！")

def delect():
    """
    删除学生信息
    :return:
    """
    cid = input("请输入要删除的学生学号：")
    index = exists(cid)
    if index:
         data = file_read()
         del data[index]
         file_overwrite(data)
         print("学生信息删除成功！")
    else:
        print("该学号不存在！")

def exists(cid):
    """
    是否存在该学号的学生信息
    :param cid:
    :return:
    """
    data = file_read()
    for i in range(len(data)):
        if data[i].decode("utf-8").split()[0] == cid:
            return i
    return 0
