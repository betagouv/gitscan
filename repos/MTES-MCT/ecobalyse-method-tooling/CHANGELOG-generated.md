## Changelog : ecobalyse-method-tooling (30 derniers jours, au 22/10/2026)

### Résumé
Cette période a été principalement consacrée à l'amélioration de l'outil de correspondance (mapping) entre les données ecoinvent et les référentiels BAFU. Les utilisateurs bénéficient désormais d'une meilleure visibilité sur les processus non appariés et d'une analyse plus fine par impact. La stabilité de l'outil a été renforcée et la documentation a été considérablement enrichie pour faciliter l'installation, notamment pour les utilisateurs Windows.

### Évolutions fonctionnelles
- **Amélioration du mapping ecoinvent-BAFU** :
    - Possibilité de vérifier l'impact du mapping processus par processus.
    - Détection améliorée des colonnes via les en-têtes et gestion plus précise des facteurs d'unité.
    - Meilleure visibilité des processus ecoinvent n'ayant aucune correspondance BAFU (affichage d'une ligne dédiée).
- **Correction de bugs** :
    - Résolution d'un plantage de l'explorateur Jupyter lors de l'utilisation de méthodes autres que EF 3.1.
    - Correction de la lecture des colonnes pour éviter les doublons et assurer la distinction des lignes via leurs cellules BAFU.

### Évolutions techniques
- **Refonte de l'outil de mapping** : Intégration de `pyvolca` pour permettre le calcul, le scoring et la comparaison des données [#4](https://github.com/MTES-MCT/ecobalyse-method-tooling/pull/4).
- **Robustesse et maintenance** :
    - Amélioration de la gestion des chemins relatifs et verrouillage de la version du moteur (engine) pour garantir la reproductibilité.
    - Mise à jour de l'outil pour suivre la dernière version du moteur de calcul.

### Autres changements
- **Documentation** :
    - Ajout d'un guide complet pour l'installation et l'utilisation sous Windows.
    - Instructions pour exécuter l'outil directement depuis son adresse GitHub sans téléchargement local du dépôt.
    - Ajout de documentation sur la gestion des erreurs lors du premier lancement.
- **Contenu** : Ajout d'un nouveau notebook de travail.
