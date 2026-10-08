## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 05/10/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision de l'analyse documentaire et l'enrichissement de l'interface utilisateur. Le système est désormais capable de traiter plus finement les documents (notamment via l'OCR et l'extraction de sommaires) et offre de nouveaux outils pour explorer les données textuelles utilisées par l'intelligence artificielle.

### Évolutions fonctionnelles
- **Importation de documents** : Ajout de la possibilité d'importer des fichiers PDF via une URL distante directement depuis le tableau de bord.
- **Exploration des données** : Mise en place d'une interface permettant de visualiser les segments de texte (chunks) extraits d'un document ainsi que leur source.

### Évolutions techniques
- **Amélioration du traitement documentaire et OCR** :
    - Extraction du sommaire hiérarchique des documents.
    - Optimisation du nettoyage des sommaires issus de l'OCR (gestion des pointillés et des continuations).
    - Amélioration de la précision de l'extraction (traitement des légendes et conservation des sections après une figure).
    - Normalisation des noms de documents.
- **Optimisation du moteur RAG (Retrieval-Augmented Generation)** :
    - Contextualisation des segments (chunks) pour améliorer la pertinence des recherches.
    - Tri des segments par identifiant pour une meilleure organisation des données.

### Autres changements
- **Tests** : Amélioration de la couverture et de la documentation des tests relatifs au contexte documentaire.
