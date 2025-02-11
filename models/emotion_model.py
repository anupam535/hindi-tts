import torch
import torch.nn as nn

class EmotionModel(nn.Module):
    def __init__(self):
        super(EmotionModel, self).__init__()
        self.emotion_embeddings = nn.Embedding(num_embeddings=7, embedding_dim=512)  # Assuming 7 emotions

    def forward(self, emotion_index):
        """
        Get emotion embedding for a given emotion index.
        :param emotion_index: Index of the emotion (0-6)
        :return: Emotion embedding
        """
        return self.emotion_embeddings(emotion_index)
