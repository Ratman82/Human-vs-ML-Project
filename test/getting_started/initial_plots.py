import osfrom test.data.fetch_data import load_moves
import matplotlib.pyplot as plt
import seaborn as sns

def makeplot(catagory1, catagory2):
    catagory1_label = catagory1.replace('_', ' ')
    catagory2_label = catagory2.replace('_', ' ')

    df, target_name = load_moves()

    os.makedirs("plots", exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x = factor_1,
        y = factor_2,
        hue = target_name,
        style=target_name,
        s=90
    )

    plt.title(f"Move type: {catagory2_label} compared to {catagory1_label}")
    plt.xlabel(factor_1_label)
    plt.ylabel(factor_2_label)
    plt.legend(title='Move Types by ID')
    plt.grid(True)
    plt.savefig(f'test/getting_started/plots/{catagory1_label}_v_{catagory2_label}.png', dpi=150)
    plt.close()

make_plot('id','damage_class')