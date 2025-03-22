import streamlit as st

def main():
    # Inicialize o app
    header = st.container()

    # Adicione o título ao container
    with header:
        st.title('Hello, World!')
        st.write('Alo, Mundo!')

if __name__ == "__main__":
    main()