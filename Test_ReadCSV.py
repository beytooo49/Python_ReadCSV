import csv

def ReadCSV():

    # Variable
    results = []
    index = -1
    score = 0
    credit = 0

    # Open File CSV
    with open('Calculate My GPA - CSV.csv', 'r') as File: 
        reader = csv.reader(File, delimiter=',')

        # Read all row in File CSV
        for row in reader:

            # Insert Calculate GPA
            if row[1] != '':
                score += int(row[1]) * float(row[2])                    # Add Score (Score = Credit*Collect ;unless Subject completely)
                credit += int(row[1])                                   # Add Credit (unless Subject Completely) 
                results[index] = float("{0:.2f}".format(score/credit))  # Find GPA from calculate (Score divide by Credit)

            # Reset Calculate GPA
            else:
                results.append(0)   # New Count 
                score = 0           # Reset Score
                credit = 0          # Reset Credit
                index += 1          # Resert Current Index

    # Show GPA and GPAX
    print("GPA: ",results)                                      # Show Calculate GPA
    print("GPAX: {0:.2f}".format(sum(results)/len(results)))    # Show Calculate GPAX (All GPA divide by all semesters)

ReadCSV()