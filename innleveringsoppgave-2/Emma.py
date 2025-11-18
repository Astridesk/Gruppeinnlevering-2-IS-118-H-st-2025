#Innledning til den fiktive historien
print ("Velkommen til den interaktive historien om prosjektlederen Erling og hans team!")
print ("I denne fiktive historien skal du spille Erling, som må navigere flere konflikter og spenninger mellom ulike teammedlemmer.")
print ("Hver gang du tar et valg, vil det påvirke prosjektets utfall.")

print ("Sivert er IT-rådgiver og opptatt av IT-sikkerhet og kostnad, mens Silje jobber som UX-designer og prioriterer brukervennlighet.")
print ("På grunn av deres ulike kompetanseområder og prioriteringer har forholdet mellom dem blitt mer anstrengt.")
print ("De anstrengte forholdene mellom de to partene gjør at gruppen blir preget av dårlig arbeidsatmosfære.")

#Beslutning 1: Konflikten mellom Sivert og Silje
print ("Som prosjektleder må Erling nå ta et valg for å håndtere konflikten så tidlig som mulig og få teamet tilbake på rett spor.")

#Første valg
valg1 = input("Hva gjør Erling? Skriv 1 for å gå til HR, eller 2 for å ta individuelle samtaler med Sivert og Silje.")

#Håndtere beslutning 1
if valg1 == "1":
  print("Erling går til HR for å finne en løsning til konflikten. HR forelsår et kompromiss mellom de to partenes ønsker, men Silje er ikke tilfreds med valget.")
  print ("Dette resulterer i at motivasjonen hennes vekkes og hun presterer dårlig i arbeidet.")
  konflikt1_resultat = "kompromiss, motivasjonen til Silje svekkes og prototypen oppnår ikke ønsket resultat."

elif valg1 == "2":
  print("Erling tar individuelle samtaler med begge parter og får mer innsikt i Sivert og Silje's synspunkter. Erling kommer med råd, og Sivert og Silje blir enige etter Erlings oppfordring.")
  konflikt1_resultat = "Konflikten mellom Sivert og Silje blir løst. Gratulerer prototypen blir en suksess!"

else:
  print ("Ugyldig valg. Vennligst velg alternativ 1 eller 2.")
  konflikt1_resultat = "ingen løsning, alternativet er ikke gyldig."

# Vis resultatet av valget
print("Resultatet av konflikten mellom Sivert og Silje: " + konflikt1_resultat)




