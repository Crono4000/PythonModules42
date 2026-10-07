
import random


achievements: list[str] = ['Crafting Genius', 'Strategist', 'World Savior',
                           'Speed Runner', 'Survivor', 'Master Explorer',
                           'Treasure Hunter', 'Unstoppable', 'First Steps',
                           'Collector Supreme', 'Untouchable', 'Sharp Mind',
                           'Boss Slayer']


def gen_player_achievements() -> set[str]:
    random_size: int = random.randint(0, len(achievements))
    return set(random.sample(achievements, random_size))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    all: set[str] = set(achievements)
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print("")
    print("All distinct achievements:", all)
    print("")
    print("Common achievements:", alice.intersection(bob, charlie, dylan))
    print("")
    print("Only Alice has:", alice.difference(bob, charlie, dylan))
    print("Only Bob has:", bob.difference(charlie, dylan, alice))
    print("Only Charlie has:", charlie.difference(bob, alice, dylan))
    print("Only Dylan has:", dylan.difference(bob, charlie, alice))
    print("")
    print("Alice is missing:", all.difference(alice))
    print("Bob is missing:", all.difference(bob))
    print("Charlie is missing:", all.difference(charlie))
    print("Dylan is missing:", all.difference(dylan))
