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
git clone https://github.com/seu-usuario/calculadora-Streamlit.git
cd calculadora-Streamlit
```
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
source .venv/Scripts/activate  # Para Windows
source venv/bin/activate  # Para Linux/Mac

```

3. Instale as dependências:
```bash
pip install streamlit
pip install pillow
```

4. Inicie o aplicativo
```bash	
streamlit run main1.py
```

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
