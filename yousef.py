# individuelle løsning for IS-118 oppgave 2 yousef

print("Hei! Du spiller som Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet ditt er midt i storming-fasen, og du må ta tre valg som påvirker historien.\n")

# ----------------- Beslutning 1 -----------------
print("BESLUTNING 1:")
print("Silje og Sivert krangler mer og mer om design vs. teknisk løsning.")
print("Hva vil du gjøre?")
print("A: Hente inn HR for å mekle.")
print("B: Snakke med dem hver for seg.")

valg1 = input("Skriv A eller B: ").lower()

if valg1 == "a":
    konflikt1 = "hr"
    print("\nHR kommer inn og prøver å roe ned situasjonen. Det hjelper litt, men ikke helt.")
elif valg1 == "b":
    konflikt1 = "samtale"
    print("\nDu tar en prat med begge. Det virker som de roer seg litt, i hvert fall foreløpig.")
else:
    konflikt1 = "ingen"
    print("\nDu gjør ikke noe konkret, og konflikten fortsetter i bakgrunnen.")

# ----------------- Beslutning 2 -----------------
print("\nBESLUTNING 2:")
print("Hamdi og Jabir er uenige om hvordan innbyggerne skal delta digitalt.")
print("Hva gjør du?")
print("A: Sette dere ned tidlig og avklare ting.")
print("B: La dem prøve å fikse det selv.")

valg2 = input("Skriv A eller B: ").lower()

if valg2 == "a":
    konflikt2 = "dialog"
    print("\nDere tar en prat sammen. Det hjelper en del og de finner noe de kan bli enige om.")
elif valg2 == "b":
    konflikt2 = "selv"
    print("\nDu lar dem være. Det virker ikke som konflikten blir bedre.")
else:
    konflikt2 = "ingen"
    print("\nDu gjør ikke noe her heller, og uenigheten vokser litt.")

# ----------------- Beslutning 3 -----------------
print("\nBESLUTNING 3:")
print("Motivasjonen i teamet begynner å falle. Hva gjør du?")
print("A: Prøve teambygging og fokus på å bedre miljøet.")
print("B: Pushe hardere for å komme i mål innen fristen.")

valg3 = input("Skriv A eller B: ").lower()

if valg3 == "a":
    motivasjon = "team"
    print("\nDere gjør litt teambygging og det blir litt bedre stemning.")
elif valg3 == "b":
    motivasjon = "push"
    print("\nDu pusher teamet. Det funker for noen, men stresser de andre.")
else:
    motivasjon = "ingen"
    print("\nDu gjør ikke noe med motivasjonen. Stemningen forblir litt dårlig.")

# ----------------- SLUTT -----------------
print("\n--- SLUTTRESULTAT ---")

if konflikt1 in ["hr", "samtale"] and konflikt2 == "dialog" and motivasjon == "team":
    print("Teamet finner litt tilbake til hverandre og samarbeidet blir bedre.")
    print("Dere går videre mot norming-fasen og prosjektet holder seg på planen.")
elif konflikt1 != "ingen" and konflikt2 != "ingen" and motivasjon != "ingen":
    print("Konfliktene er litt løst, men det er fortsatt litt sår stemning i gruppa.")
    print("Prosjektet går videre, men det er ikke helt stabilt ennå.")
else:
    print("Teamet sliter fortsatt med konflikter og samarbeidet faller litt sammen.")
    print("Prosjektet blir forsinket og motivasjonen er lav.")


print("\nTakk for at du spilte historien!")
