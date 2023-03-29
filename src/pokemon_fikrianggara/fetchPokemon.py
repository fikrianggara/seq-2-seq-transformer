import requests

def getFirstNPokemon(n):
    url = 'https://pokeapi.co/api/v2/pokemon?offset=20&limit='+str(n)
    r = requests.get(url)
    return r.json()