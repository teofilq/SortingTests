# Rezumatul Sortărilor

1. **Counting Sort:**
   - Eficient pentru seturi de date cu valori întregi.
   - Avantaje: rapid și stabil pentru seturi de date mici.
   - Dezavantaje: necesită spațiu suplimentar pentru tabelele de frecvență - foarte costisitor dpdv al memoriei.

2. **Quick Sort:**
   - Bun pentru seturi de date mari și VARIATE.
   - Avantaje: rapid pe seturi de date mari și variate.
   - Dezavantaje: performanță scăzută pentru seturi aproape sortate sau seturi de date cu o distribuție mică(pe setul nostru de date mai mari dar cu maximul mic are un timp foarte prost - din cauza distribuției).

3. **Shell Sort:**
   - Eficient pentru seturi de date de dimensiuni medii.
   - Avantaje: performanță bună pentru dimensiuni moderate.
   - Dezavantaje: performanță mai slabă pe seturi de date mari.

4. **Merge Sort:**
   - Bun pentru seturi de date mari și variate.
   - Avantaje: complexitate temporală garantată, stabil.
   - Dezavantaje: necesită spațiu suplimentar pentru stocarea sublistelor temporare.

5. **Radix Sort (baza 10 și baza 2^16):**
   - Ideal pentru date numerice, în special pentru seturi de date cu valori întregi.
   - Avantaje: performanță excelentă pentru date numerice.
   - Se observă cum radix sortul cu baza 2^16 are rezultate superioare pentru numere mai mari.
   - Dezavantaje: necesită spațiu suplimentar pentru tabelele de sortare intermediare.
