import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from enum import Enum
from arbol import ArbolDecisiones
import random
import textwrap

class EstadoReino(Enum):
    EQUILIBRIO = 1
    CAOS = 2
    ORDEN = 3
    PROSPERIDAD = 4
    DECADENCIA = 5

class ReinoDeEquilibriaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Reino de Equilibria")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg='#0f0f0f')
        self.setup_style()
        
        # Inicializar juego
        self.arbol = ArbolDecisiones()
        self.nodo_actual = self.arbol.obtener_raiz()
        self.stats = {
            "ángeles": 30, 
            "demonios": 30,
            "pueblo": 50,
            "tesoro": 50
        }
        self.historial_decisiones = []
        self.estado_reino = EstadoReino.EQUILIBRIO
        self.turno = 1
        self.finales_desbloqueados = set()
        
        # Configuración de rangos y colores mejorados
        self.rangos = {
            "Crítico": (0, 15),
            "Bajo": (16, 35),
            "Moderado": (36, 65),
            "Alto": (66, 85),
            "Extremo": (86, 100)
        }
        
        self.colores = {
            "Crítico": "#ff4757",
            "Bajo": "#ffa726",
            "Moderado": "#26a69a",
            "Alto": "#42a5f5",
            "Extremo": "#ab47bc",
        }
        
        # Colores por estadística
        self.colores_stats = {
            "ángeles": "#FFD700",    # Dorado
            "demonios": "#FF4500",   # Rojo-naranja
            "pueblo": "#32CD32",     # Verde lima
            "tesoro": "#FF69B4"      # Rosa fuerte
        }
        
        self.create_widgets()
        self.mostrar_introduccion()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilos generales mejorados
        style.configure('TFrame', background='#0f0f0f')
        style.configure('TLabel', background='#0f0f0f', foreground='#ffffff', 
                       font=('Segoe UI', 10))
        style.configure('TButton', background='#1a1a1a', foreground='#ffffff', 
                       font=('Segoe UI', 10, 'bold'), borderwidth=0, 
                       relief='flat', focuscolor='none')
        
        # Estilos específicos
        style.configure('Stats.TLabel', font=('Segoe UI', 11, 'bold'))
        style.configure('Title.TLabel', font=('Segoe UI', 18, 'bold'), 
                       foreground='#ffffff')
        style.configure('Event.TLabel', font=('Segoe UI', 12), 
                       foreground='#e0e0e0')
        style.configure('Option.TButton', width=40, padding=15, 
                       font=('Segoe UI', 11))
        style.configure('TLabelframe', background='#0f0f0f', 
                       foreground='#ffffff', borderwidth=2)
        style.configure('TLabelframe.Label', background='#0f0f0f', 
                       foreground='#ffffff', font=('Segoe UI', 11, 'bold'))
        
        # Mapeo de botones mejorado
        style.map('TButton', 
                 background=[('active', '#2d2d2d'), ('pressed', '#404040')],
                 foreground=[('active', '#ffffff'), ('pressed', '#ffffff')])
        
        style.map('Option.TButton',
                 background=[('active', '#2d2d2d'), ('pressed', '#404040')],
                 relief=[('pressed', 'flat'), ('!pressed', 'flat')])

    def create_widgets(self):
        # Frame principal con padding
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header con título y turno
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Título centrado con estilo mejorado
        self.title_label = ttk.Label(self.header_frame, text="⚔️ REINO DE EQUILIBRIA ⚔️", 
                                   style='Title.TLabel')
        self.title_label.pack(expand=True)
        
        # Frame para contenido principal (dividido en columnas)
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Columna izquierda - Estadísticas y estado
        self.left_column = ttk.Frame(self.content_frame)
        self.left_column.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        
        # Turno en la parte superior izquierda
        self.turn_frame = ttk.LabelFrame(self.left_column, text="Progreso")
        self.turn_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.turn_label = ttk.Label(self.turn_frame, text=f"Turno: {self.turno}", 
                                  style='Stats.TLabel')
        self.turn_label.pack(pady=10)
        
        # Frame de estadísticas mejorado
        self.stats_frame = ttk.LabelFrame(self.left_column, text="Estado del Reino")
        self.stats_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.create_stat_displays()
        
        # Frame del estado narrativo
        self.narrative_frame = ttk.LabelFrame(self.left_column, text="Situación Actual")
        self.narrative_frame.pack(fill=tk.X)
        
        self.narrative_label = ttk.Label(
            self.narrative_frame, text="", 
            style='Event.TLabel', wraplength=300, justify=tk.CENTER
        )
        self.narrative_label.pack(padx=15, pady=15)
        
        # Columna derecha - Evento y opciones
        self.right_column = ttk.Frame(self.content_frame)
        self.right_column.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Frame del evento
        self.event_frame = ttk.LabelFrame(self.right_column, text="Evento Actual")
        self.event_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.event_title = ttk.Label(self.event_frame, text="", 
                                   style='Title.TLabel')
        self.event_title.pack(pady=(15, 10))
        
        self.event_desc = scrolledtext.ScrolledText(
            self.event_frame, wrap=tk.WORD, width=50, height=12,
            font=('Segoe UI', 12), bg='#1a1a1a', fg='#e0e0e0', 
            insertbackground='#ffffff', borderwidth=0, relief='flat'
        )
        self.event_desc.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        self.event_desc.config(state=tk.DISABLED)
        
        # Frame de opciones mejorado
        self.options_frame = ttk.LabelFrame(self.right_column, text="Decisiones Disponibles")
        self.options_frame.pack(fill=tk.X)
        
        self.actualizar_estadisticas()

    def create_stat_displays(self):
        """Crea displays de estadísticas más visuales y modernos"""
        self.stat_displays = {}
        self.stat_labels = {}
        
        for i, (stat, value) in enumerate(self.stats.items()):
            # Frame para cada estadística
            stat_frame = ttk.Frame(self.stats_frame)
            stat_frame.pack(fill=tk.X, pady=8, padx=10)
            
            # Nombre de la estadística con emoji
            emojis = {"ángeles": "👼", "demonios": "😈", "pueblo": "👥", "tesoro": "💰"}
            stat_name = f"{emojis.get(stat, '')} {stat.capitalize()}"
            
            name_label = ttk.Label(stat_frame, text=stat_name, 
                                 style='Stats.TLabel', width=12, anchor=tk.W)
            name_label.pack(side=tk.LEFT)
            
            # Valor numérico
            value_label = ttk.Label(stat_frame, text=f"{value}", 
                                  style='Stats.TLabel', width=6, anchor=tk.E)
            value_label.pack(side=tk.RIGHT)
            self.stat_labels[stat] = value_label
            
            # Barra de progreso personalizada
            progress_frame = ttk.Frame(stat_frame)
            progress_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 10))
            
            # Canvas para barra personalizada
            canvas = tk.Canvas(progress_frame, height=20, bg='#0f0f0f', 
                             highlightthickness=0, borderwidth=0)
            canvas.pack(fill=tk.X)
            
            self.stat_displays[stat] = canvas

    def actualizar_estadisticas(self):
        """Actualiza las barras de estadísticas con animación mejorada"""
        for stat, valor in self.stats.items():
            canvas = self.stat_displays[stat]
            canvas.delete("all")
            
            # Obtener dimensiones del canvas
            canvas.update_idletasks()
            width = canvas.winfo_width() if canvas.winfo_width() > 1 else 200
            height = canvas.winfo_height() if canvas.winfo_height() > 1 else 20
            
            # Dibujar fondo de la barra
            canvas.create_rectangle(0, 0, width, height, fill='#2d2d2d', outline='#404040')
            
            # Calcular ancho de la barra de progreso
            progress_width = (valor / 100) * width
            
            # Color basado en el valor y la estadística
            color = self.colores_stats[stat]
            
            # Dibujar barra de progreso con gradiente simulado
            if progress_width > 0:
                canvas.create_rectangle(0, 0, progress_width, height, 
                                      fill=color, outline='')
                
                # Efecto de brillo
                if progress_width > 10:
                    canvas.create_rectangle(0, 0, progress_width, height//3, 
                                          fill=self.lighten_color(color), outline='')
            
            # Texto del valor centrado
            canvas.create_text(width//2, height//2, text=f"{valor}%", 
                             fill='white', font=('Segoe UI', 9, 'bold'))
            
            # Actualizar etiqueta con rango
            rango = self.obtener_rango(valor)
            self.stat_labels[stat].config(
                text=f"{valor} ({rango})",
                foreground=self.colores.get(rango, "white")
            )

    def lighten_color(self, color):
        """Crea una versión más clara del color para el efecto de brillo"""
        # Conversion simple para efecto de brillo
        color_map = {
            "#FFD700": "#FFFF99",  # ángeles
            "#FF4500": "#FF6B35",  # demonios  
            "#32CD32": "#90EE90",  # pueblo
            "#FF69B4": "#FFB6C1"   # tesoro
        }
        return color_map.get(color, color)

    def mostrar_introduccion(self):
        intro_window = tk.Toplevel(self.root)
        intro_window.title("Bienvenido al Reino")
        intro_window.geometry("900x700")
        intro_window.resizable(False, False)
        intro_window.configure(bg='#0f0f0f')
        intro_window.grab_set()
        
        # Frame principal con padding
        frame = ttk.Frame(intro_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Título con estilo dramático
        title = ttk.Label(frame, text="⚔️ REINO DE EQUILIBRIA ⚔️", 
                         style='Title.TLabel')
        title.pack(pady=(0, 30))
        
        # Subtítulo
        subtitle = ttk.Label(frame, text="Un Reino en la Encrucijada del Destino", 
                           font=('Segoe UI', 14, 'italic'), 
                           foreground='#b0b0b0', background='#0f0f0f')
        subtitle.pack(pady=(0, 30))
        
        # Texto de introducción mejorado
        intro_text = textwrap.dedent("""
        En las brumas del tiempo, cuando los dioses aún caminaban entre mortales,
        un reino emergió de las cenizas de la Gran Guerra de los Tres Caminos.
        
        Como el nuevo soberano de estas tierras místicas, heredas un delicado
        equilibrio entre fuerzas ancestrales que podrían crear un paraíso...
        o desatar el apocalipsis.
        
        🔥 Cada decisión resuena a través de cuatro pilares fundamentales:
        
        👼 Los Ángeles - Representan el orden divino, la pureza y la justicia
        😈 Los Demonios - Encarnan el poder, la ambición y la transformación  
        👥 El Pueblo - Son tu gente, su bienestar y prosperidad
        💰 El Tesoro - Los recursos que alimentan tu reino
        
        Tu sabiduría será probada en cada momento crucial. ¿Mantendrás el equilibrio
        precario, o guiarás tu reino hacia un destino definitivo?
        
        El tiempo de las decisiones fáciles ha terminado.
        Tu legado comienza... ahora.
        """)
        
        # Área de scroll para el texto
        text_frame = ttk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 30))
        
        intro_scroll = scrolledtext.ScrolledText(
            text_frame, wrap=tk.WORD, width=70, height=15,
            font=('Segoe UI', 11), bg='#1a1a1a', fg='#e0e0e0', 
            insertbackground='#ffffff', borderwidth=0, relief='flat'
        )
        intro_scroll.pack(fill=tk.BOTH, expand=True)
        intro_scroll.insert(tk.END, intro_text)
        intro_scroll.config(state=tk.DISABLED)
        
        # Botón de inicio estilizado
        start_button = ttk.Button(frame, text="⚡ Comenzar mi Reinado ⚡", 
                                command=lambda: self.iniciar_juego(intro_window),
                                style='Option.TButton')
        start_button.pack(pady=20)
        
        self.center_window(intro_window)

    def iniciar_juego(self, intro_window):
        intro_window.destroy()
        self.mostrar_evento()
        self.actualizar_estado_narrativo()

    def mostrar_evento(self):
        if not self.nodo_actual:
            self.mostrar_final()
            return
        
        self.event_title.config(text=self.nodo_actual.id_evento)
        
        self.event_desc.config(state=tk.NORMAL)
        self.event_desc.delete(1.0, tk.END)
        self.event_desc.insert(tk.END, self.nodo_actual.descripcion)
        self.event_desc.config(state=tk.DISABLED)
        
        # Limpiar opciones anteriores
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Crear nuevas opciones con mejor estilo
        for i, (opcion, texto) in enumerate(self.nodo_actual.opciones.items()):
            option_frame = ttk.Frame(self.options_frame)
            option_frame.pack(fill=tk.X, pady=5, padx=15)
            
            btn = ttk.Button(
                option_frame, 
                text=f"[{opcion}] {texto}", 
                command=lambda o=opcion: self.elegir_opcion(o),
                style='Option.TButton'
            )
            btn.pack(fill=tk.X)
        
        self.turn_label.config(text=f"Turno: {self.turno}")

    def elegir_opcion(self, opcion):
        if opcion not in self.nodo_actual.opciones:
            messagebox.showerror("Error", "Opción no válida")
            return
        
        # Guardar decisión en historial
        self.historial_decisiones.append((
            self.turno,
            self.nodo_actual.id_evento, 
            opcion, 
            self.nodo_actual.opciones[opcion]
        ))
        
        # Aplicar consecuencias
        cambios = self.nodo_actual.consecuencias[opcion]
        stats_keys = list(self.stats.keys())
        
        for i, key in enumerate(stats_keys):
            if i < len(cambios):
                self.stats[key] = max(0, min(100, self.stats[key] + cambios[i]))
        
        # Actualizar todo inmediatamente sin botón continuar
        self.actualizar_estadisticas()
        self.actualizar_estado_reino()
        self.actualizar_estado_narrativo()
        self.turno += 1
        
        # Verificar condiciones de fin de juego
        if self.verificar_estadisticas():
            self.nodo_actual = None
            self.mostrar_evento()
            return
        
        # Mostrar eventos especiales si corresponde
        self.verificar_eventos_especiales()
        
        # Avanzar al siguiente nodo
        self.nodo_actual = self.nodo_actual.hijos.get(opcion, None)
        
        # Pequeña pausa visual y continuar automáticamente
        self.root.after(1000, self.mostrar_evento)

    def obtener_rango(self, valor):
        for nombre, (minimo, maximo) in self.rangos.items():
            if minimo <= valor <= maximo:
                return nombre
        return "Fuera de rango"

    def actualizar_estado_reino(self):
        diferencia = max(self.stats.values()) - min(self.stats.values())
        
        if diferencia <= 15:
            self.estado_reino = EstadoReino.EQUILIBRIO
        elif self.stats["demonios"] - self.stats["ángeles"] > 20:
            self.estado_reino = EstadoReino.CAOS
        elif self.stats["ángeles"] - self.stats["demonios"] > 20:
            self.estado_reino = EstadoReino.ORDEN
        elif self.stats["pueblo"] > 70 and self.stats["tesoro"] > 60:
            self.estado_reino = EstadoReino.PROSPERIDAD
        elif min(self.stats.values()) < 20:
            self.estado_reino = EstadoReino.DECADENCIA
        else:
            self.estado_reino = EstadoReino.EQUILIBRIO

    def actualizar_estado_narrativo(self):
        estados = {
            EstadoReino.EQUILIBRIO: "⚖️ El reino mantiene un equilibrio precario pero estable.",
            EstadoReino.CAOS: "🔥 El caos se apodera del reino. Las fuerzas luchan por dominio.",
            EstadoReino.ORDEN: "✨ El orden celestial impregna cada aspecto del reino.", 
            EstadoReino.PROSPERIDAD: "🌟 La prosperidad florece bajo tu sabio gobierno.",
            EstadoReino.DECADENCIA: "💀 La decadencia corroe los cimientos de tu reinado."
        }
        
        self.narrative_label.config(text=estados[self.estado_reino])

    def verificar_estadisticas(self):
        for stat, valor in self.stats.items():
            if valor <= 0:
                return True
        return False

    def verificar_eventos_especiales(self):
        advertencias = []
        
        if self.stats["ángeles"] >= 85:
            advertencias.append("✨ Los coros celestiales resuenan en cada rincón. El reino se ilumina con una luz divina.")
        elif self.stats["ángeles"] <= 15:
            advertencias.append("💀 Los altares están vacíos. Los sacerdotes reportan que los ángeles han dejado de responder.")
            
        if self.stats["demonios"] >= 85:
            advertencias.append("🔥 Las sombras cobran vida. Susurros infernales llenan los pasillos del palacio.")
        elif self.stats["demonios"] <= 15:
            advertencias.append("❄️ Los pactos oscuros se debilitan. Los demonios parecen haberse retirado... por ahora.")
            
        if self.stats["pueblo"] >= 85:
            advertencias.append("👑 El pueblo te aclama en las calles. Su devoción es inquebrantable.")
        elif self.stats["pueblo"] <= 15:
            advertencias.append("⚔️ Revueltas estallan en las provincias. El pueblo está al borde de la rebelión.")
            
        if self.stats["tesoro"] >= 85:
            advertencias.append("💎 Tus arcas rebosan de riquezas. Los mercaderes de todo el mundo buscan tu favor.")
        elif self.stats["tesoro"] <= 15:
            advertencias.append("💸 Los fondos del reino se agotan. Los soldados murmuran sobre salarios impagos.")
        
        if advertencias and random.random() > 0.5:
            messagebox.showinfo("⚡ Evento Especial", random.choice(advertencias))

    def determinar_final(self):
        if all(v >= 70 for v in self.stats.values()):
            return "🌟 Equilibrio Perfecto", (
                "Has logrado lo imposible: un reino donde todas las fuerzas coexisten "
                "en perfecta armonía. Tu sabiduría será recordada por milenios como "
                "el pináculo del liderazgo ilustrado. Las canciones de tu reinado "
                "resonarán por toda la eternidad."
            )
        
        if all(v <= 30 for v in self.stats.values()):
            return "💀 Colapso Total", (
                "Todas las facetas de tu reino han colapsado simultáneamente. "
                "El vacío de poder resultante sume la tierra en un caos permanente. "
                "Tu nombre se convierte en sinónimo de fracaso y advertencia para "
                "futuros gobernantes."
            )
        
        stat_dominante = max(self.stats.items(), key=lambda x: x[1])[0]
        valor_dominante = self.stats[stat_dominante]
        diferencia = valor_dominante - min(self.stats.values())
        
        if diferencia >= 40 and valor_dominante >= 75:
            if stat_dominante == "ángeles":
                return "👼 Reino Celestial", (
                    "Los ángeles han transformado tu reino en una extensión del paraíso. "
                    "La pureza reina suprema, pero a costa de la libertad individual. "
                    "Los poetas cantarán sobre tu sacrificio por la perfección divina, "
                    "aunque algunos susurren sobre el precio de la pureza absoluta."
                )
            elif stat_dominante == "demonios":
                return "😈 Señor de las Tinieblas", (
                    "Has abrazado completamente el poder infernal. Tu trono ahora se alza "
                    "sobre un reino de fuego y sombras eternas. Los demonios te saludan "
                    "como igual, pero tu humanidad es solo un recuerdo lejano. El poder "
                    "absoluto tiene un precio que has pagado con tu alma."
                )
            elif stat_dominante == "pueblo":
                return "👥 República del Pueblo", (
                    "El pueblo, empoderado por tu liderazgo visionario, ha establecido "
                    "una sociedad igualitaria próspera. Aunque has renunciado al poder "
                    "absoluto, tu visión perdura en las instituciones democráticas que "
                    "creaste. Tu nombre será recordado como el liberador."
                )
            elif stat_dominante == "tesoro":
                return "💰 Edad Dorada", (
                    "Tu reino es el más rico y próspero del mundo conocido. Mercaderes "
                    "y artistas florecen bajo tu mecenazgo generoso, pero algunos murmuran "
                    "que el alma del reino se ha vuelto tan fría como el oro que lo sustenta. "
                    "La riqueza no puede comprar todo."
                )
        
        if self.stats["ángeles"] >= 70 and self.stats["demonios"] >= 70:
            return "⚔️ Guerra Eterna", (
                "Las fuerzas celestiales e infernales libran una batalla sin fin "
                "en tu reino. Atrapado entre ambos bandos, has convertido tu tierra "
                "en un campo de batalla cósmico donde ninguna fuerza puede reclamar "
                "la victoria definitiva."
            )
        
        if self.stats["pueblo"] <= 20 and self.stats["tesoro"] >= 80:
            return "👑 Tirano Opulento", (
                "Mientras acumulabas riquezas inimaginables, el pueblo se hundía "
                "en la miseria más profunda. En tu último banquete dorado, los "
                "sirvientes hambrientos se alzaron en revolución y acabaron con "
                "tu reinado de opulencia cruel."
            )
        
        if self.estado_reino == EstadoReino.EQUILIBRIO:
            return "⚖️ Reino en la Encrucijada", (
                "Tu reinado termina, pero el destino del reino sigue siendo incierto. "
                "Las fuerzas que has puesto en movimiento continuarán luchando por "
                "dominio mucho después de tu partida. El equilibrio que lograste "
                "es frágil, pero real."
            )
        elif self.estado_reino == EstadoReino.CAOS:
            return "🔥 Caos Ascendente", (
                "El orden se desvanece mientras las fuerzas del caos se apoderan "
                "del reino. Tu legado será uno de destrucción y anarquía, donde "
                "solo los más fuertes sobreviven en un mundo sin reglas."
            )
        elif self.estado_reino == EstadoReino.ORDEN:
            return "✨ Orden Perpetuo", (
                "Has establecido un sistema de control tan perfecto que continuará "
                "funcionando sin ti por generaciones. Pero ¿a qué precio para la "
                "libertad y la individualidad de tu pueblo?"
            )
        elif self.estado_reino == EstadoReino.PROSPERIDAD:
            return "🌟 Edad de Oro", (
                "Tu pueblo prospera y las artes florecen como nunca antes. Aunque "
                "tu reinado termina, has sentado las bases para una era de paz "
                "y abundancia que perdurará por siglos."
            )
        else:
            return "🌙 Ocaso del Reino", (
                "La decadencia que sembraste ha echado raíces profundas. Tu reino "
                "sobrevive, pero como una sombra marchita de lo que pudo haber sido. "
                "Las generaciones futuras pagarán por tus decisiones."
            )

    def mostrar_final(self):
        final_window = tk.Toplevel(self.root)
        final_window.title("El Destino de tu Reino")
        final_window.geometry("1000x800")
        final_window.resizable(True, True)
        final_window.configure(bg='#0f0f0f')
        final_window.grab_set()
        
        titulo, descripcion = self.determinar_final()
        
        # Frame principal con scroll
        main_frame = ttk.Frame(final_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Título del final
        title_label = ttk.Label(main_frame, text=titulo, 
                               font=('Segoe UI', 20, 'bold'), 
                               foreground='#ffffff', background='#0f0f0f')
        title_label.pack(pady=(0, 20))
        
        # Descripción del final
        desc_frame = ttk.LabelFrame(main_frame, text="Tu Legado")
        desc_frame.pack(fill=tk.X, pady=(0, 20))
        
        desc_label = ttk.Label(desc_frame, text=descripcion, 
                             font=('Segoe UI', 12), foreground='#e0e0e0',
                             background='#0f0f0f', wraplength=900, justify=tk.LEFT)
        desc_label.pack(fill=tk.X, padx=20, pady=20)
        
        # Contenedor para estadísticas y historial
        content_container = ttk.Frame(main_frame)
        content_container.pack(fill=tk.BOTH, expand=True)
        
        # Estadísticas finales (lado izquierdo)
        stats_frame = ttk.LabelFrame(content_container, text="Estadísticas Finales del Reino")
        stats_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Crear displays mejorados para estadísticas finales
        for stat, valor in self.stats.items():
            stat_container = ttk.Frame(stats_frame)
            stat_container.pack(fill=tk.X, pady=10, padx=15)
            
            # Header con emoji y nombre
            emojis = {"ángeles": "👼", "demonios": "😈", "pueblo": "👥", "tesoro": "💰"}
            header_frame = ttk.Frame(stat_container)
            header_frame.pack(fill=tk.X, pady=(0, 5))
            
            name_label = ttk.Label(header_frame, 
                                 text=f"{emojis.get(stat, '')} {stat.capitalize()}", 
                                 font=('Segoe UI', 12, 'bold'),
                                 foreground='#ffffff', background='#0f0f0f')
            name_label.pack(side=tk.LEFT)
            
            rango = self.obtener_rango(valor)
            color = self.colores.get(rango, "white")
            
            value_label = ttk.Label(header_frame, 
                                  text=f"{valor} ({rango})", 
                                  font=('Segoe UI', 12, 'bold'),
                                  foreground=color, background='#0f0f0f')
            value_label.pack(side=tk.RIGHT)
            
            # Barra de progreso visual mejorada
            progress_frame = ttk.Frame(stat_container)
            progress_frame.pack(fill=tk.X)
            
            # Canvas para barra personalizada más grande
            canvas = tk.Canvas(progress_frame, height=25, bg='#0f0f0f', 
                             highlightthickness=0, borderwidth=0)
            canvas.pack(fill=tk.X)
            
            # Dibujar la barra después de que el canvas esté renderizado
            self.root.after(10, lambda c=canvas, v=valor, s=stat: self.draw_final_stat_bar(c, v, s))
        
        # Historial de decisiones (lado derecho)
        hist_frame = ttk.LabelFrame(content_container, text="Historial de Decisiones Clave")
        hist_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        hist_text = scrolledtext.ScrolledText(
            hist_frame, wrap=tk.WORD, width=50, height=15,
            font=('Segoe UI', 10), bg='#1a1a1a', fg='#e0e0e0', 
            insertbackground='#ffffff', borderwidth=0, relief='flat'
        )
        hist_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Mostrar todas las decisiones importantes (últimas 10)
        hist_text.insert(tk.END, "📜 Las decisiones que forjaron tu destino:\n\n")
        
        decisiones_importantes = self.historial_decisiones[-10:] if len(self.historial_decisiones) > 10 else self.historial_decisiones
        
        for i, (turno, evento, opcion, texto) in enumerate(decisiones_importantes, 1):
            hist_text.insert(tk.END, f"🔸 Turno {turno}: {evento}\n")
            hist_text.insert(tk.END, f"   Decisión: [{opcion}] {texto}\n\n")
        
        # Resumen final
        hist_text.insert(tk.END, f"\n📊 Resumen del Reinado:\n")
        hist_text.insert(tk.END, f"• Duración: {self.turno - 1} turnos\n")
        hist_text.insert(tk.END, f"• Decisiones tomadas: {len(self.historial_decisiones)}\n")
        hist_text.insert(tk.END, f"• Estado final: {self.estado_reino.name}\n")
        
        # Análisis del estilo de gobierno
        angel_demon_diff = abs(self.stats["ángeles"] - self.stats["demonios"])
        if angel_demon_diff <= 10:
            hist_text.insert(tk.END, f"• Estilo: Equilibrista - Mantuviste el balance entre fuerzas\n")
        elif self.stats["ángeles"] > self.stats["demonios"]:
            hist_text.insert(tk.END, f"• Estilo: Gobernante Divino - Te inclinaste hacia la luz\n")
        else:
            hist_text.insert(tk.END, f"• Estilo: Soberano Oscuro - Abrazaste las sombras\n")
        
        if self.stats["pueblo"] >= 70:
            hist_text.insert(tk.END, f"• Legado: Amado por el pueblo\n")
        elif self.stats["pueblo"] <= 30:
            hist_text.insert(tk.END, f"• Legado: Recordado como tirano\n")
        else:
            hist_text.insert(tk.END, f"• Legado: Un gobernante más en la historia\n")
        
        hist_text.config(state=tk.DISABLED)
        
        # Botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Botón para nuevo juego
        new_game_button = ttk.Button(button_frame, text="🔄 Nuevo Reinado", 
                                   command=lambda: self.reiniciar_juego(final_window),
                                   style='Option.TButton')
        new_game_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botón para salir
        exit_button = ttk.Button(button_frame, text="🚪 Salir del Reino", 
                               command=lambda: self.root.destroy(),
                               style='Option.TButton')
        exit_button.pack(side=tk.RIGHT)
        
        self.center_window(final_window)

    def draw_final_stat_bar(self, canvas, valor, stat):
        """Dibuja una barra de estadística final más elaborada"""
        canvas.update_idletasks()
        width = canvas.winfo_width() if canvas.winfo_width() > 1 else 300
        height = canvas.winfo_height() if canvas.winfo_height() > 1 else 25
        
        # Limpiar canvas
        canvas.delete("all")
        
        # Dibujar fondo con bordes redondeados simulados
        canvas.create_rectangle(0, 0, width, height, fill='#2d2d2d', outline='#404040', width=2)
        
        # Calcular ancho de la barra de progreso
        progress_width = (valor / 100) * (width - 4)
        
        # Color basado en la estadística
        color = self.colores_stats[stat]
        
        # Dibujar barra de progreso
        if progress_width > 0:
            canvas.create_rectangle(2, 2, progress_width + 2, height - 2, 
                                  fill=color, outline='')
            
            # Efecto de brillo superior
            if progress_width > 10:
                canvas.create_rectangle(2, 2, progress_width + 2, height//2, 
                                      fill=self.lighten_color(color), outline='')
            
            # Efecto de sombra en la parte inferior
            canvas.create_rectangle(2, height//2, progress_width + 2, height - 2, 
                                  fill=self.darken_color(color), outline='')
        
        # Texto del porcentaje con sombra
        text_x = width // 2
        text_y = height // 2
        
        # Sombra del texto
        canvas.create_text(text_x + 1, text_y + 1, text=f"{valor}%", 
                         fill='#000000', font=('Segoe UI', 10, 'bold'))
        # Texto principal
        canvas.create_text(text_x, text_y, text=f"{valor}%", 
                         fill='white', font=('Segoe UI', 10, 'bold'))

    def darken_color(self, color):
        """Crea una versión más oscura del color para efectos de sombra"""
        color_map = {
            "#FFD700": "#DAA520",  # ángeles
            "#FF4500": "#CC3300",  # demonios  
            "#32CD32": "#228B22",  # pueblo
            "#FF69B4": "#CD5C5C"   # tesoro
        }
        return color_map.get(color, color)

    def reiniciar_juego(self, final_window):
        """Reinicia el juego para una nueva partida"""
        final_window.destroy()
        
        # Reinicializar todas las variables del juego
        self.arbol = ArbolDecisiones()
        self.nodo_actual = self.arbol.obtener_raiz()
        self.stats = {
            "ángeles": 30, 
            "demonios": 30,
            "pueblo": 50,
            "tesoro": 50
        }
        self.historial_decisiones = []
        self.estado_reino = EstadoReino.EQUILIBRIO
        self.turno = 1
        self.finales_desbloqueados = set()
        
        # Actualizar la interfaz
        self.actualizar_estadisticas()
        self.actualizar_estado_narrativo()
        self.mostrar_evento()

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ReinoDeEquilibriaGUI(root)
    root.mainloop()
