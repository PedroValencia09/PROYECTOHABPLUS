import tkinter as tk
from tkinter import font, messagebox

# ======================= LISTA DE HÁBITOS ACTIVOS =======================
habitos_activos = ["Caminar", "Leer", "Dormir"]

# ======================= INFORMACIÓN DE HÁBITOS =======================
habitos_info = {
    "Caminar": {
        "tiempo": "5 minutos",
        "dias": "Lunes a Viernes",
        "descripcion": "Camina durante 5 minutos diarios para activar tu cuerpo."
    },
    "Leer": {
        "tiempo": "10 minutos",
        "dias": "Lunes a Viernes",
        "descripcion": "Lee algo que te interese durante al menos 10 minutos."
    },
    "Dormir": {
        "tiempo": "8 horas",
        "dias": "Todos los días",
        "descripcion": "Duerme al menos 8 horas para un descanso saludable."
    }
}

# ======================= VENTANA ESTADÍSTICAS =======================
def mostrar_estadisticas():
    estadisticas_window = tk.Toplevel()
    estadisticas_window.title("Estadísticas")
    estadisticas_window.attributes('-fullscreen', True)
    estadisticas_window.configure(bg="white")

    header = tk.Frame(estadisticas_window, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=estadisticas_window.destroy).place(x=20, y=30)
    tk.Label(header, text="Estadísticas", font=("Arial", 32, "bold"), bg="#d3d3d3").pack(pady=20)

    rachas_frame = tk.Frame(estadisticas_window, bg="white")
    rachas_frame.pack(pady=50, fill="x")

    frame_dias = tk.Frame(rachas_frame, bg="white")
    frame_dias.pack(side="left", expand=True)

    tk.Label(frame_dias, text="RACHA\nDÍAS", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
    tk.Label(frame_dias, text="DÍAS", font=("Arial", 14, "bold"), bg="#d3d3d3", width=10).pack()
    tk.Label(frame_dias, text="00", font=("Arial", 18, "bold"), bg="white", relief="solid", width=10, height=2).pack()

    frame_habitos = tk.Frame(rachas_frame, bg="white")
    frame_habitos.pack(side="left", expand=True)

    tk.Label(frame_habitos, text="RACHA\nHÁBITOS", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
    tk.Label(frame_habitos, text="00", font=("Arial", 18, "bold"), bg="#d3d3d3", relief="solid", width=10, height=2).pack()

    separator = tk.Frame(estadisticas_window, height=2, bg="black")
    separator.pack(fill="x", pady=30)

    nivel_frame = tk.Frame(estadisticas_window, bg="white")
    nivel_frame.pack(pady=20)

    tk.Label(nivel_frame, text="NIVEL DE JUGADOR", font=("Arial", 14), bg="white").pack()

    barra_nivel = tk.Frame(nivel_frame, bg="white", relief="solid", bd=1)
    barra_nivel.pack(pady=10)

    tk.Label(barra_nivel, text="LVL 1", font=("Arial", 14), bg="white", width=10, relief="solid").pack(side="left")
    tk.Label(barra_nivel, text="0-100", font=("Arial", 12, "bold"), bg="#d3d3d3", width=25, relief="solid").pack(side="left")
    tk.Label(barra_nivel, text="LVL 2", font=("Arial", 14), bg="white", width=10, relief="solid").pack(side="left")

    estadisticas_window.bind("<Escape>", lambda e: estadisticas_window.attributes("-fullscreen", False))


# ======================= VENTANA EDICIÓN INDIVIDUAL HABITO =======================
def mostrar_edicion_habito(nombre_habito):
    ventana = tk.Toplevel()
    ventana.title(f"Editar hábito: {nombre_habito}")
    ventana.attributes('-fullscreen', True)
    ventana.configure(bg="white")

    header = tk.Frame(ventana, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=ventana.destroy).place(x=20, y=30)
    tk.Label(header, text=f"{nombre_habito}", font=("Arial", 32, "bold"), bg="#d3d3d3").pack(pady=20)

    cuerpo = tk.Frame(ventana, bg="white")
    cuerpo.pack(pady=40)

    # Campo días
    tk.Label(cuerpo, text="Editar día(s)", font=("Arial", 20), bg="white").pack(pady=10)
    entry_dias = tk.Entry(cuerpo, font=("Arial", 16), width=30)
    entry_dias.insert(0, habitos_info[nombre_habito]["dias"])
    entry_dias.pack(pady=10)

    # Campo tiempo
    tk.Label(cuerpo, text="Editar tiempo", font=("Arial", 20), bg="white").pack(pady=10)
    entry_tiempo = tk.Entry(cuerpo, font=("Arial", 16), width=30)
    entry_tiempo.insert(0, habitos_info[nombre_habito]["tiempo"])
    entry_tiempo.pack(pady=10)

    # Botón Aceptar (actualiza datos)
    def guardar_cambios():
        nuevo_dia = entry_dias.get().strip()
        nuevo_tiempo = entry_tiempo.get().strip()
        if nuevo_dia and nuevo_tiempo:
            habitos_info[nombre_habito]["dias"] = nuevo_dia
            habitos_info[nombre_habito]["tiempo"] = nuevo_tiempo
        ventana.destroy()

    tk.Button(
        cuerpo,
        text="Aceptar",
        font=("Arial", 18, "bold"),
        bg="#d9d9d9",
        width=15,
        height=2,
        command=guardar_cambios
    ).pack(pady=40)

    # Botón Eliminar hábito
    tk.Button(
        ventana,
        text="Eliminar hábito",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="red",
        relief="raised",
        command=lambda: confirmar_eliminacion_habito(ventana, nombre_habito)
    ).pack(side="bottom", pady=30)

    ventana.bind("<Escape>", lambda e: ventana.attributes("-fullscreen", False))

    # ======================= CONFIRMACIÓN ELIMINAR HÁBITO =======================
def confirmar_eliminacion_habito(ventana_padre, habito):
    confirmacion = tk.Toplevel()
    confirmacion.title("Confirmar eliminación")
    confirmacion.geometry("400x200")
    confirmacion.configure(bg="white")

    tk.Label(confirmacion, text="¿Deseas realizar esta acción?", font=("Arial", 16), bg="white").pack(pady=30)

    botones = tk.Frame(confirmacion, bg="white")
    botones.pack(pady=10)

    def eliminar():
        if habito in habitos_activos:
            habitos_activos.remove(habito)
        confirmacion.destroy()
        ventana_padre.destroy()
        mostrar_editor_rutina()

    def cancelar():
        confirmacion.destroy()

    tk.Button(botones, text="Sí", font=("Arial", 14), bg="#d9d9d9", width=8, command=eliminar).pack(side="left", padx=20)
    tk.Button(botones, text="No", font=("Arial", 14), bg="#d9d9d9", width=8, command=cancelar).pack(side="right", padx=20)

# ======================= AGREGAR HÁBITO DESDE EDITOR =======================
def mostrar_agregar_habito():
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar hábito")
    ventana_agregar.attributes('-fullscreen', True)
    ventana_agregar.configure(bg="white")

    header = tk.Frame(ventana_agregar, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=ventana_agregar.destroy).place(x=20, y=30)
    tk.Label(header, text="Selecciona un hábito para agregar", font=("Arial", 32, "bold"), bg="#d3d3d3").pack(pady=20)

    cuerpo = tk.Frame(ventana_agregar, bg="white")
    cuerpo.pack(pady=40)

    def agregar_habito(nombre):
        if nombre not in habitos_activos:
            habitos_activos.append(nombre)
            mostrar_info_habito(nombre)
            ventana_agregar.destroy()
            for window in tk._default_root.winfo_children():
                if isinstance(window, tk.Toplevel) and window.title() == "Editor Rutina":
                    window.destroy()
            mostrar_editor_rutina()

    for nombre in ["Caminar", "Leer", "Dormir"]:
        tk.Button(
            cuerpo,
            text=nombre,
            font=("Arial", 20),
            width=20,
            bg="#d9d9d9",
            command=lambda n=nombre: agregar_habito(n)
        ).pack(pady=15)

    ventana_agregar.bind("<Escape>", lambda e: ventana_agregar.attributes("-fullscreen", False))

# ======================= VENTANA INFORMACIÓN HÁBITO NUEVO =======================
def mostrar_info_habito(nombre_habito):
    info = habitos_info.get(nombre_habito, {})
    ventana_info = tk.Toplevel()
    ventana_info.title(f"Nivel 1 - {nombre_habito}")
    ventana_info.attributes('-fullscreen', True)
    ventana_info.configure(bg="white")

    header = tk.Frame(ventana_info, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=ventana_info.destroy).place(x=20, y=30)
    tk.Label(header, text=f"Nivel 1 - {nombre_habito}", font=("Arial", 32, "bold"), bg="#d3d3d3").pack(pady=20)

    cuerpo = tk.Frame(ventana_info, bg="white")
    cuerpo.pack(pady=60)

    tk.Label(cuerpo, text=f"Tiempo sugerido: {info.get('tiempo', '')}", font=("Arial", 22), bg="white").pack(pady=10)
    tk.Label(cuerpo, text=f"Días recomendados: {info.get('dias', '')}", font=("Arial", 22), bg="white").pack(pady=10)
    tk.Label(cuerpo, text=info.get('descripcion', ''), font=("Arial", 18), wraplength=800, justify="center", bg="white").pack(pady=20)

    tk.Button(cuerpo, text="Aceptar", font=("Arial", 18, "bold"), bg="#d9d9d9", width=15, height=2, command=ventana_info.destroy).pack(pady=30)

    ventana_info.bind("<Escape>", lambda e: ventana_info.attributes("-fullscreen", False))
# ======================= EDITOR RUTINA =======================
def mostrar_editor_rutina():
    editor_window = tk.Toplevel()
    editor_window.title("Editor Rutina")
    editor_window.attributes('-fullscreen', True)
    editor_window.configure(bg="white")

    header = tk.Frame(editor_window, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    btn_volver = tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=editor_window.destroy)
    btn_volver.place(x=20, y=30)

    titulo = tk.Label(header, text="Editor Rutina", font=("Arial", 32, "bold"), bg="#d3d3d3")
    titulo.pack(pady=20)

    instruccion = tk.Label(editor_window, text="¡Selecciona el hábito que quieras editar!", font=("Arial", 20), bg="white")
    instruccion.pack(pady=30)

    contenedor = tk.Frame(editor_window, bg="white")
    contenedor.pack(pady=20)

    habitos = [("Caminar", "👣"), ("Leer", "📖"), ("Dormir", "🛎️")]

    for nombre, icono in habitos:
        if nombre in habitos_activos:
            habit_frame = tk.Frame(contenedor, bg="white")
            habit_frame.pack(side="left", padx=40)

            icon_label = tk.Label(habit_frame, text=icono, font=("Arial", 60), bg="lightgray", width=4, height=2)
            icon_label.pack()

            check = tk.Checkbutton(habit_frame, bg="white")
            check.pack(pady=10)

            label = tk.Label(habit_frame, text=nombre, font=("Arial", 16, "italic"), bg="white")
            label.pack()

            tk.Button(habit_frame, text="Aceptar", font=("Arial", 12), bg="#d9d9d9",
                      command=lambda n=nombre: mostrar_edicion_habito(n)).pack(pady=5)

    mast_btn = tk.Button(
        editor_window,
        text="+",
        font=("Arial", 32, "bold"),
        bg="#d9d9d9",
        fg="black",
        width=3,
        height=1,
        relief="solid",
        bd=2,
        command=mostrar_agregar_habito
    )
    mast_btn.place(x=30, y=editor_window.winfo_screenheight() - 110)

    editor_window.bind("<Escape>", lambda e: editor_window.attributes("-fullscreen", False))

# ======================= EDITOR RUTINA  =======================
def mostrar_editor_rutina():
    editor_window = tk.Toplevel()
    editor_window.title("Editor Rutina")
    editor_window.attributes('-fullscreen', True)
    editor_window.configure(bg="white")

    header = tk.Frame(editor_window, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    btn_volver = tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=editor_window.destroy)
    btn_volver.place(x=20, y=30)

    titulo = tk.Label(header, text="Editor Rutina", font=("Arial", 32, "bold"), bg="#d3d3d3")
    titulo.pack(pady=20)

    instruccion = tk.Label(editor_window, text="¡Selecciona el hábito que quieras editar!", font=("Arial", 20), bg="white")
    instruccion.pack(pady=30)

    contenedor = tk.Frame(editor_window, bg="white")
    contenedor.pack(pady=20)

    habitos = [("Caminar", "👣"), ("Leer", "📖"), ("Dormir", "🛏️")]

    for nombre, icono in habitos:
        habit_frame = tk.Frame(contenedor, bg="white")
        habit_frame.pack(side="left", padx=40)

        icon_label = tk.Label(habit_frame, text=icono, font=("Arial", 60), bg="lightgray", width=4, height=2)
        icon_label.pack()

        check = tk.Checkbutton(habit_frame, bg="white")
        check.pack(pady=10)

        label = tk.Label(habit_frame, text=nombre, font=("Arial", 16, "italic"), bg="white")
        label.pack()

        # Botón Aceptar que abre edición individual
        tk.Button(habit_frame, text="Aceptar", font=("Arial", 12), bg="#d9d9d9", command=lambda n=nombre: mostrar_edicion_habito(n)).pack(pady=5)

   

   
    boton_agregar = tk.Button(editor_window, text="+", font=("Arial", 28, "bold"), bg="#f0f0f0", relief="flat", width=2, command=mostrar_agregar_habito)
    boton_agregar.place(x=30, y=editor_window.winfo_screenheight() - 100)

    editor_window.bind("<Escape>", lambda e: editor_window.attributes("-fullscreen", False))


# ======================= PESTAÑA PROGRESO =======================
def mostrar_progreso():
    progreso_window = tk.Toplevel()
    progreso_window.title("Progreso")
    progreso_window.attributes('-fullscreen', True)
    progreso_window.configure(bg="white")

    header = tk.Frame(progreso_window, bg="#d3d3d3", height=100)
    header.pack(fill="x")

    btn_volver = tk.Button(header, text="←", font=("Arial", 20), bg="#d3d3d3", relief="flat", command=progreso_window.destroy)
    btn_volver.place(x=20, y=30)

    titulo = tk.Label(header, text="Progreso", font=("Arial", 32, "bold"), bg="#d3d3d3")
    titulo.pack(pady=20)

    instruccion = tk.Label(progreso_window, text="Registra tu progreso diario:", font=("Arial", 20), bg="white")
    instruccion.pack(pady=30)

    contenedor = tk.Frame(progreso_window, bg="white")
    contenedor.pack(pady=20)

    # Día
    label_dia = tk.Label(contenedor, text="Día (Ej: Lunes, 2025-07-06)", font=("Arial", 18), bg="white")
    label_dia.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    entry_dia = tk.Entry(contenedor, font=("Arial", 16), width=25)
    entry_dia.grid(row=0, column=1, padx=10, pady=10)

    # Tiempo
    label_tiempo = tk.Label(contenedor, text="Tiempo (Ej: 00:15 o 15 minutos)", font=("Arial", 18), bg="white")
    label_tiempo.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    entry_tiempo = tk.Entry(contenedor, font=("Arial", 16), width=25)
    entry_tiempo.grid(row=1, column=1, padx=10, pady=10)

    # Hábito (desplegable)
    label_habito = tk.Label(contenedor, text="Hábito", font=("Arial", 18), bg="white")
    label_habito.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    var_habito = tk.StringVar(progreso_window)
    var_habito.set(habitos_activos[0])  # valor por defecto

    opcion_habito = tk.OptionMenu(contenedor, var_habito, *habitos_activos)
    opcion_habito.config(font=("Arial", 16), width=20)
    opcion_habito.grid(row=2, column=1, padx=10, pady=10)

    # Botón para guardar progreso
    def guardar_progreso():
        dia = entry_dia.get().strip()
        tiempo = entry_tiempo.get().strip()
        habito = var_habito.get()

        if not dia or not tiempo:
            messagebox.showwarning("Campos incompletos", "Por favor, llena todos los campos.")
            return

        # Aquí podrías guardar los datos en base de datos o archivo
        messagebox.showinfo("Guardado", f"Progreso guardado:\nHábito: {habito}\nDía: {dia}\nTiempo: {tiempo}")

        # Limpiar campos
        entry_dia.delete(0, tk.END)
        entry_tiempo.delete(0, tk.END)

    boton_guardar = tk.Button(progreso_window, text="Guardar Progreso", font=("Arial", 18, "bold"),
                              bg="#d9d9d9", width=20, command=guardar_progreso)
    boton_guardar.pack(pady=40)

    progreso_window.bind("<Escape>", lambda e: progreso_window.attributes("-fullscreen", False))


# ======================= VENTANA INICIO =======================
def mostrar_inicio():
    inicio_window = tk.Toplevel()
    inicio_window.title("Habitus + - Inicio")
    inicio_window.attributes('-fullscreen', True)
    inicio_window.configure(bg="white")

    header = tk.Frame(inicio_window, bg="#d9d9d9", height=120)
    header.pack(fill="x")

    header_label = tk.Label(header, text="Inicio", font=("Arial", 36, "bold"), bg="#d9d9d9")
    header_label.pack(pady=30)

    botones_frame = tk.Frame(inicio_window, bg="white")
    botones_frame.pack(expand=True)

    botones = [
        ("Mira tus hábitos", mostrar_mi_rutina),
        ("Progreso", mostrar_progreso),
        ("Editar Rutina", mostrar_editor_rutina),
        ("Estadísticas", mostrar_estadisticas)
    ]
