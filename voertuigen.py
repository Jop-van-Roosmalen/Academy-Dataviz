import matplotlib.pyplot as plt

def get_voertuigen_data():
    voertuigen_data = {
        "step": 23,
        "vrachtwagen": 8,
        "auto": 12,
        "motor": 52,
        "fiets": 30
    }
    return voertuigen_data

def get_graph(show = False):
    voertuigen_data = get_voertuigen_data()

    # Color bars
    colors = ["C0", "C1", "C2", "C3", "C4"]

    # Make barplot
    fig, ax = plt.subplots()
    for i, (voertuig, aantal) in enumerate(voertuigen_data.items()):
        ax.bar(voertuig, aantal, color=colors[i], label=voertuig)

    # Add annotations
    for container in ax.containers:
        ax.bar_label(container)

    # Add axes labels
    ax.set_xlabel("Type voertuig")

    # Add legend
    ax.legend(voertuigen_data.keys())

    if show:
        plt.show()
    return fig, ax

if __name__ == "__main__":
    fig,ax = get_graph(show=True)


