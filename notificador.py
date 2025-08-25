from abc import ABC, abstractmethod


# Define uma classe abstrata chamada Notificador
# ABC (Abstract Base Class) indica que essa classe não deve ser instanciada diretamente
class Notificador(ABC):
    
    # Define um método abstrato que todas as subclasses devem implementar
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        # Pass indica que a implementação será feita pelas subclasses
        pass


# Define uma classe concreta que herda de Notificador para enviar emails
class EmailNotificador(Notificador):
    
    # Construtor da classe, recebe o remetente do email
    def __init__(self, remetente: str):
        self.remetente = remetente

    # Implementa o método abstrato enviar, específico para emails
    def enviar(self, destinatario: str, mensagem: str) -> None:
        # Simula o envio de um email imprimindo no console
        print(f"[EMAIL] De: {self.remetente} Para: {destinatario}")
        print(f"Mensagem: {mensagem}\n")


# Define uma classe concreta que herda de Notificador para enviar SMS
class SMSNotificador(Notificador):
    
    # Construtor da classe, recebe o número de origem do SMS
    def __init__(self, numero: str):
        self.numero = numero

    # Implementa o método abstrato enviar, específico para SMS
    def enviar(self, destinatario: str, mensagem: str) -> None:
        # Simula o envio de um SMS imprimindo no console
        print(f"[SMS] De: {self.numero} Para: {destinatario}")
        print(f"Mensagem: {mensagem}\n")
