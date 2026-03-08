# CHAPTER 6 EXERCISE 1
'''
Student Grade Lookup (Dictionary) Exercise

A teacher wants a quick way to store and look up student grades.

Create a program that:
- Stores student names and grades in a dictionary
- Lets the user choose from multiple actions:
    add/update a grade
    search a student’s grade
    print all students and grades
    loop until they select 0 (zero)

- If the student is not found, print a message

Example data
"Anna": 5
"Mikko": 4
"Sara": 3

'''

# Hint! Use a dictionary and while loop for example!

student = {}

def student_Add(name, grade):
    """Add a new student to the database"""
    student[name] = grade

def add_students():
    """Function to add multiple students"""
    print("Enter first student Name then their grade")
    while True:
        student_name = input("Enter the student name (or 0 to exit): ")
        if student_name == "0":
            break
        else:
            student_grade = input("Enter student grade: ")
            try:
                student_grade = int(student_grade)
                student_Add(student_name, student_grade)
                print(f"Student {student_name} added successfully!")
            except ValueError:
                print("Please enter student grade as an integer")

def student_Look_Up():
    """Look up a student's grade"""
    while True:
        student_Name = input("Enter the student Name to check their grade (or 0 to exit): ")
        if student_Name == "0":
            break
        else:
            if student_Name in student:
                print(f"Grade of {student_Name} is {student[student_Name]}")
            else:
                print(f"Student with name {student_Name} not found in the database")

def student_dict_update():
    """Update an existing student's grade"""
    while True:
        student_name = input("Enter the student name to update their grade (or 0 to exit): ")
        if student_name == "0":
            break
        else:
            if student_name in student:
                try:
                    student_New_Grade = int(input("Enter the student new grade: "))
                    student[student_name] = student_New_Grade
                    print(f"Grade for {student_name} updated successfully!")
                except ValueError:
                    print("Student Grade must be an integer")
            else:
                print(f"Student with name {student_name} not found in the database")


add_students()
    
print("\nCurrent Student Database:")
print(student)
    

print("\n--- Student Look Up ---")
student_Look_Up()
    

print("\n--- Update Student Grades ---")
student_dict_update()
    

print("\nUpdated Student Database:")
print(student)

# this is a comment

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

# this is a exercise

# CHAPTER 6 EXERCISE 3
'''
URL Shortener Simulator Exercise

Create a mini URL shortener like a simplified TinyURL.

Requirements

- A long URL should get a short code (for example: "a1b2c3")
- If the same URL is shortened again, return the same code
- If a collision happens (same code for different URL), resolve it
- Be able to:
    - shorten a URL
    - retrieve the original URL from a short code
    - track how many times a short code was used

Hint!
Use hashlib (built-in Python module)
Store:
    code -> url
    url -> code
    code -> click_count

'''


# Here's a base where you can start! Implement the TODO's

import hashlib

class URLShortener:
    """
    Mini URL shortener.

    Store:
    - code_to_url   : short_code -> long_url
    - url_to_code   : long_url -> short_code
    - click_counts  : short_code -> int

    Collision rule:
    - If generated code already exists for another URL,
      generate a new one using an extra value (counter).
    """

    def __init__(self):
        # TODO: initialize dictionaries
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        """
        Create a short code using hashing.

        HINT 1 (recommended):
            import hashlib
            digest = hashlib.md5((url + extra).encode()).hexdigest()
            return digest[:6]

        HINT 2 (simpler beginner option):
            Use Python's built-in hash(), but note:
            hash() values can differ between runs.
        """
        # TODO: implement code generation
        digest = hashlib.md5((url + extra).encode()).hexdigest()

        return digest[:6]

    def shorten(self, url):
        """
        Return a short code for the URL.

        Rules:
        - If URL already shortened, return existing code
        - Otherwise generate code
        - Resolve collisions if code belongs to a different URL
        - Save mappings + click count = 0
        """
        # TODO: implement
        if url in self.url_to_code:
            return self.url_to_code[url]
        else:
            code = self._make_code(url)
            counter = 0
            while True:
                if code not in self.code_to_url:
                    break
                elif code in self.code_to_url and self.code_to_url[code] == url:
                    break
                else:
                    counter += 1
                    code = self._make_code(url,str(counter))
                    

            self.url_to_code[url] =  code
            self.code_to_url[code] = url
            self.click_counts[code] = 0
            return code

    def open_url(self, code):
        """
        Return original URL and increase click count.
        Return None if code not found.
        """
        # TODO: implement
        if code in self.code_to_url:
            url = self.code_to_url[code]
            self.click_counts[code] +=1
            return url
        else:
            return None

    def get_stats(self, code):
        """
        Return a dictionary with:
        { "code": ..., "url": ..., "clicks": ... }

        Return None if code not found.
        """
        # TODO: implement
        if code in self.code_to_url:
            return {"code" : code , "url" : self.code_to_url[code] ,"clicks" : self.click_counts[code]}
        else:
            return None




# FOR TESTING:

shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"  # same as url1

# TODO: Uncomment after implementing methods
code1 = shortener.shorten(url1)
code2 = shortener.shorten(url2)
code3 = shortener.shorten(url3)
print("Codes:", code1, code2, code3)  # code1 and code3 should match
print("Open code1:", shortener.open_url(code1))
print("Open code1 again:", shortener.open_url(code1))
print("Stats code1:", shortener.get_stats(code1))
#this is a comment
