def main():
    print("-----------------------")
    print("-    通讯录系统V1.0     -")
    print("-  输入不同数字选择功能   -")
    print("- 输入 1 添加联系人      -")
    print("- 输入 2 浏览所有联系人   -")
    print("- 输入 3 寻找联系人      -")
    print("- 输入 0 退出程序        -")
    print("-----------------------")
def add_():
    f=open("D:\\py\\通讯录数据.txt","a",encoding="UTF-8")
    while True:
        try:
            name,number=input("||请按照姓名（空格）手机号的顺序填入系统||").split()
        except ValueError as e:
            print("异常符号，输入错误，请重新输入")
            continue
        else:
            break
    f.write("姓名：{}  电话号：{}\n".format(name,number))
    print("写入完成，姓名是{}，电话号是{}".format(name,number))
    print("-----------------------")
    while True:
        try:
            i = int(input("输入1返回主菜单"))
        except ValueError as e:
            print("异常符号，输入错误，请重新输入")
            continue
        if i==1:
            break
        else:
            print("输入错误，请重新输入")
            continue
    f.close()
def find_sb():
    is_find=True
    while True:
        try:
            sb=input("请输入要查找的姓名")
        except ValueError as e:
            print("异常符号，输入错误，请重新输入")
            continue
        else:
            break
    f=open("D:\\py\\通讯录数据.txt","r",encoding="UTF-8")
    for i in f:
        information=i.split()
        if information[0][3:len(information[0])]==sb:
            print("已找到该联系人，姓名是：{} 电话号是{}".format(information[0],information[1]))
            print("-----------------------")
            while True:
                try:
                    a=int(input("输入1返回主菜单"))
                except ValueError as e:
                    print("异常符号，输入错误，请重新输入")
                    continue
                if a==1:
                    break
                else:
                    print("重新输入")
                    continue
            is_find=False
            break
        else :
             continue
    if is_find:
        print("没有找到该名联系人,或输入异常")
        print("-----------------------")
    while(is_find):
        try :
            i=int(input("是否要添加该联系人，是请输入1，否请输入2"))
        except ValueError as e:
            print("异常符号，输入错误，请重新输入")
            continue
        if i ==1:
            add_()
            break
        elif i==2:
            print("将回到主菜单")
            break
        else :
            print("输入错误请重新输入")
            continue
    f.close()
def all_():
    f = open("D:\\py\\通讯录数据.txt", "r", encoding="UTF-8")
    for i in f:
        information=i.split()
        print("姓名{} 电话号是：{}".format(information[0],information[1]))
    print("打印完毕")
    print("-----------------------")
    while(True):
        try:
            a=int(input("输入 0 返回主菜单"))
        except ValueError as e:
            print("异常符号，输入错误，请重新输入")
            continue
        if a==0:
            break

        else:
            print("输入错误，重新输入")
            continue
    f.close()

while True:
    main()
    try:
        user_choice=int(input())
    except ValueError as e:
        print("异常符号，输入错误，请重新输入")
        continue
    if user_choice == 1 :
        add_()
    elif user_choice == 2 :
        all_()
    elif user_choice == 3 :
        find_sb()
    elif user_choice == 0 :
        break
    else :
        print("错误数字,输入错误，请重现输入")
        continue
