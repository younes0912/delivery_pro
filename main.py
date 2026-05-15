from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# واجهة التطبيق الاحترافية
KV = '''
MDScreen:
    md_bg_color: 0.96, 0.96, 0.96, 1

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Delivery Pro Algeria"
            elevation: 3
            md_bg_color: 0.1, 0.4, 0.2, 1
            specific_text_color: 1, 1, 1, 1
            left_action_items: [["menu", lambda x: None]]

        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                padding: "16dp"
                spacing: "20dp"

                MDTextField:
                    hint_text: "ابحث عن مطعم أو صيدلية..."
                    mode: "round"
                    fill_color_normal: 1, 1, 1, 1
                    icon_left: "magnify"

                MDLabel:
                    text: "الخدمات المتاحة"
                    font_style: "H6"
                    bold: True

                MDGridLayout:
                    cols: 3
                    adaptive_height: True
                    spacing: "12dp"
                    
                    CategoryCard:
                        text: "طعام"
                        icon: "food"
                    CategoryCard:
                        text: "بقالة"
                        icon: "cart"
                    CategoryCard:
                        text: "صيدلية"
                        icon: "pill"
                    CategoryCard:
                        text: "طرود"
                        icon: "package"
                    CategoryCard:
                        text: "هدايا"
                        icon: "gift"
                    CategoryCard:
                        text: "المزيد"
                        icon: "dots-grid"

        MDBottomNavigation:
            panel_color: 1, 1, 1, 1
            text_color_active: 0.1, 0.4, 0.2, 1
            MDBottomNavigationItem:
                name: 'home'
                text: 'الرئيسية'
                icon: 'home'
            MDBottomNavigationItem:
                name: 'orders'
                text: 'طلباتي'
                icon: 'receipt'
            MDBottomNavigationItem:
                name: 'wallet'
                text: 'المحفظة'
                icon: 'wallet'

<CategoryCard@MDCard>:
    orientation: 'vertical'
    padding: "8dp"
    radius: 15
    elevation: 1
    size_hint: None, None
    size: "100dp", "90dp"
    md_bg_color: 1, 1, 1, 1
    text: ""
    icon: ""
    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: "30sp"
        theme_text_color: "Custom"
        text_color: 0.1, 0.4, 0.2, 1
    MDLabel:
        text: root.text
        halign: "center"
        font_style: "Caption"
        bold: True
'''

class DeliveryApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

if __name__ == '__main__':
    DeliveryApp().run()
