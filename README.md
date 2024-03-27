# Axelrodův turnaj
Vytvoří turnaj mezi algoritmy pomocí axelord knihovny.
Z výsledku vezme průměrný bodový zisk za tah pro každý z algoritmů.
Výsledná tabulka pak zobrazuje v řádku jednotlivé ohodnocení 
oproti algoritmu ve sloupci.
První sloupec vedle názvu algoritmu je průměr ze všech odehraných her.

Druhá tabulka vyjadřuje procento tahů, 
kdy algoritmus Kooperoval s daným protihráčem.


Vlastní algoritmus jsem pojmenoval CupAlg - primární vlastností je, 
že Zradí pouze pokud ho zradí častokrát soupeř.
S každou soupeřovou kooperací mu odpouští.
Má tři vlastnosti které lze měnit:
    - defectivness - počáteční hodnota jeho pocitu zrazení
        pokud tato hodnota překročí jedna, další tah bude Zrada
    - defect_growth - o kolik se zvýší defectivness, když je zrazen
    - forgivness_rate - o kolik se sníží defectivness, když soupeř kooperuje
Lze je nastavovat během tvorby třídy a po vyzkoušení různých hodnot,
jsem ponechal dvě možnosti:
   0.5; 0.5; 0.1 - lehce odpouští
   a
   0.6; 0.6; 0.0 - vůbec neodpouští, po první zradě pouze zrazuje
Překvapilo mě, že v soušasném sestavení turnaje vyhrává ta neodopuštěcí varianta. 
Druhá varianta je schopna odpustit, pokud se soupeř rozhodne dále kooperovat.
Její úspěšnost bývala v lepší polovině výsledků, ale horší než TFT.
