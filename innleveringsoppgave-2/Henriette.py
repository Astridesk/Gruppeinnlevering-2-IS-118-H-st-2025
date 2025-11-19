# IS-118 Del 2 av gruppeinnlevering 2

print("Velkommen til Henriette sin del av fortellingen.")
print("Her skal du få ta del i en historie med flere valg og mulige utfall.")
print("Hvilke valg du tar vil påvirke hvordan historien ender.")
print("Lykke til, og gjør dine valg med omhu!")

print("\n-----------------------------------\n")

# 1: Bakgrunnshistorie om konflikt 1 mellom Silje og Sivert 
print("På kontoret i Kristiansand har det blitt amper stemning mellom flere av medlemmene som jobber der, og de står nå midt i en storming fase.")
Medlem_1 = "Silje"
Medlem_2 = "Sivert"
print(f"Konflikten mellom {Medlem_1} og {Medlem_2} har utviklet seg fra sakskonflikt til personkonflikt, og de klarer ikke bli enige om teknologivalg og design.")
print(f"{Medlem_1} mener at {Medlem_2} sitt forslag vil låse brukeropplevelsen og hindre innovasjon.")
print(f"{Medlem_2} på sin side mener at {Medlem_1} sitt forslag er urealistisk, usikkert og for kostbart.")
print("Konflikten utvikler seg emosjonelt og påvirket arbeidsmiljøet negativt.")
# 2: Bakgrunnshistorie om konflikt 2 mellom Hamdi og Jabir
Medlem_3 = "Hamdi"
Medlem_4 = "Jabir"
print(f"Samtidig er {Medlem_3} og {Medlem_4} uenige om innbyggernes deltakelse i digitale folkemøter.")
print(f"{Medlem_3} ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, men {Medlem_4} ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
# 3: Prosjektlederens rolle
Prosjekt_leder = "Erling"
print(f"Som prosjektleder må {Prosjekt_leder} klare å balansere tid, relasjoner og resultater.")
print(f"Kan han klare å finne løsninger som alle kan leve med, eller vil konfliktene føre til negative konsekvenser for prosjektet?")

print("\n-----------------------------------\n")

Arbeidsmiljø = 5 

print(f"\nNåværende arbeidsmiljønivå: {Arbeidsmiljø}/10\n")

# Konflikt 1 mellom Silje og Sivert
print(f"{Prosjekt_leder} kan prøve å fikse konflikten mellom {Medlem_1} og {Medlem_2} gjennom to beslutninger.")
Valg_1 = input(
    "1 = Gå til HR\n"
    "2 = Ha individuelle samtaler\n"
    "Skriv ditt valg (1 eller 2): "
)

print("\n--- RESULTAT KONFLIKT 1 ---")

# Beslutningsmuligheter for Erling i konflikt 1 mellom Silje og Sivert

# Valg 1: HR griper inn
if Valg_1 == "1":
    print(f"{Prosjekt_leder} går til HR for å løse konflikten mellom {Medlem_1} og {Medlem_2}.")

# Positivt utfall
    if Arbeidsmiljø >= 5:
        print ("\n Positiv konsekvens:")
        print(f"HR fungerer som nøytral part, og {Medlem_1} og {Medlem_2} klarer å bli enige.")

        print("\n Positivt resultat:")
        konflikt1_løsning = f"{Medlem_1} og {Medlem_2} har begynt å samarbeide for å unngå videre konflikt."
        Arbeidsmiljø += 1

# Negativt utfall
    else:
        print("\n Negativ konsekvens:")
        print("De blir ikke enige, så HR kommer med et kompromiss de må følge.")

        print("\n Negativt resultat:")
        konflikt1_løsning = f"Stemningen mellom {Medlem_1} og {Medlem_2} er fortsatt anspent og {Medlem_1} føler at hun kom dårligere ut enn {Medlem_2} og mister motivasjon."
        Arbeidsmiljø -= 1

# Valg 2: Individuelle samtaler
elif Valg_1 == "2":
    print(f"{Prosjekt_leder} holder individuelle samtaler med både {Medlem_1} og {Medlem_2}.")

# Positivt utfall
    if Arbeidsmiljø >= 6:
        print("\n Positiv konsekvens:")
        print(f"De føler seg hørt, og {Prosjekt_leder} forstår deres bekymringer.")

        print("\n Positivt resultat:")
        konflikt1_løsning = f"{Medlem_1} og {Medlem_2} er inneforstått med at de må samarbaide, og klarer å finne en løsning sammen."
        Arbeidsmiljø += 1

# Negativt utfall
    else:
        print("\n Negativ konsekvens:")
        print(f"De føler seg overkjørt, og at {Prosjekt_leder} ikke forstår virkeligheten av deres meninger.")

        print("\n Negativt resultat:")
        konflikt1_løsning = f"{Medlem_1} og {Medlem_2} føler at {Prosjekt_leder} ikke hørte etter. Konflikten blir ikke løst, tilliten til {Prosjekt_leder} svekkes og arbeidsmiljøet forverres ytterligere."
        Arbeidsmiljø -= 1
else:
    print("Dette svaret er ugyldig. Vennligst prøv igjen.")
    exit()

print(f"Resultatet av konflikten mellom {Medlem_1} og {Medlem_2}:")
print(konflikt1_løsning)
print(f"\nNytt arbeidsmiljønivå: {Arbeidsmiljø}/10\n") 

print("\n-----------------------------------\n")

# Konflikt 2 mellom Hamdi og Jabir
print(f"Uavhengig av konflikten mellom {Medlem_1} og {Medlem_2}, kan {Prosjekt_leder} fortsatt prøve å fikse konflikten mellom {Medlem_3} og {Medlem_4}.")
print("Dette kan han gjøre gjennom to beslutninger.")
Valg_2 = input(
    "4 = Ta en dialog med begge parter\n"
    "5 = La dem finne ut av det selv\n"
    "Skriv ditt valg (4 eller 5): "
)   

print("\n--- RESULTAT KONFLIKT 2 ---")

# Beslutningsmuligheter for Erling i konflikt 2 mellom Hamdi og Jabir

# Valg 4: Tidlig dialog
if Valg_2 == "4":
    print(f"{Prosjekt_leder} tar tidlig dialog med både {Medlem_3} og {Medlem_4}.")
 
# Positivt utfall
    if Arbeidsmiljø >= 6:
        print("\n Positiv konsekvens:")
        print("Kommunikasjonen mellom {Medlem_3} og {Medlem_4} forbedres.")

        print("\n Positivt resultat:")
        konflikt2_løsning = f"{Medlem_3} og {Medlem_4} har begynt å samarbeide for å unngå videre konflikt."
        Arbeidsmiljø += 1

# Negativt utfall
    else:
        print("\n Negativ konsekvens:")
        print("Konflikten eskalerer fordi begge vil ha sin egen løsning.")

        print("\n Negativt resultat:")
        konflikt2_løsning = f"Stemningen mellom {Medlem_3} og {Medlem_4} er fortsatt anspent, og velger å engasjere sine kollegaer. Prosjektet blir dermed forsinket."
        Arbeidsmiljø -= 1

# Valg 5: La dem finne ut av det selv
elif Valg_2 == "5":
    print(f"{Prosjekt_leder} lar {Medlem_3} og {Medlem_4} finne ut av konflikten på egenhånd.")

# Positivt utfall
    if Arbeidsmiljø >= 6:
        print("\n Positiv konsekvens:")
        print("De klarer å finne en løsning begge to kan støtte.")

        print("\n Positivt resultat:")
        konflikt2_løsning = f"Via å samarbeide, forbedres relasjonen mellom {Medlem_3} og {Medlem_4} og de kan levere prototypen i tide."
        Arbeidsmiljø += 1

# Negativt utfall
    else:
        print("\n Negativ konsekvens:")
        print(f"Misnøyen mellom {Medlem_3} og {Medlem_4} eskalerer.")

        print("\n Negativt resultat:")
        konflikt2_løsning = f"Uenigheten mellom {Medlem_3} og {Medlem_4} utvikler seg til en større sakskonflikt. {Prosjekt_leder} må ta en ny avgjørelse, og prosjektet blir forsinket."
        Arbeidsmiljø -= 1
else:
    print("Dette svaret er ugyldig. Vennligst prøv igjen.")
    exit()

print(f"Resultatet av konflikten mellom {Medlem_3} og {Medlem_4}:")
print(konflikt2_løsning)
print(f"\nNytt arbeidsmiljønivå: {Arbeidsmiljø}/10\n")

print("\n-----------------------------------\n")

#  Bevare motivasjonen i teamet

print("\n--- BEVARE MOTIVASJONEN I TEAMET ---\n")

print(f"Etter å ha håndtert begge konfliktene, er det viktig for {Prosjekt_leder} å fokusere på å bevare motivasjonen i teamet.")
print("Han har to valg for å bevare teamet motivasjon:")
Valg_3 = input(
    "6 = Fokusere på team-building\n"
    "7 = Pushe mot fremgang\n"
    "Skriv ditt valg (6 eller 7): "
)

print("\n--- RESULTAT MOTIVASJON ---")

# Beslutningsmuligheter for Erling for å bevare motivasjonen i teamet
# Valg 6: Fokusere på team-building
if Valg_3 == "6":
    print(f"{Prosjekt_leder} velger å fokusere på team-building for å styrke relasjonene i teamet.")

#Positivt utfall
    if Arbeidsmiljø >= 6:
        print("\n Positiv konsekvens:")
        print("Medlemmene i teamet får positive opplevelser med hverandre og lærer å kommunisere bedre.")

        print("\n Positivt resultat:")
        motivasjons_resultat = "Etter team-building har medlemmene lært å samarbeide bedre og forstå hverandres perspektiver."
        Arbeidsmiljø += 1

# Negativt utfall
    else:
        print("\n Negativ konsekvens:")
        print(f"Frustrasjonen fra prosjekter bærer over til team-buildingen, og relasjonene svekkes.")

        print("\n Negativt resultat:")
        motivasjons_resultat = "Relasjonene er fortsatt anspente, og det lover ikke godt for prosjektet."
        Arbeidsmiljø -= 1

# Valg 7: Pushe mot fremgang
elif Valg_3 == "7":
    print(f"{Prosjekt_leder} velger å pushe teamet mot fremgang for å møte prosjektets mål.")

# Positivt utfall
    if Arbeidsmiljø >= 6:
        print("\n Positiv konsekvens:")
        print("Teamet føler seg motivert av fremgangen og fokuserer på å levere resultater.")

        print("\n Positivt resultat:")
        motivasjons_resultat = "Teamet er fokusert og leverer prototypen i tide, og demper ønsket om å presse sine egne forslag gjennom."
        Arbeidsmiljø += 1

# Negativt utfall
    else:
        print("\n Negativ konsekvens:")
        print("Teamet klarer ikke å jobbe effektivt når kommunikasjonen er dårlig og stemningen er spent")

        print("\n Negativt resultat:")
        motivasjons_resultat = f"Frustrasjonen fortsetter å vokse. Teamet har lav motivasjon, dårlig kommunikasjon og lav tillit til {Prosjekt_leder}, noe som fører til at prosjektet stagnerer."
        Arbeidsmiljø -= 1
else:
    print("Dette svaret er ugyldig. Vennligst prøv igjen.")
    exit()

print("Resultatet av tiltakene for å bevare motivasjonen i teamet:")
print(motivasjons_resultat)
print(f"\nNytt arbeidsmiljønivå: {Arbeidsmiljø}/10\n")

print("\n-----------------------------------\n")

print("\n--- SLUTTRESULTAT ---\n")

print("Historien er nå ferdig, og her er slutresultatet basert på dine valg gjennom historien:\n")
print ("Sluttresultat:")
if Arbeidsmiljø >= 6:
    print(f"Til tross for utfordringene, har {Prosjekt_leder} klart å navigere gjennom konfliktene og bevare motivasjonen i teamet.")
    print("Prosjektet fortsetter fremover med et styrket team og forbedret arbeidsmiljø.")
else:
    print("Konfliktene og lav motivasjon har tatt en toll på teamet.")
    print(f"Prosjektet står overfor betydelige utfordringer, og {Prosjekt_leder} må jobbe hardt for å gjenopprette tillit og samarbeid i teamet.") 

print(f"\nEndelig arbeidsmiljønivå: {Arbeidsmiljø}/10\n")

print("\n-----------------------------------\n")

print("Takk for at du deltok i historien!")
