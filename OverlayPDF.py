
path1 = "/Users/traviskochel/Desktop/temp/Kablammo-8-21-d.pdf"
path2 = "/Users/traviskochel/Desktop/temp/Kablammo-8-24-b.pdf"

exportPath = "/Users/traviskochel/Desktop/temp/Kablammo-8-21-8-24.pdf"

# rgba
color1 = (1,0,0,1) 
color2 = (0,0,1,1)

# PDF exports in raster, so raise this if it's too pixellated. Lower for quicker export times.
pdfScale = 2


pageCount = numberOfPages(path1)

def buildLayer(path, color, pageNumber):
    img = ImageObject()

    with img:
        w, h = imageSize(path)
        size(w*pdfScale, h*pdfScale)
        scale(pdfScale)
        image(path, (0, 0), pageNumber=pageNumber)
        
    img.falseColor(color0=color)

    return img

def main():
    for pageNumber in range(1, pageCount+1):
    #for pageNumber in range(1, 3):
        w, h = imageSize(path1, pageNumber=pageNumber)
        np = newPage(w*pdfScale, h*pdfScale)
        
        layer1 = buildLayer(path1, color1, pageNumber)
        layer2 = buildLayer(path2, color2, pageNumber)
        
        layer1.multiplyBlendMode(backgroundImage=layer2)
        
        image(layer1, (0, 0))
        
    saveImage(exportPath)

main()