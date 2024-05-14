from src.requetes import *


def test_format_personne():
    assert format_personne("[[Michael Raymond-James]]") == "Michael Raymond-James"
    assert format_personne("[[Jack Shea (director)|Jack Shea]]") == "Jack Shea"
    assert format_personne("[[Glenn Beck (actor)|Glenn Beck]]") == "Glenn Beck"
