import numpy as np
import scipy as sp
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
from PIL import Image 
## Parameters
sigma1 = 1
sigma2 = 5

# Aplicar filtro gaussiano com diferente sigmas
img = Image.open("Arquivos\eight.bmp")
imgF1 = gaussian_filter(img , sigma1)
imgF2 = gaussian_filter(img , sigma2)

# Gerar diferença de gaussiana
DoG = imgF1 - imgF2


fig = plt.figure()
plt.gray()  
ax1 = fig.add_subplot(221)  
ax2 = fig.add_subplot(222)  
ax3 = fig.add_subplot(223)  
ax4 = fig.add_subplot(224)  

## Plotting

#Imagens
ax1.imshow(img)
ax2.imshow(imgF1)
ax3.imshow(imgF2)
ax4.imshow(DoG)
#Titulos
ax1.title.set_text('Raw Image')
ax2.title.set_text('G1')
ax3.title.set_text('G2')
ax4.title.set_text('DoG')
#Show
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[]);
plt.savefig("Q2\DiferencaGaussianas.png")
plt.show()

