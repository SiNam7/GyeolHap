class Tile:
    def __init__(self):

        self.tileDict = {}  # key: tilename, value: list(figure shape, figure color, background color)

        f = open("../GUI/tile.txt", "r")
        lines = f.readlines()
        colorList = lines[0].split()
        shapeList = lines[1].split()
        bckcolorList = lines[2].split()
        f.close()

        for color in colorList:
            for shape in shapeList:
                for bckcolor in bckcolorList:
                    name = f"{color}/{shape}/{bckcolor}"
                    path = f"../image/{color}_{shape}_{bckcolor}.png"
                    self.tileDict[name] = [color, shape, bckcolor, path]


if __name__ == "__main__":
    t = Tile()
    print(t.tileDict)

