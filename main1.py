import streamlit as st  # usar a abreviação


with st.sidebar:                 #criar barra lateral - fica na esqurda td q esta dentro dele
    st.title("calculadora IMC")  # titulo
    
    st.header("O que é o IMC?")
    st.markdown("""O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. Desenvolvido pelo polímata Lambert Quételet no fim do século XIX, trata-se de um método fácil e rápido para a avaliação do nível de gordura de cada pessoa, sendo, por isso, um preditor internacional de obesidade adotado pela Organização Mundial da Saúde (OMS).
""")    # Permite por um texto grande
    
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5   
    - **Peso ideal**: IMC entre 18.5 e 24.9
    - **Sobrepeso**: IMC entre 25 e 29.9
    - **Obesidade**: IMC entre 30 e 39.9
    - **Obesidade mórbida**: IMC acima de 40          
    """) # ** usando para deixar em negrito 
    
st.title("Calculadora IMC")   # titulo

# CRIANDO A ENTRADA DE DADOS - PESO

peso = st.number_input(label = "Digite o seu peso atual: ",min_value = 0.0, step = 0.10, format = "%.1f" )  # "label" é para criar o titulo do input // min_value é o valo9r minimo // format formata as casas decimais

altura = st.number_input(label = "Digite a sua altura atual em metros: ",min_value = 0.0, step = 0.10, format = "%.2f" )  

if st.button("calcular"):
    if peso > 0 and altura > 0: 
        imc = peso / (altura ** 2)
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal
        if imc < 18.2:
            classe = "Abaixo do peso"
        elif imc < 24.9:
            classe = "Peso ideal"
        elif imc < 29.9:
            classe = "Sobrepeso"
        elif imc < 40:
            classe = "Obesidade"
        else:
            classe = "Obsedidade morbida"
        st.success("Calculo feito com sucesso!")   # msg de acerto 

        # escrever valores 
        st.write(f"seu imc é: {imc:.2f}")
        st.write(f"sua classe é: {classe}")
        st.write(f"Comparação com o IMC ideal: **{imc_delta:.2f}**")    # o :.2f é para arredondar 

        # dividir a kinha em duas colunas
        col1, col2 = st.collumns(2)
        
        col1.metric("Classificação", classe, f"{imc_delta:.2f}", delta_color = "inverse")  
        
        col2.metric("IMC", f"{imc:.2f}", f"{imc_delta:.2f}", delta_color = "off")
        
        st.divider()
        
        st.image("./imc2.png")
        
    else:
        st.error("Por favor, insire valores válidos!")  # mensagem de erro 
        
        
    