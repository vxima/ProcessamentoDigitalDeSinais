import cv2
import numpy as np

image = cv2.imread('Arquivos\Flor_Joaninha.jpg')

# Converter imagem para grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Filtro gaussiano para detecção de bordas, visto que a parte ja borrada vai se tornar destacada para borda
blurred = cv2.GaussianBlur(gray, (19, 19), 0)

# Computar diferença absoluta entre a imagem grayscale e a com filtro gaussiano
diff = cv2.absdiff(gray, blurred)

# Threshold the difference image to create a binary mask
threshold = 10  
mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

# Achar contornos 
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

# Inicializar mascara
segmented_mask = np.zeros_like(image)

# Criação da mascara para segmentação, desenhando os contornos da imagem
for contour in contours:
    cv2.drawContours(segmented_mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

# Extrair parte segmentada da imagem utilizando a mascara
segmented_image = cv2.bitwise_and(image, segmented_mask)
cv2.imwrite('Q2\ResultSegmentation.jpg', segmented_image)
