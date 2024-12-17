# 📊👾 Calculadora de IMC

## 📜 Descrição do Projeto:
Desenvolvido com a biblioteca Streamlit, este projeto apresenta uma página interativa dedicada à calculadora de **IMC (Índice de Massa Corporal)**. Além de permitir que os usuários calculem seu IMC de forma simples e rápida, a aplicação oferece uma variedade de informações relevantes sobre o tema. 

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem principal para lógica.
- **Streamlit**: Framework para criação de interfaces web interativas.
- **Pillow**: Biblioteca de manipulação de imagens.
- **HTML**: Utilizado para o footer

## 💻 Como Rodar o Projeto

### Passo a Passo:
1. Clone este repositório:
```bash
git clone (https://github.com/Isabelle-maximow/Calculadora-Streamlit.git)
cd calculadora-Streamlit
```
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
.venv/Scripts/activate  # Para Windows
venv/bin/activate  # Para Linux/Mac

```

3. Instale as dependências:
```bash
pip install streamlit 
```

4. Inicie o aplicativo
```bash	
streamlit run main1.py
```
## Recomendações
- Para uma melhor visualização recomendo alterar a aparencia e o tema. Você pode fazer isso indo em:
  1. Settings
  2. Selecionar o modo "Wilde mode"
  3. Em theme, selecionar opção "Light" 

  
## 📝 Funcionalidades
- Entrada de dados: Permite que o usuário insira seu peso (em kg) e altura (em metros).
- Comparação com IMC ideal: O valor calculado é comparado com o IMC ideal de 21.7.
- Cálculo do IMC: O aplicativo calcula o IMC com base nos dados fornecidos e classifica em uma das categorias abaixo.
- Classificação do IMC:
    - Abaixo do peso
    - Peso ideal
    - Sobrepeso
    - Obesidade
    - Obesidade mórbida
