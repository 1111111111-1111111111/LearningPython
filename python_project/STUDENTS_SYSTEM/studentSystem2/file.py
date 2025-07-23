def file_read():
    """
    读取文件内容
    :return:
    """
    file = open("students.txt", "rb")
    data = file.readlines()
    file.close()
    return data

def file_write(data):
    """
    追加写
    :param data:
    :return:
    """
    file = open("students.txt", "ab")
    file.write(data.encode("utf-8"))
    file.flush() # 重刷新
    file.close()


def file_overwrite(data):
    """
    覆盖写
    :param data:
    :param i:
    :return:
    """
    file = open("students.txt", "wb")
    file.writelines(data)
    file.close()
