# =======================================================
# 1. 定義 Course 類別 (這是課程)
# =======================================================
class Course:
    def __init__(self, course_id, day, time, capacity):
        self.course_id = course_id
        self.capacity = int(capacity)
        
        # --- 核心觀念：Tuple ---
        # 我們把 (星期, 時間) 綁在一起變成一個 Tuple
        # 這樣要比對衝堂時，只要看這個 Tuple 一不一樣就好
        self.schedule = (day, time)
        
        # --- 核心觀念：Set ---
        # 用集合來存學生名單，因為學生名字不會重複
        self.students = set()

    # --- 實體方法：檢查是否額滿 ---
    def is_full(self):
        # 目前人數 >= 容量 就是滿了
        return len(self.students) >= self.capacity

# =======================================================
# 2. 定義 Student 類別 (這是學生)
# =======================================================
class Student:
    def __init__(self, name):
        self.name = name
        # 這是個人的課表 (List)，裡面存的是 Course 物件
        self.my_courses = []

    # --- 實體方法：檢查衝堂 ---
    def has_conflict(self, new_course):
        # 拿出我已經選上的每一堂課
        for enrolled_course in self.my_courses:
            # 比對時間：如果 Tuple 一模一樣，就是衝堂！
            # 例如 ('Mon', '10') == ('Mon', '10')
            if enrolled_course.schedule == new_course.schedule:
                return True
        return False

    # --- 實體方法：加選課程 (雙向更新) ---
    def enroll(self, course):
        # 1. 學生記住這堂課
        self.my_courses.append(course)
        # 2. 課程記住這個學生
        course.students.add(self.name)

# =======================================================
# 3. 主程式：選課系統
# =======================================================

try:
    # 讀取指令數量
    line = input()
    if line:
        N = int(line)
        
        # 用字典存所有開課的課程 (Key: ID, Value: Course Object)
        all_courses = {}
        # 用字典存所有學生 (Key: Name, Value: Student Object)
        # 這樣才能記住學生選過什麼課
        all_students = {}
        
        for _ in range(N):
            parts = input().split()
            command = parts[0]
            
            # --- 情境 1: 開課 (add_course) ---
            if command == "add_course":
                c_id = parts[1]
                day = parts[2]
                time = parts[3]
                cap = parts[4]
                
                # 建立課程物件並存入字典
                all_courses[c_id] = Course(c_id, day, time, cap)
                
            # --- 情境 2: 選課 (register) ---
            elif command == "register":
                s_name = parts[1]
                c_id = parts[2]
                
                # 1. 確保學生存在 (如果第一次來，就幫他建檔)
                if s_name not in all_students:
                    all_students[s_name] = Student(s_name)
                student = all_students[s_name]
                
                # 2. 確保課程存在
                if c_id in all_courses:
                    course = all_courses[c_id]
                    
                    # --- 選課邏輯開始 ---
                    # 順序很重要：先看有沒有位子 -> 再看有沒有衝堂 -> 最後加選
                    
                    if course.is_full():
                        print("Full")
                    elif student.has_conflict(course):
                        print("Time Conflict")
                    else:
                        # 通過檢查，執行加選
                        student.enroll(course)
                        print("Success")

except ValueError:
    pass
except IndexError:
    pass
except EOFError:
    pass