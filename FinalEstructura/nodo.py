class DecisionNode:
    """
    Nodo que representa una decisión en el reino de Equilibria.
    Cada nodo contiene una situación, dos opciones posibles con sus efectos correspondientes,
    y condiciones específicas que podrían causar el fin del juego.
    """
    
    def __init__(self, 
                 id, 
                 text, 
                 choice1_text, 
                 choice1_effect, 
                 choice2_text, 
                 choice2_effect, 
                 choice1_result=None, 
                 choice2_result=None, 
                 game_over_conditions=None):
        """
        Inicializa un nodo de decisión.
        
        Args:
            id: Identificador único de la decisión
            text: Descripción de la situación
            choice1_text: Texto de la primera opción
            choice1_effect: Efecto en las estadísticas de la primera opción
            choice2_text: Texto de la segunda opción
            choice2_effect: Efecto en las estadísticas de la segunda opción
            choice1_result: Resultado de elegir la opción 1
            choice2_result: Resultado de elegir la opción 2
            game_over_conditions: Condiciones específicas de game over
        """
        self.id = id                          # Identificador único de la decisión
        self.text = text                      # Descripción de la situación
        self.choice1_text = choice1_text      # Texto de la primera opción
        self.choice1_effect = choice1_effect  # Efecto en las estadísticas de la primera opción
        self.choice2_text = choice2_text      # Texto de la segunda opción
        self.choice2_effect = choice2_effect  # Efecto en las estadísticas de la segunda opción
        self.choice1_result = choice1_result or f"Has elegido: {choice1_text}"  # Resultado de elegir la opción 1
        self.choice2_result = choice2_result or f"Has elegido: {choice2_text}"  # Resultado de elegir la opción 2
        self.game_over_conditions = game_over_conditions or {}  # Condiciones específicas de game over
    
    def display_decision(self):
        """Muestra la información de la decisión al usuario."""
        print(self.text)
        print(f"1️⃣ {self.choice1_text}")
        print(f"2️⃣ {self.choice2_text}")
    
    def display_effects(self, effects, choice_icon):
        """
        Muestra los efectos de una decisión con emojis.
        
        Args:
            effects: Diccionario con los efectos sobre las estadísticas
            choice_icon: Emoji que indica la opción (1️⃣ o 2️⃣)
        """
        effect_str = f"→ "
        for stat, value in effects.items():
            if stat == "angeles":
                effect_str += f"👼 {'+' if value > 0 else ''}{value} | "
            elif stat == "demonios":
                effect_str += f"😈 {'+' if value > 0 else ''}{value} | "
            elif stat == "pueblo":
                effect_str += f"🧍 {'+' if value > 0 else ''}{value} | "
            elif stat == "tesoro":
                effect_str += f"💰 {'+' if value > 0 else ''}{value} | "
        
        print(f"{choice_icon} {effect_str[:-3]}")  # Eliminar el último " | "
    
    def show_options_effects(self):
        """Muestra los efectos de ambas opciones de la decisión."""
        self.display_effects(self.choice1_effect, "1️⃣")
        self.display_effects(self.choice2_effect, "2️⃣")