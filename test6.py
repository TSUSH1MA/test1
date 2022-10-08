import random

def create_votes(parties, people):
    """Creates random result of voting certain ammount of people

    Args:
        - parties, people (int)
    
    Returns:
        - result of votes in list
    """
    result = []
    for h in range(people):
        vote = random.randint(0, parties)
        result.append(vote if vote > 0 else -1)
    return result

def election_results(parties, votes):
    """Returns all votes for parties in the number of voters and percentages

    Args:
        - parties, votes (int)
    
    Returns:
        - (str) table of parties with number of voters and parcentages
    """
    results = {}
    for party in range(1, parties + 1):
        results[party] = votes.count(party)
    index = 0
    for party, vote_number in sorted(results.items(), key = lambda
    item: item[1], reverse = True):
        index += 1
        print(f'{index:>2}. Party №{party:<3} | {vote_number:>8} | ',
                f'{(vote_number/len(votes)*100):>10.2f}%')

votes = create_votes(10, 1000)
election_results(10, votes)