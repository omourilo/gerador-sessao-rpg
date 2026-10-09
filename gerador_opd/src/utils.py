import datetime
import os

def salvar_relatorio(missao: dict) -> str:
    """Salva a missão gerada em um arquivo de texto dentro da pasta missoes_salvas."""
    
    # Cria o diretório de salvamento automaticamente, caso não exista
    pasta_destino = "missoes_salvas"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Formata a data atual para criar um nome de arquivo único
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{pasta_destino}/Operacao_{missao['tema']}_{data_atual}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write("       ORDO REALITAS - RELATÓRIO OFICIAL DE MISSÃO\n")
        f.write("="*60 + "\n\n")
        f.write(f"🩸 ELEMENTO DOMINANTE: {missao['tema'].upper()}\n")
        f.write(f"📍 LOCALIZAÇÃO: {missao['local']}\n")
        f.write(f"📜 BRIEFING: {missao['briefing']}\n\n")
        f.write("-" * 60 + "\n")
        f.write(f"🕵️ INVESTIGAÇÃO (Existências): {missao['encontros_iniciais']}\n")
        f.write(f"⚠️ PERIGO CRESCENTE (Manifestação): {missao['ameaca_meio']}\n")
        f.write(f"💀 ENTIDADE FINAL (Boss): {missao['chefe_final']}\n\n")
        f.write("-" * 60 + "\n")
        f.write(f"🔄 REVIRAVOLTA: {missao['reviravolta']}\n")
        f.write(f"📊 VD TOTAL ESTIMADO: {missao['vd_estimado']}\n")
        f.write("="*60 + "\n")

    return nome_arquivo