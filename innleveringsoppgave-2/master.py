def wait():
    input("\n(Trykk Enter for å fortsette...)")

score = 0
print("-----------------------------------------------------------------------------------------------------------")
print("\nErling er prosjektleder og trenger din hjelp til å håndtere konflikter i teamet sitt.")
wait()
print("-----------------------------------------------------------------------------------------------------------")

print("\n\033[1mHvordan håndterer Erling konflikten mellom Silje og Sivert?\033[0m \n") #bold tekst: \033[1m tekst \033[0m

print("1A, Går han til HR? \n1B, Eller tar han individuelle samtaler?\n")

while True:
    valg_1 = input("Velg 1A eller 1B  ").strip().upper()

    if valg_1 == "1A":
        print("\nErling går til HR. De blir ikke enige, og HR kommer med et kompromiss som de må følge.")
        score += 0
        break
    elif valg_1 == "1B":
        print("\nErling tar individuelle samtaler. Han oppfordrer dem til å bli enige, ellers vil han ta en bestemmelse.")
        score += 1
        break
    else:
        print("\nUgyldig svar. Vennligst velg 1A eller 1B.")
wait()


print("-----------------------------------------------------------------------------------------------------------")
print("\n\033[1mHvordan håndterer Erling konflikten mellom Hamdi og Jabir?\033[0m \n")

print("2A, Tar han tidlig dialog? \n2B, Eller lar han dem ordne opp på egenhånd?\n")

while True:
    valg_2 = input("Velg 2A eller 2B  ").strip().upper()

    if valg_2 == "2A":
        print("\nErling tar tidlig dialog med dem, og Hamdi og Jabir begynner å kommunisere bedre. ")
        score += 1
        break
    elif valg_2 == "2B":
        print("\nErling lar dem ordne opp selv. Misnøyen mellom dem bygger seg opp.")
        score -= 1
        break
    else:
        print("\nUgyldig svar. Vennligst velg 2A eller 2B.")
wait()

print("-----------------------------------------------------------------------------------------------------------")
print("\n\033[1mHvordan bevarer Erling motivasjonen i temaet?\033[0m \n")

print("3A, Fokuserer han på teambygging? \n3B, Eller fokuserer han på fremgang?\n")

while True:
    valg_3 = input("Velg 3A, eller 3B  ").strip().upper()

    if valg_3 == "3A":
        print("\nErling fokuserer på teambygging. Teammedlemmene får positive opplevelser med hverandre og de lærer å kommunisere bedre.")
        score += 1
        break
    elif valg_3 == "3B":
        print("\nErling fokuserer på fremgang. Etter teambyggingen har de ulike medlemmene forbedret relasjonen med sine støttespillere\n" \
        "og stemningen mellom de uenige forblir antent." \
        " Dette lover ikke godt for prosjektet.")
        score -= 1
        break
    else:
        print("\nUgyldig svar. Vennligst velg 3A eller 3B.")
wait()

print("-----------------------------------------------------------------------------------------------------------")
#Avlutning 3 mulige utfall. Lag en score, summen bestemmer utfallene.

#positiv
if score > 0:
    print("Teamet gjennompretter tillit og går videre til norming fasen.")
#nøytral
elif score == 0:
    print("En del av konflikten blir løst, men relasjonen er fortsatt svak.")
#negativ
else:
    print("Prosjektet stopper, og felleskapet ryker.")

wait()
print("-----------------------------------------------------------------------------------------------------------")
print("\nTakk for at du spilte historien om Erling!\n")
