# =======================================================
# 1. 定義 Library 類別 (這是中央圖書管理系統)
# =======================================================
class Library:
    # --- 類別屬性：借閱池 ---
    # 這是一個 Set，裡面放著「目前不在館內」的書的 ISBN
    # 為什麼用 Set？因為我們要用最快速度檢查這本書是不是「被借走了」
    borrowed_books = set()

    # --- 靜態函式：檢查書在不在 ---
    @staticmethod
    def is_available(isbn):
        # 如果 ISBN 不在「借閱池」裡，代表書在館內 (True)
        return isbn not in Library.borrowed_books

    # --- 靜態函式：把書借出去 ---
    @staticmethod
    def borrow_book(isbn):
        # 把 ISBN 丟進「借閱池」，標示為已借出
        Library.borrowed_books.add(isbn)

    # --- 靜態函式：把書還回來 ---
    @staticmethod
    def return_book(isbn):
        # 如果書真的在「借閱池」裡，就把它拿掉 (discard 不會報錯)
        Library.borrowed_books.discard(isbn)

# =======================================================
# 2. 定義 Member 類別 (這是借書證)
# =======================================================
class Member:
    def __init__(self, name):
        self.name = name
        # 每個會員都有一本借閱存摺 (History List)
        # 裡面會存一筆一筆的紀錄
        self.history = []

    # --- 實體方法：借書動作 ---
    def borrow(self, isbn, date):
        # 1. 先問圖書館系統：這本書還在嗎？
        if Library.is_available(isbn):
            # 2. 在的話，告訴系統這本書被我借走了
            Library.borrow_book(isbn)
            
            # 3. 在自己的存摺記上一筆
            # 這裡用 Tuple (ISBN, Date) 因為這筆紀錄不該被隨便改
            record = (isbn, date)
            self.history.append(record)
            
            print("Borrowed")
        else:
            # 不在的話，就是被借走了
            print("Unavailable")

# =======================================================
# 3. 主程式：圖書館櫃台
# =======================================================

try:
    # 讀取指令數量
    line = input()
    if line:
        N = int(line)
        
        # 用字典來管理所有會員 (Key: 名字, Value: 會員物件)
        members = {}
        
        for _ in range(N):
            parts = input().split()
            command = parts[0]
            
            # --- 情境 1: 借書 ---
            if command == "borrow":
                user_name = parts[1]
                isbn = parts[2]
                date = parts[3]
                
                # 如果是新會員，先發一張借書證 (建立物件)
                if user_name not in members:
                    members[user_name] = Member(user_name)
                
                # 執行借書動作
                members[user_name].borrow(isbn, date)
                
            # --- 情境 2: 還書 ---
            elif command == "return":
                isbn = parts[1]
                # 告訴圖書館系統書回來了
                Library.return_book(isbn)
                
            # --- 情境 3: 查詢歷史紀錄 ---
            elif command == "history":
                user_name = parts[1]
                if user_name in members:
                    # 取出該會員的物件
                    member = members[user_name]
                    # 遍歷他的歷史紀錄 (List of Tuples)
                    for record in member.history:
                        # record[0] 是 ISBN, record[1] 是 Date
                        # 題目要求輸出格式: Date: ISBN
                        print(f"{record[1]}: {record[0]}")

except ValueError:
    pass
except IndexError:
    pass
except EOFError:
    pass