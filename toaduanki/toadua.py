import requests

def get_toadua_entry(id: str) -> dict[str, str]:
    print(id)
    query = { "action": "search", "query": ["id", id]}

    request = requests.post("https://toadua.uakci.pl/api", json=query)

    response = request.json()
    print(response)
    try:
        result = response["results"][0]
    except IndexError:
        print("no results")
        raise IndexError

    try:
        return {"id": id, "head": result["head"], "body": result["body"]}

    except KeyError:
        print("invalid word")
        raise KeyError

