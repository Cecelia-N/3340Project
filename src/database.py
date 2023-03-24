"""Database management"""
import pymongo

class Database:
    """Database containing product data"""
    @classmethod
    def start_db(db):
        """Start the database"""
        db.dbclient = pymongo.MongoClient()
        db.database = db.dbclient["db"]
        db.plants = db.database["plants"]

    @classmethod
    def add_product(db, product: dict):
        """Add a product to the database"""
        db.plants.insert_one(product)

    @classmethod
    def get_product(db, id: int):
        """Get a product's data from the database"""
        query = {"id": id}
        return db.plants.find_one(query)

    @classmethod
    def update_inventory(db, id: int, inventory: int):
        """Change inventory quantity of a product"""
        query = {"id", id}
        newvalue = {"$set": {"inventory": inventory}}
        db.plants.update_one(query, newvalue)

    @classmethod
    def sell(db, id: int):
        """Sell a plant (decrement inventory, return false if 0"""
        query = {"id" : id}
        plant = db.plants.find_one(query)
        inventory = plant["inventory"]
        if inventory == 0:
            return False
        newvalue = {"$set": {"inventory": inventory - 1}}
        db.plants.update_one(query, newvalue)
        return True
