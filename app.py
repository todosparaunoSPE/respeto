# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:24:47 2024

@author: jperezr
"""

import streamlit as st

# Título del proyecto
st.title("Proyecto: Campaña de Respeto en el Trabajo")

# Introducción
st.header("Introducción")
st.write("""
El respeto en el lugar de trabajo es esencial para crear un ambiente laboral saludable, productivo y colaborativo. Un entorno de respeto no solo mejora la moral y la satisfacción de los empleados, sino que también reduce el riesgo de conflictos, bullying y otros comportamientos negativos. Este proyecto tiene como objetivo diseñar e implementar una campaña de respeto en nuestra organización, fomentando una cultura donde todos los empleados sean tratados con dignidad y consideración.
""")

# Objetivo General
st.header("Objetivo General")
st.write("""
Promover y establecer una cultura de respeto en el lugar de trabajo, asegurando que todos los empleados, independientemente de su jerarquía, reciban un trato cordial y digno, contribuyendo así a un entorno laboral positivo y productivo.
""")

# Objetivos Específicos
st.header("Objetivos Específicos")
st.write("""
1. Evaluar el estado actual del respeto en la organización mediante encuestas y entrevistas.
2. Obtener el compromiso y apoyo de la alta dirección para la campaña.
3. Desarrollar y comunicar un código de conducta claro y políticas de quejas.
4. Implementar programas de capacitación y talleres sobre el respeto y la resolución de conflictos.
5. Reconocer y premiar comportamientos ejemplares de respeto.
6. Monitorear y evaluar continuamente el progreso de la campaña.
7. Crear espacios de diálogo para el feedback y la mejora continua.
8. Promover la inclusión y la diversidad en el lugar de trabajo.
""")

# Metodología
st.header("Metodología")

# Sub-secciones de la Metodología
metodologia = {
    "1. Evaluación Inicial": [
        "Encuestas y Entrevistas: Realizar encuestas anónimas y entrevistas para entender la percepción y el estado actual del respeto en la organización.",
        "Análisis de Resultados: Identificar áreas problemáticas y establecer una línea base para medir el progreso."
    ],
    "2. Compromiso de la Dirección": [
        "Reuniones Informativas: Realizar reuniones con la alta dirección para asegurar su apoyo y compromiso.",
        "Declaraciones Oficiales: Emitir comunicados oficiales donde la dirección exprese su respaldo a la campaña."
    ],
    "3. Establecimiento de Políticas y Normas": [
        "Código de Conducta: Desarrollar un código de conducta que establezca las expectativas de respeto y las consecuencias de no cumplirlas.",
        "Políticas de Quejas: Implementar procedimientos claros para reportar y manejar quejas de falta de respeto y bullying."
    ],
    "4. Comunicación y Educación": [
        "Lanzamiento de la Campaña: Anunciar la campaña a través de correos electrónicos, reuniones y materiales visuales como posters y boletines.",
        "Talleres y Seminarios: Organizar talleres y seminarios sobre la importancia del respeto y cómo identificar y responder a comportamientos irrespetuosos."
    ],
    "5. Entrenamiento Continuo": [
        "Capacitación Regular: Proporcionar capacitación continua sobre habilidades de comunicación, resolución de conflictos y diversidad e inclusión.",
        "Entrenamiento de Líderes: Entrenar a los líderes para manejar conflictos y fomentar un ambiente de respeto."
    ],
    "6. Incentivos y Reconocimientos": [
        "Programas de Reconocimiento: Implementar programas de reconocimiento para empleados que demuestren comportamientos ejemplares de respeto.",
        "Incentivos: Ofrecer incentivos para equipos o departamentos que muestren mejoras significativas en el comportamiento respetuoso."
    ],
    "7. Monitorización y Evaluación": [
        "Evaluaciones Periódicas: Realizar evaluaciones regulares para medir el progreso de la campaña y hacer ajustes según sea necesario.",
        "Encuestas de Seguimiento: Utilizar encuestas de seguimiento para obtener feedback continuo de los empleados."
    ],
    "8. Crear Espacios de Diálogo": [
        "Reuniones de Feedback: Organizar reuniones periódicas donde los empleados puedan expresar sus preocupaciones y sugerencias sobre el respeto en el lugar de trabajo.",
        "Comités de Bienestar: Establecer comités de bienestar dedicados a fomentar y mantener una cultura de respeto."
    ],
    "9. Promover la Inclusión y la Diversidad": [
        "Eventos de Diversidad: Organizar eventos y actividades que celebren la diversidad y promuevan la inclusión.",
        "Perspectiva de Género: Asegurar que todas las políticas y prácticas promuevan la igualdad de género y la no discriminación."
    ],
    "10. Refuerzo Continuo": [
        "Comunicación Constante: Mantener la campaña viva con recordatorios periódicos y actualizaciones.",
        "Adaptación y Mejora: Ajustar la campaña según los resultados de las evaluaciones y el feedback recibido."
    ]
}

# Desplegar metodología en secciones expandibles
for key, value in metodologia.items():
    with st.expander(key):
        for item in value:
            st.write("- " + item)

# Cronograma
st.header("Cronograma")
cronograma = {
    "Fase": ["Evaluación Inicial", "Compromiso de la Dirección", "Políticas y Normas", "Comunicación y Educación", 
             "Entrenamiento Continuo", "Incentivos y Reconocimientos", "Monitorización y Evaluación", "Espacios de Diálogo", 
             "Inclusión y Diversidad", "Refuerzo Continuo"],
    "Actividades": ["Encuestas y entrevistas, análisis de resultados", "Reuniones informativas, declaraciones oficiales", 
                    "Desarrollo de código de conducta y políticas de quejas", "Lanzamiento de campaña, talleres y seminarios", 
                    "Capacitaciones regulares y entrenamiento de líderes", "Implementación de programas de reconocimiento", 
                    "Evaluaciones periódicas, encuestas de seguimiento", "Reuniones de feedback, establecimiento de comités", 
                    "Eventos de diversidad, políticas de igualdad", "Comunicación constante, adaptación y mejora"],
    "Duración": ["1 mes", "2 semanas", "1 mes", "2 meses", "6 meses", "3 meses", "Continuo", "Continuo", "Continuo", "Continuo"]
}

import pandas as pd

df_cronograma = pd.DataFrame(cronograma)
st.table(df_cronograma)

# Presupuesto
st.header("Presupuesto")
presupuesto = {
    "Concepto": ["Encuestas y Análisis", "Talleres y Seminarios", "Materiales de Comunicación", "Capacitación", 
                 "Incentivos y Reconocimientos", "Eventos de Diversidad", "Evaluaciones y Monitoreo"],
    "Costo ($)": [2000, 5000, 1000, 4000, 3000, 2000, 2000]
}

df_presupuesto = pd.DataFrame(presupuesto)
st.table(df_presupuesto)

st.write("**Total:** $19,000")

# Indicadores de Éxito
st.header("Indicadores de Éxito")
st.write("""
- Reducción en quejas de falta de respeto y bullying.
- Aumento en la satisfacción laboral de los empleados.
- Mayor participación en programas de capacitación y eventos de diversidad.
- Feedback positivo en encuestas de seguimiento.
""")

# Conclusión
st.header("Conclusión")
st.write("""
Implementar una campaña de respeto en el trabajo es un paso esencial para construir un ambiente laboral positivo y productivo. Con el compromiso de todos los niveles de la organización y una estrategia bien definida, es posible fomentar una cultura de respeto que beneficie tanto a los empleados como a la organización en su conjunto.
""")


# Créditos del creador
st.sidebar.markdown("---")
st.sidebar.text("Creado por:")
st.sidebar.markdown("<span style='color: yellow;'>jahoperi</span>", unsafe_allow_html=True)    
