
# Pflanzensimulationsanwendung

## Zielsetzung
Diese Anwendung simuliert das Wachstum und die Entwicklung einer realistischen Pflanze mit zellbasiertem Aufbau. Die Pflanze besteht aus verschiedenen Pflanzenteilen wie Stängeln, Blättern, Blüten und Knospen, die sich prozedural und nach den Regeln der Natur entwickeln.

## Zielgruppe
- **Forscher:** Biologen, Botaniker, Informatiker, die sich mit Pflanzenmodellierung und Simulation beschäftigen.
- **Studenten und Schüler:** Biologie, Umweltwissenschaften, Informatik.
- **Interessierte Öffentlichkeit:** Personen, die mehr über Pflanzen und ihre Entwicklung erfahren möchten.

## Funktionsumfang
### Pflanzenmodell
- **Zellbasierte Modellierung:** Die Pflanze besteht aus verschiedenen Zelltypen (Meristemzellen, Parenchymzellen, Leitbündelzellen).
- **Wachstumsregeln und Algorithmen:** Regeln und Algorithmen für die Zellteilung, Zelldifferenzierung und den Zelltod.
- **Energiefluss:** Modell für den Energiefluss in der Pflanze.
- **Wachstumsprozesse:** Lokalisiertes Wachstum, hormonelle Regulation und Umwelteinflüsse.

### Umgebungsmodell
- **Simulation relevanter Umweltfaktoren:** Lichtintensität, Wasserverfügbarkeit, Temperatur.
- **Erstellung verschiedener Umgebungsszenarien:** Jahreszeiten, Klimazonen, benutzerdefinierte Szenarien.

### 3D-Visualisierung
- **Realistische 3D-Darstellung:** Detaillierte Modelle für verschiedene Pflanzenteile.
- **Visualisierung der Zelltypen:** Unterschiedliche Farben oder Formen für verschiedene Zelltypen.
- **Visualisierung des Wachstums:** Animationen des Wachstumsprozesses.
- **Visualisierung des Energieflusses:** Pfeile oder Farbverläufe zur Darstellung des Energieflusses.
- **Interaktive Visualisierung:** Verschiedene Perspektiven, Pausieren und Anpassen der Simulation.

## Installation
1. Klonen Sie das Repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Installieren Sie die erforderlichen Bibliotheken:
    ```bash
    pip install -r requirements.txt
    ```

## Nutzung
1. Führen Sie die Simulation aus:
    ```bash
    python3 growth_algorithm.py
    ```
2. Visualisieren Sie die Pflanze:
    ```bash
    python3 visualization.py
    ```

## Module
- **cell_model.py:** Modelliert die verschiedenen Zelltypen und ihre Eigenschaften.
- **growth_algorithm.py:** Implementiert die Regeln und Algorithmen für das Zellwachstum und die Zellteilung.
- **visualization.py:** Visualisiert die Pflanze und ihr Wachstum in 3D.
- **test_simulation.py:** Enthält Unit-Tests für die Zellmodelle und das Wachstum der Pflanze.

## Lizenz
Diese Anwendung ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE-Datei.

