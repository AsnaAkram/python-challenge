import os
import csv

votes_cast=0
candidates_nm=[]
candidates_votes={}
percent_votes=0


# dir = os.path.dirname(__file__)
text_file=os.path.join("election_analysis.txt")

file_path = os.path.join("Resources", "election_data.csv")

with open(file_path) as file:
    data = csv.reader(file)
    col_names = next(data)

    for row in data:
        votes_cast= votes_cast+1
        if row[2] not in candidates_nm:
            candidates_nm.append(row[2])
            candidates_votes[row[2]]=0

        candidates_votes[row[2]]= candidates_votes[row[2]]+1

    for x in candidates_votes:
        percent_votes[x]= round((candidates_votes[x]/votes_cast)*100,2)    

             





print (votes_cast)
print (candidates_nm)
print (candidates_votes)
