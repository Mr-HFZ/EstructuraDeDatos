from nodo import Nodo
from Infernal import construir_camino_infernal
from Celestial import construir_camino_celestial
from Humanista import construir_camino_humanista

class ArbolDecisiones:
    def __init__(self):
        """
        Clase principal que representa el árbol de decisiones del juego.
        Contiene el prólogo inicial y conecta los tres caminos principales.
        """
        self.raiz = self._crear_nodo_raiz()
        self._construir_estructura_completa()

    def _crear_nodo_raiz(self) -> Nodo:
        """
        Crea el nodo raíz del árbol con la decisión filosófica inicial.
        
        Returns:
            Nodo: El nodo raíz con las opciones del prólogo
        """
        return Nodo(
            id_evento="PRÓLOGO",
            descripcion=(
                "El continente de Verthania yace en ruinas tras la Gran Calamidad. "
                "De las cenizas, tu reino emerge como un faro. "
                "Antes de tu primer decreto, un consejero pregunta:\n\n"
                "'Majestad... ¿qué principio debe guiar todas nuestras decisiones a partir de ahora?'"
            ),
            opciones={
                "A": "La pureza y el orden divino deben prevalecer. (Camino Celestial)",
                "B": "El equilibrio y la prosperidad de todos. (Camino Humanista)",
                "C": "El poder y la ambición sin límites. (Camino Infernal)"
            },
            consecuencias={
                "A": (12, -5, 0, 0),   # 👼 +12, 😈 -5, 🧍 +0, 💰 +0
                "B": (8, 8, 15, 0),     # 👼 +8, 😈 +8, 🧍 +15, 💰 +0
                "C": (-8, 18, -8, 8)    # 👼 -8, 😈 +18, 🧍 -8, 💰 +8
            }
        )

    def _construir_estructura_completa(self):
        """
        Construye la estructura completa del árbol conectando:
        - La raíz (prólogo) con los tres caminos principales
        - Cada camino con sus respectivos eventos y ramificaciones
        """
        # Construir cada camino por separado
        camino_celestial = construir_camino_celestial()
        camino_humanista = construir_camino_humanista()
        camino_infernal = construir_camino_infernal()

        # Conectar la raíz con los caminos principales
        self.raiz.agregar_hijo("A", camino_celestial)
        self.raiz.agregar_hijo("B", camino_humanista)
        self.raiz.agregar_hijo("C", camino_infernal)

    def obtener_raiz(self) -> Nodo:
        """
        Método para acceder al nodo raíz del árbol.
        
        Returns:
            Nodo: El nodo raíz del árbol de decisiones
        """
        return self.raiz