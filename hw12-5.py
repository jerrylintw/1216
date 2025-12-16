# =======================================================
# 1. 定義 Stats 類別 (這是一個數學工具箱)
# =======================================================
class Stats:
    # --- 靜態函式：計算平均 ---
    # 這個函式不關心是哪個學生的成績，它只負責「算數學」
    # 給它一串數字 (List)，它就吐回平均值 (Float)
    @staticmethod
    def calculate_avg(scores_list):
        if not scores_list: # 防呆：如果列表是空的
            return 0.0
        # 平均 = 總分 / 科目數
        return sum(scores_list) / len(scores_list)

# =======================================================
# 2. 定義 Student 類別 (這是學生的資料夾)
# =======================================================
class Student:
    # --- 建構子 ---
    def __init__(self, name):
        self.name = name
        # 每個學生都有自己的成績單 (List)
        self.scores = []

    # --- 實體方法：新增成績 ---
    # 把這次考的分數加到成績單裡
    def add_score(self, score):
        self.scores.append(score)

    # --- 實體方法：取得平均 ---
    # 學生自己不會算平均，但他會把成績單交給工具箱 (Stats) 去算
    def get_average(self):
        # 呼叫上面的靜態工具
        return Stats.calculate_avg(self.scores)

# =======================================================
# 3. 主程式：班級管理系統
# =======================================================

try:
    # 讀取指令數量
    line = input()
    if line:
        N = int(line)
        
        # 核心資料結構：用字典來管理全班學生
        # Key: 學生名字, Value: 學生物件 (Student Object)
        # 這樣我們就可以用 students["Alice"] 快速找到 Alice 的資料夾
        students = {}
        
        for _ in range(N):
            parts = input().split()
            command = parts[0]
            name = parts[1]
            
            # --- 情境 1: 新增成績 ---
            if command == "add":
                score = int(parts[2])
                
                # 如果這個學生還沒建檔，先幫他開一個新資料夾 (物件)
                if name not in students:
                    students[name] = Student(name)
                
                # 從字典把學生物件抓出來，幫他加分
                students[name].add_score(score)
                
            # --- 情境 2: 查詢平均 ---
            elif command == "query":
                # 確保學生存在才查詢
                if name in students:
                    # 呼叫學生物件的方法取得平均
                    avg = students[name].get_average()
                    # 格式化輸出，保留一位小數
                    print(f"{name} Average: {avg:.1f}")

except ValueError:
    pass
except IndexError:
    pass
except EOFError:
    pass