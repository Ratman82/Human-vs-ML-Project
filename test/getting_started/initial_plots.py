import os
import matplotlib.pyplot as plt
import seaborn as sns
from test.data.fetch_data import load_moves

def make_plot(category1, category2):

    category1_label = category1.replace('_', ' ').title()
    category2_label = category2.replace('_', ' ').title()
    

    df, target_name = load_moves()


    plot_dir = "test/getting_started/plots"
    os.makedirs(plot_dir, exist_ok=True)

    # 4. Plotting
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x=category1,
        y=category2,
        hue=target_name,
        style=target_name,
        palette="viridis",
        s=100,
        alpha=0.7
    )

    plt.title(f"{category2_label} vs {category1_label}")
    plt.xlabel(category1_label)
    plt.ylabel(category2_label)
    plt.legend(title='Move ID', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    save_path = f"{plot_dir}/{category1}_v_{category2}.png"
    plt.savefig(save_path, dpi=150)
    print(f"Successfully saved plot to: {save_path}")
    plt.close()

if __name__ == "__main__":
    make_plot('id', 'damage_class')