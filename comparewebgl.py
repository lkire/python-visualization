import numpy as np
import pandas as pd

from bokeh.layouts import column
from bokeh.plotting import figure, show, output_file, curdoc

N = 10000

x = np.random.normal(0, np.pi, N)
y = np.sin(x) + np.random.normal(0, 0.2, N)

df = pd.DataFrame()
df["x"] = x
df["y"] = y
df["ytop"] = y + 0.5

output_file("scatter10k.html", title="scatter 10k points (with WebGL)")

p = figure(output_backend="webgl")
p.vbar(df.x, .1, df.y, df.ytop, alpha=0.1)

p2 = figure(output_backend="canvas")
p2.vbar(df.x, .1, df.y, df.ytop, alpha=0.1)
show(column([p,p2]))

#curdoc().add_root(column([p,p2]))