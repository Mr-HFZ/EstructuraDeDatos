from nodo import Nodo

def construir_camino_infernal():
    # Definición de los eventos del camino infernal basados en la historia
    i1 = Nodo(
        id_evento="I1",
        descripcion="Descubres que tu consejero más leal ha estado conspirando en tu contra. Tienes pruebas irrefutables.",
        opciones={
            "A": "Ejecutarlo públicamente como advertencia",
            "B": "Usarlo como doble agente", 
            "C": "Torturarlo para obtener todo lo que sabe"
        },
        consecuencias={
            "A": (-5, 10, -10, 5),    # 👼 -5, 😈 +10, 🧍 -10, 💰 +5
            "B": (-5, 8, -5, 12),     # 👼 -5, 😈 +8, 🧍 -5, 💰 +12
            "C": (-10, 15, -15, 8)    # 👼 -10, 😈 +15, 🧍 -15, 💰 +8
        }
    )

    i2 = Nodo(
        id_evento="I2",
        descripcion="Un herrero demoníaco ofrece crear armas invencibles a cambio de las almas de diez voluntarios de tu ejército.",
        opciones={
            "A": "Aceptar inmediatamente",
            "B": "Negociar mejores términos",
            "C": "Ofrecer criminales condenados en lugar de soldados"
        },
        consecuencias={
            "A": (-15, 20, -12, 8),   # 👼 -15, 😈 +20, 🧍 -12, 💰 +8
            "B": (-8, 15, -8, 12),    # 👼 -8, 😈 +15, 🧍 -8, 💰 +12
            "C": (-5, 12, 3, 15)      # 👼 -5, 😈 +12, 🧍 +3, 💰 +15
        }
    )

    i1.agregar_hijo("A", i2)
    i1.agregar_hijo("B", i2) 
    i1.agregar_hijo("C", i2)

    i3 = Nodo(
        id_evento="I3",
        descripcion="Un demonio mercader te ofrece riquezas incalculables a cambio de un objeto aparentemente insignificante de tu reino.",
        opciones={
            "A": "Aceptar sin preguntar detalles",
            "B": "Investigar el objeto antes de decidir",
            "C": "Rechazar el trato por precaución"
        },
        consecuencias={
            "A": (-10, 15, -5, 25),   # 👼 -10, 😈 +15, 🧍 -5, 💰 +25
            "B": (-3, 8, 0, 5),       # 👼 -3, 😈 +8, 🧍 +0, 💰 +5
            "C": (2, -8, 5, -3)       # 👼 +2, 😈 -8, 🧍 +5, 💰 -3
        }
    )

    i2.agregar_hijo("A", i3)
    i2.agregar_hijo("B", i3)
    i2.agregar_hijo("C", i3)

    i4 = Nodo(
        id_evento="I4",
        descripcion="Una plaga sobrenatural se extiende. Solo la magia oscura puede detenerla, pero requiere sacrificios.",
        opciones={
            "A": "Sacrificar a los enfermos para salvar al resto",
            "B": "Sacrificar riquezas y objetos valiosos",
            "C": "Buscar una cura convencional arriesgando más muertes"
        },
        consecuencias={
            "A": (-20, 18, -25, 10),  # 👼 -20, 😈 +18, 🧍 -25, 💰 +10
            "B": (-5, 8, 5, -30),     # 👼 -5, 😈 +8, 🧍 +5, 💰 -30
            "C": (8, -12, -15, -15)   # 👼 +8, 😈 -12, 🧍 -15, 💰 -15
        }
    )

    i3.agregar_hijo("A", i4)
    i3.agregar_hijo("B", i4)
    i3.agregar_hijo("C", i4)

    i5 = Nodo(
        id_evento="I5",
        descripcion="Un señor feudal se rebela. Tienes tres opciones: negociar, aplastarlo, o usar magia para dominarlo.",
        opciones={
            "A": "Negociar un acuerdo de poder compartido",
            "B": "Movilizar ejércitos para aplastarlo",
            "C": "Usar magia para controlar su mente"
        },
        consecuencias={
            "A": (3, -5, 8, -8),      # 👼 +3, 😈 -5, 🧍 +8, 💰 -8
            "B": (-8, 12, -12, -20),  # 👼 -8, 😈 +12, 🧍 -12, 💰 -20
            "C": (-15, 20, -8, 5)     # 👼 -15, 😈 +20, 🧍 -8, 💰 +5
        }
    )

    i4.agregar_hijo("A", i5)
    i4.agregar_hijo("B", i5)
    i4.agregar_hijo("C", i5)

    i6 = Nodo(
        id_evento="I6",
        descripcion="Una revuelta interna es sofocada. Los cabecillas están a tu merced. El pueblo observa expectante.",
        opciones={
            "A": "Ejecutarlos brutalmente en la plaza",
            "B": "Convertirlos en sirvientes malditos",
            "C": "Liberarlos con marcas infamantes"
        },
        consecuencias={
            "A": (-10, 18, -20, 5),   # 👼 -10, 😈 +18, 🧍 -20, 💰 +5
            "B": (-15, 22, -12, 8),   # 👼 -15, 😈 +22, 🧍 -12, 💰 +8
            "C": (-5, 8, -8, 3)       # 👼 -5, 😈 +8, 🧍 -8, 💰 +3
        }
    )

    i5.agregar_hijo("A", i6)
    i5.agregar_hijo("B", i6)
    i5.agregar_hijo("C", i6)

    i7 = Nodo(
        id_evento="I7",
        descripcion="Encuentras un libro de hechizos que puede aumentar dramáticamente tu poder, pero cada uso corrompe tu alma.",
        opciones={
            "A": "Estudiarlo completamente sin restricciones",
            "B": "Usarlo solo en emergencias extremas",
            "C": "Encerrarlo lejos de tu alcance"
        },
        consecuencias={
            "A": (-25, 30, -10, 20),  # 👼 -25, 😈 +30, 🧍 -10, 💰 +20
            "B": (-8, 15, -3, 8),     # 👼 -8, 😈 +15, 🧍 -3, 💰 +8
            "C": (5, -12, 8, -5)      # 👼 +5, 😈 -12, 🧍 +8, 💰 -5
        }
    )

    i6.agregar_hijo("A", i7)
    i6.agregar_hijo("B", i7)
    i6.agregar_hijo("C", i7)

    i8 = Nodo(
        id_evento="I8",
        descripcion="Un reino vecino se desmorona en guerra civil. Puedes intervenir para anexar territorio o mantenerte neutral.",
        opciones={
            "A": "Invadir aprovechando el caos",
            "B": "Apoyar al bando más débil para prolongar la guerra",
            "C": "Ofrecer asilo a refugiados a cambio de información"
        },
        consecuencias={
            "A": (-12, 15, -8, 25),   # 👼 -12, 😈 +15, 🧍 -8, 💰 +25
            "B": (-18, 22, -12, 15),  # 👼 -18, 😈 +22, 🧍 -12, 💰 +15
            "C": (-5, 8, 5, -8)       # 👼 -5, 😈 +8, 🧍 +5, 💰 -8
        }
    )

    i7.agregar_hijo("A", i8)
    i7.agregar_hijo("B", i8)
    i7.agregar_hijo("C", i8)

    i9 = Nodo(
        id_evento="I9",
        descripcion="Un ritual te exige corromper el alma más pura del reino para obtener poder absoluto. ¿Lo harás?",
        opciones={
            "A": "Sí, el poder lo justifica todo",
            "B": "Buscar otra alma menos pura",
            "C": "Intentar corromper tu propia alma en su lugar"
        },
        consecuencias={
            "A": (-25, 25, -18, 12),  # 👼 -25, 😈 +25, 🧍 -18, 💰 +12
            "B": (-12, 15, -8, 8),    # 👼 -12, 😈 +15, 🧍 -8, 💰 +8
            "C": (-20, 30, 10, 15)    # 👼 -20, 😈 +30, 🧍 +10, 💰 +15
        }
    )

    i8.agregar_hijo("A", i9)
    i8.agregar_hijo("B", i9)
    i8.agregar_hijo("C", i9)

    i10 = Nodo(
        id_evento="I10",
        descripcion="Establecer un sistema judicial basado en el miedo vs. mantener alguna apariencia de justicia.",
        opciones={
            "A": "Crear tribunales donde el miedo es la única ley",
            "B": "Juicios manipulados pero con apariencia legal",
            "C": "Permitir algo de justicia real para mantener orden"
        },
        consecuencias={
            "A": (-15, 20, -18, 8),  # 👼 -15, 😈 +20, 🧍 -18, 💰 +8
            "B": (-8, 15, -5, 12),    # 👼 -8, 😈 +15, 🧍 -5, 💰 +12
            "C": (5, -8, 12, -5)      # 👼 +5, 😈 -8, 🧍 +12, 💰 -5
        }
    )

    i9.agregar_hijo("A", i10)
    i9.agregar_hijo("B", i10)
    i9.agregar_hijo("C", i10)

    i11 = Nodo(
        id_evento="I11",
        descripcion="Un oráculo predice que tu reino será destruido por 'la luz más pura'. Puedes prevenirlo eliminando toda influencia angelical.",
        opciones={
            "A": "Comenzar una purga contra toda influencia celestial",
            "B": "Buscar formas de corromper las fuerzas celestiales",
            "C": "Ignorar la profecía y seguir tu curso"
        },
        consecuencias={
            "A": (-35, 25, -20, 10),  # 👼 -35, 😈 +25, 🧍 -20, 💰 +10
            "B": (-20, 20, -8, 5),    # 👼 -20, 😈 +20, 🧍 -8, 💰 +5
            "C": (0, 5, 5, 0)         # 👼 +0, 😈 +5, 🧍 +5, 💰 +0
        }
    )

    i10.agregar_hijo("A", i11)
    i10.agregar_hijo("B", i11)
    i10.agregar_hijo("C", i11)

    i12 = Nodo(
        id_evento="I12",
        descripcion="Los señores del infierno te ofrecen convertirte en uno de ellos: poder eterno, a cambio de tu humanidad.",
        opciones={
            "A": "Aceptar completamente la transformación",
            "B": "Aceptar pero mantener parte de tu humanidad",
            "C": "Rechazar la transformación pero mantener el pacto"
        },
        consecuencias={
            "A": (-25, 30, -15, 15), # 👼 -25, 😈 +30, 🧍 -15, 💰 +15
            "B": (-15, 20, -8, 10),   # 👼 -15, 😈 +20, 🧍 -8, 💰 +10
            "C": (-8, 15, 5, 12)      # 👼 -8, 😈 +15, 🧍 +5, 💰 +12
        }
    )

    i11.agregar_hijo("A", i12)
    i11.agregar_hijo("B", i12)
    i11.agregar_hijo("C", i12)

    return i1