import torch
import torch.nn as nn
from fastspeech2.model import FastSpeech2
from fastspeech2.loss import Loss
from fastspeech2.dataset import Dataset
from torch.utils.data import DataLoader

class FastSpeech2Model:
    def __init__(self, model_path=None):
        self.model = FastSpeech2()
        if model_path:
            self.model.load_state_dict(torch.load(model_path))
        self.model.train()

    def train(self, dataset, num_epochs=10, batch_size=16, lr=1e-4):
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        criterion = Loss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)

        for epoch in range(num_epochs):
            for batch in dataloader:
                optimizer.zero_grad()
                outputs = self.model(batch['text'], batch['mel'])
                loss = criterion(outputs, batch['mel'])
                loss.backward()
                optimizer.step()
            print(f'Epoch {epoch+1}, Loss: {loss.item()}')

    def save_model(self, output_path):
        torch.save(self.model.state_dict(), output_path)

# Example usage
if __name__ == "__main__":
    dataset = Dataset('data/processed/delhi/data.csv')
    model = FastSpeech2Model()
    model.train(dataset, num_epochs=10)
    model.save_model('models/fastspeech2/model.pth')
