import mathLib
import menu
import config
import numpy
import pylab as pb
import functionSolving
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg


def main():
    table_data = []
    file_path = 'chebyshev.txt'
    functions_list = menu.functions_menu()
    right_boundary, left_boundary, nodes_value = menu.interval_menu()
    approx = menu.approximation_menu()

    plt.rcParams['figure.figsize'] = config.PLOT_FIGURE_SIZE
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = config.PLOT_FIGURE_DPI

    x_plot = numpy.linspace(left_boundary, right_boundary, 1000)
    # y_lagrange = lagrange_polynomial(x_plot)
    # y_lagrange_nodes = [lagrange_polynomial(n) for n in nodes]

    # plt.plot(x_plot, y_lagrange, color=config.PLOT_LAGRANGE_COLOR, label='Interpolacja Lagrange\'a', linewidth=2)
    y_poly: list[float] = [mathLib.evaluate_composite(e, functions_list) for e in x_plot]
    plt.plot(x_plot, y_poly, color=config.PLOT_POLY_COLOR, label="Oryginalna funkcja", linestyle='dashed')

    plt.xlabel('x', fontsize=config.PLOT_LABEL_FONT_SIZE)
    plt.ylabel('f(x)', fontsize=config.PLOT_LABEL_FONT_SIZE)
    plt.title('Interpolacja Lagrange\'a', fontsize=config.PLOT_TITLE_FONT_SIZE)
    plt.legend()

    plt.grid(True)

    plt.show()
    plt.clf()

# precision = menu.precision_menu()
# print("Tworzenie tabeli...")
#
# newton_cotes = functionSolving.newton_cotes_limes(functions_list, precision)
# print("Wartość Newtona-Cotesa wynosi:", newton_cotes)
# table_data.append(['Newton-Cotes', newton_cotes, precision])
#
# for nodes in range(2, 8):
#     data = menu.read_data(file_path, nodes)
#     gauss_chebyshev = functionSolving.gauss_chebyshev(functions_list, nodes, data)
#     print("Dla", nodes, "węzłów, wartość Gaussa-Czybyszewa wynosi:", gauss_chebyshev)
#     table_data.append(['Gauss-Chebyshev', gauss_chebyshev, nodes])


if __name__ == '__main__':
    main()
