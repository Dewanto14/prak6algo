# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:46:30 2023

@author: Huawei
"""

print("Masukkan Nilai A")
nilai_a = float(input("Nilai : "))
print("Masukkan Nilai C")
nilai_c = float(input("Nilai : "))

def rata():
    hasil = (nilai_a + nilai_c) / 2
    return hasil
print("Rata-ratanya: ", rata())