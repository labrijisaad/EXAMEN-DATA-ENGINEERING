from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from umap import UMAP
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np


def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)


def get_embeddings_from_dataframe(df):
    corpus = df['content'].tolist()
    labels = df['target'].tolist()
    corpus = corpus[:200]
    labels = labels[:200]

    # Load pre-trained SentenceTransformer model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    # Encode sentences to get embeddings
    embeddings = model.encode(corpus)
    return embeddings, labels


def clust(mat, k):
    '''
    Perform clustering

    Input:
    -----
        mat : input list
        k : number of cluster
    Output:
    ------
        pred : list of predicted labels
    '''
    kmeans = KMeans(n_clusters=k, random_state=42)
    pred = kmeans.fit_predict(mat)
    return pred


def apply_umap(embeddings, labels, export_path='./data/umap_kmeans_plot.png'):
    # Perform dimensionality reduction using UMAP
    red_emb_umap = UMAP(n_components=2).fit_transform(embeddings)

    # Perform clustering using K-means with UMAP
    pred_umap = clust(red_emb_umap, 20)

    # Evaluate clustering results with UMAP
    nmi_score_umap = normalized_mutual_info_score(pred_umap, labels)
    ari_score_umap = adjusted_rand_score(pred_umap, labels)

    print(f'UMAP - NMI: {nmi_score_umap:.2f} \nUMAP - ARI: {ari_score_umap:.2f}')

    # Plot UMAP + K-means
    plt.figure(figsize=(10, 5))
    for label in set(labels):
        indices = np.where(pred_umap == label)
        plt.scatter(red_emb_umap[indices, 0], red_emb_umap[indices, 1], label=f'Cluster {label}', s=5, alpha=0.7)
    plt.title('UMAP + K-means')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.savefig(export_path)
    print(f'Plot saved to {export_path}')

    plt.show()

    return nmi_score_umap, ari_score_umap, pred_umap, red_emb_umap


def apply_tsne(embeddings, labels, export_path='./data/tsne_kmeans_plot.png'):
    # Perform dimensionality reduction using TSNE
    red_emb_tsne = TSNE(n_components=2).fit_transform(embeddings)

    # Perform clustering using K-means with TSNE
    pred_tsne = clust(red_emb_tsne, 20)

    # Evaluate clustering results with TSNE
    nmi_score_tsne = normalized_mutual_info_score(pred_tsne, labels)
    ari_score_tsne = adjusted_rand_score(pred_tsne, labels)

    print(f'TSNE - NMI: {nmi_score_tsne:.2f} \nTSNE - ARI: {ari_score_tsne:.2f}')

    # Plot TSNE + K-means
    plt.figure(figsize=(10, 5))
    for label in np.unique(labels):
        indices = np.where(pred_tsne == label)
        plt.scatter(red_emb_tsne[indices, 0], red_emb_tsne[indices, 1], label=f'Cluster {label}', s=5, alpha=0.7)
    plt.title('TSNE + K-means')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Export the plot
    plt.savefig(export_path, bbox_inches='tight')
    plt.show()

    return nmi_score_tsne, ari_score_tsne, pred_tsne, red_emb_tsne


def apply_acp(embeddings, labels, output_path='./data/plot_pca_kmeans.png'):
    # Perform dimensionality reduction using PCA
    red_emb_pca = PCA(n_components=2).fit_transform(embeddings)

    # Perform clustering using K-means with PCA
    pred_pca = clust(red_emb_pca, 20)

    # Evaluate clustering results with PCA
    nmi_score_pca = normalized_mutual_info_score(pred_pca, labels)
    ari_score_pca = adjusted_rand_score(pred_pca, labels)

    print(f'PCA - NMI: {nmi_score_pca:.2f} \nPCA - ARI: {ari_score_pca:.2f}')

    # Plotting
    plt.figure(figsize=(10, 5))
    for label in np.unique(pred_pca):
        indices = np.where(pred_pca == label)
        plt.scatter(red_emb_pca[indices, 0], red_emb_pca[indices, 1], label=f'Cluster {label}', s=5, alpha=0.7)
    plt.title('PCA + K-means')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(output_path)
    plt.show()

    return nmi_score_pca, ari_score_pca, pred_pca, red_emb_pca
