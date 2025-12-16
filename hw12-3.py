# =======================================================
# 1. 定義 Member 類別 (這是一個全家桶)
# =======================================================
class Member:
    # --- 類別屬性 (Class Attribute) ---
    # 這是全家共享的「點數倍率」
    # 預設是 1.0 (沒活動)，這個變數不屬於任何一個人，是屬於這整個家的
    rate = 1.0

    # --- 類別方法 (Class Method) ---
    # @classmethod 就像是家長控制模式
    # 用來修改那個全家共享的 rate
    @classmethod
    def set_rate(cls, new_rate):
        # cls 代表 Member 這個類別本身
        # 把全家的倍率改成新的數值
        cls.rate = new_rate
        print(f"Rate updated to {cls.rate}")

    # --- 建構子 (Constructor) ---
    # 這是每個家庭成員出生 (建立物件) 時會跑的地方
    def __init__(self, name, spend):
        # 這些是個人的秘密 (實體屬性)
        self.name = name       # 我的名字
        self.spend = spend     # 我花的錢

    # --- 實體方法 (Instance Method) ---
    # 計算這個成員這次消費可以拿多少點
    def calculate_points(self):
        # 點數 = 我花的錢 (self.spend) * 全家的倍率 (Member.rate)
        # 記得要取整數 (int)，不然會有小數點
        points = int(self.spend * Member.rate)
        return points

# =======================================================
# 2. 主程式：處理輸入與操作
# =======================================================

try:
    # 讀取指令數量 N
    line = input()
    if line:
        N = int(line)
        
        # 開始處理每一行指令
        for _ in range(N):
            parts = input().split()
            command = parts[0]
            
            # --- 情境 1: 建立新成員並結帳 ---
            if command == "member":
                name = parts[1]
                spend = int(parts[2])
                
                # 1. 建立一個新成員物件
                new_member = Member(name, spend)
                
                # 2. 幫他算點數 (會用到當下的倍率)
                points = new_member.calculate_points()
                
                # 3. 印出結果
                print(f"{new_member.name} got {points} points")
                
            # --- 情境 2: 修改全家倍率 ---
            elif command == "rate":
                new_rate_val = float(parts[1])
                
                # 呼叫類別方法，直接改全域設定
                Member.set_rate(new_rate_val)
                
except ValueError:
    pass
except IndexError:
    pass
except EOFError:
    pass