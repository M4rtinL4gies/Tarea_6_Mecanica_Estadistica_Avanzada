reset session

# PARÁMETROS ------------------------------------------------------------------
k = 4 * pi**2
ka = 1e-4
f(x) = ka / (2*pi * ((k - x**2)**2 + x**2))

# AJUSTES Y GRÁFICOS ----------------------------------------------------------
set grid
set size 0.9
set origin 0.07,0.05
set border 31

unset label
unset arrow
unset logscale
set xtics auto
set ytics auto

set key font "Times New Roman, 20"
set tics font "Times New Roman, 22"
set xtics offset 0,-1
set ytics offset -1,0

numero = system("read number; echo $number")

# GRÁFICOS -----------------------------------------------------------------   

# Posición
if (numero == 0) {
    set xlabel "w" font "Times New Roman, 22" offset 0,-2
    set ylabel "I_x(w) (× 10^{-7})" font "Times New Roman, 22" offset -5,0

    p [0:20][] f(x)*10**7 w l lw 2 linecolor "blue" notitle
}