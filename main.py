import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Sigmoid fonksiyonu ve türevi
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# YSA modelini eğiten sınıf
class NeuralNetwork:
    def __init__(self, input_neurons, hidden_neurons, output_neurons, learning_rate=0.5):
        self.input_neurons = input_neurons
        self.hidden_neurons = hidden_neurons
        self.output_neurons = output_neurons
        self.learning_rate = learning_rate
        
        # Ağırlıkları rastgele başlatma
        self.weights_input_hidden = np.random.uniform(-1, 1, (self.input_neurons, self.hidden_neurons))
        self.weights_hidden_output = np.random.uniform(-1, 1, (self.hidden_neurons, self.output_neurons))
        
        # Biasları rastgele başlatma
        self.bias_hidden = np.random.uniform(-1, 1, (1, self.hidden_neurons))
        self.bias_output = np.random.uniform(-1, 1, (1, self.output_neurons))
    
    def train(self, inputs, targets, epochs=100):
        errors = []
        for epoch in range(epochs):
            # Forward geçiş
            hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
            hidden_output = sigmoid(hidden_input)
            final_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            final_output = sigmoid(final_input)
            
            # Hata Matrisi (Loss Calculation)
            error = targets - final_output
            errors.append(np.mean(np.abs(error)))
            
            # Geri yayılım
            output_delta = error * sigmoid_derivative(final_output)
            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
            
            # Ağırlıkları güncelleme
            self.weights_hidden_output += hidden_output.T.dot(output_delta) * self.learning_rate
            self.weights_input_hidden += inputs.T.dot(hidden_delta) * self.learning_rate
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate
            
            # Hata raporlama
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Hata: {np.mean(np.abs(error))}")
        return errors
    
    def predict(self, inputs):
        hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = sigmoid(hidden_input)
        final_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        return sigmoid(final_input)

# Eğitim verisi
inputs = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
])

targets = np.array([
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0]
])

hidden_neuron_options = [3, 5, 10]  # Denenecek gizli katman nöron sayıları
learning_rate_options = [0.1, 0.5, 10.0]  # Denenecek öğrenme oranları

for hidden_neurons in hidden_neuron_options:
    for learning_rate in learning_rate_options:
        print(f"\n🔹 Testing with {hidden_neurons} hidden neurons and learning rate {learning_rate}")
        
        # Ağın giriş, gizli ve çıkış katmanındaki nöron sayıları parametrik olarak belirleniyor
        nn = NeuralNetwork(input_neurons=4, hidden_neurons=hidden_neurons, output_neurons=2, learning_rate=learning_rate)
        nn.train(inputs, targets, epochs=10000) #Eğitim 10.000 iterasyon boyunca gerçekleştirildi.
        
        # Yeni tahminleri al
        predictions = nn.predict(inputs)
        rounded_predictions = np.round(predictions)
        
        # Performans Ölçekleri (Accuracy, Precision, Recall, F1-Score)
        accuracy = accuracy_score(targets.flatten(), rounded_predictions.flatten())
        precision = precision_score(targets.flatten(), rounded_predictions.flatten(), zero_division=1)
        recall = recall_score(targets.flatten(), rounded_predictions.flatten(), zero_division=1)
        f1 = f1_score(targets.flatten(), rounded_predictions.flatten(), zero_division=1)
        
        # Sonuçları yazdır
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
