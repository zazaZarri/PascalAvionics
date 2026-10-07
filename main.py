from apparati import APPARATI, aggiorna_stato
from report import filtra_per_stato, filtra_per_bus
from riepilogo import crea_riepilogo


def stampa_apparati(titolo, apparati):
    print(f"\n--- {titolo} ---")
    if not apparati:
        print("(nessun apparato)")
        return
    for codice, dati in apparati.items():
        print(f"{codice}: {dati['nome']} | {dati['bus']} | {dati['stato']}")


def stampa_riepilogo(riepilogo):
    print("\n--- RIEPILOGO ---")
    for chiave, valore in riepilogo.items():
        print(f"{chiave}: {valore}")


def mostra_tutto():
    stampa_apparati("REGISTRO", APPARATI)
    stampa_apparati("REPORT STATO: OFFLINE", filtra_per_stato("OFFLINE"))
    stampa_apparati("REPORT BUS: BUS-A", filtra_per_bus("BUS-A"))
    stampa_riepilogo(crea_riepilogo())


def main():
    print("=== DATI INIZIALI ===")
    mostra_tutto()

    print("\n=== AGGIORNAMENTO: SEN-03 -> ok ===")
    if aggiorna_stato("SEN-03", "ok"):
        print("Stato aggiornato.")
    mostra_tutto()


if __name__ == "__main__":
    main()