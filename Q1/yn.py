import numpy as np
import matplotlib.pyplot as plt

# Definir o vetor n
n = np.arange(0, 10, 0.01)

# Calcular o sinal y(n)
y = np.sin(20*np.pi*n) + np.cos(30*np.pi*n)

# Calcular a DFT do sinal y
Y = np.fft.fft(y)

# Calcular as frequências correspondentes à DFT
fs = 1 / (n[1] - n[0])  # Frequência de amostragem
frequencies = np.fft.fftfreq(len(n), 1/fs)



# Subplot da sequência temporal
plt.figure(figsize=((12, 9)) )
plt.stem(n, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sequência Temporal')
plt.savefig('Q1\YN\SequenciaTemporal.png')
# Subplot da magnitude da DFT
plt.figure(figsize=((12, 9)) )
plt.stem(frequencies, np.abs(Y))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude da DFT')
plt.savefig('Q1\YN\Magnitude.png')
# Subplot da fase da DFT
plt.figure(figsize=((12, 9)) )
plt.stem(frequencies, np.angle(Y))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (radianos)')
plt.title('Fase da DFT')
plt.savefig('Q1\YN\Fase.png')


