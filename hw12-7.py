# =======================================================
# 1. 定義 Account 類別 (這是銀行帳戶)
# =======================================================
class Account:
    # --- 類別屬性：全行凍結狀態 ---
    # 預設是 False (沒凍結)，這是一個全銀行共享的開關
    is_frozen = False

    # --- 靜態函式：檢查帳號格式 ---
    # 規則：必須 'A' 開頭，後面接 5 個數字，總長度 6
    @staticmethod
    def is_valid_id(acc_id):
        # 條件 1: 長度是否為 6
        if len(acc_id) != 6: return False
        # 條件 2: 第一個字是不是 'A'
        if acc_id[0] != 'A': return False
        # 條件 3: 後面 5 碼是不是數字
        if not acc_id[1:].isdigit(): return False
        
        return True

    # --- 類別方法：設定凍結狀態 ---
    # 只有銀行高層 (Class Method) 可以按這個按鈕
    @classmethod
    def set_freeze(cls, status):
        cls.is_frozen = status

    # --- 建構子 ---
    def __init__(self, acc_id, balance):
        self.id = acc_id
        self.balance = balance

    # --- 實體方法：執行轉帳 ---
    # self 是「轉出者」，target 是「轉入者」
    def transfer(self, target, amount):
        # 關卡 1: 檢查全行是否凍結？
        # 注意：要查全行狀態，用 Account.is_frozen
        if Account.is_frozen:
            return "Frozen"

        # 關卡 2: 檢查目標帳戶是否存在？
        # 這裡的 target 預期會是一個 Account 物件，如果主程式傳進來 None，代表找不到人
        if target is None:
            return "Invalid Account"

        # 關卡 3: 檢查錢夠不夠？
        if self.balance < amount:
            return "Insufficient Funds"

        # 通過所有關卡 -> 執行轉帳
        self.balance -= amount        # 我扣錢
        target.balance += amount      # 他加錢
        return "Success"

# =======================================================
# 2. 主程式：銀行櫃台系統
# =======================================================

try:
    # 讀取指令數量
    line = input()
    if line:
        N = int(line)
        
        # 用字典管理所有帳戶 (Key: ID, Value: Account Object)
        accounts = {}
        
        for _ in range(N):
            parts = input().split()
            command = parts[0]
            
            # --- 情境 1: 開戶 (create) ---
            if command == "create":
                acc_id = parts[1]
                balance = int(parts[2])
                
                # 先檢查帳號格式是否合法 (呼叫靜態函式)
                if Account.is_valid_id(acc_id):
                    # 合法 -> 建立物件並存入字典
                    new_acc = Account(acc_id, balance)
                    accounts[acc_id] = new_acc
                    # 題目沒要求輸出 create 成功訊息，所以這裡不用 print
                else:
                    # 雖然題目沒特別說 create 失敗要印什麼，但通常是不建立
                    pass
            
            # --- 情境 2: 轉帳 (transfer) ---
            elif command == "transfer":
                from_id = parts[1]
                to_id = parts[2]
                amount = int(parts[3])
                
                # 從字典中找出轉出者
                sender = accounts.get(from_id) # 如果找不到會回傳 None
                
                # 從字典中找出轉入者
                receiver = accounts.get(to_id) # 如果找不到會回傳 None

                # 這裡有個細節：如果 sender 根本不存在 (None)，題目沒說怎麼辦
                # 但根據常理，我們可以先判斷 sender
                if sender is None:
                     print("Invalid Account")
                else:
                    # 呼叫 sender 的轉帳方法
                    # receiver 如果是 None，會在 transfer 方法內被擋下來
                    result = sender.transfer(receiver, amount)
                    print(result)
            
            # --- 情境 3: 凍結/解凍 (freeze/unfreeze) ---
            elif command == "freeze":
                Account.set_freeze(True)
            elif command == "unfreeze":
                Account.set_freeze(False)

except ValueError:
    pass
except IndexError:
    pass
except EOFError:
    pass