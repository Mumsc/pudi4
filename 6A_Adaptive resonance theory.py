pip install minisom

from minisom import MiniSom
import matplotlib.pyplot as plt

data = [[ 0.80, 0.55, 0.22, 0.03],
[ 0.82, 0.50, 0.23, 0.03],
[ 0.80, 0.54, 0.22, 0.03],
[ 0.80, 0.53, 0.26, 0.03],
[ 1.0, 0.76, 0.77, 0.13],
[ 0.75, 0.60, 0.25, 0.03],
[ 0.77, 0.59, 0.22, 0.03]]
som = MiniSom(6, 6, 4, sigma=0.3, learning_rate=0.5)
som.train_random(data, 100)
qnt=som.quantization(data)
plt.title("numbers")
for i,m in enumerate(qnt):
    plt.text(m[1],m[0],data[i],ha='center',va='center',
             bbox=dict(facecolor='white',alpha=0.5,lw=0))
plt.imshow(som.distance_map())
plt.show()




