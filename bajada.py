import flet as ft
import math

# Constantes
h_max = 0.91
w = 1.53
g = 9.81
t_bajada = 2

def spacing_slider_change(e):
    # Convertir el valor del control deslizante a una fracción del tiempo total de bajada
    frac_t = int(e.control.value) / 100
    # Tiempo actual basado en la fracción del tiempo total de bajada
    t_actual = frac_t * t_bajada
    
    # Calcular la altura durante la caída
    h = h_max - 0.5 * g * t_actual**2
    if h < 0:
        h = 0  # Asegurarse de que la altura no sea negativa
    
    # Calcular la velocidad durante la caída
    V_final = math.sqrt(2 * g * h)
    
    # Calcular la energía potencial
    E_potencial = w * g * h
    # Calcular la energía cinética
    E_cinetica = 0.5 * w * V_final**2
    # Calcular la aceleración
    a = -g  # Aceleración de la gravedad durante la caída

    # Actualizar el tiempo de caída
    tiempo_caida = t_actual
    
    # Actualizar los textos
    E_p.value = f"Valor: {E_potencial:.2f} J"
    E_k.value = f"Valor: {E_cinetica:.4f} J"
    A_m.value = f"Aceleración: {a:.4f} m/s^2"
    V_f.value = f"Velocidad final: {V_final:.4f} m/s"
    T_c.value = f"Tiempo de caída: {tiempo_caida:.2f} s"

    E_k.update()
    E_p.update()
    A_m.update()
    V_f.update()
    T_c.update()

# Inicializar textos
E_k = ft.Text(size=25, color="BLACK")
E_p = ft.Text(size=25, color="BLACK")
A_m = ft.Text(size=25, color="BLACK")
V_f = ft.Text(size=25, color="BLACK")
T_c = ft.Text(size=25, color="BLACK")

# Definir contenedor
Energia_Potencial_Cinetica = ft.Container(
    content=ft.Column([
        ft.Text("Energía Potencial", size=25, color="BLACK"),
        E_p,
        ft.Divider(),
        ft.Text("Energía Cinética", size=25, color="BLACK"),
        E_k,
        ft.Divider(),
        A_m,
        V_f,
        T_c
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
                Energia_Potencial_Cinetica
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(target=main)
