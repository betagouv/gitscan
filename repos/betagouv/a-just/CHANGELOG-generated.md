## Changelog : a-just (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution du projet a-just. Les principales améliorations concernent le cockpit (nouvelle interface), l'extracteur de données (collecte 2026) et les tests automatisés (E2E et unitaires). Des corrections de bugs ont également été apportées, notamment concernant la gestion des valeurs négatives dans les exports Excel et l'affichage des données dans l'interface.

### Évolutions fonctionnelles
- Amélioration de l'interface du cockpit avec l'ajout de données et la gestion des popins d'alerte (#449).
- Correction de l'affichage des options dans le sélecteur "Att. J" pour ne proposer que les valeurs pertinentes (Siège autres et Parquet) (#449).
- Correction de l'affichage des ratios dans le simulateur.
- Amélioration de l'affichage des données dans le simulateur (correction des projections).
- Ajout de la gestion du SSO (Single Sign-On) pour l'authentification.
- Modification des libellés "Exporter la situation" en "Exporter" pour une meilleure lisibilité.

### Évolutions techniques
- Refonte de l'extracteur de données pour la collecte 2026 (#446, #445, #444, #440).
- Correction d'un problème de gestion des valeurs négatives dans les exports Excel, avec suppression temporaire de l'arrondi côté backend et ajout de fonctions MAX dans les formules Excel.
- Amélioration de la robustesse des tests E2E avec une configuration plus stable de l'image Cypress et une meilleure gestion des rapports de tests.
- Mise à jour de l'infrastructure de tests avec l'ajout de tests unitaires et l'amélioration des tests d'intégration.
- Optimisation des scripts CI/CD pour réduire la consommation de mémoire et améliorer la fiabilité des builds.
- Ajout de logs plus détaillés pour faciliter le débogage.
- Correction de problèmes liés à l'anonymisation des données.

### Autres changements
- Mise à jour de la documentation et des fichiers de configuration.
- Nettoyage du code et suppression de fichiers inutiles.
- Correction de noms de fichiers et de branches.
- Mise à jour des versions des dépendances.
- Ajout de fichiers de configuration pour les tests Cypress.
- Correction de l'upload des fichiers Excel.
- Correction des noms de fichiers pour les rapports de tests.
- Ajout de tests pour la base de données.
- Correction de l'affichage des libellés.
- Amélioration de la gestion des erreurs dans les tests.
