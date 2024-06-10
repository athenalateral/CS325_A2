# Dataclass

from dataclasses import dataclass
 
# A class for holding an employees content
@dataclass
class book:
 
    # Attributes Declaration
    # using Type Hints
    name: str
    author: str
    year: int
    description: str
 
 
book1 = employee("Paradise Lost", "John Milton", 1667, 'Poetry on the fall of man')
book2 = employee("Moby Dick", "Herman Melville", 1851, 'Captain Ahab is deteremined to hunt a whale')
book3 = employee("All Quiet on the Western Front", "Erich Maria Remarque", 1929, 'Anti-war story set in WWI Germany')
 
print("Books on the shelf are :")
print(book1)
print(book2)
print(book3)
 
# printing new line
print()
 
# referring two object to check equality
print("Data in book1 and book2 are same? ", emp1 == emp2)
print("Data in book1 and book3 are same? ", emp1 == emp3)
