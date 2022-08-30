
# add our dependencies
import csv
import os


# The data we need to retrieve.

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize the vote counter
total_votes = 0

#candidate options
candidate_options = []

#create a voter count for each candidate
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    #to do: read and analyze the data here
      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV File
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match an existing candidate
        if candidate_name not in candidate_options:
          #add the candidate name to the candidate list.
          candidate_options.append(candidate_name)

          #begin tracking the candidate's vote count
          candidate_votes[candidate_name] = 0

          #add a vote to that candidate's count
          candidate_votes[candidate_name] =+ 1

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#iterate through the candidate's list
for candidate_name in candidate_votes:
  #retrieve the vote count of a candidate
  votes = candidate_votes[candidate_name]
  #calculate the percentage of votes
  vote_percentage = round((float(votes) / float(total_votes) * 100), 1)
  #print the candudate name and percentage of votes
  print(f"{candidate_name}: received {vote_percentage}% of the vote")

  #determine winning vote and candidate
  if (votes > winning_count) and (vote_percentage > winning_percentage):
    #if true set winning count = votes and winning percent = vote_percentage
    winning_count = votes
    winning_percentage = vote_percentage
    #set the winning candidate equal to the candidate's name
    winning_candidate = candidate_name

# print the total votes
print(f" The total number of votes is {total_votes}.")

#print out the winning candidate, vote count, and percentage to terminal
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winnning_candidate_summary = (
  f"-----------------------\n"
  f"Winner: {winning_candidate}\n"
  f"Winning Vote Count: {winning_count:,}\n"
  f"Winning Percentage: {winning_percentage:.1f}%\n"
  f"------------------------\n"
)

print(winnning_candidate_summary)

