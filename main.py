from notificador import EmailNotificador
from decorators import ComRegistro, ComAssinatura, ComAnexo, ComValidacao


# Bloco principal de execução do script
if __name__ == "__main__":
    
    # -----------------------------
    # Componente base
    # -----------------------------
    # Cria o notificador de email básico, especificando o remetente
    base = EmailNotificador(remetente="noreply@empresa.com") # Email fictício para teste

    # -----------------------------
    # Envolvendo com decorators
    # -----------------------------
    # Aplica múltiplos decorators de forma aninhada:
    # 1. ComValidacao: valida o tamanho da mensagem (máx. 280 caracteres)
    # 2. ComAnexo: adiciona um anexo à mensagem
    # 3. ComAssinatura: adiciona assinatura ao final da mensagem
    # 4. ComRegistro: registra logs antes e depois do envio
    notificador = ComRegistro(
        ComAssinatura(
            ComAnexo(
                ComValidacao(base, max_len=280),
                anexo_id="relatorio_2025.pdf"
            ),
            assinatura="Equipe de Suporte"
        )
    )

    # -----------------------------
    # Uso final
    # -----------------------------
    # Envia a mensagem usando todos os decorators aplicados
    notificador.enviar("cliente@exemplo.com", "Olá! Segue atualização do seu chamado.")

    # No terminal dentro da pasta do projeto, digite no terminal: 'python main.py' para iniciar o programa.
