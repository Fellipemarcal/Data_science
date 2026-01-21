# 📊 Reconhecimento de Dígitos Manuscritos com TensorFlow (MNIST)

<p align="center">
  <strong>Projeto de Machine Learning para reconhecimento de números escritos à mão utilizando TensorFlow e Keras</strong>
</p>

<hr>

## 📌 Sobre o Projeto

Este projeto tem como objetivo desenvolver, treinar e testar um modelo de **Machine Learning** capaz de reconhecer dígitos manuscritos (0 a 9) a partir de imagens em escala de cinza, utilizando o famoso dataset **MNIST**.

O foco é demonstrar todo o fluxo de um projeto de **Inteligência Artificial**, desde o pré-processamento dos dados até a predição de imagens desenhadas manualmente.

<hr>

## 🧠 Tecnologias Utilizadas

<ul>
  <li>Python 3</li>
  <li>TensorFlow / Keras</li>
  <li>NumPy</li>
  <li>Matplotlib</li>
  <li>Jupyter Notebook</li>
</ul>

<hr>

## 📂 Estrutura do Repositório

```bash
📁 reconhecimento-digitos-mnist
 ├── treinamento.ipynb        # Treinamento do modelo
 ├── utl_modelo.ipynb         # Testes com imagens externas
 ├── modelo_treinado.h5       # Modelo salvo
 ├── imagens_teste/           # Imagens desenhadas à mão
 └── README.md                # Documentação do projeto
```

<hr>

## 📊 Dataset MNIST

O **MNIST (Modified National Institute of Standards and Technology)** é um dos datasets mais utilizados em visão computacional.

* 60.000 imagens para treinamento
* 10.000 imagens para teste
* Imagens 28x28 pixels
* Escala de cinza

Cada imagem representa um dígito manuscrito entre **0 e 9**.

<hr>

## ⚙️ Funcionamento do Modelo

1. Carregamento do dataset MNIST
2. Normalização dos valores dos pixels (0–255 → 0–1)
3. Criação da rede neural
4. Treinamento do modelo
5. Avaliação da acurácia
6. Predição de novas imagens

<hr>

## 🧩 Arquitetura da Rede Neural

* **Flatten**: transforma a imagem 28x28 em um vetor 1D
* **Dense (128 neurônios)** com ativação ReLU
* **Dense (10 neurônios)** com ativação Softmax

Essa arquitetura permite classificar os dígitos com alta precisão.

<hr>

## ✍️ Testando com Imagens Desenhadas à Mão

É possível testar o modelo com imagens criadas manualmente. Para obter bons resultados, as imagens devem:

* Estar em escala de cinza
* Ter resolução **28x28 pixels**
* Fundo preto e número em branco

O notebook `utl_modelo.ipynb` é responsável por esse processo.

<hr>

## ▶️ Como Executar o Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta do projeto
cd reconhecimento-digitos-mnist

# Execute os notebooks
jupyter notebook
```

1. Execute o notebook `treinamento.ipynb`
2. Em seguida, utilize `utl_modelo.ipynb` para testar novas imagens

<hr>

## 📈 Resultados

O modelo atinge uma acurácia média superior a **95%** no conjunto de testes, apresentando excelente desempenho para classificação de dígitos manuscritos.

<hr>

## 🚀 Melhorias Futuras

* Implementação de **Redes Neurais Convolucionais (CNN)**
* Criação de uma interface gráfica para desenho dos números
* Treinamento com dataset personalizado
* Deploy do modelo em uma aplicação web

<hr>

## 📄 Licença

Este projeto é de uso educacional e livre para estudos, modificações e melhorias.

<hr>

### 👤 Autor

**Fellipe Marçal**

---

⭐ Se este projeto te ajudou, considere deixar uma estrela no repositório!

