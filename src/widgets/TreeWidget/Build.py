from PySide6 import QtWidgets

from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=None,
            height=None,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,

            # Paramètres
            animate=False,
            scroll_h=vb_wg.SCROLL_H,
            scroll_v=vb_wg.SCROLL_V,
            focus_policy=FocusPolicy().no_focus(),
            frame_shape=vb_wg.FRAME_SHAPE,
            frame_shadow=vb_wg.FRAME_SHADOW,
            line_width=0,
            header_hidden=True,
            sorting=False,

            # Curseur
            cursor=vb_wg.CUR,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_item=vb_wg.BG_ITEM,
            bg_item_hover=vb_wg.BG_ITEM_HOVER,
            bg_item_checked=vb_wg.BG_ITEM_CHECKED,
            bg_item_checked_hover=vb_wg.BG_ITEM_CHECKED_HOVER,
            bg_header=Rgb().th2(),
            # Couleurs FG
            fg=vb_wg.FG,
            fg_item=vb_wg.FG_ITEM,
            fg_item_hover=vb_wg.FG_ITEM_HOVER,
            fg_item_checked=vb_wg.FG_ITEM_CHECKED,
            fg_item_checked_hover=vb_wg.FG_ITEM_CHECKED_HOVER,
            fg_header=Rgb().th1(),

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures HD
            border_hd=vb_wg.BORDER_WIDTH,
            border_hd_style=vb_wg.BORDER_STYLE,
            border_hd_rgb=vb_wg.BORDER_RGB,
            # Bordures item
            border_item=vb_wg.BORDER_WIDTH,
            border_item_style=vb_wg.BORDER_STYLE,
            border_item_rgb=vb_wg.BORDER_RGB,
            # Bordures item hover
            border_item_hover=vb_wg.BORDER_WIDTH,
            border_item_hover_style=vb_wg.BORDER_STYLE,
            border_item_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures item checked
            border_item_checked=vb_wg.BORDER_WIDTH,
            border_item_checked_style=vb_wg.BORDER_STYLE,
            border_item_checked_rgb=vb_wg.BORDER_RGB,
            # Bordures item checked hover
            border_item_checked_hover=vb_wg.BORDER_WIDTH,
            border_item_checked_hover_style=vb_wg.BORDER_STYLE,
            border_item_checked_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
            radius_item=vb_wg.RADIUS,

            # Scroll
            scroll_bg=vb_wg.SCROLL_BG,
            scroll_width=vb_wg.SCROLL_WIDTH,
            scroll_height=vb_wg.SCROLL_HEIGHT,
            scroll_handle_bg=vb_wg.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=vb_wg.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=vb_wg.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=vb_wg.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=vb_wg.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=vb_wg.SCROLL_HANDLE_MIN_HEIGHT,
    ):
        """
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *Font: int() : Font().%nomFont() \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *FrameShape: QtWidgets.QFrame : FrameShape().%nomFrameForme \n
        *FrameShadow: QtWidgets.QFrame : FrameShadow().%nomFrameOmbre \n
        *Scroll: QtCore.Qt : Scroll().%nomScroll() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param font: str()
        :param font_size: *Font
        :param animate: bool()
        :param scroll_h: *Scroll
        :param scroll_v: *Scroll
        :param focus_policy: *FocusPolicy
        :param frame_shape: *FrameShape
        :param frame_shadow: *FrameShadow
        :param line_width: int()
        :param header_hidden: bool()
        :param sorting: bool()
        :param cursor: *Cur
        :param bg: *RgbBox
        :param bg_item: *RgbBox
        :param bg_item_hover: *RgbBox
        :param bg_item_checked: *RgbBox
        :param bg_item_checked_hover: *RgbBox
        :param bg_header: *RgbBox
        :param fg: *RgbBox
        :param fg_item: *RgbBox
        :param fg_item_hover: *RgbBox
        :param fg_item_checked: *RgbBox
        :param fg_item_checked_hover: *RgbBox
        :param fg_header: *RgbBox
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param border_hd: *Tuple
        :param border_hd_style: *Border_Style
        :param border_hd_rgb: *RgbBox
        :param border_item: *Tuple
        :param border_item_style: *Border_Style
        :param border_item_rgb: *RgbBox
        :param border_item_hover: *Tuple
        :param border_item_hover_style: *Border_Style
        :param border_item_hover_rgb: *RgbBox
        :param border_item_checked: *Tuple
        :param border_item_checked_style: *Border_Style
        :param border_item_checked_rgb: *RgbBox
        :param border_item_checked_hover: *Tuple
        :param border_item_checked_hover_style: *Border_Style
        :param border_item_checked_hover_rgb: *RgbBox
        :param radius: *Tuple
        :param radius_item: *Tuple
        :param scroll_bg: *RgbBox
        :param scroll_width: *Dim
        :param scroll_height: *Dim
        :param scroll_handle_bg: *RgbBox
        :param scroll_handle_bg_hover: *RgbBox
        :param scroll_handle_fg: *RgbBox
        :param scroll_handle_fg_hover: *RgbBox
        :param scroll_handle_min_width: *Dim
        :param scroll_handle_min_height: *Dim
        """
        
        style = f"""
                /* TREEWIDGET */
                QHeaderView::section {{
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                border-top: {border_hd[0]}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd[1]}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd[2]}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd[3]}px {border_hd_style} rgba{border_hd_rgb};
                }}

                QTreeWidget, QTreeView {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}

                QTreeWidget::item, QTreeView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item[0]}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item[1]}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item[2]}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item[3]}px {border_item_style} rgba{border_item_rgb};
                border-top-right-radius: {radius_item[0]}px;
                border-top-left-radius: {radius_item[1]}px;
                border-bottom-right-radius: {radius_item[2]}px;
                border-bottom-left-radius: {radius_item[3]}px;
                }}

                QTreeWidget::item:hover, QTreeView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_hover[0]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-bottom: {border_item_hover[1]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-right: {border_item_hover[2]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-left: {border_item_hover[3]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                }}

                QTreeWidget::item:selected, QTreeView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_checked[0]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-bottom: {border_item_checked[1]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-right: {border_item_checked[2]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-left: {border_item_checked[3]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                }}

                QTreeWidget::item:selected:hover, QTreeView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_checked_hover[0]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-bottom: {border_item_checked_hover[1]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-right: {border_item_checked_hover[2]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-left: {border_item_checked_hover[3]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                }}

                /* BORDURES */
                .QTreeWidget, .QTreeView {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QTreeWidget:hover, .QTreeView:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QTreeWidget, .QTreeView {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}

                /* SCROLL */
                QScrollBar {{
                background-color: rgba{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QScrollBar::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QScrollBar::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QScrollBar::handle {{
                background-color: rgba{scroll_handle_fg};
                }}
                QScrollBar::handle:hover {{
                background-color: rgba{scroll_handle_fg_hover};
                }}

                QScrollBar::add-page, QScrollBar::sub-page {{
                background-color: rgba{scroll_handle_bg};
                border: none;
                }}
                QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
                background-color: rgba{scroll_handle_bg_hover};
                border: none;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setAnimated(animate)
            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)
            wg.setFrameShape(QtWidgets.QFrame.NoFrame)
            wg.setFocusPolicy(focus_policy)
            wg.setFrameShape(frame_shape)
            wg.setFrameShadow(frame_shadow)
            wg.setLineWidth(line_width)
            wg.setHeaderHidden(header_hidden)
            wg.setSortingEnabled(sorting)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
