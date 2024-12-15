import streamlit as st  # usar a abreviação
from PIL import Image  # para importar imagens
import html 


with st.sidebar:                 #criar barra lateral - fica na esqurda td q esta dentro dele
    # logo e link ao clicar 
    st.logo('https://logospng.org/download/sus-sistema-Unico-de-saude/sus-sistema-unico-de-saude-2048.png',
    link = 'https://www.gov.br/saude/pt-br/sus')       
           
    # titulo
    st.title(" ***CALCULADORA IMC***")  
    
    #titulo da coluna 1
    st.header("O que é o IMC?")
    st.markdown("""O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. 
    Desenvolvido pelo polímata Lambert Quételet no fim do século XIX, trata-se de um método fácil e rápido para a avaliação do nível de gordura de cada pessoa, 
    sendo, por isso, um preditor internacional de obesidade adotado pela Organização Mundial da Saúde (OMS).
""")    # Permite por um texto grande
    

    # sistema 'abre e fecha'
    with st.expander ("***Por que devemos saber o nosso IMC?***", expanded = False):
        st.text('O IMC é um cálculo, adotado pela OMS (Organização Mundial da Saúde) e considerado um padrão internacional, para medir se o seu peso, considerando a altura, está dentro do normal. Dessa forma, é possível saber se a pessoa está acima, abaixo ou dentro de um peso saudável.')

    with st.expander ("***Como podemos combater a obesidade?***", expanded = False):
        st.text('A principal recomendação é ter uma alimentação baseada em alimentos in natura e minimamente processados, conforme orienta o Guia Alimentar para a População Brasileira. Junto a isso, evitar o consumo de alimentos ultraprocessados, que estão amplamente associados ao ganho de peso.')
 
    with st.expander ("***Medidas Corretas***", expanded = False):
        st.write("""
        - **Abaixo do peso**: IMC menor que 18.5 
        
        - **Peso ideal**: IMC entre 20 e 24.9
        
        - **Sobrepeso**: IMC entre 25 e 29.9
    
        
        - **Obesidade**: IMC entre 30 e 35
        
        - **Obesidade mórbida**: IMC acima de 35         
        """) # ** usando para deixar em negrito 
    

# CRIANDO A ENTRADA DE DADOS - PESO
# colunas 1 e 2

col1, col2 = st.columns(2)

# coluna 1:
with col1:
    
    col1.subheader("Calcule seu IMC:")   # titulo
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
            st.write(f"seu imc é: **{imc:.2f}**")
            st.write(f"sua classe é: {classe}")
            st.write(f"Comparação com o IMC ideal: **{imc_delta:.2f}**")    # o :.2f é para arredondar 

        else:
            st.error("Por favor, insire valores válidos!")  # mensagem de erro 
 
# tabela IMC 
# coluna 2
with col2:
    col2.subheader("Confira a tebela completa com as medidas IMC!")
    path = 'image.jpeg'
    imagem = Image.open(path)
    st.image(imagem, caption = "Dados do MEC", width = 500)

# INFORMAÇÕES 
st.header('Sobre o IMC', divider = 'blue')   # TITULO PARA INICiAR AS INFO

# TABS 
tab1, tab2= st.tabs(["Obesidade Infaltil", "Doenças Relacionadas"])

# conteudo dos tabs 
with tab1:
    st.header("Obesidade Infantil")
    st.markdown("""Obesidade infantil é uma condição em que uma criança tem um peso acima do normal para a sua idade e altura. De acordo com a OMS, uma criança é considerada obesa quando o seu IMC está acima do percentil 97 para o seu sexo e idade. 
A obesidade infantil é um problema de saúde pública complexo que pode levar a uma série de doenças crônicas, como:
Diabetes, Colesterol alto, Hipertensão, Doenças cardiovasculares, Câncer, Doenças respiratórias. 
Além disso, a obesidade infantil pode causar problemas psicológicos, como depressão, baixa autoestima e isolamento social. """)      
     # imagem sobre o tema:
    st.image('image1.jpeg', width = 900)
    
    with st.expander ("***A importancia de uma alimentação saudavel na infâcia***", expanded = False):
        st.text('A alimentação saudável na infância é crucial para o desenvolvimento físico e mental das crianças. Nutrientes adequados são essenciais para o crescimento, fortalecendo o sistema imunológico e prevenindo doenças. Hábitos alimentares saudáveis formados na infância ajudam a reduzir o risco de problemas como obesidade e diabetes na vida adulta. Além disso, uma dieta nutritiva melhora o desempenho escolar e as habilidades cognitivas. Investir em uma boa alimentação desde cedo garante que as crianças cresçam fortes, saudáveis e preparadas para o futuro.')
     
    with st.expander ("***Esportes na infância***", expanded = False):
        st.text('O esporte melhora a coordenação motora e aprimora a cognição de crianças e adolescentes. Os esportes auxiliam as crianças e adolescentes a desenvolverem as habilidades necessárias para praticá-los. Todo o conhecimento aprendido também possui um papel fundamental na capacidade cognitiva.')

with tab2:
    st.header("Doenças Relacionadas")
    st.text('O peso corporal é crucial para a saúde e pode afetar o desenvolvimento de doenças.')
    with st.expander("***Doenças causadas ao peso excessivo***"):
        st.text('O excesso de peso, ou obesidade, é um problema de saúde que vai além da estética, pois está associado a várias doenças e condições que afetam a qualidade de vida, como problemas cardiovasculares, diabetes tipo 2, dores nas articulações e doenças respiratórias. O acúmulo de gordura sobrecarrega o sistema cardiovascular, aumentando a pressão arterial e os níveis de colesterol, o que eleva o risco de doenças cardíacas e derrames. Além disso, a resistência à insulina causada pelo excesso de gordura abdominal pode levar ao diabetes tipo 2 e suas complicações. As articulações, especialmente joelhos e quadris, também sofrem com a pressão adicional, aumentando o risco de osteoartrite. A saúde respiratória é impactada, contribuindo para condições como apneia do sono. Não menos importante, a obesidade pode afetar a saúde mental, levando a questões como ansiedade e depressão devido ao estigma social e à baixa autoestima. Portanto, adotar um estilo de vida saudável com alimentação balanceada e atividade física regular é fundamental para prevenir essas doenças associadas ao excesso de peso e investir no bem-estar físico e emocional. ')
    with st.expander("***Doenças causadas pelo baixo peso***"):
        st.text('O baixo peso, ou desnutrição, pode ser tão prejudicial quanto o excesso de peso e está associado a uma série de problemas de saúde que afetam tanto o corpo quanto a mente. Indivíduos com baixo peso podem ter um sistema imunológico enfraquecido, tornando-os mais vulneráveis a infecções e doenças, já que a falta de nutrientes essenciais compromete as defesas naturais do organismo. Além disso, a desnutrição pode levar a deficiências vitamínicas e minerais, resultando em condições como anemia, que causa fadiga e fraqueza, e osteoporose, que aumenta o risco de fraturas ósseas. O baixo peso também pode impactar o desenvolvimento físico e cognitivo em crianças e adolescentes, resultando em dificuldades de aprendizado e crescimento inadequado. Em adultos, essa condição pode causar problemas de fertilidade e complicações durante a gravidez, tanto para a mãe quanto para o bebê. Além das implicações físicas, o baixo peso pode afetar a saúde mental, contribuindo para condições como depressão e ansiedade. Portanto, é fundamental buscar uma alimentação equilibrada e nutritiva para garantir que o corpo receba os nutrientes necessários para funcionar adequadamente e manter uma boa saúde geral. ')


# cabecalho com link
footer="""<style>
a:link , a:visited{
color: red;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: relative;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Desenvolvido por <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/isabelle-ferreira-316351300/" target="_blank">Isabelle Ferreira S</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
