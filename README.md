<h1>Spider and Stemmer scripts</h1>

W celu prawidłowego działania wymagany jest Python w wersji powyżej 3.0 oraz biblioteka NLTK.

Aby uruchomić spidera należy zmodyfikować kod w następujący sposób:
- w pole 'url' wprowadzić link do sitemapy
- w metodzie get_single_item_data należy podać miejsce gdzie znajdują się interesujące nas dane
- po przekonwertowaniu dane powinny zostać pobrane i zapisane w pliku tekstowym

Oprócz tego w folderze znajduje się skrypt do pobierania komentarzy, który działa analogicznie do powyższego spidera. 
Dodatkowo nim właśnie został pobrany opis produktów (po delikatnej modyfikacji kodu).

W kodzie stemmera natomiast znajduje się ścieżka do danych pozyskanych podczas działania spidera.
Po uruchomieniu otrzymamy wynik w postaci danych, które zostały poddane stemmingowi. Oprócz tego otrzymamy wyniki takie jak czas działania algorytmu, średnia długość rdzenia itp.

