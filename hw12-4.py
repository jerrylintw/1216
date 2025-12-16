# =======================================================
# 1. 定義 Warehouse 類別 (這是一個智慧倉庫)
# =======================================================
class Warehouse:
    # --- 建構子 (Constructor) ---
    # 初始化倉庫的狀態
    def __init__(self, initial_items):
        # 1. 庫存清單 (Inventory)
        # 我們用 set() 集合，因為查找速度超快，而且商品種類不重複
        # initial_items 是一個 list，set() 會自動把它轉成集合
        self.inventory = set(initial_items)
        
        # 2. 缺貨紀錄 (Missing List)
        # 我們用 list []，因為我們要記錄每一次的缺貨，就算重複也要記下來
        self.missing = []

    # --- 實體方法：處理訂單 ---
    def order(self, item):
        # 檢查倉庫裡有沒有這個東西？
        # 使用 item in set 是非常高效率的操作
        if item in self.inventory:
            # 有貨 -> 出貨
            print("Shipped")
        else:
            # 沒貨 -> 記錄到缺貨清單，並回報缺貨
            self.missing.append(item)
            print("Out of Stock")

    # --- 實體方法：補貨入庫 ---
    def restock(self, item):
        # 把東西加進庫存集合
        # set.add() 會自動處理重複，如果已經有了就不會重複加
        self.inventory.add(item)

# =======================================================
# 2. 主程式：處理輸入與操作
# =======================================================

try:
    # 讀取第一行：初始庫存 (例如 "Apple Banana")
    # split() 會把它切成 ['Apple', 'Banana']
    initial_stock_list = input().split()
    
    # 建立倉庫物件
    my_warehouse = Warehouse(initial_stock_list)
    
    # 讀取指令數量 N
    line = input()
    if line:
        N = int(line)
        
        for _ in range(N):
            parts = input().split()
            command = parts[0]
            item_name = parts[1]
            
            # --- 情境 1: 客人下訂單 ---
            if command == "order":
                my_warehouse.order(item_name)
                
            # --- 情境 2: 廠商補貨 ---
            elif command == "restock":
                my_warehouse.restock(item_name)
                
        # 3. 最後報告：總共缺貨幾次？
        print(f"Total Missing: {len(my_warehouse.missing)}")

except ValueError:
    pass
except IndexError:
    pass
except EOFError:
    pass