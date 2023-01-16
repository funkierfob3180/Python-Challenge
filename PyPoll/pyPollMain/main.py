import csv

file_to_load ="../pyPollResources/election_data.csv"
file_to_output= "../pyPollAnalysis/analysis.txt"


#initalizing variables
total_votes = 0 
#list of available candidates
candidate_options = []
#votes attributed to candidates
candidate_votes = {}
# winning candidats and winning vote counter
winning_candidate = ""
winning_count = 0


with open(file_to_load)as election_data:
    #open reader and access data 
    reader = csv.DictReader(election_data)
    #loop throug reader
    for row in reader:
        #add to the total vote count
        total_votes = total_votes + 1
        #extract condidate from each row
        candidate_name = row["Candidate"]
        #check if there is no candidate match
        if candidate_name not in candidate_options:
            #add candidates
            candidate_options.append(candidate_name)
            #begin tracking candidate voter count
            candidate_votes[candidate_name] = 0
        #then add a vote to that candidates count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
#text file set up
with open(file_to_output, 'w')as txt_file:
                #print the final count
        election_results = ( 
            f"\n\nElection Results\n"
            f"------------------------------------\n"
            f"Total Votes:  {total_votes}\n"
            f"------------------------------------\n"
        )

        print(election_results)

        #save vote count to file
        txt_file.write(election_results)

        #determine the winner by looping through the counts
        for candidate in candidate_votes:
            #vote percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes)/float(total_votes)* 100

            #winning count
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate
            #each candidates vote count and percentage
            voter_output = f"{candidate} : {vote_percentage: .3f}%  ({votes})\n"
                        
            print(voter_output)

            #save each candidate's count and percentage to a text file
            txt_file.write(voter_output)
        #print winning candidate
        winning_candidate_summary = (
            f"------------------------------------\n\n"
            f"Winner : {winning_candidate}\n\n"
            f"------------------------------------\n\n"
        )

        print(winning_candidate_summary)
        #save winning candidate to text file
        txt_file.write(winning_candidate_summary)




