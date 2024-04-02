#Autores : Steven Diaz Aquino 2021-0083 - Joseph rafael almanzar 2023-0696 - César Jesus Martinez Urbaez 2022-2132

import streamlit as st


# Función para procesar la entrada del usuario
def procesar_entrada(prompt):
    # Aquí se implementaría la lógica para interpretar la entrada del usuario y generar una respuesta adecuada
    opciones = {
    "info": "Aquí puedes\nencontrar información sobre horarios, tarifas, clases y más: https://www.gymbrothers.in/ Ubicación: Calle Principal #123, Ciudad Gimnasio, Estado ZonaFit , Propietario: Juan Pérez , Horario: Lunes a Viernes: 6:00 AM - 10:00 PM Sábados: 8:00 AM - 8:00 PM Domingos: 9:00 AM - 6:00 PM",
    "descanso": "¿Cuánto tiempo de descanso debo tomar entre series? aproximadamente entre 1 minutos",
    "hidratacion": "¿Cuánta agua debo beber durante mi entrenamiento? 2 litros de agua",
    "suplementos": "¿Cuales suplementos son para mejorar el rendimiento deportivo?: Multivitamínico: Para cubrir posibles deficiencias nutricionales , Creatina: Suplemento popular para mejorar el rendimiento deportivo, especialmente en ejercicios de fuerza , Proteína: Útil para la recuperación muscular después del ejercicio intenso.",
    "rutina": "¿Necesitas ayuda para crear una rutina de entrenamiento? Puedes Ver todas las recomendaciones de entremaniento escribiendo: rutina abdominales , rutina brazos , rutina_piernas , rutina_pecho , rutina_espalda",
    "rutina abdominales":  "claro aqui tienes un rutina sencilla de abdominales Posición inicial: acostado boca arriba con las rodillas dobladas y los pies apoyados en el suelo, manos detrás de la cabeza o cruzadas sobre el pecho. Movimiento: levanta los hombros y la parte superior de la espalda del suelo, contrayendo los abdominales. Exhala mientras realizas el movimiento. Realiza 3 series de 15-20 repeticiones",
    "rutina brazos": "Aquí te presentamos una rutina sencilla para trabajar los brazos, enfocándonos tanto en los bíceps como en los tríceps. Esta rutina puede realizarse en casa o en el gimnasio y no requiere mucho equipamiento: Flexiones de bíceps con mancuernas (Curls de bíceps con mancuernas) : Posición inicial: de pie con una hombrecuerna en cada mano, brazos extendidos a los lados del cuerpo con las palmas mirando hacia adelante.",
    "rutina piernas": "Claro aqui tienes una rutina de piernas sencilla:  Posición inicial: de pie, con los pies a la anchura de los hombros 2- Movimiento: flexiona las rodillas y baja el cuerpo como si fueras a sentarte en una silla, manteniendo la espalda recta, 3- ",
    "rutina pecho": "Aquí te presento una rutina sencilla para trabajar el pecho, que puedes realizar en casa o en el gimnasio. Esta rutina incluye ejercicios básicos y efectivos para desarrollar los músculos pectorales: Flexiones de pecho (Push-ups): Posición inicial: en posición de plancha, con las manos ligeramente más anchas que la anchura de los hombros y los pies juntos o separados a la anchura de los hombros para mayor estabilidad. Movimiento: baja el cuerpo flexionando los codos hasta que el pecho casi toque el suelo, manteniendo el cuerpo en línea recta desde la cabeza hasta los talones. Luego empuja el cuerpo hacia arriba hasta volver a la posición inicial. Realiza 3 series de 10-15 repeticiones",
    "rutina espalda": "Aquí te propongo una rutina sencilla para trabajar la espalda, que puedes realizar en casa o en el gimnasio. Esta rutina incluye ejercicios básicos para fortalecer los músculos de la espalda: Dominadas o Pull-ups : Posición inicial: colgado de una barra con las manos a la anchura de los hombros y las palmas mirando hacia adelante. Movimiento: levanta el cuerpo hacia la barra flexionando los codos y contrayendo los músculos de la espalda. Luego baje lentamente el cuerpo hasta volver a la posición inicial. Si no puedes realizar dominadas completas, puedes hacerlo con asistencia utilizando una banda elástica o una máquina de asistencia. Realiza 3 series de 5-10 repeticiones.",
    "suscripciones": "Plan Básico: $30 al mes , Incluye Acceso completo a las instalaciones del gimnasio durante horas de operación regulares Participación en clases grupales básicas, como aeróbicos y yoga Uso de equipos de cardio y pesas Plan Premiun: $50 al Mes. Incluye: Todos los beneficios del Plan Básico. Acceso ilimitado a todas las clases grupales, incluidas las clases especializadas como spinning o pilates. ",
}   

    # Respuesta por defecto
    respuesta = "Estoy procesando tu solicitud... ¡Un momento, por favor!"

    # Búsqueda de coincidencias en la entrada del usuario
    for palabra_clave, respuesta_especifica in opciones.items():
        if palabra_clave in prompt.lower():
            respuesta = respuesta_especifica
            break
    return respuesta  # Respuesta corregida

# Título y diseño
st.title("⛹️ Asistente virtual de Gymbrothers")
st.markdown("**¡Bienvenido a tu guía inteligente para un entrenamiento exitoso!**")

# Inicialización del estado de la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Visualización del historial de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mensaje de bienvenida inicial
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("¡Hola! Estoy aquí para ayudarte a alcanzar tus objetivos fitness en Gymbrothers. ¿Cómo puedo ayudarte hoy?")
        
    st.session_state.messages.append({"role": "user", "content": "¡Hola! Estoy aquí para ayudarte a alcanzar tus objetivos fitness en Gymbrothers. ¿Cómo puedo ayudarte hoy?"}) 
    st.session_state.first_message = False       

# Captura de la entrada del usuario
prompt = st.text_input("Escribe tu pregunta u objetivo aquí:")

# Procesamiento de la entrada y respuesta del asistente
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt}) 

    # Aquí se procesaría la entrada del usuario y se generaría la respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(procesar_entrada(prompt))  # Llamada a la función después de definirla
    st.session_state.messages.append({"role": "assistant", "content": procesar_entrada(prompt)})
