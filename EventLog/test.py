from csv import reader, DictReader, writer, DictWriter, field_size_limit
import os


def writedata_with_writer():
    with open(r"E:\python codes\csv_file\file.csv", "a", newline="") as objw:
        name = input("enter name ")
        email = input("enter email ")
        ph = input("enter ph")
        letstr = name + "," + email + "," + ph
        lst = letstr.split(",")
        objw = writer(objw)
        objw.writerow(lst)


def writedata_with_dictwriter():
    with open(r"C:\python codes\csv_file\file.csv", "a", newline="") as objw:
        name = input("enter name ")
        email = input("enter email ")
        ph = input("enter ph")
        objw = DictWriter(objw, fieldnames=["name", "email", "ph"])
        objw.writeheader()
        objw.writerow({
            "name": name,
            "email": email,
            "ph": ph
        })

def readdata_with_reader():
    with open(r"H:\file.csv.csv", "r") as obj:
        read = reader(obj)
        for row in read:
            print(row)


def readdata_with_dictreader():
    with open(r"H:\file.csv.csv", "r") as obj:
        read = DictReader(obj)
        for singledict in read:
            print(singledict)


def searchdata():
    f = 0
    search = input("enter name to search")
    with open(r"E:\python codes\csv_file\file.csv", "r") as obj:
        read = DictReader(obj)
        for singledict in read:
            # print("now singledict is :",singledict)
            for i in singledict:
                # print("now i in singledict is :",i)
                if search == singledict.get(i):
                    f = 1
                    print("you serach : ", i)
        if f == 0:
            print("data not found")


def deletedata():
    os.chdir(r"E:\python codes\csv_file")
    f = 0
    lst = []
    delete = input("enter name to delete")
    with open(r"E:\python codes\csv_file\file.csv", "r") as obj:
        with open(r"E:\python codes\csv_file\file1.csv", "a", newline="") as obj1:
            read = reader(obj)
            for single in read:
                print("single in read : ", single)
                for i in single:
                    print("i in single : ", i)
                    if delete == i:
                        f = 1
                        break
                    else:
                        lst.append(i)
                else:
                    w = writer(obj1)
                    w.writerow(lst)
                    lst = []
        os.chdir(r"E:\python codes\csv_file")
    os.remove(r"E:\python codes\csv_file\file.csv")
    os.rename(r"E:\python codes\csv_file\file1.csv", r"E:\python codes\csv_file\file.csv")

    if f == 0:
        print("data not found")
    else:
        print("data is deleted")


def updatedata():
    os.chdir(r"E:\python codes\csv_file")
    f = 0
    lst = []
    update = input("enter name to update")
    with open(r"E:\python codes\csv_file\file.csv", "r") as obj:
        with open(r"E:\python codes\csv_file\file2.csv", "a", newline="") as obj1:
            read = reader(obj)
            for single in read:
                print("single in read : ", single)
                for i in single:
                    print("i in single : ", i)
                    if update == i:
                        f = 1
                        name = input("enter new name ")
                        email = input("enter new email ")
                        ph = input("enter new ph")
                        letstr = name + "," + email + "," + ph
                        lst1 = letstr.split(",")
                        objwr = writer(obj1)
                        objwr.writerow(lst1)
                        lst1 = []
                        break
                    else:
                        lst.append(i)
                else:
                    w = writer(obj1)
                    w.writerow(lst)
                    lst = []
        os.chdir(r"E:\python codes\csv_file")
    os.remove(r"E:\python codes\csv_file\file.csv")
    os.rename(r"E:\python codes\csv_file\file2.csv", r"E:\python codes\csv_file\file.csv")

    if f == 0:
        print("data not found")
    else:
        print("data is updated")


# def print_specific_data():
#     pass


def main():
    while (True):
        print("1 for write data in csv file with writer fun")
        print("2 for write data in csv file with DictWriter fun")
        print("3 for read data in csv file with reader fun")
        print("4 for read data in csv file with Dictreader fun")
        print("5 search data")
        print("6 delete data data")
        print("7 update data data")
        print("8 print specific row and coulmns")
        print("9 exit")
        choice = int(input("enter choice"))
        if choice == 1:
            writedata_with_writer()
        elif choice == 2:
            writedata_with_dictwriter()
        elif choice == 3:
            readdata_with_reader()
        elif choice == 4:
            readdata_with_dictreader()
        elif choice == 5:
            searchdata()
        elif choice == 6:
            deletedata()
        elif choice == 7:
            updatedata()
        # elif choice==8:
        #     print_specific_data()
        elif choice == 9:
            exit()
        else:
            print("invalid input")


main()
