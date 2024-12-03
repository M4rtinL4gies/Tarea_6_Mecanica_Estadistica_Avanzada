reset session

# PARÁMETROS ------------------------------------------------------------------
arch_1 = "data_d_1.txt"

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

# PROBLEMA 1 -----------------------------------------------------------------   

# Posición
if (numero == 0) {
    set xlabel "t" font "Times New Roman, 22" offset 0,-2
    set ylabel "x(t)" font "Times New Roman, 22" offset -5,0

    p arch_1 u 1:2 w l lw 2 linecolor "blue" notitle
}

# Velocidad
if (numero == 1) {
    set xlabel "t" font "Times New Roman, 22" offset 0,-2
    set ylabel "v(t)" font "Times New Roman, 22" offset -5,0

    p arch_1 u 1:3 w l lw 2 linecolor "blue" notitle
}

# Ruido
if (numero == 2) {
    set xlabel "t" font "Times New Roman, 22" offset 0,-2
    set ylabel "f(t)" font "Times New Roman, 22" offset -5,0

    p [][-1.1:1.1] arch_1 u 1:4 w l lw 2 linecolor "blue" notitle
}