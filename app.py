import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Valerapp", page_icon="👻", layout="wide")

email_address ="emailcontact@gmail.com"
url = "https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")

def load_lottie(url):
    response = requests.get(url)
    if response.status_code !=200:
        return None
    return response.json()

lottie = load_lottie(url)

# intro
with st.container():
    st.header("Hola, somos Valerapp 👋")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write("Somos unos apasionados de la tecnología y la innovación, especializados en IA")
    st.write("[Saber mas>](https://valerapp.com/)")

# sobre nosotros

with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 🔍")
        st.write(
            """
            Nuestro obetivo es poder aportar valor a los negocios ayudandolos a ahorrar tiempo y dinero.
            Seguramente te vamos a poder ayudar si:
            
            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usar herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo
            
            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***
            """
        )
        st.write("[Más sobre nosotros>](https://valerapp.com/about/)")
    with animation_column:
        st_lottie(lottie, height=400)

# Servicios

with st.container():
    st.write("---")
    st.header("Servicios 🛠")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/apps.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tu procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")
with st.container():    
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/automation.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Automatización de procesos")
        st.write(
            """
            Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras tareas más productivas.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/visualizacion.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Visualización de datos")
        st.write(
            """
            Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

# Contacto

with st.container():
    st.write("---")
    st.header("Contacta con nostros 📩")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder ="Tu nombre" required>
     <input type="email" name="email" placeholder ="Tu email" required>
     <textarea type="message" name="message" placeholder ="Tu mensaje aquí" required></textarea>
     <button type="submit">Enviar</button>
    </form>
    """
    
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with rigth_column:
        st.empty()
