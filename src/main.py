from nicegui import ui

@ui.page('/', dark=True)
def home_page():
    with ui.card().classes('fixed-center'):
        ui.label('GitGlide')
        ui.label('Discover your Code Crush!')
        ui.separator()
        ui.button('Like', icon='thumb_up')
        ui.button('Dislike', icon='thumb_down')
        ui.button('Next', icon='history')

ui.run()