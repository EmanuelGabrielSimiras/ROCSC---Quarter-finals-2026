# CTF Challenge: Just a jail with numbers
**Category:** Misc / Jailbreak
**Difficulty:** Medium

## Description
A Python sandbox escape challenge using `RestrictedPython` and `NumPy`. The goal is to read `flag.txt` from a restricted environment.

## Solution Summary
1. **Bypass RestrictedPython**: Used a payload without underscores (`_`) to pass the compiler's safety check.
2. **Bypass NumPy Whitelist**: Identified that `np.core` was missing from the `BLOCKS` list, allowing access to internal file-reading functions.
3. **Data Exfiltration**: Used `ValueError` via `int()` to leak the flag content when the custom `Print` class failed to output data.

### Final Payload:
```python
int(np.core.records.fromfile('flag.txt', formats='S70', shape=1)[0][0])