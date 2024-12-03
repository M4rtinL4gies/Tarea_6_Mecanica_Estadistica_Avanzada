import numpy as np

# Parámetros
m = 1                                       # masa
delta_t = 0.02                              # paso de tiempo
t_max = 1000                                # tiempo total de simulación
n_steps = int(t_max / delta_t)              # número de pasos
t_values = np.linspace(0, t_max, n_steps)   # tiempos

x_t = 0
x2_t = 0
v_t = 0
v2_t = 0
f_t = 0
f2_t = 0

# Condiciones iniciales
x = np.zeros(n_steps)                       # posición
v = np.zeros(n_steps)                       # velocidad

# Generar el ruido aleatorio f(t) en [-1, 1]
f = np.random.uniform(-1, 1, n_steps)
f_t += f[0]
f2_t += (f[0])**2

# Método de Euler para integrar la ecuación de Langevin
for i in range(1, n_steps):
    # Actualizar velocidad y posición
    v[i] = v[i-1] + (f[i] / m) * delta_t
    x[i] = x[i-1] + v[i] * delta_t

    # Actualizar valores acumulados
    x_t += x[i]
    x2_t += (x[i])**2
    v_t += v[i]
    v2_t += (v[i])**2
    f_t += f[i]
    f2_t += (f[i])**2

x_t /= n_steps
x2_t /= n_steps
v_t /= n_steps
v2_t /= n_steps
f_t /= n_steps
f2_t /= n_steps

data = np.array([t_values, x, v, f])
data_save = np.transpose(data)
np.savetxt("data_d_1.txt", data_save, fmt = "%.10f", delimiter="\t")

with open("data_d_2.txt", "w") as file:
    file.write("\n")
    file.write(f"<x> = {x_t}\n<x^2> = {x2_t}\n<v> = {v_t}\n<v^2> = {v2_t}\n<f> = {f_t}\n<f^2> = {f2_t}\n")
