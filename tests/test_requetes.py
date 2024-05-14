from src.requetes import *


def test_format_personne():
    assert format_personne("[[Michael Raymond-James]]") == "Michael Raymond-James"
    assert format_personne("[[Jack Shea (director)|Jack Shea]]") == "Jack Shea"
    assert format_personne("[[Glenn Beck (actor)|Glenn Beck]]") == "Glenn Beck"
    assert format_personne("[[Antonino Faà di Bruno|Antonino Faa Di Bruno]]") == "Antonino Faà di Bruno"
    assert format_personne("Dennis Cleveland Stewart|Dennis Stewart") == "Dennis Cleveland Stewart"
    assert format_personne("[[John C. Reilly]]") == "John C. Reilly"
