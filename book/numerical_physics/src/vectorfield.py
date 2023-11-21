import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as lina
from scipy.constants import pi, epsilon_0


K = 1 / (4*pi*epsilon_0)


def make_vector_field(qtopos):
    """Возвращает функцию поля `E(mesh)`.
    
    * `qtopos` - массив размера `n` на `3`, где в
      каждая из `n` строк имеет вид
      `(qi, xi, yi)`.
    """
    qs = qtopos[:, 0]
    rs = qtopos[:, [1, 2]]

    def field(mesh):
        mx, my = mesh
        r = np.vstack([mx.flatten(), my.flatten()])
        return K*_superposition(qs, rs, r).reshape(np.shape(mesh))
    
    return field


def _superposition(qs, rs, r):
    return np.sum([
        _calc_partial_field(qi, ri, r)
        for qi, ri in zip(qs, rs)
    ], axis=0)


def _calc_partial_field(qi, ri, r):
    dr = r.T - ri
    return qi*dr.T / lina.norm(dr, axis=1)**3


def create_mesh(x_minmax: tuple, y_minmax: tuple, n_xy: tuple):
    """Равномерно расположить расчётные точки на осях.
    
    * `x_minmax` и `y_minmax` - границы области
      по соответствующим осям.
    * `n_xy` - число точек по соответствующим осям.

    Возвращает расчётную сетку, созданную как `np.meshgrid`.
    """
    x = np.linspace(*x_minmax, n_xy[0])
    y = np.linspace(*y_minmax, n_xy[1])
    return np.asarray(np.meshgrid(x, y))


def plot_mesh_2d(mesh, figax=None, **kw):
    """Визуализировать двумерную расчётную сетку.
    
    * `mesh` - расчётная сетка.
    * `figax` - кортеж вида `(figure, axis)`.
      По умолчанию `None`.
    
    Возвращает кортеж `(figure, axis)`.
    """
    if figax is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = figax
    x, y = mesh
    ax.plot(x.flatten(), y.flatten(), ls="", **kw)
    ax.set(xlabel="$x$, м", ylabel="$y$, м")
    return fig, ax


def plot_vectorfield_2d(mesh, field,
                        figax=None, cbar_label=None, **kw):
    """Визуализировать векторное поле `field`.
    
    * `mesh` - двумерная расчётная сетка.
    * `field` - двумерное векторное поле.
    * `figax` - кортеж вида `(figure, axis)`.
    * `cbar_label` - название цветовой шкалы, если она есть.

    Возвращает кортеж вида `(figure, axis)`.
    """
    if figax is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = figax
    mx, my = mesh
    fx, fy = field
    if "cmap" in kw and cbar_label is not None:
        stream = ax.streamplot(mx, my, fx, fy, **kw)
        fig.colorbar(stream.lines, ax=ax, label=cbar_label)
        return fig, ax
    ax.streamplot(mx, my, fx, fy, **kw)
    return fig, ax


def plot_charges(qtopos: dict, figax=None):
    """Отобразить заряды.
    
    * `qtopos` - словарь, ключом которого является
      величина заряда `qi`, а значением -
      координата заряда `(xi, yi)`.
    * `figax` - кортеж вида `(figure, axis)`.

    Возвращает кортеж вида `(figure, axis)`.
    """
    if figax is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = figax
    kw_positive = dict(c="r", ls="", marker=".")
    kw_negative = dict(c="b", ls="", marker=".")
    ax.plot([], [], label="Заряд $+$", **kw_positive)
    ax.plot([], [], label="Заряд $-$", **kw_negative)
    for qi, xi, yi in qtopos:
        kw = kw_positive if qi > 0 else kw_negative
        ax.plot(xi, yi, **kw)
    return fig, ax
