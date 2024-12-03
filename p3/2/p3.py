import numpy as np
from tqdm import tqdm

# Parámetros
m = 1.0                                         # Masa
k = 4 * (np.pi)**2                              # Constante del resorte
b = 1.0                                         # Coeficiente de fricción
kappa = 10**(-4)                                # Magnitud fuerza
delta_t = 0.01                                 # Paso de tiempo
t_max = 500                                     # Tiempo total
a = (3 * kappa / delta_t)**(1/2)                # Intervalo de probabilidad de f
n_steps = int(t_max / delta_t)
n_loop = 100
p_x_total = 0

# Inicialización
#Loop
for n in tqdm(range(n_loop)):
    t_values = np.linspace(0, t_max, n_steps)
    x = np.zeros(n_steps)                           # Posición
    v = np.zeros(n_steps)                           # Velocidad

    # Fuerza externa: ruido aleatorio en [-a, a]
    f = np.random.uniform(-a, a, n_steps)

    # Condiciones iniciales
    x[0] = 0.0
    v[0] = 0.0

    # Método de Euler
    for i in range(1, n_steps):
        v[i] = v[i-1] + (delta_t / m) * (f[i-1] - k * x[i-1] - b * v[i-1])
        x[i] = x[i-1] + v[i-1] * delta_t

    # Transformada de Fourier
    ft_x = np.fft.fft(x) * delta_t
    freq = (2 * np.pi) * np.fft.fftfreq(n_steps, delta_t)
    p_x_total += np.abs(ft_x)**2 / (2 * np.pi * t_max)

p_x_total /= n_loop

# Guardar datos
data = np.array([t_values, x, freq, p_x_total])
data_save = np.transpose(data)
np.savetxt("data_a.txt", data_save, fmt = "%.10f", delimiter="\t")