## Changelog : vigieau (30 derniers jours, au 29/08/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur trois axes majeurs : la mise en conformité de l'interface avec les normes d'accessibilité (RGAA), la fiabilisation de l'historique des données de restrictions et l'optimisation des processus de synchronisation avec les sources externes (Sandre). Ces évolutions garantissent une plateforme plus inclusive, des données historiques plus robustes et une meilleure continuité de service lors des mises à jour.

### Évolutions fonctionnelles
- **Accessibilité (RGAA) :** Améliorations significatives pour l'utilisation par tous les publics :
    - Correction de la navigation, de la gestion du focus et de la hiérarchie du contenu.
    - Mise en conformité des formulaires, des champs de recherche d'adresse et des messages de validation.
    - Amélioration de l'accessibilité des cartes, des tableaux de données, des cartes de restriction et des boîtes de dialogue.
    - Optimisation du contraste et de la sémantique des liens et images.
- **Expérience utilisateur :**
    - Garantie de l'affichage des dernières restrictions d'eau connues par les utilisateurs pendant les phases de mise à jour des données.
    - Correction et amélioration de la fonction de téléchargement des fichiers GeoJSON.

### Évolutions techniques
- **Gestion de l'historique et des statistiques :**
    - Mise en place d'un système de "backfill" (reconstitution de données) distribué avec un plan de contrôle dédié pour gérer la charge de production.
    - Amélioration de la résilience des processus de publication historique et de la gestion des snapshots statistiques.
    - Optimisation des performances via la compaction des données de réparation et l'indexation des communes par département.
- **Synchronisation et précision des données :**
    - Amélioration de la précision géométrique lors de la synchronisation avec les données Sandre [#46](https://github.com/MTES-MCT/vigieau/pull/46).
    - Renforcement de la fiabilité de la réconciliation des données Sandre (gestion des preuves MDM et des cas limites).
    - Sécurisation de l'atomicité des publications de zones pour éviter les états de données incohérents.
- **Infrastructure et performance :**
    - Optimisation du traitement des fichiers cartographiques (PMTiles et Tippecanoe).
    - Amélioration de la robustesse des pipelines de monitoring (smoke tests) en production.

### Autres changements
- **Documentation :**
    - Établissement d'un plan de remédiation RGAA.
    - Documentation des opérations de "backfill" historique et de la branche `master` comme branche canonique.
- **CI/CD et Maintenance :**
    - Renforcement des politiques de fraîcheur des données et des tests de santé (smoke tests) dans les pipelines CI/CD.
    - Mise à jour des dépendances pour corriger des vulnérabilités de sécurité.
