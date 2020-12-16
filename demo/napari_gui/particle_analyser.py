# Particle analyzer GUI using napari
#
# This example shows how one can call operations from the graphical user interface and implment an
# image-data-flow-graph. When parameters of operations high in the hierarchy are updated, downstream
# operations are updated. This facilitates finding a good parameter setting for complex workflows.
#
from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox
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
    QTableWidgetItem, QLabel, QMenu, QAction
)
from qtpy.QtCore import Qt, QSize
from pathlib import Path
from qtpy import QtGui
import napari
from napari.layers import Image, Labels
from magicgui import magicgui

import pyclesperanto_prototype as cle

from enum import Enum
from functools import partial

# -----------------------------------------------------------------------------
# We define an enum that represents operations in a given category
#
# inspired from https://github.com/pr4deepr/pyclesperanto_prototype/blob/master/napari_clij_widget.py
# Using Enums for getting a dropdown menu
class CallableEnum:
    def __init__(self, enum):
        self.enum = enum

    _all_cle_methods = None

    #define the call method for the functions or it won't return anything
    def call(self, *args, **kwargs):
        method = self.function()

        print(method)
        print(method.fullargspec)

        return method(*args, **kwargs)

    def function(self):
        from inspect import getmembers

        if CallableEnum._all_cle_methods is None:
            index = -1
            methods = getmembers(cle)
        for i, method in enumerate(methods):
            if str(method[0]) == self.enum.value:
                index = i

        return methods[index][1]

class Filter(Enum):
    please_select = cle.copy.__name__
    gaussian_blur = cle.gaussian_blur.__name__
    top_hat_box = cle.top_hat_box.__name__
    sobel = cle.sobel.__name__
    laplace = cle.laplace_box.__name__
    mean_box = cle.mean_box.__name__
    maximum_box = cle.maximum_box.__name__
    minimum_box = cle.minimum_box.__name__
    subtract_gaussian_background = cle.subtract_gaussian_background.__name__
    divide_by_gaussian_background = cle.divide_by_gaussian_background.__name__
    bottom_hat_box = cle.bottom_hat_box.__name__
    gamma_correction = cle.gamma_correction.__name__
    gradient_x = cle.gradient_x.__name__
    gradient_y = cle.gradient_y.__name__
    gradient_z = cle.gradient_z.__name__
    binary_edge_detection = cle.binary_edge_detection.__name__
    invert = cle.invert.__name__
    logarithm = cle.logarithm.__name__
    exponential = cle.exponential.__name__
    power = cle.power.__name__

    def __call__(self, *args, **kwargs):
        CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec

# The user interface of the operations is build by magicgui
@magicgui(auto_call=True, layout='vertical')
def filter(input1: Image, operation: Filter = Filter.please_select, x: float = 1, y: float = 1, z: float = 0):
    if input1:
        # execute operation
        cle_input = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input)
        operation(cle_input, output, x, y, z)
        output = cle.pull_zyx(output)

        # show result in napari
        if (filter.initial_call):
            filter.self.viewer.add_image(output, colormap=input1.colormap)
            filter.initial_call = False
        else:
            filter.self.layer.data = output
            filter.self.layer.name = str(operation)

# -----------------------------------------------------------------------------
class Binarize(Enum):
    please_select = cle.copy.__name__
    threshold_otsu = cle.threshold_otsu.__name__
    detect_maxima = cle.detect_maxima_box.__name__
    greater_constant = cle.greater_constant.__name__
    smaller_constant = cle.smaller_constant.__name__
    equal_constant = cle.equal_constant.__name__
    not_equal_constant = cle.not_equal_constant.__name__
    detect_label_edges = cle.detect_label_edges.__name__

    def __call__(self, *args, **kwargs):
        CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec

@magicgui(auto_call=True, layout='vertical')
def binarize(input1: Image, operation: Binarize= Binarize.threshold_otsu, constant : int = 0):
    if input1 is not None:
        # execute operation
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, constant)
        output = cle.pull_zyx(output)

        # show result in napari
        if (binarize.initial_call):
            binarize.self.viewer.add_image(output)
            binarize.initial_call = False
        else:
            binarize.self.layer.data = output
            binarize.self.layer.contrast_limits = (0, 1)
            binarize.self.layer.name = str(operation)

# -----------------------------------------------------------------------------
class Combine(Enum):
    please_select = cle.copy.__name__
    binary_and = cle.binary_and.__name__
    binary_or = cle.binary_or.__name__
    binary_xor = cle.binary_xor.__name__
    add = cle.add_images_weighted.__name__
    subtract = cle.subtract_images.__name__
    multiply = cle.multiply_images.__name__
    divide = cle.divide_images.__name__
    greater = cle.greater.__name__
    smaller = cle.smaller.__name__
    equal = cle.equal.__name__
    not_equal = cle.not_equal.__name__

    def __call__(self, *args, **kwargs):
        CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec

@magicgui(auto_call=True, layout='vertical')
def combine(input1: Image, input2: Image = None, operation: Combine = Combine.please_select):
    if input1 is not None:
        if (input2 is None):
            input2 = input1

        # execute operation
        cle_input1 = cle.push_zyx(input1.data)
        cle_input2 = cle.push_zyx(input2.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, cle_input2, output)
        output = cle.pull_zyx(output)

        # show result in napari
        if (combine.initial_call):
            combine.self.viewer.add_image(output, colormap=input1.colormap)
            combine.initial_call = False
        else:
            combine.self.layer.data = output
            combine.self.layer.name = str(operation)

# -----------------------------------------------------------------------------
class Label(Enum):
    please_select = cle.copy.__name__
    connected_component = cle.connected_components_labeling_box.__name__
    voronoi = cle.voronoi_labeling.__name__

    def __call__(self, *args, **kwargs):
        return CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec


@magicgui(auto_call=True, layout='vertical')
def label(input1: Image, operation: Label = Label.connected_component):
    if input1 is not None:
        # execute operation
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output)
        output = cle.pull_zyx(output)

        # show result in napari
        if (label.initial_call):
            label.self.viewer.add_labels(output)
            label.initial_call = False
        else:
            label.self.layer.data = output
            label.self.layer.name = str(operation)

# -----------------------------------------------------------------------------
class LabelProcessing(Enum):
    please_select = cle.copy.__name__
    exclude_on_edges = cle.exclude_labels_on_edges.__name__
    exclude_out_of_size_range = cle.exclude_labels_outside_size_range.__name__
    extend_via_voronoi = cle.extend_labeling_via_voronoi.__name__
    extend_with_maximum_radius = cle.extend_labels_with_maximum_radius.__name__

    def __call__(self, *args, **kwargs):
        CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec


@magicgui(auto_call=True, layout='vertical')
def label_processing(input1: Image, operation: LabelProcessing = LabelProcessing.please_select, min: float=0, max:float=100):
    if input1 is not None:
        # execute operation
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, min, max)
        output = cle.pull_zyx(output)

        # show result in napari
        if (label_processing.initial_call):
            label_processing.self.viewer.add_labels(output)
            label_processing.initial_call = False
        else:
            label_processing.self.layer.data = output
            label_processing.self.layer.name = str(operation)

# -----------------------------------------------------------------------------
class Mesh(Enum):
    please_select = cle.copy.__name__
    touching = cle.draw_mesh_between_touching_labels.__name__
    proximal = cle.draw_mesh_between_proximal_labels.__name__
    n_closest = cle.draw_mesh_between_n_closest_labels.__name__
    distance_touching = cle.draw_distance_mesh_between_touching_labels.__name__
    angle_touching = cle.draw_angle_mesh_between_touching_labels.__name__

    def __call__(self, *args, **kwargs):
        CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec

@magicgui(auto_call=True, layout='vertical')
def mesh(input1: Image, operation: Mesh = Mesh.touching, n : float = 1):
    if input1 is not None:
        # execute operation
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, n)
        min_intensity = cle.minimum_of_all_pixels(output)
        max_intensity = cle.maximum_of_all_pixels(output)
        if max_intensity - min_intensity == 0:
            max_intensity = min_intensity + 1 # prevent division by zero in vispy
        output = cle.pull_zyx(output)

        # show result in napari
        if (mesh.initial_call):
            mesh.self.viewer.add_image(output, colormap='green', blending='additive')
            mesh.initial_call = False
        else:
            mesh.self.layer.data = output
            mesh.self.layer.name = str(operation)
            mesh.self.layer.contrast_limits=(min_intensity, max_intensity)

# -----------------------------------------------------------------------------
class Map(Enum):
    please_select = cle.copy.__name__
    pixel_count = cle.label_pixel_count_map.__name__
    touching_neighbor_count = cle.touching_neighbor_count_map.__name__
    local_maximum_touching_neighbor_count = cle.local_maximum_touching_neighbor_count_map.__name__
    local_mean_touching_neighbor_count = cle.local_mean_touching_neighbor_count_map.__name__
    local_median_touching_neighbor_count = cle.local_median_touching_neighbor_count_map.__name__
    local_minimum_touching_neighbor_count = cle.local_minimum_touching_neighbor_count_map.__name__
    local_std_dev_touching_neighbor_count = cle.local_standard_deviation_touching_neighbor_count_map.__name__

    def __call__(self, *args, **kwargs):
        CallableEnum(self).call(*args, **kwargs)

    @property
    def fullargspec(self):
        return CallableEnum(self).function().fullargspec

@magicgui(auto_call=True, layout='vertical')
def map(input1: Image, operation: Map = Map.please_select, n : float = 1):
    if input1 is not None:
        # execute operation
        cle_input1 = cle.push_zyx(input1.data)
        output = cle.create_like(cle_input1)
        operation(cle_input1, output, n)
        max_intensity = cle.maximum_of_all_pixels(output)
        if max_intensity == 0:
            max_intensity = 1 # prevent division by zero in vispy
        output = cle.pull_zyx(output)

        # show result in napari
        if (map.initial_call):
            map.self.viewer.add_image(output, colormap='magenta')
            map.initial_call = False
        else:
            map.self.layer.data = output
            map.self.layer.name = str(operation)
            map.self.layer.contrast_limits=(0, max_intensity)

# -----------------------------------------------------------------------------
# A special case of ooperation is measurement: it results in a table instead of
# an image
@magicgui(layout='vertical', call_button="Measure")
def measure(input: Image = None, labels : Image = None):
    if input is not None and labels is not None:
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
    """
    The LayerDialog contains a dock-widget that allows configuring parameters of all operations.
    It uses events emitted by napari to toggle which dock widget is shown.
    """
    def __init__(self, viewer, operation):
        self.viewer = viewer

        self.operation = operation
        self.operation.self = self # arrrrg

        former_active_layer = self.viewer.active_layer
        try:
            former_active_layer.dialog._deselected(None)
        except AttributeError:
            pass

        self.operation.initial_call = True
        self.operation(self.viewer.active_layer)
        self.layer = self.viewer.active_layer
        if(self.layer is None):
            import time
            self.operation(self.viewer.active_layer)
            time.sleep(0.1) # dirty workaround: wait until napari has set its active_layer
            self.layer = self.viewer.active_layer

        self.layer.dialog = self

        self.layer.events.data.connect(self._updated)
        self.layer.events.select.connect(self._selected)
        self.layer.events.deselect.connect(self._deselected)

        self.filter_gui = self.operation.Gui()
        self.dock_widget = viewer.window.add_dock_widget(self.filter_gui, area='right')
        self.filter_gui.set_widget('input1', former_active_layer)

        for i in reversed(range(self.filter_gui.layout().count())):
            self.filter_gui.layout().itemAt(i).widget().setFont(QtGui.QFont('Arial', 12))

    def _updated(self, event):
        self.refresh_all_followers()

    def _selected(self, event):
        self.operation.self = self    # sigh
        self.dock_widget = viewer.window.add_dock_widget(self.filter_gui, area='right')

    def _deselected(self, event):
        self.viewer.window.remove_dock_widget(self.dock_widget)

    def _removed(self):
        self.viewer.window.remove_dock_widget(self.dock_widget)

    def refresh(self):
        """
        Refresh/recompute the current layer
        """
        former = self.operation.self
        self.operation.self = self    # sigh
        self.filter_gui()
        self.operation.self = former

    def refresh_all_followers(self):
        """
        Go through all layers and identify layers which have the current layer (self.layer) as parameter.
        Then, refresh those layers.
        """
        for layer in self.viewer.layers:
            try:
                if layer.dialog.filter_gui.get_widget('input1').currentData() == self.layer:
                    layer.dialog.refresh()
                if layer.dialog.filter_gui.get_widget('input2').currentData() == self.layer:
                    layer.dialog.refresh()
            except AttributeError:
                pass

class Gui(QWidget):
    """This Gui takes a napari as parameter and infiltrates it.

    It adds some buttons for categories of operations.
    """

    def __init__(self, viewer):
        super().__init__()

        self.viewer = viewer

        self.layout = QVBoxLayout()

        self._init_gui()

    def _init_gui(self):
        """Switches the GUI internally between a main menu
        where you can select categories and a sub menu where
        you can keep results or cancel processing.
        """
        # remove all buttons first
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        label = QLabel("Add layer")
        label.setFont(QtGui.QFont('Arial', 12))
        label.setFixedSize(QSize(400, 30))
        self.layout.addWidget(label)


        self._add_button("Filter", self._add_filter_clicked)
        self._add_button("Binarize", self._add_binarize_clicked)
        self._add_button("Combine", self._add_combine_clicked)
        self._add_button("Label", self._add_label_clicked)
        self._add_button("Label Processing", self._add_label_processing_clicked)
        self._add_button("Map", self._map_clicked)
        self._add_button("Mesh", self._mesh_clicked)
        self._add_button("Measure", self._measure_clicked)
        self._add_button("Export workflow", self._export_workflow)

        self.layout.addStretch()

        self.setLayout(self.layout)

        # Add a menu
        action = QAction('Export pyclesperanto code', viewer.window._qt_window)
        action.triggered.connect(self._export_code)
        viewer.window.plugins_menu.addAction(action)

    def _add_button(self, title : str, handler : callable):
        # text
        btn = QPushButton(title, self)
        btn.setFont(QtGui.QFont('Arial', 12))

        # icon
        btn.setIcon(QtGui.QIcon(str(Path(__file__).parent) + "/icons/" + title.lower().replace(" ", "_") + ".png"))
        btn.setIconSize(QSize(30, 30))
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

    def _export_workflow(self):
        print("action")

    def _activate(self, magicgui):
        LayerDialog(self.viewer, magicgui)

    def _export_code(self):
        print(ScriptGenerator(self.viewer.layers).generate())

class ScriptGenerator:
    def __init__(self, layers):
        self.layers = layers
    def generate(self):
        code = self._header()

        for i, layer in enumerate(self.layers):
            parse_layer = False
            try:
                layer.dialog
            except AttributeError:
                parse_layer = True
            if parse_layer:
                code = code + self._export_layer(layer, i)

        code = code + "\n# show result\n" \
                      "from skimage import imshow\n" + \
            "imshow(cle.pull_zyx(image" + str(len(self.layers) - 1) + "))\n"

        return code

    def _header(self):
        return "import pyclesperanto_prototype as cle\n"

    def _push(self, layer, layer_number):
        return "from skimage.io import imread\n" + \
            "image = imread('" + layer.filename + "')\n" + \
            self._nice_name(layer, layer_number) + " = cle.push_zyx(image)\n"

    def _execute(self, layer, layer_number):
        method = layer.dialog.filter_gui.get_widget("operation").currentData()
        method_name = str(method)
        method_name = method_name.replace(method.__class__.__name__, "cle")
        method_name = method_name.replace("please_select", "copy")
        command = method_name + "("

        parameter_names = method.fullargspec.args

        put_comma = False
        for i, parameter_name in enumerate(layer.dialog.filter_gui.param_names):
            if (i < len(parameter_names)):
                comma = ""
                if put_comma:
                    comma = ", "
                put_comma = True

                widget = layer.dialog.filter_gui.get_widget(parameter_name)

                if isinstance(widget, QDoubleSpinBox) or isinstance(widget, QSpinBox):
                    value = widget.value()
                elif isinstance(widget, QDataComboBox):
                    value = widget.currentData()
                else:
                    value = None

                if isinstance(value, Enum): # operation
                    pass
                elif isinstance(value, Image) or isinstance(value, Labels):
                    command = command + comma + parameter_names[i] + "=image" + str(self._get_index_of_layer(value))
                elif isinstance(value, str):
                    command = command + comma + parameter_names[i] + "='" + value + "'"
                else:
                    command = command + comma + parameter_names[i] + "=" + str(value)

        command = command + ")\n"

        command = "image" + str(layer_number) + " = " + command


        return command

    def _get_index_of_layer(self, layer):
        for i, other_layer in enumerate(self.layers):
            if other_layer == layer:
                return i

    def _nice_name(self, layer, layer_number : int):
        name = str(layer.name) + str(layer_number)
        name = name.replace(".", "_")
        return name

    def _export_layer(self, layer, layer_number):
        code = "\n# Layer " + self._nice_name(layer, layer_number) + "\n"

        record_push = False
        try:
            if layer.filename is not None:
                record_push = True
        except:
            pass
        if record_push:
            code = code + self._push(layer, layer_number)

        record_exec = False
        try:
            if layer.dialog is not None:
                record_exec = True
        except:
            pass
        if record_exec:
            code = code + self._execute(layer, layer_number)

        for i, other_layer in enumerate(self.layers):
            parse_layer = False
            try:
                if other_layer.dialog is not None:
                    if (other_layer.dialog.filter_gui.get_widget("input1").currentData() == layer):
                        parse_layer = True
                    if (other_layer.dialog.filter_gui.get_widget("input2").currentData() == layer):
                        parse_layer = True
            except AttributeError:
                pass
            if parse_layer:
                code = code + self._export_layer(other_layer, i)
        return code



# -----------------------------------------------------------------------------
from skimage.io import imread

#image = imread('data/Lund_000500_resampled-cropped.tif')
filename = 'data/CalibZAPWfixed_000154_max-16.tif'
image = imread(filename)
#image = imread('https://samples.fiji.sc/blobs.png'')
#image = imread('C:/structure/data/lund_000500_resampled.tif')


cle.select_device("RTX")
print(cle.get_device())

with napari.gui_qt():
    # create a viewer and add some image
    viewer = napari.Viewer()
    layer = viewer.add_image(image)
    layer.filename = filename

    def _on_removed(event):
        layer = event.value
        try:
            layer.dialog._removed()
        except AttributeError:
            pass
    viewer.layers.events.removed.connect(_on_removed)

    # add the gui to the viewer as a dock widget
    viewer.window.add_dock_widget(Gui(viewer), area='right')


