# Define a function to calculate the area of a square
def area(side_length):
    square_area = side_length ** 2
    return square_area

# Take the side length as input from the user
side_length = float(input("Enter the side length of the square: "))

# Calculate the area using the area() function
result = area(side_length)

# Display the result
print("The area of the square is:", result)
