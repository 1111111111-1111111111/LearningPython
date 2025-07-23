"""
创建一个学生管理系统
可以实现学生信息的录入(学号、姓名、年龄)
以及增删查改功能
学生管理系统
"""
students = []


def show_menu():
    info = """
    欢迎进入学生信息管理系统
    1:增加学生信息
    2:删除学生信息
    3:查询学生信息
    4:修改学生信息
    5:退出
    """
    print(info)


def add_student():
    # 增加学生信息(学号、姓名、年龄)
    student_info = input("请输入需要添加的学生信息(学号,姓名,年龄)：")
    if not student_info:
        print("请重新选择！")
        return
    info_list = student_info.split(",")
    scid, sname, sage = info_list
    for student in students:
        if scid == student["scid"]:
            print("学生已存在，请勿重新添加信息")
            return
    students.append({
        "scid": scid,
        "sname": sname,
        "sage": sage,
    })
    print(f"学生系统已成功添加学号为 {scid} 的学生信息！")
    return

def del_student():
    # 删除学生信息
    query_student()
    scid_info = input("请输入需要删除的学生学号：")
    if not len(scid_info):
        print("请重新选择！")
        return
    for student in students:
        if scid_info == student["scid"]:
            students.remove(student)
            print(f"已删除学号为 {scid_info} 的学生信息！")
            break
    else:
        print(f"没有学号为 {scid_info} 的学生信息！")

    return
def query_student():
    print(f"学号\t\t姓名\t\t年龄")
    # 查询学生信息
    for student in students:
        print(f"{student['scid']}\t\t{student['sname']}\t\t{student['sage']}")

def mod_student():
    query_student()
    # 修改学生信息
    student_info = input("请输入要修改的学生信息(学号,姓名,年龄)：")
    if not len(student_info):
        print("请重新选择！")
        return
    info_list = student_info.split(",")
    for student in students:
        if student["scid"] == info_list[0]:
            student["sname"] = info_list[1]
            student["sage"] = info_list[2]
            print(f"已成功修改学号为 {student['scid']} 的学生信息！")
            break
    else:
        print("未找到该学生！")


while True:
    show_menu()
    choice = input("请输入您的选择：")
    if choice == "1":
        add_student()
    elif choice == "2":
        del_student()
    elif choice == "3":
        query_student()
    elif choice == "4":
        mod_student()
    elif choice == "5":
        break
    else:
        print("您的输入有误，请重新输入！")
