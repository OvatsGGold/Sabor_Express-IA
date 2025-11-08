# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

Projeto desenvolvido para a disciplina *Artificial Intelligence Fundamentals*.

## 1. Descrição do Problema e Objetivos

### O Cenário

A "Sabor Express" é uma empresa local de delivery de alimentos que atua na região central da cidade. A empresa tem enfrentado grandes desafios logísticos para gerenciar suas entregas, especialmente em horários de pico (almoço e jantar).

O modelo atual de definição de percursos é totalmente manual, baseado apenas na experiência dos entregadores, sem nenhum apoio tecnológico. Isso tem resultado em:

* Rotas ineficientes e longos tempos de percurso.
* Atrasos nas entregas e aumento no custo de combustível.
* Insatisfação e consequente perda de clientes.

### Os Objetivos

O **objetivo central** deste projeto é desenvolver uma solução inteligente para otimizar as rotas de entrega da "Sabor Express". A solução deve ser capaz de:

1.  **Agrupar Entregas:** Em momentos de alta demanda, agrupar pedidos que estão geograficamente próximos para otimizar o trabalho de um único entregador.
2.  **Encontrar a Rota Ótima:** Para um conjunto de entregas, encontrar o menor caminho (rota mais eficiente) entre o restaurante e os múltiplos pontos de entrega, considerando as restrições da cidade.

## 2. Abordagem Adotada e Algoritmos Utilizados

Para resolver o desafio, a solução foi dividida em duas etapas principais, que utilizam algoritmos clássicos de Inteligência Artificial:

### Etapa 1: Agrupamento de Entregas (Clustering)

Em um horário de pico, não é eficiente enviar um entregador para cada pedido individual. Por isso, primeiro agrupamos os pedidos pendentes.

* **Algoritmo Utilizado:** **K-Means**.
* **Como Funciona:** O K-Means é um algoritmo de aprendizado não supervisionado. Nós o utilizamos para analisar a localização (coordenadas) de todos os pedidos pendentes e agrupá-los em "clusters" (zonas) eficientes.
* **Resultado:** Se tivermos 3 entregadores disponíveis, podemos pedir ao K-Means para criar 3 clusters. Cada cluster será um "lote" de entregas atribuído a um entregador.

### Etapa 2: Otimização da Rota (Busca em Grafo)

Depois que um entregador recebe seu "lote" (cluster) de entregas, precisamos definir a ordem e o caminho mais eficientes para visitar todos os pontos.

* **Modelo de Dados:** A cidade é representada como um **Grafo**. Os pontos de entrega e o restaurante são os **nós (vértices)**, e as ruas são as **arestas**, com pesos baseados em distância ou tempo.
* **Algoritmo Utilizado:** **Algoritmo de Dijkstra** (base para o A\*).
* **Como Funciona:** O Dijkstra é um algoritmo de busca que encontra o caminho mais curto (de menor peso) entre um nó inicial e todos os outros nós do grafo. Usamo-lo para encontrar a rota com a menor distância total.
* **Resultado:** O algoritmo fornece a rota otimizada (ex: Restaurante -> Ponto C -> Ponto A -> Ponto B) para o entregador, minimizando a distância total percorrida.

## 3. Diagrama do Grafo da Solução

Conforme implementado no código, o mapa da cidade foi modelado como um grafo não direcionado. Os nós representam locais de interesse (Restaurante, pontos A, B, C...) e as arestas representam as ruas, com seus respectivos pesos (distância).

O diagrama a seguir foi gerado pelo código e ilustra o modelo do grafo utilizado, destacando a rota mais curta encontrada do "Restaurante" ao "Ponto H".


<img width="1220" height="842" alt="image" src="https://github.com/user-attachments/assets/ee862a82-66e1-4faf-adf4-9890f0627065" />


## 4. Análise dos Resultados e Limitações

A solução proposta foi capaz de atingir os objetivos iniciais, dividindo o problema em duas etapas funcionais.

### Análise dos Resultados

1.  **Agrupamento (K-Means):** O algoritmo foi eficaz em agrupar os 10 pedidos pendentes em 3 "zonas" (clusters) distintas, com base em sua proximidade geográfica. Isso permite à Sabor Express atribuir um "lote" de entregas a cada um dos 3 entregadores.
2.  **Roteirização (Dijkstra):** O algoritmo foi capaz de ler o grafo da cidade (`mapa_grafo.csv`) e encontrar com sucesso o caminho **mais curto** (distância mínima) entre o "Restaurante" e o "Ponto H" (Rota: Restaurante -> B -> D -> G -> H, com Distância total: 20).

### Eficiência e Limitações da Solução

* **Eficiência:** Para a escala atual da "Sabor Express", os algoritmos K-Means e Dijkstra são extremamente eficientes e rodam instantaneamente.
* **Limitação 1 (Grafo Estático):** Nossa principal limitação é que o grafo é **estático**. Ele não considera trânsito em tempo real, acidentes ou ruas de sentido único.
* **Limitação 2 (Problema do Caixeiro Viajante):** O Dijkstra encontra o caminho mais curto entre *dois* pontos (A -> B). Nossa solução atual não resolve a *ordem* ideal de visita dentro do cluster (o "Problema do Caixeiro Viajante" - TSP).

### Sugestões de Melhoria

1.  **Rotas Dinâmicas:** Integrar com uma API de mapas (como Google Maps) para usar o **tempo de trânsito em tempo real** como o "peso" da aresta.
2.  **Resolver o TSP:** Implementar um algoritmo heurístico (como o *Algoritmo Genético*) para definir a **ordem ótima** de visitação dos pedidos dentro do cluster.
3.  **Clustering Avançado:** Substituir o K-Means pelo **DBSCAN** para identificar "pedidos" que estão muito longe para serem agrupados (ruído).

## 5. Instruções de Execução do Projeto

1.  **Clonar o Repositório:**
    ```bash
    git clone [SEU_LINK_DO_REPOSITORIO]
    cd [NOME_DO_REPOSITORIO]
    ```
2.  **Ambiente e Bibliotecas:** Recomenda-se o uso de um ambiente virtual (`venv`). Instale as bibliotecas necessárias:
    ```bash
    pip install pandas
    pip install scikit-learn
    pip install networkx
    pip install matplotlib
    ```
3.  **Execução:** Execute os scripts Python na ordem. Os gráficos serão exibidos na tela.
    
    *Primeiro, para ver o clustering:*
    ```bash
    python kmeans_clustering.py
    ```
    *Segundo, para ver a otimização de rota:*
    ```bash
    python route_optimization.py
    ```
