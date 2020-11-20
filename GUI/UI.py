import time

playersName = ["Player1", "Player2"]

playersKind = ["Name", "Score"]

imagePathList = ["../image/Blue_Circle_White.png", "../image/Blue_Circle_Black.png", "../image/Blue_Circle_Gray.png",
                 "../image/Blue_Square_White.png", "../image/Blue_Square_Black.png", "../image/Blue_Square_Gray.png",
                 "../image/Blue_Triangle_White.png", "../image/Blue_Triangle_Black.png", "../image/Blue_Triangle_Gray.png",
                 "../image/Green_Circle_White.png", "../image/Green_Circle_Black.png", "../image/Green_Circle_Gray.png",
                 "../image/Green_Square_White.png", "../image/Green_Square_Black.png", "../image/Green_Square_Gray.png",
                 "../image/Green_Triangle_White.png", "../image/Green_Triangle_Black.png", "../image/Green_Triangle_Gray.png",
                 "../image/Yellow_Circle_White.png", "../image/Yellow_Circle_Black.png", "../image/Yellow_Circle_Gray.png",
                 "../image/Yellow_Square_White.png", "../image/Yellow_Square_Black.png", "../image/Yellow_Square_Gray.png",
                 "../image/Yellow_Triangle_White.png", "../image/Yellow_Triangle_Black.png", "../image/Yellow_Triangle_Gray.png"]

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
