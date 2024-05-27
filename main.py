import mathLib
import menu
import config
import numpy
import functionSolving
import matplotlib.pyplot as plt


def main():
    file_path = 'chebyshev.txt'
    functions_list = menu.functions_menu()
    left_boundary, right_boundary = menu.interval_menu()
    nodes_value = menu.nodes_menu()
    data = menu.read_data(file_path, nodes_value)
    n = menu.approximation_menu()
    array = functionSolving.chebyshev_coef(functions_list, nodes_value, data, n)

    plt.rcParams['figure.figsize'] = config.PLOT_FIGURE_SIZE
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = config.PLOT_FIGURE_DPI

    x_plot = numpy.linspace(left_boundary, right_boundary, 1000)
    y_gauss = functionSolving.chebyshev_calc(n, x_plot, array)
    plt.plot(x_plot, y_gauss, color=config.PLOT_LAGRANGE_COLOR, label='Aproksymowany wielomian', linewidth=2)

    y_poly: list[float] = [mathLib.evaluate_composite(e, functions_list) for e in x_plot]
    plt.plot(x_plot, y_poly, color=config.PLOT_POLY_COLOR, label="Oryginalna funkcja", linestyle='dashed')

    plt.xlabel('x', fontsize=config.PLOT_LABEL_FONT_SIZE)
    plt.ylabel('f(x)', fontsize=config.PLOT_LABEL_FONT_SIZE)
    plt.title('Chebyshev approximation', fontsize=config.PLOT_TITLE_FONT_SIZE)
    plt.legend()

    plt.grid(True)

    plt.show()
    plt.clf()


if __name__ == '__main__':
    main()
