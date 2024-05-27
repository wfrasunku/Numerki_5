import mathLib
import menu
import config
import numpy
import functionSolving
import matplotlib.pyplot as plt


def main():
    file_path = 'chebyshev.txt'
    functions_list = menu.functions_menu()
    a, b = menu.interval_menu()
    nodes_value = menu.nodes_menu()
    data = menu.read_data(file_path, nodes_value)
    choice = menu.working_mode()
    if choice == 1:
        n = menu.approximation_menu()
        array = functionSolving.chebyshev_approximation(functions_list, nodes_value, data, n)
        error = functionSolving.approximation_error(functions_list, nodes_value, data, n, array, a, b)
    else:
        precision = menu.precision_menu()
        n = 1
        working = True
        while working:
            array = functionSolving.chebyshev_approximation(functions_list, nodes_value, data, n)
            error = functionSolving.approximation_error(functions_list, nodes_value, data, n, array, a, b)
            if error < precision:
                working = False
            else:
                n += 1

    print("Blad aproksymacji:", error)
    plt.rcParams['figure.figsize'] = config.PLOT_FIGURE_SIZE
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = config.PLOT_FIGURE_DPI

    x_plot = numpy.linspace(a, b, 1000)
    y_gauss = functionSolving.approximation_evaluate(n, x_plot, array)
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
