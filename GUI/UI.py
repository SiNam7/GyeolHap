import time

playersName = ["Player1", "Player2"]

playersKind = ["Name", "Score"]

functionList = ["Gyeol", "Hap", "del", "clear"]

roundList = ["Round" + " " + str(i) for i in range(1, 10)]


class Tile:
    def __init__(self):

        self.tileDict = {}  # key: tilename, value: list(figure shape, figure color, background color)

        f = open("tile.txt", "r")
        lines = f.readlines()
        shapeList = lines[0].split()
        colorList = lines[1].split()
        bckcolorList = lines[2].split()
        f.close()

        for shape in shapeList:
            for color in colorList:
                for bckcolor in bckcolorList:
                    name = f"{color}/{shape}/{bckcolor}"
                    path = f"../image/{color}_{shape}_{bckcolor}.png"
                    self.tileDict[name] = [color, shape, bckcolor, path]


if __name__ == "__main__":
    t = Tile()
    print(t.tileDict)
