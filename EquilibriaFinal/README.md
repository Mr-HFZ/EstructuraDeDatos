
# 👑 Reino de Equilibria — Versión Épica Expandida

**Reino de Equilibria** es un juego narrativo interactivo con una interfaz gráfica en Python (usando `tkinter`), donde gobiernas un reino balanceando cuatro fuerzas fundamentales: 👼 Ángeles, 😈 Demonios, 👥 Pueblo y 💰 Tesoro. Cada decisión que tomas afecta el equilibrio del reino y lleva a diferentes finales.

## 🎮 Características del juego

- 🌳 Árbol de decisiones ramificado con múltiples caminos (Celestial, Humanista, Infernal)
- 📈 Sistema de estadísticas que afecta el destino del reino
- 📜 Registro de decisiones importantes tomadas por el jugador
- 🧠 Estado del reino dinámico: Equilibrio, Orden, Caos, Prosperidad o Decadencia
- 🔄 Rejugabilidad con múltiples finales desbloqueables
- 🎨 Interfaz gráfica con barras de progreso animadas y narrativa visual

---

## 🛠️ Requisitos

- Python 3.8 o superior
- Módulos estándar (`tkinter`, `random`)

> *Nota: `tkinter` viene preinstalado con la mayoría de instalaciones de Python. Si no lo tienes, instálalo con tu gestor de paquetes.*

---

## 🚀 Cómo ejecutar el juego

1. Clona este repositorio o descarga los archivos:

   ```bash
   git clone https://github.com/tuusuario/reino-de-equilibria.git
   cd reino-de-equilibria
   ```

2. Ejecuta el archivo principal:

   ```bash
   python main.py
   ```

   > Asegúrate de tener todos los archivos de caminos como `Celestial.py`, `Humanista.py`, `Infernal.py`, más `main.py` y clases auxiliares.

---

## 🎯 Objetivo

Gobierna tu reino tomando decisiones sabias que afectarán los valores de:

- 👼 **Ángeles** (Orden, espiritualidad, divinidad)
- 😈 **Demonios** (Caos, poder oscuro, ambición)
- 👥 **Pueblo** (Felicidad y apoyo popular)
- 💰 **Tesoro** (Economía y recursos del reino)

El equilibrio entre estas fuerzas determina el **estado del reino** y, finalmente, el **final de tu reinado**.

---

## 📊 Estados del Reino

El estado actual del reino se calcula dinámicamente con base en los valores de las estadísticas. Puede estar en:

- ⚖️ **Equilibrio** – Todas las fuerzas están relativamente balanceadas
- ✨ **Orden** – Dominan los ángeles
- 🔥 **Caos** – Dominan los demonios
- 🌟 **Prosperidad** – El pueblo y el tesoro están altos
- 💀 **Decadencia** – Una estadística ha bajado peligrosamente

---

## 🧩 Finales posibles

Basado en cómo terminas tus estadísticas, obtendrás uno de estos finales:

- 🌟 Equilibrio Perfecto  
- 💀 Colapso Total  
- 👼 Reino Celestial  
- 😈 Señor de las Tinieblas  
- 👥 República del Pueblo  
- 💰 Edad Dorada  
- ⚔️ Guerra Eterna  
- 👑 Tirano Opulento  
- ⚖️ Reino en la Encrucijada  
- 🔥 Caos Ascendente  
- ✨ Orden Perpetuo  
- 🌟 Edad de Oro  
- 🌙 Ocaso del Reino

Cada uno con una narrativa única que refleja tu estilo de gobierno.

---

## 🧠 Componentes principales del código

### `main.py`
Contiene la clase principal `ReinoDeEquilibriaGUI` que gestiona:

- Carga y navegación del árbol de decisiones  
- Aplicación de efectos a estadísticas  
- Actualización del estado visual y narrativo  
- Registro de decisiones  
- Determinación y visualización del final del juego

### `Celestial.py`, `Humanista.py`, `Infernal.py`
Definen las rutas de decisiones y eventos de cada camino filosófico.  
Son cargados dentro del árbol general de decisiones (`ArbolDecisiones`).

### `arbol_decisiones.py`
Contiene las clases `Nodo` y `ArbolDecisiones`.  
Define la estructura narrativa del juego y permite avanzar según elecciones.

---

## 💡 Ideas futuras

- Guardado y carga de partidas
- Integración con audio y efectos visuales
- Expansión con rutas adicionales o eventos aleatorios
- Traducción a varios idiomas

---

## 📜 Licencia

MIT License — Puedes usar, modificar y distribuir libremente este proyecto con atribución.

---

## 🙌 Autores

- **Hener Florez**  
- **Mateo Botero**
