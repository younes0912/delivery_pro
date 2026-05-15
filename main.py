from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# هذا الكود يجعل الواجهة احترافية وسلسة
KV = '''
MDScreen:
    md_bg_color: 0.96, 0.96, 0.96, 1

    MDBoxLayout:
        orientation: 'vertical'

        # --- شريط العنوان العلوي الأخضر ---
        MDTopAppBar:
            title: "Delivery Pro Algeria"
            elevation: 3
            md_bg_color: 0.1, 0.4, 0.2, 1  # أخضر جزائري مميز
            specific_text_color: 1, 1, 1, 1
            left_action_items: [["menu", lambda x: None]]
            right_action_items: [["bell-outline", lambda x: None]]

        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                padding: "16dp"
                spacing: "20dp"

                # --- خانة البحث الذكية ---
                MDTextField:
                    hint_text: "ابحث عن مطعم، أكلة، أو صيدلية..."
                    mode: "round"
                    fill_color_normal: 1, 1, 1, 1
                    icon_left: "magnify"
                    size_hint_x: 0.95
                    pos_hint: {"center_x": .5}

                # --- شبكة التصنيفات الجذابة ---
                MDLabel:
                    text: "خدماتنا"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Primary"

                MDGridLayout:
                    cols: 3
                    adaptive_height: True
                    spacing: "12dp"
                    
                    CategoryButton:
                        text: "طعام"
                        icon: "food"
                    CategoryButton:
                        text: "بقالة"
                        icon: "cart-outline"
                    CategoryButton:
                        text: "صيدلية"
                        icon: "pill"
                    CategoryButton:
                        text: "طرود"
                        icon: "package-variant-closed"
                    CategoryButton:
                        text: "هدايا"
                        icon: "gift-outline"
                    CategoryButton:
                        text: "المزيد"
                        icon: "dots-grid"

                # --- قسم العروض المميزة (بيتزا وتاكو) ---
                MDLabel:
                    text: "أقوى العروض 🔥"
                    font_style: "H6"
                    bold: True

                MDBoxLayout:
                    orientation: 'horizontal'
                    adaptive_height: True
                    spacing: "10dp"
                    
                    OfferCard:
                        title: "عرض البيتزا"
                        price: "1000 DZD"
                        bg_color: 0.9, 0.3, 0.2, 1
                    
                    OfferCard:
                        title: "ميكس تاكو"
                        price: "850 DZD"
                        bg_color: 0.1, 0.5, 0.4, 1

        # --- شريط التنقل السفلي الاحترافي ---
        MDBottomNavigation:
            panel_color: 1, 1, 1, 1
            selected_color_background: 0, 0, 0, 0
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
                icon: 'wallet-outline'

<CategoryButton@MDCard>:
    orientation: 'vertical'
    padding: "8dp"
    spacing: "4dp"
    radius: 18
    elevation: 1
    size_hint: None, None
    size: "100dp", "90dp"
    md_bg_color: 1, 1, 1, 1
    text: ""
    icon: ""
    
    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: "32sp"
        theme_text_color: "Custom"
        text_color: 0.1, 0.4, 0.2, 1
        
    MDLabel:
        text: root.text
        halign: "center"
        font_style: "Caption"
        bold: True

<OfferCard@MDCard>:
    orientation: 'vertical'
    padding: "12dp"
    radius: 20
    size_hint: None, None
    size: "160dp", "120dp"
    md_bg_color: root.bg_color
    title: ""
    price: ""
    bg_color: 0,0,0,1
    
    MDLabel:
        text: root.title
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        bold: True
    MDLabel:
        text: root.price
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H6"
'''

class DeliveryProApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

if __name__ == '__main__':
    DeliveryProApp().run()
