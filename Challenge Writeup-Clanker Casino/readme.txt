challenge writeup: clanker casino

1. descriere
clanker casino este un joc de tip coin flip unde trebuie sa ajungi de la 1 moneda la 200 pentru a vedea flag-ul. jocul foloseste un captcha vizual care pare greu de pacalit pentru ca cifrele din codul html sunt diferite de cele afisate pe ecran.

2. vulnerabilitate
am gasit o bresa de logica in codul serverului la verificarea captcha-ului. serverul sterge id-ul captcha din sesiune dupa prima utilizare. daca trimitem o cerere fara raspuns la captcha si fara id, serverul compara "none" cu "none". rezultatul este egal, asa ca serverul ne lasa sa pariem fara sa rezolvam verificarea.

3. exploit
am facut un script care automatizeaza tot procesul:

creeaza un cont nou ca sa avem moneda de start.

face un pariu de test ca sa goleasca id-ul captcha.

pariaza rapid de 8 ori la rand dubland miza (1, 2, 4, 8... 128) fara sa completeze captcha.

daca toate ies "heads", balanta trece de 200 si flag-ul apare in pagina.

4. concluzie

chiar daca site-ul avea protectii vizuale, am reusit sa trecem de ele folosind o eroare de programare in backend. dupa aproximativ 300 de incercari, scriptul a nimerit seria norocoasa si a extras flag-ul.
