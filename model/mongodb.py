from pymongo import MongoClient
import datetime
#Authentication Database認證資料庫
stockDB = 'mydb'
dbname=  'howard-good31'

def constructor_stock():
    #密碼藥用mongodb的密碼
    clinet = MongoClient('mongodb://pxxqzz25852:qbb852258@ac-omwctnz-shard-00-00.bmfoxdm.mongodb.net:27017,ac-omwctnz-shard-00-01.bmfoxdm.mongodb.net:27017,ac-omwctnz-shard-00-02.bmfoxdm.mongodb.net:27017/?ssl=true&replicaSet=atlas-1dwvdm-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = clinet [stockDB]
    return db
#-----------------------------更新暫存的股票名稱---------------
def update_my_stock(user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collent = db[user_name]
    collent.update_many({'favorite_stock': stockNumber},{'$set':{'condition':condition,'price':target_price}})
    content = f'股票{stockNumber}更新成功'
    return content

# ---------------- 新增使用者的股票 -------------------


def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({'favorite_stock': stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock":stockNumber,
                "condition" : condition,
                "price" : target_price,
                "tag" : "stock",
                "date_info" : datetime.datetime.now()
        })
    return f'{stockNumber}以新增至您的股票清單'

#-------------------秀出使用者的股票條件----------------------------
def show_stock_setting(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({'userID': userID}))
    if dataList == []: return '您的股票清單為空，請透過指令新增股票至清單中'
    content = '您清單中的選股條件為: \n'
    for i in range(len(dataList)):
        content += f"{dataList[i]['favorite_stock']} {dataList[i]['condition']} {dataList[i]['price']}\n"
    return content
    
#-----------------刪除使用者特定的股票------------------
def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock': stockNumber})
    return stockNumber + "刪除成功"


#-----------------刪除使用者特定的股票-------------------
def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({'favorite_stock': stockNumber})
    return stockNumber + "刪除成功"