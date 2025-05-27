from nodo import Nodo

def construir_camino_celestial():
    # Definición de los eventos del camino celestial basados en la historia
    c1 = Nodo(
        id_evento="C1",
        descripcion="Un grupo de ciudadanos practica rituales considerados impuros. El clero exige acción inmediata.",
        opciones={
            "A": "Ejecutar públicamente a los líderes herejes",
            "B": "Ofrecer reeducación espiritual",
            "C": "Investigar primero si realmente son herejías peligrosas"
        },
        consecuencias={
            "A": (15, -8, -18, 8),    # 👼 +15, 😈 -8, 🧍 -18, 💰 +8
            "B": (20, -12, 8, -15),    # 👼 +20, 😈 -12, 🧍 +8, 💰 -15
            "C": (12, 3, 12, -8)       # 👼 +12, 😈 +3, 🧍 +12, 💰 -8
        }
    )

    c2 = Nodo(
        id_evento="C2",
        descripcion="Un supuesto santo realiza 'milagros' que atraen multitudes. Algunos sospechan que usa trucos.",
        opciones={
            "A": "Investigar discretamente la veracidad",
            "B": "Apoyar públicamente al santo",
            "C": "Denunciarlo como charlatán sin evidencia"
        },
        consecuencias={
            "A": (8, 5, 8, -8),       # 👼 +8, 😈 +5, 🧍 +8, 💰 -8
            "B": (15, -8, 12, 5),     # 👼 +15, 😈 -8, 🧍 +12, 💰 +5
            "C": (5, 3, -12, 3)       # 👼 +5, 😈 +3, 🧍 -12, 💰 +3
        }
    )

    c1.agregar_hijo("A", c2)
    c1.agregar_hijo("B", c2)
    c1.agregar_hijo("C", c2)

    c3 = Nodo(
        id_evento="C3",
        descripcion="Los sacerdotes solicitan construir un templo monumental para glorificar a los cielos. Las arcas están ajustadas.",
        opciones={
            "A": "Donar todo el oro disponible",
            "B": "Implementar un impuesto sagrado",
            "C": "Construir un templo más modesto pero incluir servicios comunitarios"
        },
        consecuencias={
            "A": (25, -8, -15, -30),  # 👼 +25, 😈 -8, 🧍 -15, 💰 -30
            "B": (15, -5, -12, -12),   # 👼 +15, 😈 -5, 🧍 -12, 💰 -12
            "C": (18, 0, 15, -20)      # 👼 +18, 😈 +0, 🧍 +15, 💰 -20
        }
    )

    c2.agregar_hijo("A", c3)
    c2.agregar_hijo("B", c3)
    c2.agregar_hijo("C", c3)

    c4 = Nodo(
        id_evento="C4",
        descripcion="Los clérigos proponen establecer una inquisición para erradicar la corrupción espiritual del reino.",
        opciones={
            "A": "Establecer una inquisición con plenos poderes",
            "B": "Crear tribunales religiosos con supervisión real",
            "C": "Rechazar la inquisición pero fortalecer la educación religiosa"
        },
        consecuencias={
            "A": (20, -15, -25, 5),   # 👼 +20, 😈 -15, 🧍 -25, 💰 +5
            "B": (15, -8, -12, -8),    # 👼 +15, 😈 -8, 🧍 -12, 💰 -8
            "C": (8, 3, 12, -12)       # 👼 +8, 😈 +3, 🧍 +12, 💰 -12
        }
    )

    c3.agregar_hijo("A", c4)
    c3.agregar_hijo("B", c4)
    c3.agregar_hijo("C", c4)

    c5 = Nodo(
        id_evento="C5",
        descripcion="Tus caballeros capturan a un demonio menor. Te ofrece secretos valiosos a cambio de su vida.",
        opciones={
            "A": "Ejecutarlo inmediatamente",
            "B": "Interrogarlo antes de la ejecución",
            "C": "Intentar purificar su alma mediante rituales"
        },
        consecuencias={
            "A": (18, -20, 5, 0),      # 👼 +18, 😈 -20, 🧍 +5, 💰 +0
            "B": (8, -12, 3, 12),      # 👼 +8, 😈 -12, 🧍 +3, 💰 +12
            "C": (12, -8, -5, -8)      # 👼 +12, 😈 -8, 🧍 -5, 💰 -8
        }
    )

    c4.agregar_hijo("A", c5)
    c4.agregar_hijo("B", c5)
    c4.agregar_hijo("C", c5)

    c6 = Nodo(
        id_evento="C6",
        descripcion="Una maldición sobrenatural afecta a los más devotos. Solo rituales impuros podrían curarla.",
        opciones={
            "A": "Mantener la pureza y aceptar las víctimas como mártires",
            "B": "Permitir rituales impuros solo esta vez",
            "C": "Buscar una cura divina mediante oración masiva"
        },
        consecuencias={
            "A": (25, -12, -20, 0),   # 👼 +25, 😈 -12, 🧍 -20, 💰 +0
            "B": (-8, 12, 15, -12),    # 👼 -8, 😈 +12, 🧍 +15, 💰 -12
            "C": (20, -8, 8, -15)      # 👼 +20, 😈 -8, 🧍 +8, 💰 -15
        }
    )

    c5.agregar_hijo("A", c6)
    c5.agregar_hijo("B", c6)
    c5.agregar_hijo("C", c6)

    c7 = Nodo(
        id_evento="C7",
        descripcion="Un hombre proclama ser enviado divino y contradice las enseñanzas establecidas. Gana seguidores.",
        opciones={
            "A": "Arrestarlo como hereje",
            "B": "Permitir que predique pero bajo vigilancia",
            "C": "Someterlo a pruebas divinas públicas"
        },
        consecuencias={
            "A": (12, -5, -15, 3),    # 👼 +12, 😈 -5, 🧍 -15, 💰 +3
            "B": (8, 8, 8, -5),        # 👼 +8, 😈 +8, 🧍 +8, 💰 -5
            "C": (15, 5, 12, -8)       # 👼 +15, 😈 +5, 🧍 +12, 💰 -8
        }
    )

    c6.agregar_hijo("A", c7)
    c6.agregar_hijo("B", c7)
    c6.agregar_hijo("C", c7)

    c8 = Nodo(
        id_evento="C8",
        descripcion="Se descubre una reliquia sagrada en territorio enemigo. Recuperarla requeriría guerra o diplomacia.",
        opciones={
            "A": "Declarar guerra santa para recuperarla",
            "B": "Negociar su compra o intercambio",
            "C": "Declararla perdida y crear una nueva tradición"
        },
        consecuencias={
            "A": (18, -8, -12, -25),   # 👼 +18, 😈 -8, 🧍 -12, 💰 -25
            "B": (8, 5, 8, -20),       # 👼 +8, 😈 +5, 🧍 +8, 💰 -20
            "C": (12, 0, 15, 0)        # 👼 +12, 😈 +0, 🧍 +15, 💰 +0
        }
    )

    c7.agregar_hijo("A", c8)
    c7.agregar_hijo("B", c8)
    c7.agregar_hijo("C", c8)

    c9 = Nodo(
        id_evento="C9",
        descripcion="Un profeta anuncia que un niño ha nacido con un destino trágico: si vive, traerá caos; si muere, salvará el mundo.",
        opciones={
            "A": "Buscar al elegido para protegerlo de su destino",
            "B": "Preparar su sacrificio cuando llegue el momento",
            "C": "Cuestionar la validez de la profecía"
        },
        consecuencias={
            "A": (12, 3, 8, -8),       # 👼 +12, 😈 +3, 🧍 +8, 💰 -8
            "B": (20, -5, -15, 0),     # 👼 +20, 😈 -5, 🧍 -15, 💰 +0
            "C": (-8, 3, 15, 0)        # 👼 -8, 😈 +3, 🧍 +15, 💰 +0
        }
    )

    c8.agregar_hijo("A", c9)
    c8.agregar_hijo("B", c9)
    c8.agregar_hijo("C", c9)

    c10 = Nodo(
        id_evento="C10",
        descripcion="Los ciudadanos reportan pequeños milagros diarios. ¿Es genuino despertar espiritual o histeria colectiva?",
        opciones={
            "A": "Proclamar una era de milagros",
            "B": "Investigar cada caso cuidadosamente",
            "C": "Desalentar las supersticiones pero respetar la fe genuina"
        },
        consecuencias={
            "A": (25, -12, 10, -5),   # 👼 +25, 😈 -12, 🧍 +10, 💰 -5
            "B": (15, 5, 15, -12),     # 👼 +15, 😈 +5, 🧍 +15, 💰 -12
            "C": (12, 3, 12, 0)        # 👼 +12, 😈 +3, 🧍 +12, 💰 +0
        }
    )

    c9.agregar_hijo("A", c10)
    c9.agregar_hijo("B", c10)
    c9.agregar_hijo("C", c10)

    c11 = Nodo(
        id_evento="C11",
        descripcion="Un demonio invisible tienta a tus nobles con promesas de riqueza. ¿Cómo reaccionas?",
        opciones={
            "A": "Organizar exorcismos masivos públicos",
            "B": "Investigar en secreto sin alarmar al pueblo",
            "C": "Fortalecer la educación espiritual de los nobles"
        },
        consecuencias={
            "A": (15, -15, -8, 3),    # 👼 +15, 😈 -15, 🧍 -8, 💰 +3
            "B": (3, -8, 5, 8),        # 👼 +3, 😈 -8, 🧍 +5, 💰 +8
            "C": (18, -12, 8, -12)     # 👼 +18, 😈 -12, 🧍 +8, 💰 -12
        }
    )

    c10.agregar_hijo("A", c11)
    c10.agregar_hijo("B", c11)
    c10.agregar_hijo("C", c11)

    c12 = Nodo(
        id_evento="C12",
        descripcion="El clero se divide en dos facciones con interpretaciones diferentes de las escrituras sagradas.",
        opciones={
            "A": "Apoyar a la facción más tradicional",
            "B": "Intentar reconciliar ambas facciones",
            "C": "Crear un concilio ecuménico para resolver las diferencias"
        },
        consecuencias={
            "A": (20, -8, -15, 5),     # 👼 +20, 😈 -8, 🧍 -15, 💰 +5
            "B": (15, 0, 12, -15),     # 👼 +15, 😈 +0, 🧍 +12, 💰 -15
            "C": (12, 5, 18, -20)      # 👼 +12, 😈 +5, 🧍 +18, 💰 -20
        }
    )

    c11.agregar_hijo("A", c12)
    c11.agregar_hijo("B", c12)
    c11.agregar_hijo("C", c12)

    c13 = Nodo(
        id_evento="C13",
        descripcion="Los ángeles descienden y exigen que elimines toda sombra de tu reino, incluso emociones humanas 'impuras'.",
        opciones={
            "A": "Aceptar completamente su voluntad",
            "B": "Aceptar, pero con compasión hacia la naturaleza humana",
            "C": "Rechazar su demanda extrema en nombre del libre albedrío"
        },
        consecuencias={
            "A": (35, -25, -30, 0),   # 👼 +35, 😈 -25, 🧍 -30, 💰 +0
            "B": (25, -18, -5, -8),    # 👼 +25, 😈 -18, 🧍 -5, 💰 -8
            "C": (-5, 8, 15, 0)        # 👼 -5, 😈 +8, 🧍 +15, 💰 +0
        }
    )

    c12.agregar_hijo("A", c13)
    c12.agregar_hijo("B", c13)
    c12.agregar_hijo("C", c13)

    return c1