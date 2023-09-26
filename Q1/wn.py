import numpy as np
import matplotlib.pyplot as plt

# Definir o vetor n
n = np.arange(0, 10, 0.01)

# Calcular o sinal w(n)
y = np.sin(20*np.pi*n) + np.cos(30*np.pi*n)
z = np.sin(40*np.pi*n) + np.cos(60*np.pi*n)
w = np.concatenate((y  ,z)) #Concatenação
# Calcular a DFT do sinal w
W = np.fft.fft(w)

# Calcular as frequências correspondentes à DFT
fs = 1 / (n[1] - n[0])  # Frequência de amostragem
frequencies = np.fft.fftfreq(2*len(n), 1/fs)
n = 2*n
# Crie os subplots
plt.figure(figsize=(12, 9))

# Subplot da sequência temporal
plt.stem(w)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sequência Temporal')
plt.savefig('Q1\WN\SequenciaTemporal.png')
# Subplot da magnitude da DFT
plt.figure(figsize=((12, 9)) )
plt.stem(frequencies, np.abs(W))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude da DFT')
plt.savefig('Q1\WN\Magnitude.png')
# Subplot da fase da DFT
plt.figure(figsize=(12, 9)) 
plt.stem(frequencies, np.angle(W))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (radianos)')
plt.title('Fase da DFT')
plt.savefig('Q1\WN\Fase.png')
# Espectrograma de wn
# Janela maior
plt.figure(figsize=(12, 9)) 
plt.specgram(w, Fs=fs, cmap='viridis', NFFT=512, noverlap=250)
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')
plt.title('Espectrograma de wn')
plt.colorbar(label='Magnitude (dB)')
plt.savefig('Q1\WN\EspectrogramaJanelaMaior.png')
# Janela menor
plt.figure(figsize=(12, 9)) 
plt.specgram(w, Fs=fs, cmap='viridis', NFFT=256, noverlap=125)
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')
plt.title('Espectrograma de wn')
plt.colorbar(label='Magnitude (dB)')
plt.savefig('Q1\WN\EspectrogramaJanelaMenor.png')


