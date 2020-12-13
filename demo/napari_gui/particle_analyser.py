from magicgui._qt.widgets import QDataComboBox
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
    QTableWidgetItem, QLabel
)
from qtpy.QtCore import Qt, QSize
from pathlib import Path
from qtpy import QtGui


import napari
import numpy as np
from napari.layers import Image, Labels
from magicgui import magicgui

import pyclesperanto_prototype as cle


# inspired from https://github.com/pr4deepr/pyclesperanto_prototype/blob/master/napari_clij_widget.py
# Using Enums for getting a dropdown menu
from enum import Enum
from functools import partial

# -----------------------------------------------------------------------------
class Filter(Enum):
    please_select = partial(cle.copy)
    mean_box = partial(cle.mean_box)
    maximum_box = partial(cle.maximum_box)
    minimum_box = partial(cle.minimum_box)
    top_hat_box = partial(cle.top_hat_box)
    divide_by_gaussian = partial(cle.divide_by_gaussian_background)
    bottom_hat_box = partial(cle.bottom_hat_box)
    gaussian_blur = partial(cle.gaussian_blur)
    gamma_correction = partial(cle.gamma_correction)
    gradient_x = partial(cle.gradient_x)
    gradient_y = partial(cle.gradient_y)
    gradient_z = partial(cle.gradient_z)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def filter(input1: Image, operation: Filter = Filter.please_select, x: float = 1, y: float = 1, z: float = 0):
    print(filter.self)
    if input1:
        cle_input = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input)
        operation(cle_input, output, x, y, z)
        output = cle.pull_zyx(output)

        if (filter.initial_call):
            filter.count = filter.count + 1
            filter.self.viewer.add_image(output, name="filter" + str(filter.count), colormap=input1.colormap)
            filter.initial_call = False
        else:
            filter.self.layer.data = output
            filter.self.layer.name = str(operation)

filter.count = 0


# -----------------------------------------------------------------------------
class Binarize(Enum):
    please_select = partial(cle.copy)
    threshold_otsu = partial(cle.threshold_otsu)
    greater_constant = partial(cle.greater_constant)
    smaller_constant = partial(cle.smaller_constant)
    equal_constant = partial(cle.equal_constant)
    not_equal_constant = partial(cle.not_equal_constant)
    detect_label_edges = partial(cle.detect_label_edges)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def binarize(input1: Image, operation: Binarize= Binarize.threshold_otsu, constant : int = 0):
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, constant)
        output = cle.pull_zyx(output)

        if (binarize.initial_call):
            binarize.count = binarize.count + 1
            binarize.self.viewer.add_image(output, name="binarize" + str(binarize.count))
            binarize.initial_call = False
        else:
            binarize.self.layer.data = output
            binarize.self.layer.contrast_limits = (0, 1)

binarize.count = 0

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
def combine(input1: Image, input2: Image = None, operation: Combine = Combine.please_select):
    if input1 is not None:
        if (input2 is None):
            input2 = input1

        cle_input1 = cle.push_zyx(input1.data)
        cle_input2 = cle.push_zyx(input2.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, cle_input2, output)
        output = cle.pull_zyx(output)

        if (combine.initial_call):
            combine.count = combine.count + 1
            combine.self.viewer.add_image(output, name="combine" + str(combine.count), colormap=input1.colormap)
            combine.initial_call = False
        else:
            combine.self.layer.data = output

combine.count = 0




# -----------------------------------------------------------------------------
class Label(Enum):
    please_select = partial(cle.copy)
    connected_component = partial(cle.connected_components_labeling_box)
    voronoi = partial(cle.voronoi_labeling)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def label(input1: Image, operation: Label = Label.connected_component):
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output)
        output = cle.pull_zyx(output)

        if (label.initial_call):
            label.count = label.count + 1
            label.self.viewer.add_labels(output, name="label" + str(label.count))
            label.initial_call = False
        else:
            label.self.layer.data = output

label.count = 0



# -----------------------------------------------------------------------------
class LabelProcessing(Enum):
    please_select = partial(cle.copy)
    exclude_on_edges = partial(cle.exclude_labels_on_edges)
    exclude_out_of_size_range = partial(cle.exclude_labels_out_of_size_range)
    extend_via_voronoi = partial(cle.extend_labeling_via_voronoi)
    extend_with_maximum_radius = partial(cle.extend_labels_with_maximum_radius)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def label_processing(input1: Image, operation: LabelProcessing = LabelProcessing.please_select, min: float=0, max:float=100):
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, min, max)
        output = cle.pull_zyx(output)

        if (label_processing.initial_call):
            label_processing.count = label_processing.count + 1
            label_processing.self.viewer.add_labels(output, name="label_processing" + str(label_processing.count))
            label_processing.initial_call = False
        else:
            label_processing.self.layer.data = output
            label_processing.self.layer.name = str(operation)
label_processing.count = 0

# -----------------------------------------------------------------------------
class Mesh(Enum):
    please_select = partial(cle.copy)
    touching = partial(cle.draw_mesh_between_touching_labels)
    proximal = partial(cle.draw_mesh_between_proximal_labels)
    n_closest = partial(cle.draw_mesh_between_n_closest_labels)
    distance_touching = partial(cle.draw_distance_mesh_between_touching_labels)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def mesh(input1: Image, operation: Mesh = Mesh.please_select, n : float = 1):
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, n)
        max_intensity = cle.maximum_of_all_pixels(output)
        if max_intensity == 0:
            max_intensity = 1 # prevent division by zero in vispy
        output = cle.pull_zyx(output)

        if (mesh.initial_call):
            mesh.count = mesh.count + 1
            mesh.self.viewer.add_image(output, name="mesh" + str(mesh.count), colormap='green', blending='additive')
            mesh.initial_call = False
        else:
            mesh.self.layer.data = output
            mesh.self.layer.name = str(operation)
            mesh.self.layer.contrast_limits=(0, max_intensity)


mesh.count = 0

# -----------------------------------------------------------------------------
class Map(Enum):
    please_select = partial(cle.copy)
    pixel_count = partial(cle.label_pixel_count_map)
    touching_neighbor_count = partial(cle.touching_neighbor_count_map)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)

@magicgui(auto_call=True, layout='vertical')
def map(input1: Image, operation: Map = Map.please_select, n : float = 1):
    if input1 is not None:
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, n)
        max_intensity = cle.maximum_of_all_pixels(output)
        if max_intensity == 0:
            max_intensity = 1 # prevent division by zero in vispy
        output = cle.pull_zyx(output)

        if (map.initial_call):
            map.count = map.count + 1
            map.self.viewer.add_image(output, name="map" + str(map.count), colormap='magenta')
            map.initial_call = False
        else:
            map.self.layer.data = output
            map.self.layer.name = str(operation)
            map.self.layer.contrast_limits=(0, max_intensity)

map.count = 0

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

class LayerDialog():
    def __init__(self, viewer, operation):
        self.viewer = viewer

        self.operation = operation
        self.operation.self = self # arrrrg

        former_active_layer = self.viewer.active_layer
        try:
            former_active_layer.dialog._deselected(None)
        except AttributeError:
            print() # whatever

        self.operation.initial_call = True
        self.operation(self.viewer.active_layer)
        self.layer = self.viewer.active_layer
        self.layer.dialog = self

        self.layer.events.data.connect(self._updated)
        self.layer.events.select.connect(self._selected)
        self.layer.events.deselect.connect(self._deselected)

        self.filter_gui = self.operation.Gui()
        self.dock_widget = viewer.window.add_dock_widget(self.filter_gui, area='right')
        self.filter_gui.set_widget('input1', former_active_layer)

    def _updated(self, event):
        print("Updated : " + self.layer.name)
        self.refresh_all_followers()
        #print(event)
    def _selected(self, event):
        print("Selected : " + self.layer.name)
        self.operation.self = self    # sigh
        self.dock_widget = viewer.window.add_dock_widget(self.filter_gui, area='right')
        #print(event)
    def _deselected(self, event):
        print("Deselected : " + self.layer.name)
        self.viewer.window.remove_dock_widget(self.dock_widget)
        #print(event)

    def _removed(self):
        print("removed: " + self.layer.name)
        self.viewer.window.remove_dock_widget(self.dock_widget)

    def refresh(self):
        print("Refresh " + self.layer.name)
        former = self.operation.self
        self.operation.self = self    # sigh
        self.filter_gui()
        self.operation.self = former

    def refresh_all_followers(self):
        for layer in self.viewer.layers:
            print(layer.name)
            try:
                if layer.dialog.filter_gui.get_widget('input1').currentData() == self.layer:
                    layer.dialog.refresh()
                if layer.dialog.filter_gui.get_widget('input2').currentData() == self.layer:
                    layer.dialog.refresh()
            except AttributeError:
                print()

class Gui(QWidget):
    """This Gui takes a napari as parameter and infiltrates it.

    It adds some buttons for categories of operations.
    """

    def __init__(self, viewer):
        super().__init__()

        self.viewer = viewer

        self.layout = QVBoxLayout()

        self._init_gui()

        self.setLayout(self.layout)

        self.dock_widget = None

    def _init_gui(self):
        """Switches the GUI internally between a main menu
        where you can select categories and a sub menu where
        you can keep results or cancel processing.
        """
        # remove all buttons first
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        self._add_button("Filter", self._add_filter_clicked)
        self._add_button("Binarize", self._add_binarize_clicked)
        self._add_button("Combine", self._add_combine_clicked)
        self._add_button("Label", self._add_label_clicked)
        self._add_button("Label Processing", self._add_label_processing_clicked)
        self._add_button("Map", self._map_clicked)
        self._add_button("Mesh", self._mesh_clicked)
        self._add_button("Measure", self._measure_clicked)

        self.setLayout(self.layout)

    def _add_button(self, title : str, handler : callable):
        # text
        btn = QPushButton(title, self)
        btn.setFont(QtGui.QFont('Arial', 12))

        # icon
        btn.setIcon(QtGui.QIcon(str(Path(__file__).parent) + "/icons/" + title.lower().replace(" ", "_") + ".png"))
        btn.setIconSize(QSize(40, 40))
        btn.setStyleSheet("text-align:left;");

        # action
        btn.clicked.connect(handler)
        self.layout.addWidget(btn)

    def _add_filter_clicked(self):
        self._activate(filter)

    def _add_binarize_clicked(self):
        self._activate(binarize)

    def _add_combine_clicked(self):
        self._activate(combine)

    def _add_label_clicked(self):
        self._activate(label)

    def _add_label_processing_clicked(self):
        self._activate(label_processing)

    def _measure_clicked(self):
        self._activate(measure)

    def _map_clicked(self):
        self._activate(map)

    def _mesh_clicked(self):
        self._activate(mesh)

    def _activate(self, magicgui):
        LayerDialog(self.viewer, magicgui)

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

    def _on_removed(event):
        layer = event.value
        print(layer.name)
        try:
            layer.dialog._removed()
        except AttributeError:
            print()
    viewer.layers.events.removed.connect(_on_removed)

        # add the gui to the viewer as a dock widget
    dock_widget = viewer.window.add_dock_widget(Gui(viewer), area='right')


