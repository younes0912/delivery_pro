from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# إعداد لون الخلفية
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class DeliveryApp(App):
    def build(self):
        self.title = "Delivery Pro Algeria"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان التطبيق
        self.header = Label(text="مرحباً بك في ديليفري برو", font_size='28sp', color=(0, 1, 0.7, 1))
        
        # أزرار المنتجات
        btn_pizza = Button(text="طلب بيتزا (1200 DZD)", background_color=(0.2, 0.6, 1, 1))
        btn_tacos = Button(text="طلب تاكوس (850 DZD)", background_color=(0.2, 0.6, 1, 1))
        
        # ربط الأزرار بدوال البرمجة
        btn_pizza.bind(on_press=self.order_pizza)
        btn_tacos.bind(on_press=self.order_tacos)
        
        layout.add_widget(self.header)
        layout.add_widget(btn_pizza)
        layout.add_widget(btn_tacos)
        
        return layout

    def order_pizza(self, instance):
        self.header.text = "✅ تم إضافة بيتزا!"

    def order_tacos(self, instance):
        self.header.text = "✅ تم إضافة تاكوس!"

if __name__ == "__main__":
    DeliveryApp().run()
