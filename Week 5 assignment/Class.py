# --- Assignment 1: Book and EBook Classes ---

class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
       
    def display_info(self):
        print("--- Book Info ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")
        print("------------------")

# --- Inheritance Layer: EBook ---

class EBook(Book):
    def __init__(self, title, author, genre, pages, file_format, file_size_mb):
        # Call the parent class (Book) constructor to initialize common attributes
        super().__init__(title, author, genre, pages)
        self.file_format = file_format
        self.file_size_mb = file_size_mb
        self.__download_count = 0

    # Add a new attribute for checkout count
    def check_out(self):
        self.__download_count += 1
        print(f"'{self.title}' ({self.file_format}) downloaded. Total downloads: {self.__download_count}.")


    # Override display_info to include EBook specific details
    def display_info(self):

        # Custom EBook display
        print(f"\n--- EBook Info ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages} (approx)")
        print(f"Format: {self.file_format}")
        print(f"File Size: {self.file_size_mb} MB")
        print(f"Downloads: {self.__download_count}")
        print("------------------")

# --- Example Usage ---

# Create a physical book instance
book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 310)

# Create an EBook instance
ebook1 = EBook("Pride and Prejudice", "Jane Austen", "Romance", 400, "EPUB", 1.5)

# Interact with the objects
book1.display_info()
ebook1.display_info()

print("\nDownloading the EBook:")
ebook1.check_out() # Simulate downloading the EBook
ebook1.check_out() # Simulate downloading the EBook again
ebook1.display_info()




# --- Activity 2: Polymorphism with Vehicles ---

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def move(self):
        print(f"The {self.color} car '{self.name}' is Driving 🚗 on the road!")

class Plane:
    def __init__(self, name, airline):
        self.name = name
        self.airline = airline

    def move(self):
        print(f"The {self.airline} plane '{self.name}' is Flying ✈️ in the sky!")

class Boat:
    def __init__(self, name, boat_type):
        self.name = name
        self.boat_type = boat_type # e.g., Sailboat, Speedboat

    def move(self):
        print(f"The {self.boat_type} '{self.name}' is Sailing ⛵ on the water!")



# --- Polymorphism Demonstration ---

# Create instances of different vehicle types
vehicle1 = Car("Civic", "Red")
vehicle2 = Plane("Boeing 747", "Sky High Airways")
vehicle3 = Boat("The Mariner", "Sailboat")
vehicle4 = Car("Mustang", "Black")

# Store them in a list
vehicles = [vehicle1, vehicle2, vehicle3, vehicle4]

# Iterate through the list and call the move() method on each object
print("\nInitiating movement for all vehicles:")
for motion in vehicles:
   motion.move() # <--- Polymorphism in action!    