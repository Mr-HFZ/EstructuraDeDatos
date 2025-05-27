class Nodo:
    def __init__(self, id_evento: str, descripcion: str, opciones: dict = None, consecuencias: dict = None, hijos: dict = None):
        """
        Clase que representa un nodo/evento en el árbol de decisiones del Reino de Equilibria.
        
        Args:
            id_evento (str): Identificador único del evento (ej. "C1", "H3", "I5")
            descripcion (str): Texto descriptivo del evento/decisión
            opciones (dict, optional): Diccionario de opciones {clave: texto_opción}
            consecuencias (dict, optional): Diccionario de consecuencias {clave: (ángeles, demonios, pueblo, tesoro)}
            hijos (dict, optional): Diccionario de nodos hijos {opción: nodo_hijo}
        """
        self.id_evento = id_evento
        self.descripcion = descripcion
        self.opciones = opciones if opciones is not None else {}
        self.consecuencias = consecuencias if consecuencias is not None else {}
        self.hijos = hijos if hijos is not None else {}

    def agregar_hijo(self, opcion: str, nodo_hijo: 'Nodo') -> None:
        """
        Conecta un nodo hijo a este nodo mediante una opción específica.
        
        Args:
            opcion (str): La clave de opción que lleva al nodo hijo
            nodo_hijo (Nodo): El nodo hijo a conectar
            
        Raises:
            ValueError: Si la opción no existe en self.opciones
        """
        if opcion not in self.opciones:
            raise ValueError(f"La opción '{opcion}' no existe en las opciones del nodo")
        
        self.hijos[opcion] = nodo_hijo

    def obtener_hijo(self, opcion: str) -> 'Nodo':
        """
        Obtiene el nodo hijo asociado a una opción.
        
        Args:
            opcion (str): La opción seleccionada
            
        Returns:
            Nodo: El nodo hijo correspondiente
            
        Raises:
            KeyError: Si la opción no tiene nodo hijo asociado
        """
        if opcion not in self.hijos:
            raise KeyError(f"No existe nodo hijo para la opción '{opcion}'")
        
        return self.hijos[opcion]

    def __str__(self) -> str:
        """Representación en string del nodo para debugging"""
        return f"Nodo({self.id_evento}): {self.descripcion[:30]}... | Opciones: {list(self.opciones.keys())}"

    def __repr__(self) -> str:
        """Representación oficial del nodo"""
        return f"<Nodo {self.id_evento} con {len(self.hijos)} hijos>"