# 1. 定義 Drink 類別
class Drink:
    # 建構子：初始化飲料的屬性
    def __init__(self, name, price, sugar):
        self.name = name
        self.price = price
        self.sugar = sugar

    # --- 魔術方法 __str__ ---
    # 當我們 print(物件) 時，Python 會自動呼叫這個方法
    # 它必須回傳一個字串
    def __str__(self):
        return f"{self.name} ({self.sugar}) - ${self.price}"

# --- 主程式：處理輸入與輸出 ---

try:
    # 1. 讀取訂單數量 N
    line = input()
    if line:
        N = int(line)
        
        # 準備一個空列表來裝飲料物件
        orders = []
        
        # 2. 迴圈讀取每一筆訂單
        for _ in range(N):
            parts = input().split()
            # 根據題目輸入格式: 名稱 價格 甜度
            d_name = parts[0]# 資料行的第一個部分是飲料名稱
            d_price = int(parts[1]) # 資料行的第二個部分是飲料價格，轉換成整數
            d_sugar = parts[2] # 資料行的第三個部分是甜度
            
            # 建立 Drink 物件
            new_drink = Drink(d_name, d_price, d_sugar)
            
            # 把物件加入列表 (List)
            orders.append(new_drink)
            
        # 3. 輸出訂單明細並計算總金額
        total = 0
        for drink in orders:
            # 這裡直接 print(drink) 就會觸發 __str__ 方法，超方便！
            print(drink)
            
            # 累加價格
            total += drink.price
            
        # 4. 輸出總金額
        print(f"Total: ${total}")

except ValueError:
    pass
#這段是為了避免在沒有輸入時程式崩潰 except的意思是當發生某種錯誤時要執行的程式碼 valueError是指輸入的值不符合預期的錯誤類型 EOFError是指當輸入結束時發生的錯誤類型
except EOFError:
    pass