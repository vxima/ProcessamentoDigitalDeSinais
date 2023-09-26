import scipy.io.wavfile as wavfile
import numpy as np

# Carregue o arquivo de áudio .wav
sample_rate, audio_data = wavfile.read("Q4\Audios\dg105.wav")

# Inicializar os parametros
limiar_quebra = 100
duracao_min_silencio = int(sample_rate*0.3)  
duracao_min_quebra = int(sample_rate*0.01)
idx_quebra = 0
duracao = 0
quebrado = False
momentosQuebras =[]

## Identificação dos momentos de quebra, salvando os indices de começo e fim
for idx , amplitude in enumerate(audio_data):
    if np.abs(amplitude) <= limiar_quebra and not quebrado:
        idx_quebra = idx
        quebrado = True
    else:
        if  np.abs(amplitude) > limiar_quebra and quebrado:
            duracao = idx - idx_quebra
            if duracao < duracao_min_silencio and duracao > duracao_min_quebra:
                momentosQuebras.append((idx_quebra , idx))
            quebrado = False

## Criação da mascara para o audio
mascara_audio = np.ones_like(audio_data, dtype=bool)
for inicio, fim in momentosQuebras:
    mascara_audio[inicio:fim] = False

# Aplicação da mascara para remoção dos momentos de quebra
audio_filtrado = audio_data[mascara_audio]

wavfile.write("Q4\Audios\Audio_filtrado.wav", sample_rate, audio_filtrado)







# Salve o áudio filtrado
#wavfile.write("audio_filtrado.wav", sample_rate, audio_filtrado)
