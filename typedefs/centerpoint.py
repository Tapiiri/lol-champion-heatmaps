from typing import NewType, TypedDict

GameID = NewType("GameID", int)
TeamID = NewType("TeamID", int)
ClassID = NewType("ClassID", int)
Timestamp = NewType("Timestamp", float)
X_Coordinate = NewType("X_Coordinate", float)
Y_Coordinate = NewType("Y_Coordinate", float)
Health = NewType("Health", float)

CenterpointOld = NewType("Centerpoint", dict["point": (X_Coordinate, Y_Coordinate), "timestamp": Timestamp, "health": Health, "gameid": GameID, "classid": ClassID, "teamid": TeamID])

class Centerpoint(TypedDict):
    point: tuple[X_Coordinate, Y_Coordinate]
    timestamp: Timestamp
    health: Health
    gameid: GameID
    classid: ClassID
    teamid: TeamID