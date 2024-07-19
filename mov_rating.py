from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider

class MovieRatingApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.movie_title_input = TextInput(hint_text='Enter movie title')
        layout.add_widget(self.movie_title_input)
        
        self.movie_image = Image(source='movie.jpg', size_hint=(1, 2))
        layout.add_widget(self.movie_image)
        
        self.movie_rating_label = Label(text='Rating: ')
        layout.add_widget(self.movie_rating_label)
        
        self.rating_slider = Slider(min=0, max=5, value=0, step=1, orientation='horizontal')
        layout.add_widget(self.rating_slider)
        
        rate_button = Button(text='Rate Movie', on_press=self.rate_movie)
        layout.add_widget(rate_button)
        
        return layout
    
    def rate_movie(self, instance):
        movie_title = self.movie_title_input.text
        rating = self.rating_slider.value
        self.movie_rating_label.text = f'Rating: {rating}'
    
if __name__ == '__main__':
    MovieRatingApp().run()
