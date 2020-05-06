import json


def parse_feelings(snapshot):
    snapshot = json.loads(snapshot)
    return dict(
        hunger=snapshot["feelings_hunger"],
        thirst=snapshot["feelings_thirst"],
        exhaustion=snapshot["feelings_exhaustion"],
        happiness=snapshot["feelings_happiness"],
        timestamp=snapshot["datetime"])


parse_feelings.scheme = "feelings"
