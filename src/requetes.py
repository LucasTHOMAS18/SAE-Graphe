import json

import networkx as nx


def format_personne(personne: str) -> str:
    if '(' not in personne:
        return personne.strip('[]')
    
    return personne[:(personne.index('(') - 1)].strip('[]')


def json_vers_nx(chemin: str) -> nx.Graph:
    G = nx.Graph()
    
    with open(file=chemin, mode='r', encoding='UTF-8') as fichier:
        for ligne in fichier.readlines():
            film = json.loads(ligne)
            personnes = set()
            
            for metier in {'cast', 'directors', 'producers'}:
                personnes |= set(map(format_personne, film.get(metier, [])))
            
            for personne1 in personnes:
                for personne2 in personnes:
                    if personne1 != personne2 and not G.has_edge(personne1, personne2):
                        G.add_edge(personne1, personne2)
                        
    return G
