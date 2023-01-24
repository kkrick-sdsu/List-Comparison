# Summary: Compares two lists to find elements unique to each, those that intersect and the union of all elements
import csv

# Attempts to read in the filepath. Assumes that the file is a CSV with ',' as the separator.
# If successful, returns an array of objects, one for each of the rows (excluding headers).
# Otherwise returns an empty string
def read_file(filepath):
    try:
        file = open(filepath)
        file_contents = []
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            file_contents.append(row)

        return file_contents
    except:
        return ""

# Given a file and a column name returns a list of that column's rows
def column_to_list(file_contents, column):
    column_list = []
    for row in file_contents:
        column_list.append(row[column])
    return column_list

# Get filepath and column names for each list of elements
def get_input():
    input_dict = {}
    operations = {"unique", "intersection", "union"}

    input_dict["operations"] = input(f"Valid operations are: {operations}. Enter which operation(s) to perform (separating multiple operations with a comma): ").split(",")

    input_dict["list_one_filepath"] = input("Enter path to file for list one elements: ")
    input_dict["list_one_column"] = input("Enter column name for list one elements: ")

    input_dict["list_two_filepath"] = input("Enter path to file for list two elements: ")
    input_dict["list_two_column"] = input("Enter column name for list two elements: ")
    
    return input_dict

# Find unique elements in list one that are not in list two and vice versa
def unique_elements(list_one, list_two):
    list_one_unique_elements = []
    list_two_unique_elements = []
    unique_elements_dict = {}

    for item in list_one:
        if item not in list_two:
            if item not in list_one_unique_elements:
                list_one_unique_elements.append(item)

    # Find unique elements in list two that are not in list one
    for item in list_two:
        if item not in list_one:
            if item not in list_two_unique_elements:
                list_two_unique_elements.append(item)

    unique_elements_dict["list_one"] = list_one_unique_elements
    unique_elements_dict["list_two"] = list_two_unique_elements

    return unique_elements_dict

# Find elements that intersect both lists
def intersection_elements(list_one, list_two):
    list_elements_intersection = []
    for item in list_one:
        if item in list_two:
            if item not in list_elements_intersection:
                list_elements_intersection.append(item)

    for item in list_two:
        if item in list_one:
            if item not in list_elements_intersection:
                list_elements_intersection.append(item)

    return list_elements_intersection

# Create the union of unique elements between both lists
def union_elements(list_one, list_two):
    list_elements_union = []
    for item in list_one:
        if item not in list_elements_union:
            list_elements_union.append(item)

    for item in list_two:
        if item not in list_elements_union:
            list_elements_union.append(item)
    
    return list_elements_union

def output_elements(element_list, column_name, output_filepath):
    with open(output_filepath, 'w', newline='') as csv_output_file:
        csv_writer = csv.writer(csv_output_file)
        csv_writer.writerow(column_name)
        csv_writer.writerows(element_list)

def list_comparison():
    input = get_input()

    operations = input["operations"]

    list_one_filepath = input["list_one_filepath"]
    list_two_filepath = input["list_two_filepath"]

    list_one_column = input["list_one_column"]
    list_two_column = input["list_two_column"]

    list_one_file_contents = read_file(list_one_filepath)
    list_two_file_contents = read_file(list_two_filepath)

    list_one = column_to_list(list_one_file_contents, list_one_column)
    list_two = column_to_list(list_two_file_contents, list_two_column)

    if "unique" in operations:
        unique_elements_dict = unique_elements(list_one, list_two)
        list_one_unique_elements = unique_elements_dict["list_one"]
        list_two_unique_elements = unique_elements_dict["list_two"]

        output_elements(list_one_unique_elements, "list_one_unique_elements", "./list_one_unique_elements.csv")
        output_elements(list_two_unique_elements, "list_two_unique_elements", "./list_two_unique_elements.csv")
    
    if "intersection" in operations:
        list_elements_intersection = intersection_elements(list_one, list_two)
        output_elements(list_elements_intersection, "list_elements_intersection", ".list_elements_intersection.csv")
    
    if "union" in operations:
        list_elements_union = union_elements(list_one, list_two)
        output_elements(list_elements_union, "list_elements_union", "./list_elements_union.csv")

list_comparison()