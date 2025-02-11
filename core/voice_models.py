class VoiceModelManager:
    def __init__(self):
        self.models = {
            "male": "male_model.pth",
            "female": "female_model.pth",
            "child": "child_model.pth",
            "elderly": "elderly_model.pth"
        }

    def get_model_path(self, voice_model):
        return self.models.get(voice_model, "default_model.pth")
