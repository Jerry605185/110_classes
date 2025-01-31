# Authors : Jerry Chen
# Emails : yanzhechen@umass.edu
# Spire IDs : 34835664
import csv,os
os.chdir("C:/Users/20487/Desktop/python/HW5_Starter_Code")
def read_csv(fname):
    student_data = []
    try:
        with open(fname,"r") as file:
            for lines in file.readlines():
                values = lines.strip().split(",")
                if not values:
                    return None
                name = values[0]
                section = values[1]
                scores = list(map(float,values[2:12]))
                average = round(sum(scores)/len(scores),3)
                student = {
                    "name" : name,
                    "section" : section,
                    "scores" : scores,
                    "average" : average
                }
                student_data.append(student)
        return student_data
    except Exception:
        print(f"Error occurred when opening {fname} to read")
        return None
def write_csv(fname,student_data):
    try:
        file = open(fname,"w")
        writer = csv.writer(file)
        for student in student_data:
            row = [student["name"],student["section"]] + student["scores"]
            writer.writerow(row)
    except Exception:
        print(f"Error occurred when opening {fname} to write")
        return None
def filter_section(student_data,section_name):
    return [student for student in student_data if section_name == student["section"]]
def filter_average(student_data,min_inc,max_exc):
    return [student for student in student_data if min_inc <= student["average"] < max_exc]
def split_section(fname):
    student_data = read_csv(fname)
    
    if student_data is None:
        return None

    unique_sections = {student['section'] for student in student_data}

    base_name = os.path.splitext(fname)[0]

    for section_name in unique_sections:
        section_data = filter_section(student_data, section_name)
        output_fname = f"{base_name}_section_{section_name}.csv"
        write_csv(output_fname, section_data)
def get_stats(nums):
    mean = sum(nums) / len(nums)
    minimum = min(nums)
    maximum = max(nums)
    range = (maximum) - (minimum)
    std_dev = (sum((n - mean) ** 2 for n in nums) / len(nums)) ** 0.5
    return {
        'mean': mean,
        'std_dev': std_dev,
        'min': minimum,
        'max': maximum,
        'range': range
    }
def get_assignment_stats(student_data):
    return_list = []
    averages = [student["average"] for student in student_data]
    return_list.append(get_stats(averages))
    for i in range(10):
        scores = [student["scores"][i] for student in student_data]
        return_list.append(get_stats(scores))
    return return_list

