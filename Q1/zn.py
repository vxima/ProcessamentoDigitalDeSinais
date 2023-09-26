import numpy as np
import matplotlib.pyplot as plt

# Definir o vetor n
n = np.arange(0, 10, 0.01)

# Calcular o sinal z(n)
z = np.sin(40*np.pi*n) + np.cos(60*np.pi*n)

# Calcular a DFT do sinal z
Z = np.fft.fft(z)

# Calcular as frequências correspondentes à DFT
fs = 1 / (n[1] - n[0])  # Frequência de amostragem
frequencies = np.fft.fftfreq(len(n), 1/fs)


# Subplot da sequência temporal
plt.figure(figsize=((12, 9)) )
plt.stem(n, z)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sequência Temporal')
plt.savefig('Q1\ZN\SequenciaTemporal.png')
# Subplot da magnitude da DFT
plt.figure(figsize=((12, 9)) )
plt.stem(frequencies, np.abs(Z))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude da DFT')
plt.savefig('Q1\ZN\Magnitude.png')
# Subplot da fase da DFT
plt.figure(figsize=((12, 9)) )
plt.stem(frequencies, np.angle(Z))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (radianos)')
plt.title('Fase da DFT')
plt.savefig('Q1\ZN\Fase.png')
#plt.tight_layout()
#plt.show()
#plt.savefig('zn.png')
