'''
Name: Jonathon Carr
Class: CS 1400-005
Due Date: 5/5/21
Project: Was Clinton Right?

In this project I have to qualify or disqualify one of Bill Clinton's statements on the amount of jobs created by
republicans and democrats from 1961 to 2012.

Instructions:
1. Use command prompt to run this program
2. When passing in arguments, pass in main.py BLS_private.csv and presidents.txt specifically in that order.
'''

import sys

'''
The get_jobs function creates and returns a dictionary filled with the job statistics given in the bls_private.csv file.
This dictionary is used as an input for the calculate_presidents function.
'''
def get_jobs(filename):
    # open bls_private.csv
    file1 = open(filename, "r")

    line_count = 0
    jobs = {}
    # make an array of bls_private.csv contents
    for line in file1:
        line_count += 1
        if line_count > 13:
            job_array = line.split(",")
            # specified file conditions to make sure the file has all 12 months plus year of job data
            if len(job_array) == 13:
                # add array to dictionary
                jobs[job_array[0]] = job_array
            else:
                print("Invalid File input.")
                print(f"Error in {filename}.")
                print("Data missing or incorrect data added.")
                exit()
    file1.close()
    return jobs

'''
The calculate_presidents function make an array out of presidents.txt and uses it to print the name of each president,
their political party, how many jobs existed at the beginning and end of their administration, and how many jobs they
produced.
This function also tallies the total jobs produced and the partisan totals.
'''
def calculate_presidents(filename, jobs_dict):
    # open presidents.txt
    file2 = open(filename, "r")

    democrat = 0
    republican = 0

    # make an array with the file contents
    count = 0
    for line in file2:
        count += 1
        # make an array and use the elements to make variables
        president = line.split("\t")

        if count > 1:
            starting_year = president[2]
            starting_month = int(president[3])
            ending_year = president[4]
            ending_month = int(president[5])
            starting_jobs = int(jobs_dict[starting_year][starting_month])
            ending_jobs = int(jobs_dict[ending_year][ending_month])
            jobs_gained = ending_jobs - starting_jobs

            # print stats for each presidency
            print(f"Name: {president[1]} \nParty: {president[0]}")
            print(f"     Staring Jobs: {starting_jobs}")
            print(f"     Ending Jobs: {ending_jobs}")
            print(f"     Jobs Gained: {jobs_gained}")

            # calculate partisan job totals
            if president[0] == "Republican":
                republican += jobs_gained
            else:
                democrat += jobs_gained

            total_jobs = republican + democrat

    # final print statements
    print(f"Total Jobs Gained: {total_jobs}")
    print(f"Republican jobs gained: {republican}")
    print(f"Democrat jobs gained: {democrat}")
    if republican > democrat:
        print("CONCLUSION: The numbers have proven that Bill Clinton's statement was false.")
    else:
        print("CONCLUSION: The numbers have proven that Bill Clinton's statement was true based on the given information.")
        pass
    print("Just because the numbers add up as Clinton said doesn't mean that democratic administrations\ncan take all"
          " the credit for creating those jobs. Although the numbers were correct they give\nlittle insight into what a"
          " democratic administration actually does to create jobs.")
    # print(f"Percent Republican: {int(100 * (republican/ total_jobs))}%")
    # print(f"Percent Democrat: {int(100 * (democrat/ total_jobs))}%")

    file2.close()

'''
This function will run the program and take the command line parameters.
'''
def main(argv):
    # print(argv[0])
    # print(argv[1])
    # print(argv[2])
    # exit()
    if argv[1] != "BLS_private.csv":
        print("Enter BLS_private.csv file as first argument.")
        exit()
    else:
        pass
    if argv[2] != "presidents.txt":
        print("Enter presidents.txt as second argument.")
        exit()
    else:
        pass

    # make the get_jobs dictionary a variable
    jobs = get_jobs(argv[1])

    # use the jobs dictionary as input for calculate_president
    calculate_presidents(argv[2], jobs)

if __name__ == "__main__":
    main(sys.argv)

