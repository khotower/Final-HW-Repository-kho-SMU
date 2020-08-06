# Date: August 2020
# Description: This Python Script reads election_data.csv and prints election results
# Author: Ken Ho

import pandas as pd

DataFolder = 'DataFiles/'
FileName = 'election_data.csv'

election_df = pd.read_csv(DataFolder + FileName)


# Get Total Numbers of votes cast
TotalVotes_AllCandidates = len(election_df['Voter ID'].unique())

# Get the distinct count of votes for each candidate
election_df['Count'] = 1
votes_perCandidate = election_df[['Count', 'Candidate']].groupby('Candidate').sum().reset_index()

votes_perCandidate.rename(columns={'Count': 'VotesCount'}, inplace=True)

# Get Votes per candidate
votes_perCandidate['Pct Candidate Votes'] = round(votes_perCandidate['VotesCount']/TotalVotes_AllCandidates*100, 3)

# Winner
winner = votes_perCandidate[votes_perCandidate.VotesCount == max(votes_perCandidate.VotesCount)]['Candidate'].item()

# Print results
print('Election Results')
print('-' * 30)

print('Total Votes:' + str(TotalVotes_AllCandidates))
print('-' * 30)

for candidate in votes_perCandidate.Candidate.unique():
    print(candidate + ': '
          + str(votes_perCandidate[votes_perCandidate.Candidate == candidate]['Pct Candidate Votes'].item())
          + '%  (' +
          str(votes_perCandidate[votes_perCandidate.Candidate == candidate]['VotesCount'].item())
          + ')')

print('-' * 30)

print('Winner: ' + winner)
print('-' * 30)
