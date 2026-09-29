
import sys


def get_valid_scores() -> list[int]:
    scores: list[int] = []
    indice: int = 0
    for n in sys.argv:
        if indice == 0:
            indice += 1
            continue
        try:
            scores.append(int(n))
        except ValueError:
            print(f"Invalid parameter: \'{n}\'")
    return scores


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = get_valid_scores()
    if len(scores) != 0:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", sum(scores)/len(scores))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
