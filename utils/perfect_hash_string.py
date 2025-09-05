# =======================================================================
from dataclasses import dataclass
from typing import List

G = [0, 0, 0, 0, 64, 0, 76, 0, 0, 49, 0, 0, 0, 25, 8, 71,
    41, 0, 48, 0, 8, 0, 5, 72, 53, 0, 10, 55, 0, 28, 0, 70, 0, 0, 40, 0,
    58, 81, 8, 0, 28, 9, 79, 61, 97, 0, 0, 26, 0, 61, 0, 56, 87, 50, 0, 48,
    49, 11, 2, 57, 5, 0, 92, 0, 39, 69, 0, 0, 0, 58, 35, 82, 21, 26, 37, 0,
    0, 71, 41, 74, 0, 84, 0, 0, 96, 60, 0, 14, 62, 82, 18, 0, 52, 0, 86,
    64, 50, 0, 45, 22, 9]

def hash_f(key, T):
    return sum(ord(T[i % len(T)]) * ord(c) for i, c in enumerate(key)) % 101

def perfect_hash(key):
    return (G[hash_f(key, "6n6IE5O0")] +
            G[hash_f(key, "NAG7d6zS")]) % 101

# ============================ Sanity check =============================

original_K = ["V", "V2", "V3", "VS", "VM", "DM", "VPV", "PPV", "I",
    "I2", "I3", "IL", "LOAD", "T", "P", "CE", "SOC", "TTG", "Alarm",
    "Relay", "AR", "OR", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",
    "H9", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H17", "H18",
    "H19", "H20", "H21", "H22", "H23", "ERR", "CS", "BMV", "FW", "FWE",
    "PID", "SER#", "HC", "HSDS", "MODE", "AC_OUT_V", "AC_OUT_I", "AC_OUT_S",
    "WARN", "MPPT", "MON", "Checksum"]

def calc_char_sum(s: str) -> int:
    return sum(ord(c) for c in s) + ord(s[-1]) * 10


def read_keywords(file_path: str) -> List[str]:
    keywords = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if not name:
                continue
            keywords.append(name)
    return keywords

K = read_keywords("keywords.txt")
assert len(K) == 62

for h, k in enumerate(K):
    print(f"{h} {k} {calc_char_sum(k)} {perfect_hash(k)}")
    assert perfect_hash(k) == h
