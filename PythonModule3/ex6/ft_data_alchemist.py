
import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print("")

    players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                          'Gregory', 'john', 'kevin', 'Liam']
    print("Initial list of players:", players)

    capitalized_players: list[str] = [player.capitalize() for player in
                                      players]
    print("New list with all names capitalized:", capitalized_players)

    just_capitalized: list[str] = [player for player in players if player ==
                                   player.capitalize()]
    print("New list of capitalized names only:", just_capitalized)
    print("")

    score_dict: dict[str, int] = {player: random.randint(0, 1000) for player
                                  in capitalized_players}
    print("Score dict:", score_dict)

    score_average: float = sum(score_dict.values()) / len(players)
    print("Score average is", round(score_average, 1))

    high_score: dict[str, int] = {player: random.randint(int(score_average),
                                  1000) for player in capitalized_players}
    print("High scores:", high_score)
