# Just a jail with numbers - Writeup

## Analiza Vulnerabilității
Sandbox-ul a încercat să blocheze accesul la funcții periculoase prin filtrarea modulului `numpy`. Totuși, filtrarea a fost superficială (shallow copy), permițând accesul la submodulele interne.

## Exploatare
1. **Bypass RestrictedPython**: Am evitat utilizarea caracterului `_` (underscore) pentru a trece de filtrul de compilare.
2. **Bypass NumPy Blacklist**: Am folosit `np.core.records.fromfile`, o funcție care nu a fost inclusă în lista `BLOCKS`.
3. **Exfiltrare prin Error Side-Channel**: Deoarece clasa `Print` era defectă, am forțat o eroare `int()` pentru a afișa conținutul fișierului în mesajul de eroare.

## Cum se rulează exploit-ul
```bash
python3 exploit.py