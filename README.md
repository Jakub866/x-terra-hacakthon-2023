# Project: X-Terra Hackathon 2023
X-TERRA: Cross-Terrain Emergency Response and Relief Assistance

Projekt ma składać się z algorytmu znajdywania najlepszej ścieżki z punku A do punktu B. Dzięki połączeniu heatmap zebranych z satleit projektu  Copernicus. Do znalezienia danych wykorzystywać będziemy portal Mundi. Sam projekt ma wyróżniać się prostotą w możlwiościach przyszłej rozbudowy. 

Wyznaczanie ścieżki odbytwać się będzie za pomocą odnajdywania najbardziej korzystnej ścieżki w grafie. Wartości kosztu będą modfikowane w zależnośći od wartości parametrów w heatmapach. Działanie zopytmalizujemy dzięki wykorzystaniu grafów o różnych gęstościach co pozwoli nam ograniczyć ilość przeszukiwanych węzłów.

**TODO:**
* [ ] Znaleźć najbardziej odpowiednie Heatmapy tj. Pokazujące najwięcej informacji dla prouszania się pojazdów w terenie (Przykład: Im więcej wilgoci nad ziemią tym większe prawdopodobieństwo błotnistej nawierzchni, lub bagien), oraz spójność danych na dziedzinie czasu oraz miejsca pomiarów.
* [ ] Dobrać gęstości grafów w celu uzyskania dobrego balansu jakość/czas obliczeniowy.
* [ ] Zaimplementować onajdywania ścieżki na grafie ważonym (Rodzaj algorytmu nie został jeszcze wybrany, chwilowo A*)
* [ ] Opracować modifikatory zmian kosztów na grafie ważonym względem wartości heatmap. 
* [ ] Ustanadryzwoanie heatmap.
* [ ] Algorytm usuwania węzłów nieprzekraczalnych.
* [ ] front
* [ ] back
* [ ] Po uzysakniu lokalizacji od organizatorów dobranie odpowiednich wartości opisujących zajwiska na mapie SCL.


<sub> Kolejność **TODO** całkowicie przypadkowa. </sub>


**MOŻLIWE DODANIA:**
* GIF pokazujący mapy wykorzystane przy wyznaczaniu trasy