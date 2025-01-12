# An employee gets elevated to the exclusive board member position only if they bag at least n / 3 votes, with n being the total number of votes. 
# Your task: find out the ID of this popular employee. If no one hits the vote mark, return -1. 
# If multiple employees received at least n / 3 votes, return any of them!

# The votes are delivered to you in list format. As an illustration, [1, 2, 3, 3, 3] means employees 1 and 2 voted for themselves, and employee 3 received three votes. 
# Hang tight-there can be edge cases, such as no votes or everybody voting for themselves

def elect_board_member(votes):
    count_member = {}
    
    for v in votes:
        count_member[v] = count_member.get(v, 0) + 1
        if count_member[v] > len(votes) / 3:
            return v
    return -1

print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1
