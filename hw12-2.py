# =======================================================
# 1. 定義 Student 類別 (這是一個工具箱)
# =======================================================
class Student:
    # 這裡我們不需要 __init__，因為我們暫時還沒要「製造」學生
    # 我們只需要一個「工具」來檢查電話號碼
    
    # --- 靜態函式 (Static Method) ---
    # @staticmethod 就像是在說：「這個功能跟特定的某個學生無關」
    # 它只是一個掛在 Student 招牌下的「通用檢查器」
    @staticmethod
    def is_valid_phone(phone_number):
        # 步驟 1: 檢查長度是不是 10 碼？
        # 就像檢查身分證字號長度一樣，不對就直接淘汰
        check_length = len(phone_number) == 10
        
        # 步驟 2: 檢查是不是全部都是數字？
        # .isdigit() 會幫我們看字串裡有沒有混入英文或符號
        check_digit = phone_number.isdigit()
        
        # 兩個條件都要成立 (True)，這個電話才算通過 (True)
        return check_length and check_digit

# =======================================================
# 2. 主程式：這裡是櫃台，負責接待與處理資料
# =======================================================

try:
    # 讀取今天要處理幾筆資料 (N)
    line = input()
    if line:
        N = int(line)
    else:
        N = 0
    
    # --- 準備通訊錄 (Dictionary) ---
    # 想像這是一個空的聯絡簿，左邊寫學號 (Key)，右邊寫名字 (Value)
    # 為什麼用 Dict？因為透過學號找名字最快！
    student_contacts = {} 
    
    # 開始處理 N 筆資料
    for _ in range(N):
        try:
            # 讀取一行資料：學號 名字 電話
            parts = input().split()
            
            # 防呆機制：確保資料有三段，不然程式會報錯
            if len(parts) < 3:
                continue 

            s_id = parts[0]   # 學號
            name = parts[1]   # 名字
            phone = parts[2]  # 電話
            
            # --- 呼叫檢查器 ---
            # 直接用「類別名稱.方法」來呼叫，不需要建立物件
            if Student.is_valid_phone(phone):
                # 🟢 通過檢查！
                # 把資料寫入聯絡簿 (Dict)
                # 語法：Dict[Key] = Value
                student_contacts[s_id] = name
                print(f"{name} added")
            else:
                # 🔴 沒通過！
                print("Invalid Phone")
                
        except IndexError:
            continue
            
    # =======================================================
    # 3. 最終整理：依照學號順序印出名單
    # =======================================================
    
    # 從聯絡簿拿出所有的學號 (Keys)
    all_ids = student_contacts.keys()
    
    # 因為 Dict 本身是沒順序的，所以我們要用 sorted() 幫學號排排站
    # sorted() 會回傳一個排好序的 List，例如 ['S01', 'S02', 'S03']
    sorted_ids = sorted(all_ids) 
    
    # 照順序點名
    for s_id in sorted_ids:
        # 拿著學號 (Key) 去聯絡簿 (Dict) 查名字 (Value)
        s_name = student_contacts[s_id]
        print(f"{s_id}: {s_name}")
            
except ValueError:
    pass
except EOFError:
    pass