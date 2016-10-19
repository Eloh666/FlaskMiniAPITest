import os
import sqlite3

class productDB(object):
    def __init__(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.conn = sqlite3.connect(os.path.join(__location__, 'productDB.db'))
        self.conn.commit()
        self.cursor = self.conn.cursor()

    def getProducts(self):
        self.cursor.execute("SELECT * FROM products")
        self.conn.commit()
        return [i for i in self.cursor]

    def getCategories(self):
        self.cursor.execute("SELECT * FROM categories")
        self.conn.commit()
        return [i for i in self.cursor]

    def addSingleCategoryIfNecessary(self, categoryID):
        self.cursor.execute("SELECT * FROM categories WHERE id = ? ", [categoryID])
        if len([i for i in self.cursor]) == 0:
            self.cursor.execute("INSERT INTO categories (id, name) VALUES (?, ?)",
                                [categoryID, 'ToBeDetermined'])

    def addSingleProduct(self, product):
        self.cursor.execute("SELECT * FROM products WHERE name = ? ", [product['name']])
        if len([i for i in self.cursor]) != 0:
            return False
        else:
            self.addSingleCategoryIfNecessary(product['catID'])

            # This is code is only because SQLite does not have auto increment
            self.cursor.execute("SELECT MAX(id) FROM products ")
            query = [i for i in self.cursor]
            id = 0 if  len(query) == 0 else query[0][0] + 1
            # This is code is only because SQLite does not have auto increme

            self.cursor.execute("INSERT INTO products (id, name, description, catID) VALUES (?, ?, ?, ?)",
                                [id, product['name'], product['description'], product['catID']])
            self.conn.commit()
            return True

    def deleteSingleProduct(self, product):
        self.cursor.execute("DELETE FROM products WHERE id = ? and name = ?", [product['id'], product['name']])

    def __del__(self):
        self.conn.close()