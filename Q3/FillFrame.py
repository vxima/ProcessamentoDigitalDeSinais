
import numpy as np
from PIL import Image 
pathList = [
    'Q3\Frames\saida_101.bmp',
    'Q3\Frames\saida_103.bmp',
    'Q3\Frames\saida_109.bmp',
    'Q3\Frames\saida_111.bmp',
    'Q3\Frames\saida_117.bmp',
    'Q3\Frames\saida_119.bmp'
    ]

listPathFramesRecuperados = [
    "Q3\ResultsBMP\FrameRecuperado102.bmp",
    "Q3\ResultsBMP\FrameRecuperado110.bmp",
    "Q3\ResultsBMP\FrameRecuperado118.bmp"
]
def convertImage(pathF1 , pathF2):
    ## Getting previous and next frame
    prevFrame = Image.open(pathF1)
    nextFrame = Image.open(pathF2)
    ## Convert to numpy array
    im1 = np.array(prevFrame)
    im2 = np.array(nextFrame)
    
    frame1 = im1.mean(axis=2).astype(np.uint8)
    frame2 = im2.mean(axis=2).astype(np.uint8)

    return frame1, frame2

def interpolation(prevFrame , nextFrame):   
    return  np.uint8(prevFrame*0.75 + nextFrame*0.25)
    
j=0
for i in range(0, len(pathList) , 2):
    prevFrame , nextFrame = convertImage(pathList[i] , pathList[i+1])
    img = interpolation(prevFrame, nextFrame)
    img = Image.fromarray(img)
    img.save(listPathFramesRecuperados[j])
    j +=1