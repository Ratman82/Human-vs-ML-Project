import os
import matplotlib.pyplot as plt
import seaborn as sns
from test.data.fetch_data import load_moves

def make_plot(category1, category2):

    category1_label = category1.replace('_', ' ').title()
    category2_label = category2.replace('_', ' ').title()
    

    df, target_name = load_moves()
    df = df.dropna(subset=['power'])


    plot_dir = "test/getting_started/plots"
    os.makedirs(plot_dir, exist_ok=True)

    plt.figure(figsize=(20, 8))
    sns.stripplot(
        data=df,
        x=category1,
        y=category2,
        hue='damage_class',      
        jitter=0.6,          
        alpha=0.5,
        s=7              
    )   
    plt.title(f"{category2_label} vs {category1_label}")
    plt.xlabel(category1_label)
    plt.ylabel(category2_label)
    plt.legend(title='power', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    save_path = f"{plot_dir}/{category1}_v_{category2}.png"
    plt.savefig(save_path, dpi=150)
    print(f"Successfully saved plot to: {save_path}")
    plt.close()

if __name__ == "__main__":
    make_plot('accuracy','power')

#python3 -m test.getting_started.initial_plots
#just the code to print the image