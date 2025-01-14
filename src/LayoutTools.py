from PyQt5.QtCore import Qt


class LayoutTools:

    def clear_layout(layout):
        if layout is None:
            return
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
                return
            if item.layout():
                LayoutTools.clear_layout(item.layout())
                item.layout().deleteLater()
                return
        return
        
    def recalculate_layout_indices(dict_of_layouts, offset):
        for counter, i in enumerate(dict_of_layouts):
            dict_of_layouts[i].layout_index = counter + offset
        return
    
    def shared_container_formatting(layout):
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return
    
    def shared_control_formatting(layout):
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return