def create_candidates():
    candidates = {}
    num_candidates = int(input("Enter the number of candidates: "))
    for i in range(num_candidates):
        candidate_name = input(f"Enter the name of candidate {i+1}: ")
        candidates[candidate_name] = 0
    return candidates

def vote(candidates):
    print("Please vote for a candidate:")
    for candidate in candidates:
        print(f"- {candidate}")
    candidate_name = input("Enter the name of the candidate: ")
    if candidate_name in candidates:
        candidates[candidate_name] += 1
        print("Thank you for voting!")
    else:
        print("Invalid candidate. Please try again.")

def display_results(candidates):
    print("Voting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

def do_vote():
    candidates = create_candidates()
    while True:
        print("\n1. Vote\n2. Display Results\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            vote(candidates)
        elif choice == '2':
            display_results(candidates)
        elif choice == '3':
            print("Thank you for participating in the voting!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    do_vote()
