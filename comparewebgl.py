import numpy as np

from bokeh.layouts import column
from bokeh.plotting import figure, show, output_file, curdoc

N = 10000

x = np.random.normal(0, np.pi, N)
y = np.sin(x) + np.random.normal(0, 0.2, N)

output_file("scatter10k.html", title="scatter 10k points (with WebGL)")

p = figure(output_backend="webgl")
p.scatter(x, y, alpha=0.1)

p2 = figure(output_backend="canvas")
p2.scatter(x, y, alpha=0.1)
show(column([p,p2]))

#curdoc().add_root(column([p,p2]))