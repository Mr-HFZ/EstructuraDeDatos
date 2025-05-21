#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from arbol import DecisionTree, GameStats

class Game:
    """
    Clase principal que controla el flujo del juego de Equilibria.
    Gestiona la interacción del usuario con el árbol de decisiones,
    el seguimiento de estadísticas y las condiciones de fin de juego.
    """
    
    def __init__(self):
        """Inicializa el juego con las estadísticas y el árbol de decisiones."""
        self.stats = GameStats()
        self.decision_tree = DecisionTree()
        self.game_over = False
        self.end_reason = ""
        self.decision_count = 0
        self.max_decisions = 15  # Total de 15 decisiones para terminar el juego
    
    def initialize_game(self):
        """Inicializa el juego con las decisiones predefinidas y mensaje de bienvenida."""
        # Crear el árbol de decisiones predefinido
        self.decision_tree.create_default_tree()
        
        # Mostrar la bienvenida
        print("¡Bienvenido al Reino de Equilibria!")
        print("Eres el nuevo soberano de un reino entre ángeles y demonios.")
        print("Tus decisiones afectarán el equilibrio entre las fuerzas celestiales, las infernales, tu pueblo y tu tesoro.")
        print("Mantén el equilibrio para sobrevivir y lograr el final bueno.")
        
        # Mostrar estadísticas iniciales
        self.stats.display()
    
    def is_game_finished(self):
        """
        Verifica si se han tomado todas las decisiones.
        
        Returns:
            bool: True si se han tomado todas las decisiones, False en caso contrario
        """
        return self.decision_count >= self.max_decisions
    
    def play_turn(self):
        """
        Ejecuta un turno del juego, presentando una decisión al jugador
        y procesando su elección para actualizar las estadísticas.
        """
        self.decision_count += 1
        print(f"\n=== DECISIÓN {self.decision_count}/{self.max_decisions} ===")
        
        # Obtener la decisión actual
        current_decision = self.decision_tree.get_current_decision()
        
        if current_decision:
            # Presentar la decisión al jugador
            current_decision.display_decision()
            
            # Mostrar los efectos de cada opción
            current_decision.show_options_effects()
            
            # Obtener la elección del jugador
            choice = None
            while choice not in ['1', '2']:
                choice = input("¿Qué decides? (1/2): ")
            
            # Aplicar efectos según la decisión
            if choice == '1':
                print(current_decision.choice1_result)
                game_over, reason = self.stats.update_stats(current_decision.choice1_effect)
            else:
                print(current_decision.choice2_result)
                game_over, reason = self.stats.update_stats(current_decision.choice2_effect)
            
            # Mostrar estadísticas actualizadas
            self.stats.display()
            
            # Verificar condiciones específicas de game over para esta decisión
            if not game_over and current_decision.game_over_conditions:
                for stat, limit in current_decision.game_over_conditions.items():
                    if stat in self.stats.stats:
                        if limit == 0 and self.stats.stats[stat] <= 0:
                            game_over = True
                            if stat == "pueblo":
                                reason = "🛑 El pueblo se ha rebelado y tu reino ha caído."
                            elif stat == "tesoro":
                                reason = "🛑 El tesoro está vacío y tu reino se ha derrumbado económicamente."
                        elif limit == 100 and self.stats.stats[stat] >= 100:
                            game_over = True
                            if stat == "angeles":
                                reason = "🛑 Los ángeles han tomado control total de tu reino. La pureza anula la humanidad."
                            elif stat == "demonios":
                                reason = "🛑 Los demonios han tomado control total de tu reino. El caos reina eternamente."
            
            # Actualizar el estado del juego
            self.game_over = game_over
            self.end_reason = reason
            
            # Avanzar a la siguiente decisión
            if not self.game_over:
                self.decision_tree.next_decision()
        else:
            print("Error: No hay más decisiones disponibles.")
            self.game_over = True
            self.end_reason = "Error en el sistema de decisiones."
        
        # Verificar si se han tomado todas las decisiones (final bueno potencial)
        if not self.game_over and self.is_game_finished():
            if self.stats.check_balance():
                self.game_over = True
                self.end_reason = "🏆 FINAL BUENO: El equilibrio se ha mantenido. Equilibria sobrevive... por ahora."
            else:
                self.game_over = True
                self.end_reason = "Final: Has tomado todas las decisiones, pero no has logrado el equilibrio perfecto."
    
    def run(self):
        """
        Ejecuta el juego principal de Equilibria.
        Controla el bucle principal del juego y maneja la finalización.
        """
        self.initialize_game()
        
        while not self.game_over:
            self.play_turn()
            
            if not self.game_over and not self.is_game_finished():
                continue_playing = input("\n¿Continuar gobernando? (s/n): ").lower()
                if continue_playing != 's':
                    print("Has abandonado tu trono. Equilibria queda a merced del caos y la luz.")
                    break
        
        if self.game_over:
            print(f"\n=== FIN DEL JUEGO ===")
            print(self.end_reason)
            print(f"Tu reinado en Equilibria duró {self.decision_count} decisiones.")
        
        print("\n¡Gracias por jugar al Reino de Equilibria!")


if __name__ == "__main__":
    # Ejecutar el juego
    game = Game()
    game.run()