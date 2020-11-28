from qtpy.QtWidgets import (
    QPushButton,
    QComboBox,
    QTabWidget,
    QVBoxLayout,
    QGridLayout,
    QFileDialog,
    QDialogButtonBox,
    QWidget,
    QSlider,
    QTableWidget,
    QTableWidgetItem
)
from qtpy.QtCore import Qt
import napari
import numpy as np
from napari.layers import Image, Labels
from magicgui import magicgui

import pyclesperanto_prototype as cle


class Gui(QWidget):
    """This Gui takes a napari as parameter and infiltrates it.

    It adds some buttons for categories of operations.
    """

    # I don't like global variables.
    # But that's what it is.
    # It's a global variable.
    #                            haesleinhuepf
    global_last_filter_applied = None

    def __init__(self, viewer):
        super().__init__()

        self.viewer = viewer
        self.items = []

        self.layout = QVBoxLayout()

        self._init_gui()

        self.setLayout(self.layout)

        self.dock_widget = None

    def _init_gui(self, main_menu : bool = True):
        """Switches the GUI internally between a main menu
        where you can select categories and a sub menu where
        you can keep results or cancel processing.
        """
        # remove all buttons first
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        if main_menu:
            self._add_button("Filter", self._add_filter_clicked)
            self._add_button("Binarize", self._add_binarize_clicked)
            self._add_button("Combine", self._add_combine_clicked)
            self._add_button("Label", self._add_label_clicked)
            self._add_button("Measure", self._measure_clicked)
        else:
            self._add_button("Done", self._done_clicked)
            self._add_button("Cancel", self._cancel_clicked)

        self.setLayout(self.layout)

    def _add_button(self, title : str, handler : callable):
        btn = QPushButton(title, self)
        btn.clicked.connect(handler)
        self.layout.addWidget(btn)
        self.items.append(btn)

    def _add_filter_clicked(self):
        self._activate(filter)

    def _add_binarize_clicked(self):
        self._activate(binarize)

    def _add_combine_clicked(self):
        self._activate(combine)

    def _add_label_clicked(self):
        self._activate(label)

    def _measure_clicked(self):
        self._activate(measure)

    def _activate(self, magicgui):
        for layer in viewer.layers:
            layer.visible = False

        Gui.global_last_filter_applied = None
        self.filter_gui = magicgui.Gui()
        self.dock_widget = viewer.window.add_dock_widget(self.filter_gui, area='right')
        self._init_gui(False)

    def _done_clicked(self):
        # magicqui somehow internally keeps the layer.
        # Thus, we need to destroy magicguis layer and add it again
        if Gui.global_last_filter_applied is not None:
            data = viewer.layers.selected[0].data
            viewer.layers.remove_selected()
            if isinstance(Gui.global_last_filter_applied, Label):
                viewer.add_labels(data, name = str(Gui.global_last_filter_applied))
            else:
                viewer.add_image(data, name=str(Gui.global_last_filter_applied))

        self.viewer.window.remove_dock_widget(self.dock_widget)
        self._init_gui(True)

    def _cancel_clicked(self):
        if Gui.global_last_filter_applied is not None:
            viewer.layers.remove_selected()

        print("Main menu")
        self.viewer.window.remove_dock_widget(self.dock_widget)
        self._init_gui(True)



# inspired from https://github.com/pr4deepr/pyclesperanto_prototype/blob/master/napari_clij_widget.py# Using Enums for getting a dropdown menu
from enum import Enum
from functools import partial

# -----------------------------------------------------------------------------
class Filter(Enum):
    please_select = partial(cle.copy)
    mean_box = partial(cle.mean_box)
    maximum_box = partial(cle.maximum_box)
    minimum_box = partial(cle.minimum_box)
    top_hat_box = partial(cle.top_hat_box)
    bottom_hat_box = partial(cle.bottom_hat_box)
    gaussian_blur = partial(cle.gaussian_blur)
    gradient_x = partial(cle.gradient_x)
    gradient_y = partial(cle.gradient_y)
    gradient_z = partial(cle.gradient_z)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def filter(input: Image, operation: Filter, x: float = 1, y: float = 1, z: float = 0) -> Image:
    if input:
        cle_input = cle.push_zyx(input.data)
        output = cle.create_like(cle_input)
        operation(cle_input, output, x, y, z)
        output = cle.pull_zyx(output)

        # workaround to cause a auto-contrast in the viewer after returning the result
        if Gui.global_last_filter_applied is not None:
            viewer.layers.remove_selected()
        Gui.global_last_filter_applied = operation

        return output

# -----------------------------------------------------------------------------
class Binarize(Enum):
    please_select = partial(cle.copy)
    threshold_otsu = partial(cle.threshold_otsu)
    greater_constant = partial(cle.greater_constant)
    smaller_constant = partial(cle.smaller_constant)
    equal_constant = partial(cle.equal_constant)
    not_equal_constant = partial(cle.not_equal_constant)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def binarize(input1: Image, operation: Binarize, constant : int = 0) -> Image:
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, constant)
        output = cle.pull_zyx(output)

        # workaround to cause a auto-contrast in the viewer after returning the result
        if Gui.global_last_filter_applied is not None:
            viewer.layers.remove_selected()
        Gui.global_last_filter_applied = operation

        return output

# -----------------------------------------------------------------------------
class Combine(Enum):
    please_select = partial(cle.copy)
    binary_and = partial(cle.binary_and)
    binary_or = partial(cle.binary_or)
    binary_xor = partial(cle.binary_xor)
    add = partial(cle.add_images_weighted)
    subtract = partial(cle.subtract_images)
    multiply = partial(cle.multiply_images)
    divide = partial(cle.divide_images)
    greater = partial(cle.greater)
    smaller = partial(cle.smaller)
    equal = partial(cle.equal)
    not_equal = partial(cle.not_equal)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def combine(input1: Image, input2: Image, operation: Combine) -> Image:
    if input1 is not None and input2 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        cle_input2 = cle.push_zyx(input2.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, cle_input2, output)
        output = cle.pull_zyx(output)

        # workaround to cause a auto-contrast in the viewer after returning the result
        if Gui.global_last_filter_applied is not None:
            viewer.layers.remove_selected()
        Gui.global_last_filter_applied = operation

        return output



# -----------------------------------------------------------------------------
class Label(Enum):
    please_select = partial(cle.copy)
    connected_component = partial(cle.connected_components_labeling_box)
    voronoi = partial(cle.voronoi_labeling)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def label(input1: Image, operation: Label) -> Labels:
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output)
        output = cle.pull_zyx(output)

        # workaround to cause a auto-contrast in the viewer after returning the result
        if Gui.global_last_filter_applied is not None:
            viewer.layers.remove_selected()
        Gui.global_last_filter_applied = operation

        return output

# -----------------------------------------------------------------------------
@magicgui(layout='vertical', call_button="Measure")
def measure(input: Image, labels : Image):
    from skimage.measure import regionprops_table
    table = regionprops_table(labels.data.astype(int), intensity_image=input.data, properties=('area', 'centroid', 'mean_intensity'))
    dock_widget = table_to_widget(table)
    viewer.window.add_dock_widget(dock_widget, area='right')

def table_to_widget(table : dict) -> QTableWidget:
    view = QTableWidget(len(next(iter(table.values()))), len(table))
    for i, column in enumerate(table.keys()):
        view.setItem(0, i, QTableWidgetItem(column))
        for j, value in enumerate(table.get(column)):
            view.setItem(j + 1, i,  QTableWidgetItem(str(value)))
    return view

# -----------------------------------------------------------------------------
from skimage.io import imread
image = imread('https://samples.fiji.sc/blobs.png')

#image = imread('C:/structure/data/lund_000500_resampled.tif')


cle.select_device("RTX")
print(cle.get_device())

with napari.gui_qt():
    # create a viewer and add some image
    viewer = napari.Viewer()
    viewer.add_image(image)

    # add the gui to the viewer as a dock widget
    dock_widget = viewer.window.add_dock_widget(Gui(viewer), area='right')

















