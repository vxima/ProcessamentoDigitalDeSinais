import scipy.io.wavfile as wavfile
import numpy as np
sample_rate, audio_data = wavfile.read("Q4\Audios\Audio_filtrado.wav")

tamanho_janela = 7 # Ajustado por meio de testes

janela_hanning = np.hanning(tamanho_janela)

audio_suavizado = np.convolve(audio_data, janela_hanning/janela_hanning.sum(), mode='same')

wavfile.write("Q4\Audios\Audio_Hanning.wav", sample_rate, audio_suavizado.astype(np.int16))
