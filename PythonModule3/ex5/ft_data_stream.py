
import typing
import random


players: list[str] = ["alice", "bob", "charlie", "dylan"]
actions: list[str] = ["run", "eat", "sleep", "grab", "move", "climb",
                      "swim", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        pos_random: int = random.randint(0, len(events) - 1)
        yield events.pop(pos_random)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_generator: typing.Generator[tuple[str, str],
                                      None, None] = gen_event()
    for t in range(1000):
        event: tuple[str, str] = next(event_generator)
        print(f"Event {t}: Player {event[0]} did action {event[1]}")

    list_events: list[tuple[str, str]] = []
    for wow in range(10):
        list_events.append(next(event_generator))
    consumer: typing.Generator[
        tuple[str, str], None, None] = consume_event(list_events)
    consumed: tuple[str, str] = next(consumer)
    while consumed:
        print("Got event from list:", consumed)
        print("Remains in list:", list_events)
    