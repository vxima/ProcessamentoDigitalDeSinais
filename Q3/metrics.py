import numpy as np
import skimage.io
from skimage.metrics import mean_squared_error as mse
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
# Carregue as imagens que você deseja comparar
perdido1 = skimage.io.imread('Arquivos\Frames_perdidos\saida_102_2.bmp').mean(axis=2).astype(np.uint8)
recuperado1 = skimage.io.imread('Q3\ResultsBMP\FrameRecuperado102.bmp')
perdido2 = skimage.io.imread('Arquivos\Frames_perdidos\saida_110_2.bmp').mean(axis=2).astype(np.uint8)
recuperado2 = skimage.io.imread('Q3\ResultsBMP\FrameRecuperado110.bmp')
perdido3 = skimage.io.imread('Arquivos\Frames_perdidos\saida_118_2.bmp').mean(axis=2).astype(np.uint8)
recuperado3 = skimage.io.imread('Q3\ResultsBMP\FrameRecuperado118.bmp')

# Calcular metricas
def evaluation(target , pred):
    mse_value = mse(target, pred)
    psnr_value = psnr(target, pred)
    ssim_index = ssim(target, pred, multichannel=True)  # multichannel=True para imagens coloridas

    print(f"MSE: {mse_value}")
    print(f"SSIM: {ssim_index}")
    print(f"PSNR: {psnr_value}")

def printMetrics():
    print("###########################\n")
    print("         Frame102          ")
    evaluation(perdido1, recuperado1)
    print("###########################\n")
    print("         Frame110          ")
    evaluation(perdido2, recuperado2)   
    print("###########################\n")
    print("         Frame118          ")
    evaluation(perdido3, recuperado3)
    print("###########################")

if __name__ == "__main__":
    printMetrics()