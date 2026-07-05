# ==========================================
# 1. ENTRADA DE DADOS (INTERAÇÃO COM O USUÁRIO)
# ==========================================
print("--- SIMULADOR DE TCO: ON-PREMISE VS NUVEM (SAVINGS PLANS 3 ANOS) ---")
print("Este modelo inclui a recompra de hardware (CapEx) a cada 5 anos (60 meses).")
cotacao_input = input("Informe a cotação atual do Dólar (R$): ")

taxa_dolar = float(cotacao_input.replace(',', '.'))

# ==========================================
# 2. PARAMETRIZAÇÃO DOS DADOS (METODOLOGIA)
# ==========================================
meses_projecao = [3, 6, 12, 24, 36, 60, 120]

# --- Cenário On-Premise (Local) ---
capex_hardware = 169986.00
potencia_kw = 0.8
horas_dia = 24
dias_mes = 30
tarifa_kwh = 0.98
pue = 1.55
custo_msp = 2000.00

consumo_energia_mes = (potencia_kw * horas_dia * dias_mes) * tarifa_kwh * pue
opex_local_mes = consumo_energia_mes + custo_msp

# --- Cenários de Nuvem (Custos Mensais em Dólar - Savings Plans) ---
aws_usd_mensal = 1079.16
azure_usd_mensal = 1015.18

aws_brl_mensal = aws_usd_mensal * taxa_dolar
azure_brl_mensal = azure_usd_mensal * taxa_dolar

# ==========================================
# 3. MOTOR DE SIMULAÇÃO E SAÍDA NO TERMINAL
# ==========================================
print("\n=======================================================")
print(f"Cotação utilizada: 1 USD = R$ {taxa_dolar:.2f}")
print(f"OpEx Mensal On-Premise Estimado: R$ {opex_local_mes:.2f}")
print("=======================================================")

for meses in meses_projecao:
    if meses < 12:
        label_tempo = f"{meses} meses"
    elif meses == 12:
        label_tempo = "1 ano (12 meses)"
    else:
        label_tempo = f"{meses // 12} anos ({meses} meses)"
    
    # Lógica de Recompra a cada 60 meses
    qtd_compras_hardware = (meses - 1) // 60 + 1
    
    tco_local = (capex_hardware * qtd_compras_hardware) + (opex_local_mes * meses)
    tco_aws = aws_brl_mensal * meses
    tco_azure = azure_brl_mensal * meses
    
    print(f"\nProjeção para {label_tempo}:")
    print(f"  -> Ciclos de Hardware: {qtd_compras_hardware}x (Servidor)")
    print(f"  -> On-Premise: R$ {tco_local:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"  -> AWS:        R$ {tco_aws:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"  -> Azure:      R$ {tco_azure:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

print("\n=======================================================\n")