just a jail with numbers - writeup
analiza vulnerabilitatii
sandbox-ul a incercat sa blocheze accesul la functii periculoase prin filtrarea modulului numpy. totusi, filtrarea a fost superficiala (shallow copy), permitand accesul la submodulele interne.

exploatare
1. bypass restrictedpython: am evitat utilizarea caracterului _ (underscore) pentru a trece de filtrul de compilare.

2. bypass numpy blacklist: am folosit np.core.records.fromfile, o functie care nu a fost inclusa in lista blocks.

3. exfiltrare prin error side-channel: deoarece clasa print era defecta, am fortat o eroare int() pentru a afisa continutul fisierului in mesajul de eroare.

