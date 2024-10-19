import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.button import Button # кнопка
from kivy.uix.label import Label # надпись
from kivy.uix.boxlayout import BoxLayout # макет (это тоже виджет!)
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
# Создадим класс-наследник App. В нём будет дописываться функционал приложения.
class ScrButton(Button):
   def __init__(self, screen, direction="right", goal="main", **kwargs):
      super().__init__(**kwargs)
      self.screen = screen
      self.direction = direction
      self.goal = goal
   def on_press(self):
      self.screen.manager.transition.direction = self.direction
      self.screen.manager.current = self.goal
class MainScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
      hl = BoxLayout()
      txt = Label(text= 'Выбери Экран')
      vl.add_widget(ScrButton(self, direction='up', goal='first', text="1"))
      vl.add_widget(ScrButton(self, direction='left', goal='second', text="2"))
      vl.add_widget(ScrButton(self, direction='right', goal='third', text="3"))
      vl.add_widget(ScrButton(self, direction='down', goal='fourth', text="4"))
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)
      #h1.add_widget(hl)


class FirstScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
      hl = BoxLayout()
      txt = Label(text= 'Выбор: 1')
      vl.add_widget(Button(text ="Push Me !", color =(0, 0, 0, 1),background_normal = 'hamster.png',background_down ='hamster.png',size_hint = (.5, .5),pos_hint = {"x":0.35, "y":0.3}) )
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)
      #h1.add_widget(hl)
class SecondScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
      hl = BoxLayout()
      vl.add_widget(TextInput(text='ВСТАВЬТЕ ЗДЕСЬ ТЕКСТ'))
      vl.add_widget(ScrButton(self, direction='down', goal='main', text= 'Экран 2, напишите что-нибудь а потом уйдите.'))
      hl.add_widget(vl)
      self.add_widget(hl)
class ThirdScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
      hl = BoxLayout()
      txt = ScrButton(text= 'Экран 2, напишите что-нибудь а потом уйдите.')
      vl.add_widget(ScrButton(self, direction='down', goal='main', text="1"))
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)
class FourthScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
      hl = BoxLayout()
      txt = Label(text= 'Выбери Экран')
      vl.add_widget(ScrButton(self, direction='down', goal='main', text="1"))
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)
class MyApp(App):
   def build(self):
      sm = ScreenManager()
      sm.add_widget(MainScr(name="main"))
      sm.add_widget(FirstScr(name="first"))
      sm.add_widget(SecondScr(name="second"))
      sm.add_widget(ThirdScr(name="third"))
      sm.add_widget(FourthScr(name="fourth"))

      return sm
MyApp().run()