import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# --- 1. Carregamento dos Dados ---
try:
    data = pd.read_csv('pedidos_do_dia.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'pedidos_do_dia.csv' não encontrado.")
    print("Por favor, crie o arquivo com 'Pedido_ID,Coord_X,Coord_Y' e os dados.")
    exit()

# Extrai as coordenadas para o K-Means
X = data[['Coord_X', 'Coord_Y']]

# --- 2. Aplicando o K-Means ---
# Definimos o número de clusters (K) como 3, simulando 3 entregadores.
K = 3
kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
kmeans.fit(X)

# --- 3. Análise dos Resultados ---
# Adiciona os resultados (qual cluster cada pedido pertence) ao DataFrame
data['Cluster'] = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Imprime os resultados no console
print("--- Resultado do Agrupamento K-Means ---")
print(f"Pedidos agrupados em {K} clusters (zonas de entrega):")
print(data)

print("\n--- Centros dos Clusters (Pontos médios das zonas) ---")
print(cluster_centers)

# --- 4. Visualização dos Resultados ---
# Plota um gráfico de dispersão para visualizar os clusters
plt.figure(figsize=(10, 7))

# Plota cada cluster com uma cor diferente
for i in range(K):
    cluster_data = data[data['Cluster'] == i]
    plt.scatter(cluster_data['Coord_X'], cluster_data['Coord_Y'], label=f'Zona {i} (Entregador {i+1})')

# Plota os centros dos clusters (o ponto médio de cada zona)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X', label='Centro da Zona')

plt.title('Agrupamento de Pedidos (K-Means)')
plt.xlabel('Coordenada X (Localização)')
plt.ylabel('Coordenada Y (Localização)')
plt.legend()
plt.grid(True)

# Salva o gráfico como uma imagem (útil para o README)
plt.savefig('kmeans_clusters.png')
print("\nGráfico de clustering salvo como 'kmeans_clusters.png'")

# Mostra o gráfico na tela
plt.show()
