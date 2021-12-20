from pynput import keyboard
from tcpCliente import tcpCliente

quant = 0

def atribuiValor():
    global quant
    quant += 1
    return quant


def zerarValor():
    global quant
    quant = 0


class botao_bluetooth:
    def on_release(key):
        print('{0}'.format(key))
        if key == keyboard.Key.media_volume_up:
            quantClicada = atribuiValor()
            if quantClicada >= 2:
                tcpCliente.enviaPedidoSocorro()
        else:
            zerarValor()

    with keyboard.Listener(on_release=on_release) as listener: listener.join()
