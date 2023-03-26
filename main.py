import settings
from app.display import available_displays

screen = available_displays.get(settings.screen)

screen().self_test()
