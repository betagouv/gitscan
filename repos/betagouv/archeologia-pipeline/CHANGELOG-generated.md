## Changelog : archeologia-pipeline (30 derniers jours, au 02 novembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience utilisateur et une amélioration significative de la fiabilité des détections. L'interface a été totalement repensée pour guider l'utilisateur pas à pas, avec l'ajout d'une aide intégrée et de fiches détaillées pour chaque modèle d'intelligence artificielle. Parallèlement, le moteur de détection a été optimisé pour être plus rapide (via l'utilisation de la carte graphique) et plus précis dans la gestion des données géographiques.

### Évolutions fonctionnelles
- **Refonte de l'interface utilisateur** : 
    - Mise en place d'un assistant par étapes (Vérifications, Traitement) avec une frise de progression cliquable.
    - Création de fiches détaillées pour les modèles et les classes, incluant des profils de scores (précision/rappel) et des informations sur la fiabilité observée.
    - Amélioration de la navigation avec un nouveau système de fiches et de panneaux d'information non modaux.
- **Amélioration du reporting et des résultats** :
    - Génération d'un nouveau rapport de traitement au format HTML.
    - Amélioration du nommage des projets QGIS et des couches pour une meilleure traçabilité.
    - Ajout de bilans de fiabilité en fin de traitement.
- **Aide et accompagnement** :
    - Intégration d'un manuel d'aide directement dans l'outil, incluant une recherche globale et des captures d'écran actualisées.
    - Ajout d'un lexique complet pour harmoniser le vocabulaire technique (relief, structures, dalles, etc.).
- **Gestion des erreurs et avertissements** :
    - Nouveaux messages d'alerte concernant l'échelle des données, les systèmes de coordonnées (CRS) et les problèmes de téléchargement.
    - Signalement explicite des cas de "détection impossible" pour certains modèles.

### Évolutions techniques
- **Optimisation de l'Intelligence Artificielle** :
    - Accélération de la détection via l'intégration de DirectML, permettant d'utiliser la carte graphique (GPU).
    - Recompilation et optimisation du moteur de détection (`cv_runner_onnx`) pour corriger des problèmes de gestion de mémoire, de géométries imbriquées et de précision des boîtes de détection.
- **Fiabilisation du pipeline de données** :
    - Amélioration de la gestion des systèmes de coordonnées : support étendu des données hors Lambert-93 et gestion robuste des projections.
    - Passage des calculs d'indices et de rayons en mètres pour une meilleure cohérence avec les données réelles.
    - Optimisation de la fusion des nuages de points (PDAL) pour garantir la reproductibilité des MNT.
- **Qualité et Intégrité** :
    - Mise en place de contrôles d'intégrité systématiques (checksums via `talisman`) sur les fichiers critiques et les binaires.
    - Renforcement de la suite de tests (pytest) et intégration de tests de "recette" automatisés.
    - Amélioration de la CI (GitHub Actions) pour inclure des tests sur environnement Windows.

### Autres changements
- **Documentation** : Mise à jour massive du manuel, du fichier README et du changelog.
- **Nettoyage** : Suppression de fonctions obsolètes et nettoyage des fichiers de configuration et des dépendances de test.
