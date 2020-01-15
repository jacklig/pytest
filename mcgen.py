import os

class mcgen:
    slLines = []

    def GenBlock(self, vParams, l, h, w):
        sBlockType = "cobblestone"
        fEmpty = False
        sFloor = ""
        sRoof = ""
        sYoffset = ""
        sFloorYoffset = ""

        if vParams != None:
            if "BlockType" in vParams: sBlockType = vParams["BlockType"]
            if "IsEmpty" in vParams: fEmpty = True
            if "Floor" in vParams: sFloor = vParams["Floor"]
            if "Roof" in vParams: sRoof = vParams["Roof"]
            if "YOffset" in vParams: sYoffset = vParams["YOffset"]

        if sYoffset != "":
            h = h + int(sYoffset)
            sFloorYoffset = str(int(sYoffset)-1)

        if sFloorYoffset == "0":
            sFloorYoffset = ""

        sLine = "fill ~1 ~" + sYoffset + " ~1 ~" + str(l+1) + " ~" + str(h) + " ~" + str(w+1) + " " + sBlockType
        self.slLines.append( sLine )

        if fEmpty == True:
            sLine = "fill ~2 ~" + sYoffset + " ~2 ~" + str(l) + " ~" + str(h) + " ~" + str(w) + " air"
            self.slLines.append( sLine )

        if sFloor != "":
            sLine = "fill ~1 ~" + sFloorYoffset + " ~1 ~" + str(l+1) + " ~-1 ~" + str(w+1) + " " + sFloor
            self.slLines.append(sLine)
        
        if sRoof != "":
            sLine = "fill ~1 ~" + str(h) + " ~1 ~" + str(l+1) + " ~" + str(h) +" ~" + str(w+1) + " " + sRoof
            self.slLines.append(sLine)


def main():
    print("main")
    mcGen = mcgen()
    mcGen.GenBlock({"Floor":"oak_planks", "Roof":"mossy_cobblestone", "IsEmpty":""}, 20, 20, 20)
    mcGen.GenBlock({"YOffset":"4", "BlockType":"glass"},1,4,4)
    appdata = os.getenv("appdata")
    path = appdata + '\\.minecraft\\saves\\desert temple\\datapacks\\test\\data\\test\\functions\\test_cube.mcfunction'
    f = open(path,'w')
    for line in mcGen.slLines:
        f.write(line + '\n')
        
    f.close()

if __name__ == "__main__":
    main()