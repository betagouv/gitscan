## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 23/09/2026)

### Résumé
Cette période a été marquée par l'amélioration de l'interface d'évaluation de l'IA et par un renforcement significatif de la précision de l'extraction de données (OCR et RAG). Le projet a également bénéficié de mises à jour de sécurité importantes pour corriger plusieurs vulnérabilités critiques.

### Évolutions fonctionnelles
- **Interface d'évaluation** : Ajout d'une nouvelle page dédiée permettant de lancer et de piloter les évaluations du bot.
- **Exploration des données** : Mise en place d'une interface permettant de visualiser les segments de texte (*chunks*), de consulter leurs sources et d'explorer leur contenu directement depuis le tableau de bord.
- **Gestion documentaire** : Possibilité d'ajouter des fichiers PDF via des liens distants depuis le dashboard.

### Évolutions techniques
- **Amélioration du traitement documentaire (OCR & Parsing)** :
    - Optimisation de l'extraction des sommaires (gestion de la hiérarchie, des continuations et nettoyage des pointillés).
    - Amélioration de la précision de l'OCR pour le traitement des légendes et la conservation des sections après une figure.
- **Optimisation du RAG (Retrieval-Augmented Generation)** :
    - Contextualisation accrue des segments de texte (*chunks*) pour améliorer la qualité de l'indexation.
    - Tri des segments par identifiant pour une meilleure organisation.
- **Sécurité** :
    - Résolution de plusieurs vulnérabilités de niveau élevé et modéré via la mise à jour de dépendances critiques, notamment `transformers` ([#149](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/149)), `cryptography`, `idna`, et `json-repair`.
- **Tests** : Amélioration de la couverture et de l'annotation des tests concernant le contexte documentaire.

### Autres changements
- Normalisation du nommage des documents (gestion des tirets).
