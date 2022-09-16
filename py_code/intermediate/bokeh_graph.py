from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    curdoc().theme = 'dark_minimal'

    p = figure(title='dark_minimal', width=300, height=300) 

    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2, color="yellow")
    fig.star_dot(x_vals, y_vals, line_width=2, size=20, color="yellow", alpha=0.5)
    show(fig)
