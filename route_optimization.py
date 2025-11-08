import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# --- 1. Carregamento dos Dados e Criação do Grafo ---
try:
    data = pd.read_csv('mapa_grafo.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'mapa_grafo.csv' não encontrado.")
    print("Por favor, crie o arquivo com 'Ponto_Origem,Ponto_Destino,Distancia'.")
    exit()

# Cria um grafo vazio
G = nx.Graph()

# Adiciona as "ruas" (arestas) ao grafo com seus "pesos" (Distancia)
for _, row in data.iterrows():
    G.add_edge(row['Ponto_Origem'], row['Ponto_Destino'], weight=row['Distancia'])

print("--- Grafo da Cidade Criado com Sucesso ---")
print(f"Nós (pontos): {G.nodes()}")
print(f"Arestas (ruas): {G.edges()}")

# --- 2. Aplicando o Algoritmo de Busca (Dijkstra) ---
# Vamos encontrar a rota mais curta do 'Restaurante' até o 'Ponto H'
start_node = 'Restaurante'
end_node = 'H'

try:
    # Calcula o caminho mais curto usando o algoritmo de Dijkstra
    path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight', method='dijkstra')
    
    # Calcula o comprimento total desse caminho
    length = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight', method='dijkstra')
    
    print("\n--- Rota Otimizada Encontrada ---")
    print(f"Rota mais curta de '{start_node}' para '{end_node}':")
    print(" -> ".join(path))
    print(f"Distância total: {length}")

except nx.NetworkXNoPath:
    print(f"Não há caminho entre {start_node} e {end_node}.")

except nx.NodeNotFound:
    print(f"Erro: Nó '{start_node}' ou '{end_node}' não encontrado no grafo.")
    exit()

# --- 3. Visualização do Grafo e da Rota ---
plt.figure(figsize=(12, 8))

# Define a posição dos nós para a visualização
pos = nx.spring_layout(G, seed=42)

# Desenha o grafo completo
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, width=1)

# Desenha os pesos (distâncias) nas arestas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Destaca a rota mais curta (se encontrada)
if 'path' in locals():
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title(f'Visualização do Grafo e Rota Mais Curta (de {start_node} para {end_node})')

# Salva o gráfico como uma imagem (essencial para o README)
plt.savefig('diagrama_grafo.png')
print("\nDiagrama do grafo salvo como 'diagrama_grafo.png'")

# Mostra o gráfico na tela
plt.show()
