import streamlit as st  # usar a abreviação
from PIL import Image  # para importar imagens

with st.sidebar:                 #criar barra lateral - fica na esqurda td q esta dentro dele
    # logo e link ao clicar 
    st.logo('https://logospng.org/wp-content/uploads/sus-sistema-unico-de-saude.png',
    link = 'https://www.gov.br/saude/pt-br/sus' )       
           
    # titulo
    st.title("calculadora IMC")  
    
    #titulo da coluna 1
    st.header("O que é o IMC?")
    st.markdown("""O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. Desenvolvido pelo polímata Lambert Quételet no fim do século XIX, trata-se de um método fácil e rápido para a avaliação do nível de gordura de cada pessoa, sendo, por isso, um preditor internacional de obesidade adotado pela Organização Mundial da Saúde (OMS).
""")    # Permite por um texto grande
    
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5 
      
    - **Peso ideal**: IMC entre 20 e 24.9
    
    - **Sobrepeso**: IMC entre 25 e 29.9
    
    - **Obesidade**: IMC entre 30 e 35
    
    - **Obesidade mórbida**: IMC acima de 35         
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
        if imc < 18.5:
            classe = "Abaixo do peso"
        elif imc > 20 and imc < 24.9 :
            classe = "Peso ideal"
        elif imc > 25 and imc < 29.9:
            classe = "Sobrepeso"
        elif imc > 30 and imc < 35:
            classe = "Obesidade"
        else:
            classe = "Obsedidade morbida"
        st.success("Calculo feito com sucesso!")   # msg de acerto 

        # escrever valores 
        st.write(f"seu imc é: {imc:.2f}")
        st.write(f"sua classe é: {classe}")
        st.write(f"Comparação com o IMC ideal: **{imc_delta:.2f}**")    # o :.2f é para arredondar 

        # dividir a kinha em duas colunas
        col1, col2 = st.columns(2)
        
        col1.metric("Classificação", classe)  
        col2.metric("IMC", f"{imc:.2f}")
            
        st.divider()

    else:
        st.error("Por favor, insire valores válidos!")  # mensagem de erro 
 

# INOFRMAÇÕES 
st.header('Sobre o IMC', divider = 'blue')   # TITULO PARA INICAR AS INFO

# tabela IMC 
path = 'H:/calculadora=imc/WhatsApp Image 2024-12-06 at 14.41.49.jpeg'
imagem = Image.open(path)
st.image(imagem, caption = "Dados do MEC", width = 830)

# sistema 'abre e fecha'
with st.expander ("***Por que devemos saber o nosso IMC?***", expanded = False):
    st.text('O IMC é um cálculo, adotado pela OMS (Organização Mundial da Saúde) e considerado um padrão internacional, para medir se o seu peso, considerando a altura, está dentro do normal. Dessa forma, é possível saber se a pessoa está acima, abaixo ou dentro de um peso saudável.')

with st.expander ("***Como podemos combater a obesidade?***", expanded = False):
     st.text('A principal recomendação é ter uma alimentação baseada em alimentos in natura e minimamente processados, conforme orienta o Guia Alimentar para a População Brasileira. Junto a isso, evitar o consumo de alimentos ultraprocessados, que estão amplamente associados ao ganho de peso.')
 
# TABS 
tab1, tab2= st.tabs(["Obesidade Infaltil", "Doenças Relacionadas"])

# conteudo dos tabs 
with tab1:
    st.header("Obesidade Infaltil")
    # imagem sobre o tema:
    st.image('c:/Users/24271526/Downloads/WhatsApp Image 2024-12-06 at 14.40.40.jpeg', width = 10000)
    st.markdown("""Obesidade infantil é uma condição em que uma criança tem um peso acima do normal para a sua idade e altura. De acordo com a OMS, uma criança é considerada obesa quando o seu IMC está acima do percentil 97 para o seu sexo e idade. 
A obesidade infantil é um problema de saúde pública complexo que pode levar a uma série de doenças crônicas, como:
Diabetes, Colesterol alto, Hipertensão, Doenças cardiovasculares, Câncer, Doenças respiratórias. 
Além disso, a obesidade infantil pode causar problemas psicológicos, como depressão, baixa autoestima e isolamento social. """)      
    
    with st.expander ("***A importancia de uma alimentação saudavel na infâcia***", expanded = False):
        st.text('Segundo Sônia Venâncio, do Instituto de Saúde Pública da Secretaria Estadual de Saúde de São Paulo, a alimentação adequada e saudável nos primeiros 2 anos de vida vai garantir que a criança receba todos os nutrientes necessários para o seu crescimento e também o seu desenvolvimento.')
     
    with st.expander ("***Esportes na infância***", expanded = False):
        st.text('O esporte melhora a coordenação motora e aprimora a cognição de crianças e adolescentes. Os esportes auxiliam as crianças e adolescentes a desenvolverem as habilidades necessárias para praticá-los. Todo o conhecimento aprendido também possui um papel fundamental na capacidade cognitiva.')

with tab2:
    st.header("Doenças Relacionadas")
    with st.expander("***Doenças causadas ao peso excessivo***"):
        st.text('O excesso de peso, ou obesidade, é um problema de saúde que vai além da estética, pois está associado a várias doenças e condições que afetam a qualidade de vida, como problemas cardiovasculares, diabetes tipo 2, dores nas articulações e doenças respiratórias. O acúmulo de gordura sobrecarrega o sistema cardiovascular, aumentando a pressão arterial e os níveis de colesterol, o que eleva o risco de doenças cardíacas e derrames. Além disso, a resistência à insulina causada pelo excesso de gordura abdominal pode levar ao diabetes tipo 2 e suas complicações. As articulações, especialmente joelhos e quadris, também sofrem com a pressão adicional, aumentando o risco de osteoartrite. A saúde respiratória é impactada, contribuindo para condições como apneia do sono. Não menos importante, a obesidade pode afetar a saúde mental, levando a questões como ansiedade e depressão devido ao estigma social e à baixa autoestima. Portanto, adotar um estilo de vida saudável com alimentação balanceada e atividade física regular é fundamental para prevenir essas doenças associadas ao excesso de peso e investir no bem-estar físico e emocional. ')
    with st.expander("***Doenças causadas pelo baixo peso***"):
        st.text('O baixo peso, ou desnutrição, pode ser tão prejudicial quanto o excesso de peso e está associado a uma série de problemas de saúde que afetam tanto o corpo quanto a mente. Indivíduos com baixo peso podem ter um sistema imunológico enfraquecido, tornando-os mais vulneráveis a infecções e doenças, já que a falta de nutrientes essenciais compromete as defesas naturais do organismo. Além disso, a desnutrição pode levar a deficiências vitamínicas e minerais, resultando em condições como anemia, que causa fadiga e fraqueza, e osteoporose, que aumenta o risco de fraturas ósseas. O baixo peso também pode impactar o desenvolvimento físico e cognitivo em crianças e adolescentes, resultando em dificuldades de aprendizado e crescimento inadequado. Em adultos, essa condição pode causar problemas de fertilidade e complicações durante a gravidez, tanto para a mãe quanto para o bebê. Além das implicações físicas, o baixo peso pode afetar a saúde mental, contribuindo para condições como depressão e ansiedade. Portanto, é fundamental buscar uma alimentação equilibrada e nutritiva para garantir que o corpo receba os nutrientes necessários para funcionar adequadamente e manter uma boa saúde geral. ')