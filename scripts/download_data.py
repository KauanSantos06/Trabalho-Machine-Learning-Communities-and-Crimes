import os
import urllib.request

def baixar_dataset():
    """Baixa o dataset Communities and Crime da UCI para a pasta dados/"""
    pasta_destino = os.path.join(os.path.dirname(__file__), '..', 'dados')
    os.makedirs(pasta_destino, exist_ok=True)

    arquivos = {
        'communities.data': 'https://archive.ics.uci.edu/ml/machine-learning-databases/communities/communities.data',
        'communities.names': 'https://archive.ics.uci.edu/ml/machine-learning-databases/communities/communities.names'
    }

    print("Iniciando download do dataset Communities and Crime...")
    for nome, url in arquivos.items():
        caminho = os.path.join(pasta_destino, nome)
        if not os.path.exists(caminho):
            print(f"Baixando {nome}...")
            urllib.request.urlretrieve(url, caminho)
            print(f"✅ {nome} salvo em {caminho}")
        else:
            print(f"⚠️ {nome} já existe em {caminho}. Pulando download.")

if __name__ == "__main__":
    baixar_dataset()
