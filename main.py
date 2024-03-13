import requests


def lister_parties(idul, secret):

    BASE_URL = 'https://pax.ulaval.ca/quixo/api/h24/'
    rep = requests.get(BASE_URL+'parties', auth=("idul", "secret")) # idul secret ?

    if rep.status_code == 200:
        rep = rep.json()
        return(rep)
    
    elif rep.status_code == 401:
        message1 = rep.json().get('message', 'Le proggrame a butté sur un problème de permission')
        raise PermissionError(message1)

    elif rep.status_code == 406:
        message1 = rep.json().get('message', 'Le proggrame a butté sur un problème de nature inconnu')
        raise RuntimeError(message1)

    else:
        raise ConnectionError() # paranthese vide?

