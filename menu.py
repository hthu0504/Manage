import manage

def main():
    while True:
        print("\nMenu:")
        print("1. Thêm học sinh")
        print("2. Thêm thông tin học sinh")
        print("3. Xóa học sinh")
        print("4. Thêm giáo viên")
        print("5. Thêm thông tin giáo viên")
        print("6. Xóa giáo viên")
        print("7. Thoát")
        
        choice = input("Chọn tùy chọn: ")
        
        if choice == '1':
            name = input("Nhập tên học sinh: ")
            lop = input("Nhập lớp: ")
            birth = input("Nhập năm sinh: ")
            manage.AddStudent(name, lop, birth)
        
        elif choice == '2':
            name = input("Nhập tên học sinh: ")
            birth = input("Nhập năm sinh: ")
            details = {}
            while True:
                key = input("Nhập tên chi tiết hoặc 'done' để end: ")
                if key == 'done':
                    break
                value = input(f"Nhập giá trị cho {key}: ")
                details[key] = value
            manage.AddDetailstoStudent(name, birth, details)
        
        elif choice == '3':
            name = input("Nhập tên học sinh: ")
            birth = input("Nhập năm sinh: ")
            manage.RemoveStudent(name, birth)
        
        elif choice == '4':
            name = input("Nhập tên giáo viên: ")
            subj = input("Nhập môn học: ")
            birth = input("Nhập năm sinh: ")
            manage.AddTeacher(name, subj, birth)
        
        elif choice == '5':
            name = input("Nhập tên giáo viên: ")
            birth = input("Nhập năm sinh: ")
            details = {}
            while True:
                key = input("Nhập tên chi tiết hoặc 'done' để end: ")
                if key == 'done':
                    break
                value = input(f"Nhập giá trị cho {key}: ")
                details[key] = value
            manage.AddDetailstoTeacher(name, birth, details)
        
        elif choice == '6':
            name = input("Nhập tên giáo viên: ")
            birth = input("Nhập năm sinh: ")
            manage.RemoveTeacher(name, birth)
        
        elif choice == '7':
            print("Thoát chương trình")
            break
        
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()