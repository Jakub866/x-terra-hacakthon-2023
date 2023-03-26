# Project: X-Terra Hackathon 2023
X-TERRA: Cross-Terrain Emergency Response and Relief Assistance
Thic repository contains a prototype of the project for Cassini Hackathon 2023 for the challenge ***"Enable cross terrain mobility"***.

Issuse to solve
There is always a risk of crisis in the world, and there is a strictly need to obtain fast and effective way to deploy and move assets nevertherless of destination and atmospheric situation. It is crucial to have a tool focused to support mission planning, understanding of terrain and ploting routes. 

Project Idea
Create full pleaged app which will enable navigation on off road by using satelite photos supported by open source service, to search and lead the most optimalised off-road routing way for rough terrain mission planning. By obtaining satelite data about vegetation, moisture, all kind of water reservoirs compared to other open sources which gave information about elevation levels, weather conditions and if it is needed - streets. That's is why project X-Terra want to gave a idea and first impresion of solution fwhich can be use by a various assets like humanitarian convoys, firefighters emergency forces, forest protection and supervision service and also can find helpful for military use cases.

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
