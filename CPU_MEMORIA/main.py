import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# configurações do gráfico
fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('Uso de CPU e Memória')
ax.set_xlabel('Tempo')
ax.set_ylabel('Uso (%)')
cpu_line, = ax.plot([], [], label='CPU', color='#1f77b4')
mem_line, = ax.plot([], [], label='Memória', color='#ff7f0e')
ax.legend(loc='upper right')

#adicionando textos ao gráfico
cpu_text = ax.text(0.77, 0.7, '', transform=ax.transAxes)
mem_text = ax.text(0.77, 0.6, '', transform=ax.transAxes)

# FUNCAO DE ATUALIZAÇÃO DO GRÁFICO
def upd_chart(frame):

    # obtendo o uso de CPU e memória
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_percent = memory.percent

    # adicionando os dados ao gráfico
    cpu_line.set_data(list(range(frame)), [cpu_percent] * frame)
    mem_line.set_data(list(range(frame)), [memory_percent] * frame)

    # atualizando os textos
    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memória: {memory_percent:.1f}%')

    return cpu_line, mem_line, cpu_text, mem_text


# criando a animação
animation = FuncAnimation(fig, upd_chart, frames=100, interval=1000, blit=True)

#estilizando o gráfico
for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(4)

#estilizando o fundo do gráfico
ax.set_facecolor('#f0f0f0')


plt.show()