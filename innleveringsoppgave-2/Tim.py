# Enkel interaktiv historie om Erling

def valg(spørsmål, a1, a2):
    """Spør bruker om et valg med to alternativer."""
    print()
    print(spørsmål)
    print("1:", a1)
    print("2:", a2)

    while True:
        svar = input("Skriv 1 eller 2: ").strip()
        if svar == "1":
            return "1"
        elif svar == "2":     
            return "2"
        else:
            print("Ugyldig input. Prøv igjen.")


def main():
    print("=== ERLING SOM PROSJEKTLEDER ===")
    print("Du er Erling. Teamet ditt har mye konflikter.")
    print("Dine valg bestemmer hvordan det går med prosjektet.")

    # Variabler for å lagre valgene
    valg1 = ""
    valg2 = ""
    valg3 = ""

    # Brukes til å regne ut slutt (positiv eller negativ)
    score = 0

    # -------- VALG 1 --------
    valg1 = valg(
        "Konflikt 1: Sivert og Silje er veldig uenige om løsningen.",
        "Be HR om hjelp som mekler.",
        "Snakk med Sivert og Silje hver for seg."
    )

    if valg1 == "1":
        print("\nDu kontakter HR. De hjelper dere å roe ned konflikten.")
        score += 1
    else:
        print("\nDu snakker med dem hver for seg, men de føler seg ikke helt hørt.")
        score -= 1

    # -------- VALG 2 --------
    valg2 = valg(
        "Konflikt 2: Hamdi vil ha kontroll, Jabir vil ha mer frihet.",
        "Samle dem til en tidlig prat.",
        "La dem prøve å løse det selv."
    )

    if valg2 == "1":
        print("\nDere snakker sammen tidlig og finner en mellomløsning.")
        score += 1
    else:
        print("\nDu lar dem ordne opp selv. Konflikten blir større.")
        score -= 1

    # -------- VALG 3 --------
    valg3 = valg(
        "Motivasjonen i teamet synker.",
        "Ha fokus på teambygging og relasjon.",
        "Pushe hardt på framdrift og frist."
    )

    if valg3 == "1":
        print("\nDu bruker tid på teamfølelse. Folk snakker bedre sammen.")
        score += 1
    else:
        print("\nDu pusher på frist. Teamet opplever mer stress.")
        score -= 1

    # -------- SLUTT --------
    print("\n=== SLUTT PÅ HISTORIEN ===")
    print("Valgene dine:")
    print("- Valg 1:", "HR" if valg1 == "1" else "Individuelle samtaler")
    print("- Valg 2:", "Tidlig prat" if valg2 == "1" else "Lar dem ordne opp selv")
    print("- Valg 3:", "Teambygging" if valg3 == "1" else "Pushe frist")

    # Her bruker vi if / elif / else for TRE forskjellige slutt-utfall
    if score >= 2:
        print("\nSluttutfall: Sterkt team.")
        print("Teamet stoler på deg. Prosjektet går videre på en god måte.")
    elif score >= 0:
        print("\nSluttutfall: OK resultat.")
        print("Prosjektet går videre, men ikke alle er helt fornøyde.")
    else:
        print("\nSluttutfall: Prosjektet sliter.")
        print("Konfliktene blir for store, og motivasjonen er lav.")

    print("\nTakk for at du spilte historien om Erling!")


if __name__ == "__main__":
    main()
