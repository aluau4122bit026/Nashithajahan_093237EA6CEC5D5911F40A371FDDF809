'''
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
'''

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

"""
Write a function called linear_search_product that takes the list of products and a target product
name as input. The function should perform a linear search to find the target product in the list and
return a list of indices of all occurrences of the product if found, or an empty list if the product is not
found.
"""


def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)