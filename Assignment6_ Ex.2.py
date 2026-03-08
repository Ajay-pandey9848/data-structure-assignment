# CHAPTER 6 EXERCISE 2
'''
Product Inventory Hash Table Exercise

Build a simple hash table class (without using Python’s dict for storage) for a product inventory system.

Requirements

- Use a list of buckets (array)
- Handle collisions using separate chaining (each bucket stores a list)
- Each product has the following:
    sku (string key) (SKU means Stock Keeping Unit, it's just an alphanumeric code like AB12 for ex.)
    name
    quantity

Methods to implement

- set_item(sku, name, quantity) → add/update product
- get_item(sku) → return product info
- remove_item(sku) → delete product
- print_table() → print hash table contents

Hint!
Use a hash function like:
sum the character codes of the SKU
modulo by table size

'''

# Here's a base where you can start! Implement the TODO's

class InventoryHashTable:
    """
    Custom hash table for product inventory.

    Rules:
    - Use a list of buckets (self.table)
    - Each bucket is a list (separate chaining)
    - Product data: sku, name, quantity
    """

    def __init__(self, size=10):
        self.size = size
        # TODO: create a list of empty buckets
        # HINT: [[] for _ in range(size)]
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Simple hash function for string keys.
        Example approach:
        - Sum ord(ch) for each character in key
        - Return total % self.size
        """
        # TODO: implement hash function
        key_sum = 0
        for ch in key:
            key_sum += ord(ch)
        return key_sum % self.size

    def set_item(self, sku, name, quantity):
        """
        Add a new product or update existing one.

        TODO:
        - Compute bucket index with _hash
        - If sku exists in bucket -> update item
        - Else append new item to bucket

        HINT:
        - Each bucket item can be a dict:
          {"sku": sku, "name": name, "quantity": quantity}
        """
        # TODO: implement
        index = self._hash(sku)
        bucket = self.table[index]

        for item in bucket:
            if item["sku"] == sku:
                item["name"] = name
                item["quantity"] = quantity
                return

        bucket.append({
            "sku": sku,
            "name": name,
            "quantity": quantity
        })

    def get_item(self, sku):
        """
        Return product dict if found, else None.

        TODO:
        - Hash sku to find bucket
        - Loop bucket and compare item["sku"]
        """
        # TODO: implement
        index = self._hash(sku)
        bucket = self.table[index]
        for item in bucket:
            if item["sku"] == sku:
                return item
        
        return None

    def remove_item(self, sku):
        """
        Remove product by sku.
        Return True if removed, False if not found.

        TODO:
        - Hash sku
        - Loop through bucket with index (enumerate)
        - Delete matching item
        """
        # TODO: implement
        index = self._hash(sku)
        bucket = self.table[index]
        for i , item in enumerate(bucket):
            if item["sku"] == sku:
                del bucket[i]
                return True
        
        return False


    def print_table(self):
        """
        Print all buckets and their contents.
        """
        print("\n=== Inventory Hash Table ===")
        # TODO: print each bucket
        # HINT:
        # for i, bucket in enumerate(self.table):
        #     print(f"Bucket {i}: {bucket}")
        for i , item in enumerate(self.table):
            print(f"Bucket {i}: {item}")



# FOR TESTING:

inv = InventoryHashTable(size=7)

# TODO: Uncomment after implementing methods
inv.set_item("A101", "USB Cable", 25)
inv.set_item("B205", "Keyboard", 12)
inv.set_item("C333", "Mouse", 18)
inv.set_item("A101", "USB Cable", 30)  # update
inv.print_table()
print("Search B205:", inv.get_item("B205"))
print("Remove C333:", inv.remove_item("C333"))
inv.print_table()