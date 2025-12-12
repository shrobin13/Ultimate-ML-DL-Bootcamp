# `Q20`: Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record.
# Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.
#
# Show every students record in form of tuples if matches all required criteria.
#
# It is assumed that there will be only one primry skill.
#
# If no such candidate found, print `No such candidate`
#
# `Input:`
# ```
# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Mehedi
# Enter Higher Education- BSc
# Enter Primary Skill- Python
# Enter Year of Graduation- 2028
# Enter Details of student-2
# Enter Student name- Sabit
# Enter Higher Education- BSc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2028
#
# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- BSc
# Enter Year of Graduation- 2028
# ```
#
# `Output`
# ```
# ('Mehedi', 'BSc', 'Python', '2028')

student_record = []


def ui():

    no_rec = int(input("Enter no of records: "))
    print(f"Enter No of records: {no_rec}")

    for i in range(no_rec):
        print(f"Enter details of student {i}")

        name = input("Enter Student name:")
        education = input("Enter Higher Education(BSC): ")
        skill = input("Enter primary skill: ")
        grad_year = input("Enter graduation year: ")

        student_record.append((name, education, skill, grad_year))

    print("Enter Job Role Requirement- ")
    req_skill = input("Enter skill- ")
    req_edu = input("Enter Higher Education- ")
    req_grad_year = input("Enter year of graduation- ")

    req_tuple = (req_edu, req_skill, req_grad_year)

    is_found = False

    for rec in student_record:
        if (rec[1], rec[2], rec[3]) == req_tuple:
            print(rec)
            is_found = True
            break

    if not is_found:
        print("No such candidate!")


ui()
