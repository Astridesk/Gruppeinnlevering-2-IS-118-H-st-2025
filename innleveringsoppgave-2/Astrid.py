
 #Introduksjon
# Beslutningspunkt 1, Silje og Sivert
# 1A “Erling går til HR -> kompromiss -> Siljes motivasjon svekkes” 
# 1B “Erling tar individuelle samtaler -> oppfordrer til enighet -> de blir enige” 
#Beslutningspunkt 2 
#“Erling tar tidlig dialog -> bedre kommunikasjon -> enighet” 
#“Erling lar dem ordre på egenhånd -> misnøye fortsetter -> sakskonflikt” 
#Beslutningspunkt 3
#“Erling fokuserer på teambygging --> lærer å kommunisere bedre -> prøver å se fra hverandres synspunkt”
#“Erling fokuserer på fremgang -> jobber ikke effektivt ->prosjektet stagnerer” 
#Avslutning, 3 mulige utfall


print("Introduksjon")

print("-----------------------------------------------------------------------------------------------------------")

print("\nHvordan håndterer Erling konflikten mellom Silje og Sivert?\n")

print("1A, Går han til HR? \n1B, Eller tar han individuelle samtaler?\n")

#spellproof input
valg_1 = input("Velg 1A eller 1B  ")

if valg_1 == "1A":
    print("Erling går til HR. De blir ikke enige, og HR kommer med et kompromiss som de må følge.")
elif valg_1 == "1B":
    print("Erling tar individuelle samtaler. Han oppfordrer dem til å bli enige, ellers vil han ta en bestemmelse.")

print("-----------------------------------------------------------------------------------------------------------")
print("\nHvordan håndterer Erling konflikten mellom Hamdi og Jabir\n")

print("2A, Tar han tidlig dialog? \n2B, Eller lar han dem ordne opp på egenhånd?\n")

valg_2 = input("Velg 2A eller 2B  ")

if valg_2 == "2A":
    print("Hamdi og Jabir begynner å kommunisere bedre. ")
elif valg_2 == "2B":
    print(" Misnøyen mellom dem bygger seg opp.")

print("-----------------------------------------------------------------------------------------------------------")
print("\nHvordan bevarer Erling motivasjonen i temaet?\n")

print("3A, Fokuserer han på teambygging? \n3B, Eller fokuserer han på fremgang?\n")

valg_3 = input("Velg 3A, eller 3B  ")

if valg_3 == "3A":
    print("Teammedlemmene får positive opplevelser med hverandre og de lærer å kommunisere bedre.")
elif valg_3 == "3B":
    print(" Etter teambyggingen har de ulike medlemmene forbedret relasjonen med sine støttespillere\n" \
    "og stemningen mellom de uenige forblir antent." \
    " Dette lover ikke godt for prosjektet.")

print("-----------------------------------------------------------------------------------------------------------")
#Avlutning 3 mulige utfall

