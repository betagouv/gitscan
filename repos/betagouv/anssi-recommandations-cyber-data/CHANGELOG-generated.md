## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 04/08/2026)

### Résumé
Cette période a été marquée par une amélioration significative de la gestion documentaire (importation via URL, suppression de fichiers) et de l'expérience utilisateur grâce à une sélection de collections plus intuitive. Le moteur de recherche (RAG) a également bénéficié d'optimisations majeures pour mieux comprendre la structure des documents (ordre des paragraphes, blocs sur plusieurs pages), garantissant des résultats plus précis.

### Évolutions fonctionnelles
- **Gestion documentaire** : Ajout de la possibilité d'importer des documents HTML via une URL et de supprimer des documents existants.
- **Interface de sélection** : Remplacement de la saisie manuelle d'identifiants par des menus déroulants pour choisir les collections, incluant l'affichage de l'identifiant pour distinguer les collections portant le même nom.
- **Expérience utilisateur** : Redirection automatique vers le tableau de bord après l'authentification.
- **Corrections** : Résolution d'un problème où la liste des documents affichés ne correspondait pas à la collection sélectionnée dans l'interface.

### Évolutions techniques
- **Optimisation du RAG (Retrieval-Augmented Generation)** : 
    - Amélioration de la précision de la recherche en intégrant la position exacte des blocs et des paragraphes dans les métadonnées d'indexation.
    - Détection des blocs de texte s'étendant sur deux pages pour éviter les erreurs de découpage (chunking).
- **Performance d'indexation** : Ignoration automatique des pages PDF dépourvues de texte avant le passage par l'OCR.
- **Sécurité et CI/CD** : 
    - Renforcement de la sécurité des pipelines en désactivant les identifiants `git` lors du clonage des dépôts.
    - Intégration de `zizmor` pour la validation de la configuration.
- **API et Backend** : 
    - Mise en place de nouvelles routes pour la récupération et la gestion des collections.
    - Correction de l'encodage des noms de documents en UTF-8.
    - Correction de la synchronisation des suppressions pour assurer la cohérence entre les collections indexées et la collection de suivi (Jeopardy).

### Autres changements
- **Refactoring** : Extraction et réorganisation de composants UI (notamment pour les informations de collections) pour améliorer la maintenabilité du code.
- **Nettoyage** : Optimisation de l'espace de travail et nettoyage de code.
