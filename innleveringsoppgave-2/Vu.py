print("Velkommen til Erling og hans team!\n")

# --- Konflikt 1 ---
print("Konflikt 1:")
print("1: Erling går til HR")
print("2: Erling tar individuelle samtaler")
print("3: Erling planlegger en teambuilding-aktivitet")

valg1 = input("Velg 1, 2 eller 3: ")

if valg1 == "1":
    print("HR tar kontroll over teamet og dette fører til en verre situasjon.")
elif valg1 == "2":
    print("Erling holder individuelle samtaler med Silje, Sivert, Hamdi og Jabir, og dette hjelper ham å forstå situasjonen.")
elif  valg1 == "3":
    print("Aktiviteten hjelper teamet med å bygge relasjoner og samarbeidet forbedres.")
else:
    print("Ugyldig valg. Videreføres som nøytral hendelse.")


# --- Konflikt 2 ---
print("Konflikt 2:")
print("1: Erling og HR var ikke enige om hvordan konflikten skulle håndteres.")
print("2: Erling fikk høre forskjellige perspektiver fra teammedlemmene og tar nå et felles teammøte.")
print("3: Erling ser at aktiviteten forbedret kommunikasjonen og bruker nå teambuilding jevnlig.")


valg2 = input("Velg 1, 2 eller 3: ")


if valg2 == "1":
    print("Erling og HR klarer ikke å bli enige, noe som fører til at Erling trekker seg som teamleder.")
elif valg2 == "2":
    print("Teammøtet gikk vellykket og teamet føler seg mer hørt.")
elif valg2 == "3":
    print("Erling fortsetter med teambuilding og ser stadig forbedringer i samarbeidet.")
else: 
    print("Ugyldig valg. Videreføres som nøytral hendelse.")


# --- Konflikt 3 ---
print("Konflikt 3:")
print("1: Erling prøver å få teamet til å jobbe mot et felles mål.")
print("2: Erling presser teamet til å jobbe raskere.")
print("3: Erling tar en pause fra prosjektet og lar teamet tenke på egen hånd.")


valg3 = input("Velg 1, 2 eller 3: ")


if valg3 == "1":
    print("Teamet begynner å se verdien av samarbeid og retningen blir tydeligere.")
elif valg3 == "2":
    print("Presset gjør at motivasjonen synker, og arbeidet blir dårligere.")
elif valg3 == "3":
    print("Teamet finner noen egne løsninger, men mangler fortsatt retning.")
else:
    print("Ugyldig valg. Videreføres som nøytral hendelse.")

negativ = ["1", "2"] # valg som fører til negative konsekvenser


if valg1 == "3" and valg2 == "3" and valg3 == "1":
    print("Teamet gjenoppretter tillit og går videre til norming-fasen. Sterkt samarbeid!")
elif valg1 in ["2", "3"] and valg2 in ["2", "3"]:
    print("En del av konflikten løses, men relasjonene er fortsatt litt svake.")
else:
    print("Prosjektet stopper opp, og fellesskapet ryker. Dårlig konflikthåndtering førte til brudd i teamet.")


