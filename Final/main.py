from arbol import ArbolDecisiones
import textwrap
import os
import time
import random
from enum import Enum

class EstadoReino(Enum):
    """Enumeración de los posibles estados del reino"""
    EQUILIBRIO = 1
    CAOS = 2
    ORDEN = 3
    PROSPERIDAD = 4
    DECADENCIA = 5

class ReinoDeEquilibria:
    def __init__(self):
        """
        Clase principal del juego Reino de Equilibria.
        Controla el flujo del juego, las decisiones y las estadísticas del reino.
        """
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
        
        # Configuración de rangos y efectos visuales
        self.rangos = {
            "Crítico": (0, 15),
            "Bajo": (16, 35),
            "Moderado": (36, 65),
            "Alto": (66, 85),
            "Extremo": (86, 100)
        }
        
        self.colores = {
            "Crítico": "\033[91m",  # Rojo
            "Bajo": "\033[93m",     # Amarillo
            "Moderado": "\033[92m", # Verde
            "Alto": "\033[96m",     # Cyan
            "Extremo": "\033[95m",  # Magenta
            "reset": "\033[0m"      # Reset color
        }

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_introduccion(self):
        """Muestra la introducción épica del juego con arte ASCII."""
        self.limpiar_pantalla()
        
        ascii_art = r"""
          ___           ___           ___           ___           ___     
         /\__\         /\  \         /\  \         /\  \         /\__\    
        /:/  /        /::\  \       /::\  \       /::\  \       /:/  /    
       /:/  /        /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/  /     
      /:/  /  ___   /:/  \:\  \   /:/  \:\  \   /:/  \:\  \   /:/  /  ___ 
     /:/__/  /\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/  /\__\
     \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  /
      \:\  /:/  /   \:\  /:/  /   \:\  /:/  /   \:\  /:/  /   \:\  /:/  / 
       \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /  
        \::/  /       \::/  /       \::/  /       \::/  /       \::/  /   
         \/__/         \/__/         \/__/         \/__/         \/__/    
        """
        
        print("\033[95m" + ascii_art + "\033[0m")
        
        intro = textwrap.dedent("""
        👑 REINO DE EQUILIBRIA 👑

        En un mundo donde las fuerzas celestiales e infernales luchan por el dominio,
        tu reino emerge de las cenizas de la Gran Guerra de los Tres Caminos.
        
        Como nuevo soberano, cada decisión que tomes afectará el delicado equilibrio
        entre:
        
        - Los \033[96mÁngeles\033[0m (orden divino y pureza)
        - Los \033[91mDemonios\033[0m (poder y ambición)
        - El \033[93mPueblo\033[0m (bienestar y prosperidad)
        - El \033[92mTesoro\033[0m (riqueza y recursos)

        Tu sabiduría será probada en cada turno. ¿Podrás mantener el equilibrio
        o te inclinarás hacia un camino definitivo?
        """)
        
        print(intro)
        input("\nPresiona Enter para comenzar tu reinado...")

    def mostrar_estado(self):
        """Muestra las estadísticas actuales del reino con formato y colores."""
        print("\n" + "═"*50)
        print(f"📊 ESTADO DEL REINO (Turno {self.turno})".center(50))
        print("═"*50)
        
        for stat, valor in self.stats.items():
            rango = self.obtener_rango(valor)
            color = self.colores.get(rango, "")
            print(f"{stat.upper():<10} {color}{valor:>3}\033[0m ({rango})")
        
        print("═"*50)
        
        # Mostrar estado narrativo del reino
        estados = {
            EstadoReino.EQUILIBRIO: "\033[92mEl reino mantiene un equilibrio precario pero estable.\033[0m",
            EstadoReino.CAOS: "\033[91mEl caos se apodera del reino. Las fuerzas luchan por dominio.\033[0m",
            EstadoReino.ORDEN: "\033[96mEl orden celestial impregna cada aspecto del reino.\033[0m",
            EstadoReino.PROSPERIDAD: "\033[93mLa prosperidad florece bajo tu sabio gobierno.\033[0m",
            EstadoReino.DECADENCIA: "\033[90mLa decadencia corroe los cimientos de tu reinado.\033[0m"
        }
        
        print(f"\n{estados[self.estado_reino]}\n")

    def obtener_rango(self, valor):
        """Determina el rango descriptivo de un valor estadístico."""
        for nombre, (minimo, maximo) in self.rangos.items():
            if minimo <= valor <= maximo:
                return nombre
        return "Fuera de rango"

    def actualizar_estado_reino(self):
        """Actualiza el estado narrativo del reino basado en las estadísticas."""
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

    def mostrar_evento(self):
        """Muestra el evento actual con formato atractivo y efectos."""
        self.limpiar_pantalla()
        
        # Efecto de aparición del título
        titulo = f" {self.nodo_actual.id_evento} "
        print("\n" + "✨"*(len(titulo)+2))
        print(f"✨{titulo:^{len(titulo)}}✨")
        print("✨"*(len(titulo)+2) + "\n")
        
        # Mostrar descripción con efecto de escritura
        for linea in textwrap.wrap(self.nodo_actual.descripcion, width=70):
            self.escribir_lento(linea)
            print()
        
        # Mostrar opciones con formato
        print("\n" + "═"*25)
        print("📜 OPCIONES DISPONIBLES")
        print("═"*25)
        
        for clave, texto in self.nodo_actual.opciones.items():
            print(f"\n\033[1m[{clave}]\033[0m {texto}")
            time.sleep(0.2)

    def escribir_lento(self, texto, velocidad=0.03):
        """Escribe texto lentamente para efecto dramático."""
        for char in texto:
            print(char, end='', flush=True)
            time.sleep(velocidad)

    def aplicar_consecuencias(self, opcion):
        """Aplica las consecuencias de una decisión y avanza al siguiente nodo."""
        if opcion not in self.nodo_actual.consecuencias:
            print("\033[91m¡Opción inválida!\033[0m")
            return False
        
        # Registrar decisión
        self.historial_decisiones.append((
            self.turno,
            self.nodo_actual.id_evento, 
            opcion, 
            self.nodo_actual.opciones[opcion]
        ))
        
        # Aplicar cambios estadísticos con animación
        cambios = self.nodo_actual.consecuencias[opcion]
        stats_keys = list(self.stats.keys())
        
        print("\n\033[94mConsecuencias:\033[0m")
        for i, key in enumerate(stats_keys):
            if i < len(cambios):
                valor_anterior = self.stats[key]
                cambio = cambios[i]
                nuevo_valor = max(0, min(100, valor_anterior + cambio))
                
                # Animación del cambio
                print(f"{key.capitalize()}: {valor_anterior} → ", end='', flush=True)
                time.sleep(0.5)
                
                if cambio != 0:
                    signo = '+' if cambio > 0 else ''
                    print(f"\033[1m{nuevo_valor}\033[0m ({signo}{cambio})", flush=True)
                else:
                    print(f"{nuevo_valor} (sin cambio)", flush=True)
                
                self.stats[key] = nuevo_valor
                time.sleep(0.3)
        
        # Actualizar estado del reino
        self.actualizar_estado_reino()
        self.turno += 1
        
        # Verificar condiciones especiales
        self.verificar_eventos_especiales()
        
        # Avanzar al siguiente nodo
        self.nodo_actual = self.nodo_actual.hijos.get(opcion, None)
        return True

    def verificar_eventos_especiales(self):
        """Verifica si se activan eventos especiales por estadísticas extremas."""
        # Mensajes de advertencia
        advertencias = []
        
        if self.stats["ángeles"] >= 85:
            advertencias.append("\033[96mLos coros celestiales resuenan en cada rincón. El reino se ilumina con una luz divina.\033[0m")
        elif self.stats["ángeles"] <= 15:
            advertencias.append("\033[96mLos altares están vacíos. Los sacerdotes reportan que los ángeles han dejado de responder.\033[0m")
            
        if self.stats["demonios"] >= 85:
            advertencias.append("\033[91mLas sombras cobran vida. Susurros infernales llenan los pasillos del palacio.\033[0m")
        elif self.stats["demonios"] <= 15:
            advertencias.append("\033[91mLos pactos oscuros se debilitan. Los demonios parecen haberse retirado... por ahora.\033[0m")
            
        if self.stats["pueblo"] >= 85:
            advertencias.append("\033[93mEl pueblo te aclama en las calles. Su devoción es inquebrantable.\033[0m")
        elif self.stats["pueblo"] <= 15:
            advertencias.append("\033[93mRevueltas estallan en las provincias. El pueblo está al borde de la rebelión.\033[0m")
            
        if self.stats["tesoro"] >= 85:
            advertencias.append("\033[92mTus arcas rebosan de riquezas. Los mercaderes de todo el mundo buscan tu favor.\033[0m")
        elif self.stats["tesoro"] <= 15:
            advertencias.append("\033[92mLos fondos del reino se agotan. Los soldados murmuran sobre salarios impagos.\033[0m")
        
        # Mostrar advertencias aleatorias para no saturar
        if advertencias and random.random() > 0.5:
            print(f"\n💬 {random.choice(advertencias)}")
            time.sleep(2)

    def jugar(self):
        """Bucle principal del juego."""
        try:
            self.mostrar_introduccion()
            
            while self.nodo_actual:
                self.mostrar_evento()
                self.mostrar_estado()
                
                # Obtener opción válida
                opciones_validas = list(self.nodo_actual.opciones.keys())
                opcion = None
                
                while opcion not in opciones_validas:
                    opcion = input(f"\nTu decisión ({'/'.join(opciones_validas)}): ").upper().strip()
                    if opcion not in opciones_validas:
                        print("\033[91mOpción no válida. Intenta nuevamente.\033[0m")
                
                if not self.aplicar_consecuencias(opcion):
                    continue
                
                if self.nodo_actual:
                    input("\nPresiona Enter para continuar...")
            
            # Fin del juego
            self.mostrar_final()
            
        except KeyboardInterrupt:
            print("\n\n\033[93mReinado interrumpido. Que los dioses juzguen tu legado...\033[0m")
        except Exception as e:
            print(f"\n\033[91mError inesperado: {e}\033[0m")
            print("El juego se cerrará.")

    def determinar_final(self):
        """Determina el tipo de final basado en las estadísticas actuales."""
        # Primero verificar condiciones de victoria/destrucción absolutas
        if all(v >= 70 for v in self.stats.values()):
            return "Equilibrio Perfecto", (
                "Has logrado lo imposible: un reino donde todas las fuerzas coexisten "
                "en perfecta armonía. Tu sabiduría será recordada por milenios como "
                "el pináculo del liderazgo ilustrado."
            )
        
        if all(v <= 30 for v in self.stats.values()):
            return "Colapso Total", (
                "Todas las facetas de tu reino han colapsado simultáneamente. "
                "El vacío de poder resultante sume la tierra en un caos permanente. "
                "Tu nombre se convierte en sinónimo de fracaso."
            )
        
        # Verificar dominancia de cada stat
        stat_dominante = max(self.stats.items(), key=lambda x: x[1])[0]
        valor_dominante = self.stats[stat_dominante]
        diferencia = valor_dominante - min(self.stats.values())
        
        if diferencia >= 40 and valor_dominante >= 75:
            if stat_dominante == "ángeles":
                return "Reino Celestial", (
                    "Los ángeles han transformado tu reino en una extensión del paraíso. "
                    "La pureza reina, pero a costa de la libertad individual. Los poetas "
                    "cantarán sobre tu sacrificio por la perfección."
                )
            elif stat_dominante == "demonios":
                return "Señor de las Tinieblas", (
                    "Has abrazado completamente el poder infernal. Tu trono ahora se alza "
                    "sobre un reino de fuego y sombras. Los demonios te saludan como igual, "
                    "pero tu humanidad es solo un recuerdo lejano."
                )
            elif stat_dominante == "pueblo":
                return "República del Pueblo", (
                    "El pueblo, empoderado por tu liderazgo, ha establecido una sociedad "
                    "igualitaria. Aunque has renunciado al poder absoluto, tu visión "
                    "perdura en las instituciones que creaste."
                )
            elif stat_dominante == "tesoro":
                return "Edad Dorada", (
                    "Tu reino es el más rico del mundo conocido. Mercaderes y artistas "
                    "florecen bajo tu mecenazgo, pero algunos murmuran que el alma del "
                    "reino se ha vuelto tan fría como el oro que lo sustenta."
                )
        
        # Finales por combinaciones específicas
        if self.stats["ángeles"] >= 70 and self.stats["demonios"] >= 70:
            return "Guerra Eterna", (
                "Las fuerzas celestiales e infernales libran una batalla sin fin "
                "en tu reino. Atrapado entre ambos bandos, has convertido tu tierra "
                "en un campo de batalla cósmico."
            )
        
        if self.stats["pueblo"] <= 20 and self.stats["tesoro"] >= 80:
            return "Tirano Opulento", (
                "Mientras acumulabas riquezas inimaginables, el pueblo se hundía "
                "en la miseria. En tu último banquete, los sirvientes se alzaron "
                "y acabaron con tu reinado de opulencia cruel."
            )
        
        # Final por defecto basado en estado actual
        if self.estado_reino == EstadoReino.EQUILIBRIO:
            return "Reino en la Encrucijada", (
                "Tu reinado termina, pero el destino del reino sigue siendo incierto. "
                "Las fuerzas que has puesto en movimiento continuarán luchando por "
                "dominio mucho después de tu partida."
            )
        elif self.estado_reino == EstadoReino.CAOS:
            return "Caos Ascendente", (
                "El orden se desvanece mientras las fuerzas del caos se apoderan "
                "del reino. Tu legado será uno de destrucción y anarquía."
            )
        elif self.estado_reino == EstadoReino.ORDEN:
            return "Orden Perpetuo", (
                "Has establecido un sistema de control tan perfecto que continuará "
                "funcionando sin ti. Pero ¿a qué precio para la libertad y la "
                "individualidad?"
            )
        elif self.estado_reino == EstadoReino.PROSPERIDAD:
            return "Edad de Oro", (
                "Tu pueblo prospera y las artes florecen. Aunque tu reinado termina, "
                "has sentado las bases para una era de paz y abundancia."
            )
        else:  # DECADENCIA
            return "Ocaso del Reino", (
                "La decadencia que sembraste ha echado raíces profundas. Tu reino "
                "sobrevive, pero como una sombra de lo que pudo haber sido."
            )

    def mostrar_final(self):
        """Muestra el final del juego con arte y estadísticas detalladas."""
        self.limpiar_pantalla()
        
        # Arte ASCII para el final
        final_art = r"""
          _____          __  __ ______    ______      ________ _____  
         / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
        | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
        | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
        | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
         \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
        """
        
        print("\033[95m" + final_art + "\033[0m")
        
        titulo, descripcion = self.determinar_final()
        
        print("\n" + "═"*50)
        print(f"🏰 {titulo.upper()} ".ljust(50, '═'))
        print("═"*50 + "\n")
        
        # Mostrar descripción con efecto de escritura
        for linea in textwrap.wrap(descripcion, width=70):
            self.escribir_lento(linea)
            print()
        
        # Estadísticas finales
        print("\n" + "📊 RESUMEN FINAL DEL REINO".center(50, '─'))
        for stat, valor in self.stats.items():
            rango = self.obtener_rango(valor)
            color = self.colores.get(rango, "")
            print(f"{stat.upper():<10} {color}{valor:>3}\033[0m ({rango})")
        
        # Historial de decisiones importantes
        if self.historial_decisiones:
            print("\n" + "📜 DECISIONES CLAVE".center(50, '─'))
            for turno, evento, opcion, texto in self.historial_decisiones[-5:]:
                print(f"Turno {turno}: [{opcion}] {texto}")
        
        print("\n\033[1mGracias por jugar Reino de Equilibria!\033[0m")
        print("Tu legado perdurará en los anales de la historia...\n")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    juego = ReinoDeEquilibria()
    juego.jugar()