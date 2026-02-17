import os
from test.data.fetch_data import load_moves
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def make_plot(category1, category2):
    category1_label = category1.replace('_', ' ')
    category2_label = category2.replace('_', ' ')
    
    df, target_name = load_moves()

    os.makedirs("./getting_started/plots", exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x=category1,
        y=category2,
        hue=target_name,
        style=target_name,
        s=90
    )

    plt.title(f"Move type: {category2_label} compared to {category1_label}")
    plt.xlabel(category1_label)
    plt.ylabel(category2_label)
    plt.legend(title='Move Types by ID')
    plt.grid(True)

    plt.savefig(
        f'test/getting_started/plots/{category1_label}_v_{category2_label}.png',
        dpi=150
    )
    plt.close()


make_plot('id', 'damage_class')