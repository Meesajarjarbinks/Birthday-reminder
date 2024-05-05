## 1) Įžanga:
a) Šiam kursiniui darbui pasirinkau sukurti gimtadienio priminimo programą.
b) Programą paleisti galima paprasčiausiai paspaudus mygtuką „paleisti“.
c) Paleidus programą turėsite prisijungti prie savo paskyros arba susikurti naują.
Prisijungimui turėsite įvesti savo prisijungimo vardą ir slaptažodį.
Tuomet galėsite pasirinkti pridėti naują gimtadienį arba peržiūrėti šiandienos gimtadienius, po šio pasirinkimo galėsite pasirinkti tęsti arba ne.
Pasirinkus tęsti, grįžtate prie tų pačių pasirinkimų, kuriuos gavote prisijungę prie savo paskyros. Jei pasirinksite netęsti, programa baigs darbą.

## 2) Darbo analizė:
a) Naudojame abstrakčius metodus klasėje „user“  paskyrų kūrimui. Klasėje „BirthdayReminder“ naudojame abstrakčius metodus programos funkcijų kūrimui.
"ConcreteUser" klasėje enkapsuliuojami "username" ir "password" atributai.
"ConcreteUser" klasė paveldi iš "user" klasės. "ConcreteBirthdayReminder" klasė paveldi iš "BirthdayReminder" klasės. Jos paveldi panašius atributus ir metodus taip sumažinant, supaprastint kodą.
Polimorfizmas šioje programoje pasireiškia per metodų perrašymą, pavyzdžiui, su klasių "User", "BirthdayReminder" objektais gali būti elgiamasi kaip su klasių "ConcreteUser", "ConcreteBirthdayReminder" objektais.
Klasėje „ConcreteBirthdayReminder“ metodas „save_users“ įrašo paskyrų prisijungimų duomenis „user_accounts.txt“ dokumente, o metodas „load_users“ skaito duomenis iš „user_accounts.txt“ dokumento.
„create_account“ metodas patvirtina paskyros sukūrimą arba paprašo susikurti naują vartotojo vardą, jei bandėte susikurti jau egzistuojantį, tokiu atveju programa baigia darbą.
Metodas „login“ patvirtina vartotojo prisijungimą, jei buvo įvesti teisingi prisijungimo duomenys (vartotojo vardas ir slaptažodis), priešingu atveju programa baigia darbą.
Jei vartotojo prisijungimas buvo patvirtintas, tuomet programa duoda du pasirinkimus: pridėti naują gimtadienį arba peržiūrėti šiandienos gimtadienius.
Pasirinkimai yra daromi įrašant vienetą arba dvejetą.
Jei pasirenkamas vienetas, tuomet iškviečiamas „add_birthday“ metodas, kuris paprašo vartotojo įvesti žmogaus, kurio gimtadienį vartotojas nori įrašyti, vardą, gimimo metus, mėnesį ir dieną. Šie duomenys įrašomi į „birthdays.txt“ dokumentą.
Jei buvo pasirinktas dvejetas, tuomet iškviečiamas „check_birthday_today“ metodas, kuris skaito duomenis iš „birthdays.txt“ dokumento ir tikrina kokios įrašytos gimtadienio datos sutampa su šios dienos data ir atspausdina atitinkamą tekstą.
Po visų šių atliktų operacijų, nepriklausomai nuo pasirinkimo, vartotojo klausiama  ar norima tęsti.
Pasirinkimai yra daromi įrašant „yes“ arba „no“.
Jei pasirenkama „yes“ tuomet programa grįžta prie ankstesnio pasirinkimo (pridėti naują gimtadienį arba peržiūrėti šiandienos gimtadienius).
Jei pasirenkama „no“ programa baigia darbą.

## 3) Rezultatai ir santrauka
a) Programa gali palaikyti daug vartotojų, saugoja kiekvieno iš jų pridėtus gimtadienius. Vartotojas turi galimybę peržiūrėti kurie iš jo pridėtų žmonių šiandien švenčia gimtadienius.
b) Programa gali naudotis daug vartotojų, ji saugoja kiekvieno iš jų pridėtus gimtadienius ir jų prisijungimo duomenis tekstiniuose failuose.
Vartotojas turi galimybę peržiūrėti kurie iš jo pridėtų žmonių šiandien švenčia gimtadienius.
Ateityje programa galėtų būti patobulinta taip, kad automatiškai siųstų pranešimus apie artėjančius ar esamus gimtadienius. Galėtų būti suteikti keli bandymai slaptažodžiui įvesti.
c) Programa galėtų siųsti pranešimus apie artėjančius ir šiandieninius gimtadienius neprisijungiant prie savo paskyros kasdien.
