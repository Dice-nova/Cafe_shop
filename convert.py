#!/usr/bin/env python3
import mysql.connector # type: ignore
#database will be detailed as: ID, name, price, author/allergens, details, stock


def show_stock(table):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database="cafe_shop"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            results = cursor.fetchall()
            if table.lower() != "book":
                for row in results:
                    print(f"{row[1]}\t\t\t£{row[2]}\nAllergens: {row[3]}\n{row[4]}\nquantity: {row[5]}\n")
            else:
                for row in results:
                    print(f"{row[1]}\t\t\t£{row[2]}\nAuthor: {row[3]}\n{row[4]}\nquantity: {row[5]}\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_stock(table):
    name = input("Please enter the name of the item\n")
    price = float(input("Please enter how much it will cost\n"))
    auth = input("Please enter the author/allergens\n")
    detail = input("Please enter a description of the item\n")
    stock = int(input(f"Please enter how many of them are there\n"))
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database="cafe_shop"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            results = cursor.fetchall()
            ID = len(results)+1
            if table == "food":
                cursor.execute(f"INSERT INTO {table}(foodID, foodname, price, allergens, details, stock) VALUES({ID},'{name}',{price},'{auth}','{detail}',{stock})")
            elif table == "drink":
                ID += 100
                cursor.execute(f"INSERT INTO {table}(drinkID, drinkname, price, allergens, details, stock) VALUES({ID},'{name}',{price},'{auth}','{detail}',{stock})")
            elif table == "book":
                ID += 200
                cursor.execute(f"INSERT INTO {table}(bookID, bookname, price, author, details, stock) VALUES({ID},'{name}',{price},'{auth}','{detail}',{stock})")
            connection.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def rem_stock(table):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database="cafe_shop"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            results = cursor.fetchall()
            i = 0
            if table.lower() != "book":
                for row in results:
                    i+=1
                    print(f"{i}: {row[1]}\t\t\t£{row[2]}\nAllergens: {row[3]}\n{row[4]}\nquantity: {row[5]}\n")
            else:
                for row in results:
                    i+=1
                    print(f"{i}: {row[1]}\t\t\t£{row[2]}\nAuthor: {row[3]}\n{row[4]}\nquantity: {row[5]}\n")
            ID = str.title(input("Which item would you like to remove?(use the number)\n"))
            if table =="drink":
                ID +=100
            elif table =="book":
                ID +=200
            cursor.execute(f"DELETE FROM {table} WHERE {table}ID={ID}")
            connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


option= input("1.show menu\t\t2.add item\t\t3.remove item\t\t4.order something\n")
if option =="1":
    table = str.lower(input("1.food\t\t2.drink\t\t3.book\n"))
    try:
        int(table)
        if table =="1":
            table = "food"
        if table =="2":
            table = "drink"
        if table =="3":
            table = "book"
    except:
        pass
    show_stock(table)
elif option =="2":
    table = str.lower(input("1.food\t\t2.drink\t\t3.book\n"))
    try:
        int(table)
        if table =="1":
            table = "food"
        if table =="2":
            table = "drink"
        if table =="3":
            table = "book"
    except:
        pass
    add_stock(table)
elif option =="3":
    table = str.lower(input("1.food\t\t2.drink\t\t3.book\n"))
    try:
        int(table)
        if table =="1":
            table = "food"
        if table =="2":
            table = "drink"
        if table =="3":
            table = "book"
    except:
        pass
    rem_stock(table)
elif option =="4":
    pass
else:
    pass

