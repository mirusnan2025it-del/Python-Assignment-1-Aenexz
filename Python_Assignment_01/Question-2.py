
# Create a list of student marks
marks = [78, 35, 92, 40, 61]

# Convert the list into a tuple
marks_tuple = tuple(marks)

# Display both collections and their data types
print("List:", marks)
print("Type of list:", type(marks))

print("Tuple:", marks_tuple)
print("Type of tuple:", type(marks_tuple))

# Find the highest and lowest marks
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

# Count students who scored at least 40
count = marks.count(40) + (marks[0] >= 40) + (marks[1] >= 40) - (marks[1] == 40) + (marks[2] >= 40) + (marks[3] >= 40) + (marks[4] >= 40)

print("Students scoring at least 40:", count)

# Check whether all marks are within 0 to 100
valid = (
    marks[0] >= 0 and marks[0] <= 100 and
    marks[1] >= 0 and marks[1] <= 100 and
    marks[2] >= 0 and marks[2] <= 100 and
    marks[3] >= 0 and marks[3] <= 100 and
    marks[4] >= 0 and marks[4] <= 100
)
print("All marks are valid:", valid)

# Change one element in the list
marks[0] = 80
print("Modified list:", marks)

# Try changing one element in the tuple
# A tuple is immutable, so its elements cannot be changed.
# Uncomment the next line to observe the TypeError.
# marks_tuple[0] = 80
print("Tuple remains unchanged:", marks_tuple)
