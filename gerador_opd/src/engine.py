import json
import random
from typing import List, Dict

class GeradorMissao:
    def __init__(self, data_path: str):
        # Carrega o JSON garantindo que aceite caracteres especiais
        with open(data_path, 'r', encoding='utf-8') as f:
            self.db = json.load(f)

    def buscar_monstro(self, categoria: str, vd_alvo: int, elemento: str) -> Dict:
        """Busca o monstro na categoria correta sem ultrapassar o VD alvo."""
        # Tenta buscar especificamente na categoria sugerida
        pool = self.db["ameacas"][categoria]
        
        # 1. Filtra por elemento e limite de VD
        validos = [m for m in pool if m["vd"] <= vd_alvo and (m["elemento"] == elemento or m["elemento"] == "Medo")]
        
        # 2. Se não achou do elemento, ignora o elemento mas mantém a categoria e o VD
        if not validos:
            validos = [m for m in pool if m["vd"] <= vd_alvo]

        # 3. Se a categoria estiver vazia para esse VD, busca em tudo (Segurança)
        if not validos:
            todas = self.db["ameacas"]["existencias"] + self.db["ameacas"]["manifestacoes"]
            validos = [m for m in todas if m["vd"] <= vd_alvo]

        # Ordena para pegar o mais forte disponível que respeite o teto (vd_alvo)
        validos.sort(key=lambda x: x["vd"], reverse=True)
        
        # Pega o maior VD encontrado dentro dos válidos
        maior_vd = validos[0]["vd"]
        melhores = [m for m in validos if m["vd"] == maior_vd]
        
        return random.choice(melhores)

    def montar_oneshot(self, num_players: int) -> Dict:
        nex_sorteado = random.choice([10, 20])
        vd_grupo = num_players * nex_sorteado
        elemento_principal = random.choice(["Sangue", "Morte", "Energia", "Conhecimento"])
        
        # --- DEFINIÇÃO DE LIMITES RÍGIDOS ---
        # Cena 1 (Fácil): 30% do VD do grupo
        limite_f = vd_grupo * 0.4  # Para 3p NEX 10, alvo é 12 (pegará VD 10)
        
        # Cena 2 (Médio): 60% do VD do grupo (AQUI ESTAVA O ERRO)
        limite_m = vd_grupo * 0.7  # Para 3p NEX 10, alvo é 21 (pegará VD 20)
        
        # Cena 3 (Boss): VD do grupo + pequena margem se for NEX 10
        limite_b = vd_grupo if nex_sorteado == 20 else (vd_grupo + 10)

        # --- EXECUÇÃO DA BUSCA ---
        facil = self.buscar_monstro("existencias", int(limite_f), elemento_principal)
        medio = self.buscar_monstro("existencias" if nex_sorteado == 10 else "manifestacoes", int(limite_m), elemento_principal)
        
        cat_boss = "manifestacoes" if nex_sorteado == 10 else "entidades"
        boss = self.buscar_monstro(cat_boss, int(limite_b), elemento_principal)

        return {
            "config": f"{num_players} Agentes | NEX {nex_sorteado}% | VD Grupo: {vd_grupo}",
            "tema": elemento_principal,
            "briefing": random.choice(self.db["ganchos"][elemento_principal] + self.db["ganchos"]["Medo"]),
            "local": random.choice(self.db["locais"][elemento_principal]),
            "encontros_iniciais": f"{facil['nome']} (VD {facil['vd']})",
            "ameaca_meio": f"{medio['nome']} (VD {medio['vd']})",
            "chefe_final": f"{boss['nome']} (VD {boss['vd']})",
            "reviravolta": random.choice(self.db["reviravoltas"][elemento_principal] + self.db["reviravoltas"]["Medo"]),
            "vd_estimado": vd_grupo
        }