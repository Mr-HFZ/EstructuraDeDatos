from nodo import DecisionNode

class GameStats:
    """
    Clase para manejar las estadísticas del juego de Equilibria.
    Controla los valores de las cuatro estadísticas principales y verifica
    condiciones de equilibrio o fin de juego.
    """
    
    def __init__(self):
        # Inicializar estadísticas base del reino de Equilibria
        self.stats = {
            "angeles": 50,    # Favor de los ángeles (👼)
            "demonios": 50,   # Favor de los demonios (😈)
            "pueblo": 50,     # Satisfacción del pueblo (🧍)
            "tesoro": 50      # Estado del tesoro real (💰)
        }
        self.min_stat = 0
        self.max_stat = 100
    
    def update_stats(self, changes):
        """
        Actualiza las estadísticas según los cambios proporcionados.
        Retorna una tupla (game_over, reason) que indica si el juego termina y por qué.
        
        Args:
            changes: Diccionario con los cambios a aplicar a cada estadística
            
        Returns:
            Tupla (game_over, reason) que indica si el juego termina y por qué
        """
        game_over = False
        reason = ""
        
        for stat, change in changes.items():
            if stat in self.stats:
                self.stats[stat] += change
                # Limitar las estadísticas entre min_stat y max_stat
                self.stats[stat] = max(self.min_stat, min(self.max_stat, self.stats[stat]))
                
                # Verificar condiciones específicas de fin de juego
                if stat == "pueblo" and self.stats[stat] <= self.min_stat:
                    game_over = True
                    reason = "¡El pueblo se ha rebelado! Tu reino ha caído en el caos."
                elif stat == "tesoro" and self.stats[stat] <= self.min_stat:
                    game_over = True
                    reason = "¡El tesoro está vacío! Tu reino ha caído en la bancarrota."
                elif stat == "angeles" and self.stats[stat] >= self.max_stat:
                    game_over = True
                    reason = "¡Los ángeles han tomado el control total! Han impuesto un reino puro sin emociones humanas."
                elif stat == "demonios" and self.stats[stat] >= self.max_stat:
                    game_over = True
                    reason = "¡Los demonios han tomado el control total! Tu reino ha caído en la oscuridad eterna."
        
        return (game_over, reason)
    
    def display(self):
        """Muestra las estadísticas actuales con emojis."""
        print("\n=== ESTADÍSTICAS DE EQUILIBRIA ===")
        print(f"👼 Ángeles: {self.stats['angeles']}")
        print(f"😈 Demonios: {self.stats['demonios']}")
        print(f"🧍 Pueblo: {self.stats['pueblo']}")
        print(f"💰 Tesoro: {self.stats['tesoro']}")
        print("===================================\n")
    
    def check_balance(self):
        """
        Verifica si todas las estadísticas están equilibradas (entre 30 y 70).
        
        Returns:
            bool: True si todas las estadísticas están entre 30 y 70, False en caso contrario
        """
        for value in self.stats.values():
            if value < 30 or value > 70:
                return False
        return True


class DecisionTree:
    """
    Clase que gestiona el árbol de decisiones del juego Equilibria.
    Maneja la colección de nodos de decisión y el recorrido a través de ellos.
    """
    
    def __init__(self):
        """Inicializa el árbol de decisiones con una lista vacía."""
        self.decisions = []
        self.current_index = 0
    
    def add_decision(self, decision: DecisionNode):
        """
        Añade un nodo de decisión al árbol.
        
        Args:
            decision: Nodo de decisión a añadir
        """
        self.decisions.append(decision)
    
    def get_current_decision(self) -> DecisionNode:
        """
        Obtiene la decisión actual según el índice.
        
        Returns:
            El nodo de decisión actual
        """
        if 0 <= self.current_index < len(self.decisions):
            return self.decisions[self.current_index]
        return None
    
    def next_decision(self) -> bool:
        """
        Avanza a la siguiente decisión en el árbol.
        
        Returns:
            bool: True si hay una siguiente decisión, False si se ha llegado al final
        """
        if self.current_index < len(self.decisions) - 1:
            self.current_index += 1
            return True
        return False
    
    def reset(self):
        """Reinicia el índice de decisión actual."""
        self.current_index = 0
    
    def create_default_tree(self):
        """Crea el árbol de decisiones por defecto con todas las decisiones predefinidas del juego."""
        # Añadir todas las decisiones predefinidas
        self.decisions = [
            DecisionNode(
                id="1",
                text="📜 1. El templo sagrado\nEl Sumo Ángel pide restaurar el antiguo templo celestial.",
                choice1_text="Hazlo. La fe guía al pueblo.",
                choice1_effect={"angeles": 20, "tesoro": -15, "demonios": -5},
                choice2_text="No. Que el pueblo ore en su casa.",
                choice2_effect={"angeles": -10, "pueblo": 10, "tesoro": 10},
                choice1_result="Has restaurado el antiguo templo celestial. Los ángeles están complacidos, pero tu tesoro ha sufrido.",
                choice2_result="Has rechazado la petición. Los ángeles están decepcionados, pero el pueblo y el tesoro se benefician."
            ),
            DecisionNode(
                id="2",
                text="📜 2. Pacto de sombras\nEl demonio Zarkath ofrece poder a cambio de almas humanas.",
                choice1_text="Acepto tu trato.",
                choice1_effect={"demonios": 25, "pueblo": -20, "tesoro": 10},
                choice2_text="Nunca sacrificaré a mi gente.",
                choice2_effect={"angeles": 15, "demonios": -15},
                choice1_result="Has aceptado el pacto con Zarkath. Los demonios están encantados, pero tu pueblo sufre.",
                choice2_result="Has rechazado el pacto. Los ángeles aprueban tu decisión y los demonios están furiosos.",
                game_over_conditions={"pueblo": 0}
            ),
            DecisionNode(
                id="3",
                text="📜 3. El oro del norte\nUn reino aliado ofrece oro por permitir tráfico de armas oscuras.",
                choice1_text="Acepto el trato.",
                choice1_effect={"tesoro": 25, "demonios": 10, "angeles": -15},
                choice2_text="Rechazo su oro maldito.",
                choice2_effect={"angeles": 10, "tesoro": -15},
                choice1_result="Has aceptado el trato. Tu tesoro aumenta, pero los ángeles desaprueban tu decisión.",
                choice2_result="Has rechazado el oro. Los ángeles valoran tu integridad, pero tu tesoro sufre."
            ),
            DecisionNode(
                id="4",
                text="📜 4. Revueltas en la capital\nEl pueblo exige más derechos.",
                choice1_text="Reformaremos el reino.",
                choice1_effect={"pueblo": 20, "angeles": -10, "demonios": -10},
                choice2_text="Silencien a los revoltosos.",
                choice2_effect={"pueblo": -25, "tesoro": -5},
                choice1_result="Has decidido reformar el reino. El pueblo está satisfecho, pero tanto ángeles como demonios ven debilidad.",
                choice2_result="Has silenciado las revueltas. El pueblo está aterrorizado y tu tesoro ha gastado recursos en la represión.",
                game_over_conditions={"pueblo": 0}
            ),
            DecisionNode(
                id="5",
                text="📜 5. Milagro celestial\nUn ángel trae una reliquia curativa a cambio de los tesoros reales.",
                choice1_text="Salva a los inocentes.",
                choice1_effect={"angeles": 15, "pueblo": 10, "tesoro": -25},
                choice2_text="No podemos permitirlo.",
                choice2_effect={"tesoro": 15, "angeles": -15},
                choice1_result="Has aceptado la reliquia. Tu pueblo y los ángeles están agradecidos, pero tu tesoro está casi vacío.",
                choice2_result="Has rechazado la reliquia. Tu tesoro está a salvo, pero los ángeles cuestionan tu compasión.",
                game_over_conditions={"tesoro": 0}
            ),
            DecisionNode(
                id="6",
                text="📜 6. La grieta abisal\nUna grieta al infierno aparece. ¿Contenerla o dejarla abierta?",
                choice1_text="Ofrézcanse riquezas y rezos.",
                choice1_effect={"angeles": 10, "tesoro": -20, "demonios": -20},
                choice2_text="Que el infierno venga.",
                choice2_effect={"demonios": 25, "pueblo": -15},
                choice1_result="Has contenido la grieta con ofrendas y oraciones. Los ángeles aprueban, pero tu tesoro y los demonios sufren.",
                choice2_result="Has permitido que la grieta permanezca abierta. Los demonios están complacidos, pero tu pueblo está aterrorizado."
            ),
            DecisionNode(
                id="7",
                text="📜 7. El cielo desciende\nLos ángeles desean imponer un reino puro, sin emociones humanas.",
                choice1_text="Acepto la perfección.",
                choice1_effect={"angeles": 30, "demonios": -10, "pueblo": -30},
                choice2_text="La humanidad necesita libertad.",
                choice2_effect={"pueblo": 15, "angeles": -15},
                choice1_result="Has aceptado el reino puro. Los ángeles están extasiados, pero tu pueblo pierde su humanidad.",
                choice2_result="Has defendido la libertad humana. Tu pueblo te agradece, pero los ángeles están decepcionados.",
                game_over_conditions={"angeles": 100}
            ),
            DecisionNode(
                id="8",
                text="📜 8. Los banqueros oscuros\nUna orden secreta ofrece préstamos a cambio de tu sueño.",
                choice1_text="Acepto el trato.",
                choice1_effect={"tesoro": 25, "pueblo": -10, "demonios": 5},
                choice2_text="¡Fuera de mi reino!",
                choice2_effect={"angeles": 5, "tesoro": -10},
                choice1_result="Has aceptado el préstamo. Tu tesoro crece, pero tu pueblo sufre pesadillas y los demonios ganan influencia.",
                choice2_result="Has expulsado a los banqueros. Los ángeles aprueban tu decisión, pero tu tesoro sufre."
            ),
            DecisionNode(
                id="9",
                text="📜 9. La hija del demonio\nUna demonio desea casarse contigo y traer la paz.",
                choice1_text="Acepto su mano.",
                choice1_effect={"demonios": 20, "angeles": -20, "pueblo": 10},
                choice2_text="¡Jamás!",
                choice2_effect={"angeles": 15, "demonios": -15, "pueblo": -10},
                choice1_result="Has aceptado casarte con la demonio. Los demonios celebran la unión, pero los ángeles están horrorizados.",
                choice2_result="Has rechazado la propuesta. Los ángeles están complacidos, pero los demonios y parte del pueblo están decepcionados."
            ),
            DecisionNode(
                id="10",
                text="📜 10. La cruzada santa\nLos ángeles planean atacar a los demonios con todo su poder.",
                choice1_text="Lancen el ataque.",
                choice1_effect={"angeles": 25, "demonios": -20, "tesoro": -20},
                choice2_text="Negociación, no guerra.",
                choice2_effect={"demonios": 15, "angeles": -15, "pueblo": 10},
                choice1_result="Has autorizado la cruzada. Los ángeles triunfan, pero tu tesoro se ha vaciado en la guerra.",
                choice2_result="Has elegido la diplomacia. Los demonios respetan tu decisión, los ángeles están frustrados, pero tu pueblo valora la paz.",
                game_over_conditions={"tesoro": 0}
            ),
            DecisionNode(
                id="11",
                text="📜 11. El profeta errante\nUn loco predica el fin del mundo y causa caos.",
                choice1_text="Cárcel o silencio.",
                choice1_effect={"pueblo": -10, "tesoro": -5},
                choice2_text="Déjenlo hablar, la libertad es sagrada.",
                choice2_effect={"pueblo": 15, "demonios": 10},
                choice1_result="Has silenciado al profeta. El pueblo teme tu autoridad y tu tesoro gasta recursos en mantenerlo callado.",
                choice2_result="Has permitido que el profeta hable. El pueblo valora la libertad, pero los demonios aprovechan el caos."
            ),
            DecisionNode(
                id="12",
                text="📜 12. El ídolo de fuego\nUn culto demoníaco ofrece protección a cambio de aceptar su fe.",
                choice1_text="Permítanles practicar su culto.",
                choice1_effect={"demonios": 20, "angeles": -20, "tesoro": 10},
                choice2_text="Destrúyanlos.",
                choice2_effect={"angeles": 10, "demonios": -25, "tesoro": -10},
                choice1_result="Has permitido el culto al ídolo. Los demonios están complacidos y tu tesoro crece, pero los ángeles están furiosos.",
                choice2_result="Has destruido el culto. Los ángeles aprueban, los demonios están furiosos y tu tesoro sufre por la campaña."
            ),
            DecisionNode(
                id="13",
                text="📜 13. Hambre y frío\nEl invierno llega y el pueblo sufre.",
                choice1_text="Distribuid comida y madera.",
                choice1_effect={"tesoro": -25, "pueblo": 20, "angeles": 5},
                choice2_text="No podemos ayudar a todos.",
                choice2_effect={"pueblo": -20, "tesoro": 10},
                choice1_result="Has distribuido recursos. Tu pueblo está agradecido y los ángeles aprueban tu compasión, pero tu tesoro casi se agota.",
                choice2_result="Has conservado recursos. Tu tesoro está más seguro, pero tu pueblo sufre hambre y enfermedad.",
                game_over_conditions={"pueblo": 0, "tesoro": 0}
            ),
            DecisionNode(
                id="14",
                text="📜 14. El mercader de almas\nUn viajero ofrece una gema mágica a cambio de una parte de tu alma.",
                choice1_text="La tomo. El poder lo vale.",
                choice1_effect={"demonios": 15, "angeles": -10, "tesoro": 10},
                choice2_text="Demasiado arriesgado.",
                choice2_effect={"angeles": 10, "tesoro": -5},
                choice1_result="Has aceptado la gema. Tu poder y tesoro aumentan, pero los ángeles ven como tu alma se oscurece.",
                choice2_result="Has rechazado la gema. Los ángeles aprueban tu prudencia, aunque tu tesoro pierde una oportunidad."
            ),
            DecisionNode(
                id="15",
                text="📜 15. El juicio final\nLos cielos y el infierno exigen que elijas un lado.",
                choice1_text="Con los ángeles, para siempre.",
                choice1_effect={"angeles": 50, "demonios": -50, "pueblo": -20},
                choice2_text="Con los demonios, aceptamos el caos.",
                choice2_effect={"demonios": 50, "angeles": -50, "pueblo": -20},
                choice1_result="Has elegido el bando celestial. Los ángeles toman control total mientras los demonios son expulsados.",
                choice2_result="Has elegido el bando infernal. Los demonios toman control mientras los ángeles abandonan tu reino.",
                game_over_conditions={"angeles": 100, "demonios": 100}
            )
        ]