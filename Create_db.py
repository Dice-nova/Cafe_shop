#!/usr/bin/env python3
import mysql.connector # type: ignore
#database will be detailed as: ID, name, price, author/allergens, details, stock

Food= {
        "Chocolate Muffins": {
            "Price": 6.99,
            "Allergens": "Gluten (from wheat flour), eggs, and milk",
            "Details": "Rich and delicious Chocolate Muffins made with an intense chocolate batter and studded with chocolate chips throughout",
            "Stock": 1
        },
        "Scones": {
            "Price": 5.99,
            "Allergens": "gluten (from wheat flour), dairy (milk and butter), and egg",
            "Details": "A small, often round, quick bread-like pastry, traditionally from Britain and Ireland",
            "Stock": 1
        },
        "Cookie": {
            "Price": 7.99,
            "Allergens": "wheat (gluten), milk, eggs, nuts (such as peanuts and tree nuts), and soy",
            "Details": "A baked snack or dessert that is typically small, flat, and sweet.",
            "Stock": 1
        },
        "Victoria Sponge Cakes": {
            "Price": 8.99,
            "Allergens": "eggs, gluten (from wheat flour), and milk (from butter and/or milk powder)",
            "Details": "Soft, tender, and fluffy, this Victoria Sponge Cake is a simple but delicious cake that's a British classic for a reason",
            "Stock": 1
        },
        "Lemon Loaf Cake": {
            "Price": 12.99,
            "Allergens": " gluten, eggs, and dairy (milk and butter)",
            "Details": "This lemon loaf cake is soft, velvety, super moist and is bursting with lemon flavour",
            "Stock": 1
        },
        "Surloin Steak": {
            "Price": "29.99",
            "Allergens": "",
            "Details": "Hassiba was talking about a surloin steak after not realising they weren't muted lol",
            "Stock" : 1
        }}

Drink= {
        "Espresso": {
            "Price": 4.99,
            "Allergens": "gluten, milk, soy, nuts, and eggs",
            "Details": "A concentrated coffee beverage made by forcing hot water under pressure through finely ground coffee beans",
            "Stock": 1
        },
        "Latte": {
            "Price": 4.99,
            "Allergens": "The main allergen concern is milk",
            "Details": "A milk-based coffee drink typically made with espresso, steamed milk, and a thin layer of frothed milk on top",
            "Stock": 1
        },
        "Cappuccino": {
            "Price": 4.99,
            "Allergens": "milk the primary allergen for most people",
            "Details": "A popular coffee drink, typically made with espresso, steamed milk, and milk foam, all in equal parts",
            "Stock": 1
        },
        "Macchiato": {
            "Price": 4.99,
            "Allergens": "include allergens such as caramel sauce and vanilla syrup which can contain milk and/or soy",
            "Details": "A coffee beverage that typically consists of a shot of espresso 'marked' or 'stained' with a small amount of steamed or foamed milk",
            "Stock": 1
        },
        "Mocha": {
            "Price": 4.99,
            "Allergens": "milk and soy",
            "Details": "A coffee beverage that combines the flavors of espresso, steamed milk, and chocolate",
            "Stock": 1
        }}

Book = {
        "American Psycho": {
            "Price": "10.00",
            "Author": "Bret Easton Ellis",
            "Details": "American Psycho is a black comedy horror novel by American writer Bret Easton Ellis, published in 1991. The story is told in the first-person by Patrick Bateman, a wealthy, narcissistic, and vain Manhattan investment banker who lives a double life as a serial killer",
            "Stock": 1
        },
        "House Of Leaves": {
            "Price": 12.99,
            "Author": "Mark Z. Danielewski",
            "Details": "House of Leaves is the debut novel by American author Mark Z. Danielewski, published in March 2000 by Pantheon Books. A bestseller, it has been translated into a number of languages, and is followed by a companion piece, The Whalestoe Letters",
            "Stock": 1
        },
        "The Picture Of Dorian Gray": {
            "Price": 15.99,
            "Author": "Oscar Wilde",
            "Details": "The Picture of Dorian Gray is an 1890 philosophical fiction and gothic horror novel by Irish writer Oscar Wilde. A shorter novella-length version was published in the July 1890 issue of the American periodical Lippincott's Monthly Magazine, while the novel-length version was published in April 1891",
            "Stock": 1
        },
        "A Little Life": {
            "Price": 10.99,
            "Author": "Hanya Yanagihara",
            "Details": "A Little Life is a 2015 novel by American writer Hanya Yanagihara. Lengthy and tackling difficult subject matter, it garnered critical acclaim, was shortlisted for the 2015 Man Booker Prize and the National Book Awards, and became a best selle",
            "Stock": 1
        },
        "The Love Hypothesis": {
            "Price": 12.99,
            "Author": "Ali Hazelwood",
            "Details": "The Love Hypothesis is a romance novel by Ali Hazelwood, published September 14, 2021 by Berkley Books.",
            "Stock": 1
        }}



def create_tables():
    cursor.execute("CREATE TABLE food (ID INT NOT NULL PRIMARY KEY, name VARCHAR(30), price INT UNSIGNED NOT NULL, allergens VARCHAR(100), details VARCHAR(350), stock INT UNSIGNED)")
    cursor.execute("CREATE TABLE drink (ID INT NOT NULL PRIMARY KEY, name VARCHAR(30), price INT UNSIGNED NOT NULL, allergens VARCHAR(100), details VARCHAR(350), stock INT UNSIGNED)")
    cursor.execute("CREATE TABLE book (ID INT NOT NULL PRIMARY KEY, name VARCHAR(30), price INT UNSIGNED NOT NULL, author VARCHAR(100), details VARCHAR(350), stock INT UNSIGNED)")

def create_rec():
    base_command = """INSERT INTO %s (ID, name, price, allergens, details, stock) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")"""
    ID=0
    for item in Food:
        price = Food[item]["Price"]
        allergens = Food[item]["Allergens"]
        details = Food[item]["Details"]
        stock = Food[item]["Stock"]
        command = base_command % ("food", ID, item, price, allergens, details, stock)
        ID +=1
        cursor.execute(command)
    ID=100
    for item in Drink:
        price = Drink[item]["Price"]
        allergens = Drink[item]["Allergens"]
        details = Drink[item]["Details"]
        stock = Drink[item]["Stock"]
        command = base_command % ("drink", ID, item, price, allergens, details, stock)
        ID +=1
        cursor.execute(command)
    ID=200
    base_command = """INSERT INTO book (ID, name, price, author, details, stock) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")"""
    for item in Book:#current error: column "author" not found in the sql segment
        price = Book[item]["Price"]
        allergens = Book[item]["Author"]
        details = Book[item]["Details"]
        stock = Book[item]["Stock"]
        command = base_command % (ID, item, price, allergens, details, stock)
        ID +=1
        cursor.execute(command)



try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database="cafe_shop"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        create_tables()
        create_rec()
        connection.commit()


except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()