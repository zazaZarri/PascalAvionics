from apparati import APPARATI

STATI_AMMESSI = ("OK", "ATTENZIONE", "OFFLINE")


def crea_riepilogo(apparati=None):
    """Restituisce un dizionario con il totale degli apparati e il conteggio per stato.

    Esempio: {"totale": 3, "OK": 1, "ATTENZIONE": 1, "OFFLINE": 1}
    """
    if apparati is None:
        apparati = APPARATI

    riepilogo = {"totale": len(apparati)}
    for stato in STATI_AMMESSI:
        riepilogo[stato] = 0

    for dati in apparati.values():
        stato = dati["stato"]
        if stato in riepilogo:
            riepilogo[stato] += 1

    return riepilogo