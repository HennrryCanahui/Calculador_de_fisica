import flet as ft
import math


# Constantes
h_max = 0.91
w = 1.53
g = 9.81
t_subida = 6
t_bajada = 2
V_max = h_max / t_subida  # Velocidad máxima
lambda_ = 1  # Constante de crecimiento

def spacing_slider_change(e):
    # Convertir el valor del control deslizante a una fracción del tiempo total de subida
    frac_t = int(e.control.value) / 100
    # Tiempo actual basado en la fracción del tiempo total de subida
    t_actual = frac_t * t_subida
    
    # Calcular la velocidad exponencial
    V_motor = V_max * (1 - math.exp(-lambda_ * t_actual))
    
    # Convertir el valor del control deslizante a una altura en metros
    h = frac_t * h_max
    
    # Calcular las energías
    E_potencial = w * g * h
    E_cinetica = 0.5 * w * V_motor**2
    
    # Calcular la potencia del motor (P = F * v, donde F = w * g)
    P_motor = w * g * V_motor

    # Actualizar el texto de las energías
    E_p.value = f"Valor: {E_potencial:.2f} J"
    E_k.value = f"Valor: {E_cinetica:.4f} J"
    
    # Trabajo del motor (igual a la energía potencial en este caso)
    W_motor = E_potencial
    W_m.value = f"Trabajo del motor {W_motor:.2f} J"
    
    # Actualizar la velocidad del motor
    V_m.value = f"Velocidad del motor: {V_motor:.4f} m/s"
    
    # Actualizar la potencia del motor
    P_m.value = f"Potencia del motor: {P_motor:.4f} W"
    
    E_k.update()
    E_p.update()
    W_m.update()
    V_m.update()
    P_m.update()

E_k = ft.Text(size = 25, color = "BLACK")
E_p = ft.Text(size = 25, color = "BLACK")
W_m = ft.Text(size = 25, color = "BLACK")
V_m = ft.Text(size = 25, color = "BLACK")
P_m = ft.Text(size = 25, color = "BLACK")

Energia_Potencial = ft.Container(

    content=ft.Column([
        ft.Text("Energía Potencial", size=25, color="BLACK"),
        E_p,
        ft.Divider(),
        W_m, V_m, P_m

    ]),
    width=450,
    height=450,
    bgcolor=ft.colors.AMBER,
    margin=15,
)



Energia_Cinetica = ft.Container(
    content=ft.Column([
        ft.Text("Energía Cinética", size=25, color="BLACK"),
        E_k
    ]),
    width=450,
    height=450,
    bgcolor=ft.colors.AMBER,
    margin=15
)

desplazamiento = ft.Container(
    content=ft.Slider(
        min=0,
        max=100,
        divisions=10,
        value=0,
        label="{value}",
        width=500,
        on_change=spacing_slider_change
    ),
    margin=25
)

def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                desplazamiento
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                Energia_Cinetica,
                Energia_Potencial
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(target=main)
