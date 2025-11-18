print("Erlings valg")

print("Konflikt1: Sivert og Silje samarbeider dårlig.")
print("Alt1: Erling går til HR for støtte.")
print("Alt2: Erling tar individuelle samtaler med dem.")
Valg1 = input("Hva velger du? (Alt1/Alt2): ").strip().lower()

if Valg1 == "alt1":
    print("Erling kontakter HR. Samtalen går greit.")
    print("1: HR foreslår tettere samarbeid.")
    print("2: Det ender med et kompromiss som svekker Siljes motivasjon.")
    Valg1a = input("Velg 1 eller 2: ").strip()
else:
    print("Erling tar samtaler med hver av dem.")
    print("1: De oppfordres til samarbeid og blir enige.")
    print("2: De føler seg overkjørt og blir ikke enige.")
    Valg1a = input("Velg 1 eller 2: ").strip()

print("Konflikt2: Kommunikasjon glipper i teamet.")
print("Alt1: Erling tar en tidlig dialog.")
print("Alt2: Han lar teamet ordne opp på egen hånd.")
Valg2 = input("Hva velger du? (Alt1/Alt2): ").strip().lower()

if Valg2 == "alt1":
    print("Tidlig dialog settes i gang.")
    print("1: Kommunikasjonen bedres og de finner enighet.")
    print("2: Ingen forbedring – konflikten eskalerer.")
    Valg2a = input("Velg 1 eller 2: ").strip()
else:
    print("Erling lar teamet forsøke selv.")
    print("1: De finner en løsning sammen.")
    print("2: Misnøyen fortsetter og blir en sakskonflikt.")
    Valg2a = input("Velg 1 eller 2: ").strip()

print("Konflikt3: Teamet mangler framdrift og samhold.")
print("Alt1: Erling fokuserer på teambygging.")
print("Alt2: Han pusher for rask fremgang.")
Valg3 = input("Hva velger du? (Alt1/Alt2): ").strip().lower()

if Valg3 == "alt1":
    print("Teambygging iverksettes.")
    print("1: De lærer å kommunisere og ser hverandres perspektiv.")
    print("2: Relasjonene forbedres ikke – stemningen blir anspent.")
    Valg3a = input("Velg 1 eller 2: ").strip()
else:
    print("Erling prioriterer fremdrift.")
    print("1: Teamet setter pris på tydelig fremdrift og motiveres.")
    print("2: Det fungerer dårlig, og prosjektet stagnerer.")
    Valg3a = input("Velg 1 eller 2: ").strip()

print("Resultat av Erlings Valg")

if (Valg1 == "alt1" and Valg1a == "1") and (Valg2 == "alt1" and Valg2a == "1") and (Valg3 == "alt1" and Valg3a == "1"):
    print("Erling håndterte konfliktene eksemplarisk! Teamet blomstrer under hans ledelse.")

elif (Valg1 == "alt2" and Valg1a == "2") or (Valg2 == "alt2" and Valg2a == "2") or (Valg3 == "alt2" and Valg3a == "2"):
    print("Erling slet med å håndtere konfliktene. Teamet opplevde flere utfordringer og lav moral.")

else:
    print("Erling gjorde noen gode valg, men også noen mindre vellykkede. Teamet har potensialet til å forbedre seg med riktig veiledning.")