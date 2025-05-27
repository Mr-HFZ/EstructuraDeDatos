from nodo import Nodo

def construir_camino_humanista():
    # Definición de los eventos del camino humanista basados en la historia
    h1 = Nodo(
        id_evento="H1",
        descripcion="Una enfermedad desconocida comienza a propagarse. No hay cura inmediata, y el pánico crece.",
        opciones={
            "A": "Imponer una cuarentena estricta",
            "B": "Distribuir medicinas igualitariamente",
            "C": "Crear hospitales especializados financiados públicamente"
        },
        consecuencias={
            "A": (3, -5, -8, -8),     # 👼 +3, 😈 -5, 🧍 -8, 💰 -8
            "B": (5, 0, 15, -18),      # 👼 +5, 😈 +0, 🧍 +15, 💰 -18
            "C": (8, 0, 20, -25)       # 👼 +8, 😈 +0, 🧍 +20, 💰 -25
        }
    )

    h2 = Nodo(
        id_evento="H2",
        descripcion="Miles huyen de reinos vecinos en guerra. Tu territorio se satura, pero negarles entrada significaría condenarlos.",
        opciones={
            "A": "Abrir las fronteras completamente",
            "B": "Establecer campos temporales hasta encontrar soluciones",
            "C": "Ayudar a establecer un territorio seguro en sus tierras originales"
        },
        consecuencias={
            "A": (12, 0, 18, -20),    # 👼 +12, 😈 +0, 🧍 +18, 💰 -20
            "B": (8, 3, 12, -12),      # 👼 +8, 😈 +3, 🧍 +12, 💰 -12
            "C": (5, 5, 8, -15)        # 👼 +5, 😈 +5, 🧍 +8, 💰 -15
        }
    )

    h1.agregar_hijo("A", h2)
    h1.agregar_hijo("B", h2)
    h1.agregar_hijo("C", h2)

    h3 = Nodo(
        id_evento="H3",
        descripcion="Un nuevo sistema económico promete crecimiento, pero beneficiará más a unos que a otros.",
        opciones={
            "A": "Implementarlo gradualmente con salvaguardas sociales",
            "B": "Rechazarlo para mantener igualdad total",
            "C": "Crear un sistema híbrido que beneficie a todos"
        },
        consecuencias={
            "A": (8, 0, 12, -5),       # 👼 +8, 😈 +0, 🧍 +12, 💰 -5
            "B": (5, -3, 5, -12),      # 👼 +5, 😈 -3, 🧍 +5, 💰 -12
            "C": (3, 3, 18, -15)       # 👼 +3, 😈 +3, 🧍 +18, 💰 -15
        }
    )

    h2.agregar_hijo("A", h3)
    h2.agregar_hijo("B", h3)
    h2.agregar_hijo("C", h3)

    h4 = Nodo(
        id_evento="H4",
        descripcion="Puedes invertir en educación universal, pero eso significa menos recursos para defensa en tiempos inciertos.",
        opciones={
            "A": "Priorizar educación sobre todo",
            "B": "Equilibrar educación y defensa",
            "C": "Crear un sistema donde educación y defensa se complementen"
        },
        consecuencias={
            "A": (10, 5, 20, -18),    # 👼 +10, 😈 +5, 🧍 +20, 💰 -18
            "B": (5, 5, 12, -12),      # 👼 +5, 😈 +5, 🧍 +12, 💰 -12
            "C": (8, 3, 15, -10)       # 👼 +8, 😈 +3, 🧍 +15, 💰 -10
        }
    )

    h3.agregar_hijo("A", h4)
    h3.agregar_hijo("B", h4)
    h3.agregar_hijo("C", h4)

    h5 = Nodo(
        id_evento="H5",
        descripcion="Descubren una biblioteca antigua con saberes poderosos… y peligrosos.",
        opciones={
            "A": "Destruirla por seguridad",
            "B": "Estudiarla en secreto con eruditos confiables",
            "C": "Hacerla pública con advertencias y educación sobre los riesgos"
        },
        consecuencias={
            "A": (8, -8, -12, 0),     # 👼 +8, 😈 -8, 🧍 -12, 💰 +0
            "B": (0, 8, 5, -8),        # 👼 +0, 😈 +8, 🧍 +5, 💰 -8
            "C": (-3, 12, 15, -8)      # 👼 -3, 😈 +12, 🧍 +15, 💰 -8
        }
    )

    h4.agregar_hijo("A", h5)
    h4.agregar_hijo("B", h5)
    h4.agregar_hijo("C", h5)

    h6 = Nodo(
        id_evento="H6",
        descripcion="Los jóvenes demandan cambios radicales, los ancianos exigen tradición. La tensión social crece.",
        opciones={
            "A": "Apoyar las reformas juveniles",
            "B": "Crear consejos mixtos donde ambas generaciones colaboren",
            "C": "Mantener el statu quo hasta que pase la tormenta"
        },
        consecuencias={
            "A": (-5, 8, 12, -8),     # 👼 -5, 😈 +8, 🧍 +12, 💰 -8
            "B": (5, 0, 18, -12),      # 👼 +5, 😈 +0, 🧍 +18, 💰 -12
            "C": (8, -3, -5, 5)        # 👼 +8, 😈 -3, 🧍 -5, 💰 +5
        }
    )

    h5.agregar_hijo("A", h6)
    h5.agregar_hijo("B", h6)
    h5.agregar_hijo("C", h6)

    h7 = Nodo(
        id_evento="H7",
        descripcion="Un extranjero llega a tus puertas, perseguido por enemigos desconocidos. Suplica por asilo.",
        opciones={
            "A": "Concederle asilo sin condiciones",
            "B": "Investigarlo antes de decidir",
            "C": "Ofrecer protección temporal mientras negocias con sus perseguidores"
        },
        consecuencias={
            "A": (5, 0, 12, -8),      # 👼 +5, 😈 +0, 🧍 +12, 💰 -8
            "B": (3, 3, 3, -3),        # 👼 +3, 😈 +3, 🧍 +3, 💰 -3
            "C": (8, 5, 8, -12)        # 👼 +8, 😈 +5, 🧍 +8, 💰 -12
        }
    )

    h6.agregar_hijo("A", h7)
    h6.agregar_hijo("B", h7)
    h6.agregar_hijo("C", h7)

    h8 = Nodo(
        id_evento="H8",
        descripcion="Inventores proponen máquinas que revolucionarían la producción, pero eliminarían muchos empleos.",
        opciones={
            "A": "Prohibir la tecnología para proteger empleos",
            "B": "Implementar la tecnología gradualmente con reentrenamiento laboral",
            "C": "Adoptar la tecnología y crear nuevas industrias para los desempleados"
        },
        consecuencias={
            "A": (5, -5, 12, -15),     # 👼 +5, 😈 -5, 🧍 +12, 💰 -15
            "B": (8, 5, 20, -20),      # 👼 +8, 😈 +5, 🧍 +20, 💰 -20
            "C": (3, 10, 8, 15)        # 👼 +3, 😈 +10, 🧍 +8, 💰 +15
        }
    )

    h7.agregar_hijo("A", h8)
    h7.agregar_hijo("B", h8)
    h7.agregar_hijo("C", h8)

    h9 = Nodo(
        id_evento="H9",
        descripcion="Tus ministros se dividen entre proteger tradiciones antiguas o reformar las leyes para el bien común.",
        opciones={
            "A": "Conservar las tradiciones con mejoras menores",
            "B": "Promover reformas con consenso amplio",
            "C": "Crear un sistema donde tradición y reforma coexistan"
        },
        consecuencias={
            "A": (12, -5, -8, 5),     # 👼 +12, 😈 -5, 🧍 -8, 💰 +5
            "B": (5, 0, 12, -8),       # 👼 +5, 😈 +0, 🧍 +12, 💰 -8
            "C": (8, 3, 15, -15)       # 👼 +8, 😈 +3, 🧍 +15, 💰 -15
        }
    )

    h8.agregar_hijo("A", h9)
    h8.agregar_hijo("B", h9)
    h8.agregar_hijo("C", h9)

    h10 = Nodo(
        id_evento="H10",
        descripcion="Un reino poderoso amenaza con invasión. Puedes prepararte para la guerra, buscar aliados o intentar diplomacia.",
        opciones={
            "A": "Preparar defensas masivas",
            "B": "Formar una coalición defensiva con reinos vecinos",
            "C": "Intentar una solución diplomática directa"
        },
        consecuencias={
            "A": (5, 8, -12, -25),     # 👼 +5, 😈 +8, 🧍 -12, 💰 -25
            "B": (12, 0, 8, -15),      # 👼 +12, 😈 +0, 🧍 +8, 💰 -15
            "C": (8, 5, 12, -8)        # 👼 +8, 😈 +5, 🧍 +12, 💰 -8
        }
    )

    h9.agregar_hijo("A", h10)
    h9.agregar_hijo("B", h10)
    h9.agregar_hijo("C", h10)

    h11 = Nodo(
        id_evento="H11",
        descripcion="La magia existe en tu reino. Algunos quieren regularla, otros prohibirla, otros liberalizarla completamente.",
        opciones={
            "A": "Crear academias mágicas reguladas",
            "B": "Prohibir toda práctica mágica",
            "C": "Permitir magia libre pero con responsabilidad personal"
        },
        consecuencias={
            "A": (10, 8, 12, -20),    # 👼 +10, 😈 +8, 🧍 +12, 💰 -20
            "B": (15, -12, -8, 5),     # 👼 +15, 😈 -12, 🧍 -8, 💰 +5
            "C": (-5, 15, 8, 10)       # 👼 -5, 😈 +15, 🧍 +8, 💰 +10
        }
    )

    h10.agregar_hijo("A", h11)
    h10.agregar_hijo("B", h11)
    h10.agregar_hijo("C", h11)

    h12 = Nodo(
        id_evento="H12",
        descripcion="Una guerra se aproxima. Puedes aliarte con los ángeles (cediendo libertades), con los demonios (sacrificando moral), o luchar solo (arriesgando todo).",
        opciones={
            "A": "Aliarte con los ángeles",
            "B": "Aliarte con los demonios",
            "C": "Forjar tu propio camino independiente"
        },
        consecuencias={
            "A": (20, -15, -12, -8),  # 👼 +20, 😈 -15, 🧍 -12, 💰 -8
            "B": (-15, 20, -12, 15),   # 👼 -15, 😈 +20, 🧍 -12, 💰 +15
            "C": (5, 5, 20, -20)       # 👼 +5, 😈 +5, 🧍 +20, 💰 -20
        }
    )

    h11.agregar_hijo("A", h12)
    h11.agregar_hijo("B", h12)
    h11.agregar_hijo("C", h12)

    return h1