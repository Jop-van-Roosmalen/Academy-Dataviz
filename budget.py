import matplotlib.pyplot as plt
import pandas as pd

def get_budget_data():
    budget_df = pd.read_csv(r"budget.csv", sep=",", index_col=0)
    return budget_df

def get_graph(show = False):
    budget_df = get_budget_data()

    fig, ax = plt.subplots()
    budget_df.plot(ax=ax, marker=".")

    if show:
        plt.show()
    return fig, ax

if __name__ == "__main__":
    fig, ax = get_graph(show=True)


