import  pandas as pd
try:
    df = pd.read_csv("products.csv")
except FileNotFoundError:
    df = pd.dataframe(columns=["id","name","price","stock"])
def add_products():
    global df
    pid = int(input("enter product ID:"))
    if pid in df["id"].values:
        print("product id already exits")
        return
    name = input("enter product name:")
    price = float(input("enter product price:"))
    stock = int(input("enter product stock:"))
    new_product = {
        "id" : pid,
        "name" : name,
        "price" : price,
        "stock" : stock
        }
    df.loc[len(df)] = new_product
    df.to_csv("products.csv", index = False)
    print("product added successfully")
def view_products():
    if df.empty:
        print("no products available")
    else:
        print("\n---------PRODUCTS----------")
        print(df.to_string(index=False))
def search_product():
    name = input("enter product name to search:")
    result = df[df["name"].str.lower() == name.lower()]
    if result.empty:
        print("product not found")
    else:
        print("\n--------PRODUCT FOUND--------")
        print(result)
def update_product():
    global df
    pid = int(input("enter product id to update:"))
    if pid in df["id"].values:
        new_price = float(input("enter new price:"))
        new_stock = int(input("enter new stock:"))
        df.loc[df["id"] == pid, "price"] = new_price
        df.loc[df["id"] == pid, "stock"] = new_stock
        df.to_csv("products.csv", index = False)
        print("product updated successfully")
    else:
        print("product not found")
def delete_product():
    global df
    pid = int(input("enter product id to delete:"))
    if pid in df["id"].values:
        df = df[df["id"] != pid]
        df.to_csv("products.csv",index = False)
        print("product deleted successfully")
    else:
        print("product not found")
def low_stock():
    result = df[df["stock"] < 5]
    if result.empty:
        print("no low stock products")
    else:
        print("\n----------LOW STOCK PRODUTS-------")
        print(result)
def sort_by_price():
    print(df.sort_values(by= "price" , ascending= False))
def sort_by_stock():
    print(df.sort_values(by="stock" , ascending=False))
def highest_price():
    print("\n---------HIGHEST PRICED PRODUCT---------")
    print(df[df["price"] == df["price"].max()])
def lowest_product():
    print("\n---------LOWEST PRICED PRODUCT---------")
    print(df[df["price"] == df["price"].min()])
def total_product():
    print("total products:",len(df))
def inventory_value():
    total = (df["price"] * df["stock"]).sum()
    print("total inventory value:" , total)
while True:
    print("\n--------INVENTORY MANAGEMENT SYSTEM-------")
    print("1. Add product")
    print("2. view product")
    print("3. search product")
    print("4. update product")
    print("5. delete product")
    print("6. low stock alert")
    print("7. sort by price")
    print("8. sort by stock")
    print("9. highest price product")
    print("10. lowest price product")
    print("11. total product")
    print("12. inventory value")
    print("13. exit")
    choice = input("enter your choice:")
    if choice == "1":
        add_products()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        low_stock()
    elif choice == "7":
        sort_by_price()
    elif choice == "8":
        sort_by_stock()
    elif choice == "9":
        highest_price()
    elif choice == "10":
        lowest_price()
    elif choice == "11":
        total_product()
    elif choice == "12":
        investory_value()
    elif choice == "13":
        print("thank you for using investory management system")
        break
    else:
        print("invalid choice")
    
    
    

