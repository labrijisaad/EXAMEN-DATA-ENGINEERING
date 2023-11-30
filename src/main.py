from utils import (
    get_embeddings_from_dataframe,
    load_data,
    apply_tsne,
    apply_acp,
    apply_umap,
)

import pandas as pd


def main():
    # Specify the path to the CSV file
    csv_path = './data/NewsGroups_Data.csv'

    # # Load data from the CSV file
    df = load_data(csv_path)

    # Get user's preferred method
    chosen_method = get_user_input()

    # Get embeddings from df
    embeddings, labels = get_embeddings_from_dataframe(df)

    # Check the chosen method and perform the corresponding action
    if chosen_method == "ACP":
        apply_acp(embeddings, labels)
    elif chosen_method == "TSNE":
        apply_tsne(embeddings, labels)
    elif chosen_method == "UMAP":
        apply_umap(embeddings, labels)
    else:
        print("Invalid method. Please choose ACP, TSNE, or UMAP.")


def get_user_input():
    """Get user input for the preferred method."""
    return input("Which method do you want to use on your data? ACP, TSNE, UMAP? ").upper()


# Ensure the script is being run directly and not imported
if __name__ == "__main__":
    main()
