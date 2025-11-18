#Innledning til den fiktive historien
print("Velkommen til den interaktive historien om prosjektlederen Erling og hans team!")
print("I denne fiktive historien skal du spille Erling, som må navigere flere konflikter og spenninger mellom ulike teammedlemmer.")
print("Hver gang du tar et valg, vil det påvirke prosjektets utfall.")

#Introduksjon av Silje og Sivert
print("Sivert er IT-rådgiver og opptatt av IT-sikkerhet og kostnad, mens Silje jobber som UX-designer og prioriterer brukervennlighet.")
print("På grunn av deres ulike kompetanseområder og prioriteringer har forholdet mellom dem blitt mer anstrengt.")
print("De anstrengte forholdene mellom de to partene gjør at gruppen blir preget av dårlig arbeidsatmosfære.")

#Introduksjon av Hamdi og Jabir 
print("Hamdi er representant fra kulturavdelingen og ansvarlig for innbyggerdialog og kommunikasjon.")
print("Jabir er brukerrepresentant fra en lokal innbyggerforening.")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, mens Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print("De to motsatte ønskene gjør det vanskelig for Hamdi og Jabir å komme til en enighet.")

#Konflikt 1: Konflikten mellom Sivert og Silje
print("Som prosjektleder må Erling nå ta et valg for å håndtere konfliktene mellom teammedlemmene og få teamet tilbake på rett spor.")
print("Han starter med konflikten mellom Sivert og Silje.")

#Valgmuligheter mellom Sivert og Silje
valg1 = input("Hva gjør Erling? Skriv 1 for å gå til HR, 2 for å ta individuelle samtaler med Sivert og Silje, eller 3 for å gjøre ingenting og håpe at konflikten løser seg selv: ")

#Håndtering av Konflikt 1
if valg1 == "1":
  print("Erling går til HR for å finne en løsning til konflikten. HR forelsår et kompromiss mellom de to partenes ønsker, men Silje er ikke tilfreds med valget.")
  print("Dette resulterer i at motivasjonen hennes vekkes og hun presterer dårlig i arbeidet.")
  konflikt1_resultat = "Kompromiss, motivasjonen til Silje svekkes og prototypen oppnår ikke ønsket resultat. Prototypen blir likevel godkjent."
  print ("Du fikk godkjent, men klarer du å løse konflikten mellom Hamdi og Jabir på en bedre måte?")
  
elif valg1 == "2":
  print("Erling tar individuelle samtaler med begge parter og får mer innsikt i Sivert og Silje's synspunkter. Erling kommer med råd, og Sivert og Silje blir enige etter Erlings oppfordring.")
  konflikt1_resultat = "Konflikten mellom Sivert og Silje blir løst. Gratulerer, prototypen blir en suksess!"
  print("Gratulerer, du reddet prototypen! Nå kan du prøve å løse konflikten mellom Hamdi og Jabir på en like god måte!")

elif valg1 == "3":
  print("Erling tenker at konflikten løser seg selv og velger derfor å ikke gjøre noe.")
  print("Dette fører til økt frustrasjon blant teammedlemmene og prototypen blir dårlig.")
  konflikt1_resultat = "Ingen handling, konflikten vedvarer og prototypen blir ikke godkjent."
  print("Selv om det gikk dårlig med arbeidet til Sivert og Silje, har Erling fortsatt mulighet til å rette opp i spenningene mellom Hamdi og Jabir.")

# Vis resultatet av konflikten mellom Sivert og Silje
print("Resultatet av konflikten mellom Sivert og Silje: " + konflikt1_resultat)

#Konflikt 2: Konflikten mellom Hamdi og Jabir
print("Nå som konflikten mellom Sivert og Silje er løst, er det på tide at Erling løser konflikkten mellom Hamdi og Jabir.")

#Valgmuligheter mellom Hamdi og Jabir
if konflikt1_resultat == ("Du fikk godkjent, men klarer du å løse konflikten mellom Hamdi og Jabir på en bedre måte?")
print("Stemningen mellom teammedlemmene er fortsatt anspente, klarer Erling å lette på den?")
valg2 = input("Hva gjør Erling? Skriv 1 for å ta saken opp med HR, 2 for å ta individuelle samtaler med begge parter, eller 3 for å la dem ordne det selv.")

elif konflikt1_resultat == ("Gratulerer, du reddet prototypen! Nå kan du prøve å løse konflikten mellom Hamdi og Jabir på en like god måte!")
valg2 = input("Hva gjør Erling? Skriv 1 for å ta saken opp med HR, 2 for å ta individuelle samtaler med begge parter, eller 3 for å la dem ordne det selv.")

elif konflikt1_resultat == ("Selv om det gikk dårlig med arbeidet til Sivert og Silje, har Erling fortsatt mulighet til å rette opp i spenningene mellom Hamdi og Jabir.")
valg2 = input("Hva gjør Erling? Skriv 1 for å ta en tidlig dialog med Hamdi og Jabir, 2 for å la dem ordne opp på egenhånd eller 3 for å fokusere på teambygging").

#Håndtering av Konflikt 2
if valg2 == "1":
print("Erling tar en tidlig dialog med Hamdi og Jabir.")
print("Den tidlige dialogen fremmet bedre kommunikasjon mellom de to partene. Hamdi og Jabir kommer til en enighet!")
konflikt2_resultat = "Hamdi og Jabir kommer til en enighet, og de gjennomfører prosjektet med glans!")

elif valg2 == "2":
print("Erling lar Hamdi og Jabir ordne opp i konflikten på egenhånd.")
print("Dette resulterer i at misnøyen fortsetter, og det eskalerer seg til en sakskonflikt som senere utvikler seg til en personkonflikt.")
konflikt2_resultat = "Nå kan ikke Hamdi og Jabir fordra hverandre. Prosjektet går i dass."

elif valg2 == "3":
print("Erling bestemmer seg for å fokusere på teambygging, slik at teammedlemmene kan lære å kommunisere bedre og enklere ta hensyn til hverandres synspunker.")
print("Teambyggingen fungerte til teamets fordel, og konflikten mellom Hamdi og Jabir ble løst.")
konflikt2_resultat = "Teamet blir venner utenfor arbeidsplassen, og prototypen blir godkjent. Godt jobbet!"

print("Resultatet av konflikten mellom Hamdi og Jabir: " + konflikt2_resultat)












