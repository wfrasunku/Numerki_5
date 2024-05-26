import menu
import functionSolving
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg


def main():
    table_data = []
    file_path = 'chebyshev.txt'
    functions_list = menu.functions_menu()
    precision = menu.precision_menu()
    print("Tworzenie tabeli...")

    newton_cotes = functionSolving.newton_cotes_limes(functions_list, precision)
    print("Wartość Newtona-Cotesa wynosi:", newton_cotes)
    table_data.append(['Newton-Cotes', newton_cotes, precision])

    for nodes in range(2, 6):
        data = menu.read_data(file_path, nodes)
        gauss_chebyshev = functionSolving.gauss_chebyshev(functions_list, nodes, data)
        print("Dla", nodes, "węzłów, wartość Gaussa-Czybyszewa wynosi:", gauss_chebyshev)
        table_data.append(['Gauss-Chebyshev', gauss_chebyshev, nodes])

    table_df = pd.DataFrame(table_data, columns=['Method', 'Value', 'Nodes/Precision'])

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')

    table = ax.table(cellText=table_df.values, colLabels=table_df.columns, loc='center', cellLoc='center')

    table.auto_set_font_size(True)
    table.scale(1, 1)

    plt.savefig('table.png', bbox_inches='tight', pad_inches=0.01)
    img = mpimg.imread('table.png')
    plt.imshow(img)
    plt.show()
    print("Tabela ukończona!")


if __name__ == '__main__':
    main()
