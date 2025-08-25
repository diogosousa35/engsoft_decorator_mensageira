from abc import ABC
from notificador import Notificador


# Classe abstrata para implementar o padrão Decorator
# Herda de Notificador para manter a interface consistente
class NotificadorDecorator(Notificador, ABC):
    
    # Construtor recebe um objeto Notificador que será "decorado"
    def __init__(self, wrappee: Notificador):
        self._wrappee = wrappee  # Armazena o objeto que será decorado

    # Método enviar delega a execução para o objeto decorado
    def enviar(self, destinatario: str, mensagem: str) -> None:
        self._wrappee.enviar(destinatario, mensagem)


# Decorator que adiciona registro de logs antes e depois do envio
class ComRegistro(NotificadorDecorator):
    
    # Sobrescreve o método enviar
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[LOG] Iniciando envio para {destinatario}...")  # Log antes do envio
        super().enviar(destinatario, mensagem)  # Chama o envio do wrappee
        print(f"[LOG] Envio concluído para {destinatario}.")  # Log após o envio


# Decorator que adiciona uma assinatura à mensagem
class ComAssinatura(NotificadorDecorator):
    
    # Construtor recebe o wrappee e a assinatura
    def __init__(self, wrappee: Notificador, assinatura: str):
        super().__init__(wrappee)
        self.assinatura = assinatura  # Armazena a assinatura

    # Sobrescreve o método enviar para anexar a assinatura
    def enviar(self, destinatario: str, mensagem: str) -> None:
        mensagem = f"{mensagem}\n\n-- {self.assinatura}"  # Adiciona assinatura
        super().enviar(destinatario, mensagem)  # Chama envio do wrappee


# Decorator que adiciona um anexo à mensagem
class ComAnexo(NotificadorDecorator):
    
    # Construtor recebe o wrappee e o identificador do anexo
    def __init__(self, wrappee: Notificador, anexo_id: str):
        super().__init__(wrappee)
        self.anexo_id = anexo_id  # Armazena o ID do anexo

    # Sobrescreve o método enviar para anexar o identificador
    def enviar(self, destinatario: str, mensagem: str) -> None:
        mensagem = f"{mensagem}\n[Anexo: {self.anexo_id}]"  # Adiciona anexo
        super().enviar(destinatario, mensagem)  # Chama envio do wrappee


# Decorator que valida o tamanho da mensagem antes de enviar
class ComValidacao(NotificadorDecorator):
    
    # Construtor recebe o wrappee e o tamanho máximo permitido da mensagem
    def __init__(self, wrappee: Notificador, max_len: int = 200):
        super().__init__(wrappee)
        self.max_len = max_len  # Armazena tamanho máximo permitido

    # Sobrescreve o método enviar para validar o tamanho da mensagem
    def enviar(self, destinatario: str, mensagem: str) -> None:
        if len(mensagem) > self.max_len:
            # Lança erro se a mensagem exceder o tamanho permitido
            raise ValueError(f"Mensagem muito longa (>{self.max_len} caracteres)")
        super().enviar(destinatario, mensagem)  # Chama envio do wrappee
