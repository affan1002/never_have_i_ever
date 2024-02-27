import random

def never_have_i_ever(players):
    print("Welcome to Never Have I Ever!")
    print("Each player takes turns saying something they've never done.")
    print("If any other player has done it, they need to take a sip of their drink.")
    print("The game continues until everyone's secrets are revealed!")

    # Initialize a dictionary to track each player's answers
    player_answers = {player: [] for player in players}

    while True:
        for player in players:
            input(f"\n{player}, it's your turn. Press Enter to continue...")

            # Prompt the player for their "Never have I ever" statement
            statement = input("Say something you've never done: ").strip()

            # Check if any other player has done the given statement
            other_players = [p for p in players if p != player]
            random_player = random.choice(other_players)
            print(f"{random_player}! Have you ever {statement}?")

            # Check if the other player has done the statement
            answer = input("Type 'yes' if you have, otherwise press Enter: ").strip().lower()

            # If the other player has done the statement, they take a sip
            if answer == "yes":
                print(f"{random_player} takes a sip!")
                player_answers[random_player].append(statement)

            # If all players have revealed their secrets, end the game
            if all(len(player_answers[player]) == len(players) - 1 for player in players):
                print("\nAll secrets are revealed! Game over!")
                return

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter player {i+1}'s name: ") for i in range(num_players)]
    never_have_i_ever(players)
