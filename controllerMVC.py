class DrawController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def draw(self):
        self.model.draw_question()