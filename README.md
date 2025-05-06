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
