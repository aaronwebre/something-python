def num_teachers(teachers):
    num = len(teachers)
    return num

def num_courses(courses):
    total = 0
    for num in courses:
        total += len(courses[num])
    return total  

def courses(courses):
    all_values = []
    for course in courses.values():
        all_values.extend(course)
    return all_values

def most_courses(dictionary):
    num = 0
    for name, courses in dictionary.items():
        if len(courses) > num:
            num = len(courses)
            teacher = name
    return teacher

def stats(dictionary):
    stat_list = []
    for name, courses in dictionary.items():
        stat_list.append([name, len(courses)])
    return stat_list
