import os
from src.engine import GeradorMissao
from src.utils import salvar_relatorio

def limpar_tela():
    """Limpa o terminal independentemente do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar_output(missao: dict):
    """Imprime a missão no terminal com uma formatação limpa e organizada."""
    print("\n" + "="*60)
    print("       PROJETO ORDO REALITAS - RELATÓRIO DE MISSÃO")
    print("="*60)
    print(f"📊 STATUS: {missao['config']}") # Nova linha para mostrar o NEX e Jogadores
    print(f"🔮 ELEMENTO DOMINANTE: {missao['tema'].upper()}")
    print(f"📍 LOCALIZAÇÃO: {missao['local']}")
    print(f"📜 BRIEFING: {missao['briefing']}")
    print("-" * 60)
    print(f"🕵️ INVESTIGAÇÃO: {missao['encontros_iniciais']}")
    print(f"⚠️ PERIGO CRESCENTE: {missao['ameaca_meio']}")
    print(f"💀 ENTIDADE FINAL (Boss): {missao['chefe_final']}")
    print("-" * 60)
    print(f"🔄 REVIRAVOLTA: {missao['reviravolta']}")
    print(f"📊 VD TOTAL DO GRUPO: {missao['vd_estimado']}")
    print("="*60 + "\n")

def main():
    path_db = os.path.join("data", "database.json")
    
    try:
        gerador = GeradorMissao(path_db)
    except FileNotFoundError:
        print("Erro Crítico: O arquivo database.json não foi encontrado na pasta 'data'.")
        return
    except Exception as e:
        print(f"Erro Crítico ao iniciar a Engine: {e}")
        return

    while True:
        limpar_tela()
        print("="*60)
        print("         TERMINAL DE OPERAÇÕES - ORDO REALITAS")
        print("="*60)
        
        try:
            # Pergunta a quantidade de jogadores para calcular o balanceamento
            entrada = input("\nDigite a quantidade de jogadores (3 ou 4) ou 'sair': ").lower()
            
            if entrada == 'sair':
                break
                
            qtd = int(entrada)
            if qtd not in [3, 4]:
                print("⚠️ Quantidade inválida. O sistema suporta apenas grupos de 3 ou 4 agentes.")
                input("\n[Pressione ENTER para tentar novamente]")
                continue

            # 1. Gera a missão passando a quantidade de jogadores
            missao = gerador.montar_oneshot(qtd)
            
            # 2. Exibe na tela
            formatar_output(missao)
            
            # 3. Salva no disco (Utils)
            arquivo_salvo = salvar_relatorio(missao)
            print(f"✅ Relatório arquivado em: {arquivo_salvo}\n")
            
        except ValueError:
            print("⚠️ Erro: Por favor, digite um número (3 ou 4).")
            input("\n[Pressione ENTER para continuar]")
            continue

        continuar = input("Deseja gerar uma nova operação? (s/n): ").lower()
        if continuar != 's':
            print("\nEncerrando conexão... Que a Realidade te proteja.")
            break

if __name__ == "__main__":
    main()