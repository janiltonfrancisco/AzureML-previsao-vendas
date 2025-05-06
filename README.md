*Projeto de Machine Learning Automatizado no Azure ML*

Visão Geral

Este projeto utiliza Azure Machine Learning Automatizado para treinar e selecionar o melhor modelo preditivo com base em um conjunto de dados de vendas e temperaturas. A abordagem automatizada permite obter insights sem a necessidade de escrita manual de código.

- Arquitetura do Projeto

A implementação foi estruturada usando:

. AutoML: Para seleção e treinamento do modelo mais eficiente.

. Pipelines: Para organizar o processamento dos dados e garantir reprodutibilidade.

. Computes: Cluster de computação (cpu-cluster) para execução dos experimentos.

. Designers: Interface visual para auxiliar no desenvolvimento e ajuste dos modelos.

- Dados Utilizados
  
O dataset contém 100 registros distribuídos entre três colunas:

.Data (período de janeiro a abril de 2025).

.Vendas (unidades) registradas diariamente.

.Temperatura (°C) correspondente ao dia.

--- Algumas etapas do processo de Machine Learning:

-Primeiramente iremos criar um grupo de recurso, e dentro dele criar o Azure ML.

*Na imagem abaixo temos o workspace, ele contém o grupo de recurso:

![Image](https://github.com/user-attachments/assets/68ba791a-e7cc-4e56-82f3-f5910ce5177c)

*O Machine Learning Automatizado (AutoML) é uma abordagem que permite treinar, otimizar e selecionar modelos de aprendizado de máquina sem a necessidade de um desenvolvimento manual complexo. Ele é especialmente útil para quem deseja construir modelos preditivos de forma eficiente, sem precisar ajustar manualmente cada hiperparâmetro ou testar diversos algoritmos manualmente. Para treinar um modelo de classificação, o ML Automatizado escolherá entre uma lista de algorítmos de classificação. No projeto foi usado Regressão linear. Observe abaixo:

![Image](https://github.com/user-attachments/assets/76efbc9c-e38d-4826-a3a9-fb03e7d9497b)


*Logo abaixo podemos observar a criação dos designs e consequentemente das pipelines, que são os fluxos dos treinamentos:

![Image](https://github.com/user-attachments/assets/af4b4b61-0c99-4d70-820d-5438c4f66b0c)

![Image](https://github.com/user-attachments/assets/30a67fc9-87c0-4cde-9ac2-521f5a35fc55)


*Abaixo temos o resultado apóes o treinamento, com o aprendizado de máquina. Uma previsão de resultados:
![Image](https://github.com/user-attachments/assets/e7401e3a-e049-410f-a4b3-146a2da9003a)
