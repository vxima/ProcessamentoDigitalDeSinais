import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

# Carregue o arquivo de áudio .wav
sample_rate, audio_data = wavfile.read("Q4\Audios\Audio_suavizado_hanning.wav")

# Calcule o eixo do tempo
tempo = np.arange(0, len(audio_data)) / sample_rate

# Plot no domínio do tempo
plt.figure(figsize=(12, 4))
plt.subplot(2, 1, 1)
plt.plot(tempo, audio_data, color='b')
plt.title('Áudio no Domínio do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()

# Calcule a Transformada de Fourier de Curta Duração (Short-Time Fourier Transform - STFT)
nfft = 1024  # Tamanho da janela de análise da STFT
plt.subplot(2, 1, 2)
plt.specgram(audio_data, NFFT=nfft, Fs=sample_rate, noverlap=512, cmap='viridis')
plt.title('Espectrograma')
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')
plt.colorbar(label='Magnitude (dB)')

plt.tight_layout()
plt.savefig("Q4\Graficos\GraficoAudioHanning.png")
