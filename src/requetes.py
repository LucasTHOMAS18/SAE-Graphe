import json
from pathlib import Path
from time import perf_counter

import networkx as nx


def format_personne(personne: str) -> str:
    if '(' in personne:
        personne = personne[:personne.index('(')]
    
    if '|' in personne:
        personne = personne[:personne.index('|')]
    
    return personne.strip("[]").strip()


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


def collaborateurs_communs(G: nx.Graph, u: str, v: str) -> set:
    return set(G[u]) & set(G[v])


def collaborateurs_proches(G: nx.Graph, u: str, k: int) -> set:
    if u not in G.nodes:
        return set()
    
    collaborateurs = {u}
    a_traiter = {u}
    
    for _ in range(k):
        seront_traites = set()
        
        for sommet in a_traiter:
            voisins = set(G.adj[sommet])
            seront_traites |= voisins - collaborateurs
            
        collaborateurs |= seront_traites
        a_traiter = seront_traites
    
    return collaborateurs



def est_proche(G: nx.Graph, u: str, v: str, k: int = 1) -> bool:
    return v in collaborateurs_proches(G, u, k)


def distance_naive(G: nx.Graph, u: str, v: str) -> int:
    if u == v:
        return 0
    
    for k in range(1, nx.number_of_nodes(G)):
        if est_proche(G, u, v, k):
            return k
    
    return -1


def distance(G: nx.Graph, u: str, v: str):
    if u not in G or v not in G:
        return -1

    if u == v:
        return 0

    niveau = 0
    niveau_actuel = {u}
    niveau_suivant = set()

    while niveau_actuel:
        courant = niveau_actuel.pop()
        
        for voisin in G[courant]:
            if voisin not in niveau_actuel:
                if voisin == v:
                    return niveau + 1
                
                niveau_suivant.add(voisin)
                
        if not niveau_actuel:
            niveau += 1
            niveau_actuel = niveau_suivant
            niveau_suivant = set()
            
    return -1


def centralite(G, u):
    a_parcourir = [u]
    distances = {u: 0}
    distance_max = 0
    
    while a_parcourir:
        courrant = a_parcourir.pop(0)
        
        for voisin in G[courrant]:
            if voisin not in distances:
                distances[voisin] = distances[courrant] + 1
                a_parcourir.append(voisin)

                if distances[voisin] > distance_max:
                    distance_max = distances[voisin]

    return distance_max


def centre_hollywood(G: nx.Graph):
    min_centralite = float('inf')
    centre = None
    
    for u in G.nodes:
        c = centralite(G, u)
        if c < min_centralite:
            min_centralite = c
            centre = u
            
    return centre


def eloignement_max(G: nx.Graph):
    max_centralite = float('-inf')
    
    for u in G.nodes:
        c = centralite(G, u)
        if c > max_centralite:
            max_centralite = c
            
    return max_centralite


# Tests des temps d'exécution
def chrono(fonction, *args, **kwargs):
    t0 = perf_counter()
    res = fonction(*args, **kwargs)
    print(f"Temps d'exécution de {fonction.__name__}: {perf_counter() - t0}")
    return res
    

if __name__ == "__main__":
    graphe = chrono(json_vers_nx, Path(__file__).parent / "data/data.txt")
