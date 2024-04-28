from fastapi import FastAPI

app = FastAPI()

players = {
    1: {"id": 1, "name": "ShadowBlade92", "events": 0, "server": "America"},
    2: {"id": 2, "name": "MysticGamer47", "events": 0, "server": "Europe"},
    3: {"id": 3, "name": "CyberNinjaX", "events": 0, "server": "Asia"},
    4: {"id": 4, "name": "PhoenixRising78", "events": 0, "server": "America"},
    5: {"id": 5, "name": "QuantumKnight", "events": 0, "server": "Europe"},
    6: {"id": 6, "name": "CrystalVortex", "events": 0, "server": "Asia"},
    7: {"id": 7, "name": "NeonSpectre", "events": 0, "server": "America"},
    8: {"id": 8, "name": "DigitalWarlock", "events": 0, "server": "Europe"},
    9: {"id": 9, "name": "BlazeStormer", "events": 0, "server": "Asia"},
    10: {"id": 10, "name": "LunarEclipse88", "events": 0, "server": "America"}
}


#Kysely parametri /players/server=Asia

@app.get("/players")
def get_players(server: str = ""):
    if server != "":
        return [players[s] for s in players if players[s]['server'] == server]
    return [players[s] for s in players]


@app.get("/players/{id}")
def get_player(id: int):
    return players[id]  


