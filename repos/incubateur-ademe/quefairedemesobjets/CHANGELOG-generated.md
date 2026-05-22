## Changelog : quefairedemesobjets (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la performance de la plateforme, notamment avec la migration vers Airflow v3. Des corrections ont été apportées à l'interface utilisateur et aux tests, et des fonctionnalités ont été ajoutées pour améliorer la recherche et la configuration des sources de données. Plusieurs mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la compatibilité.

### Évolutions fonctionnelles
- Amélioration de la recherche : Ajout d'un filtre pour rechercher des suggestions ayant des corrections (#2801).
- Amélioration de la recherche : Possibilité de filtrer les suggestions par groupe lorsqu'une suggestion unitaire existe sur un champ donné (#2796).
- Amélioration de la carte : Affichage de la mini carte sur mobile dans la fiche détaillée (#2797).
- Correction d'un bug : Correction de l'affichage dupliqué du nom dans les résultats de recherche Vélovélo (#2754).
- Redirection de domaine : Redirection du domaine legacy vers le domaine principal (#2756).
- Ajout d'une nouvelle source de données : Possibilité de configurer une source générique entièrement personnalisable (#2466).
- Amélioration du clustering : Permet de clusteriser par distance exprimée en mètres (#2728).

### Évolutions techniques
- Migration vers Airflow v3 : Adaptation du code pour la compatibilité avec Airflow v3 (#2568, #2832).
- Adaptation du déploiement : Adaptation du déploiement GitHub Actions à la version v1 du CLI SCW (#2855).
- Mise à jour de la base de données : Mise à jour du mapping de la base de données (#2829).
- Suppression de code inutile : Suppression de fichiers inutiles (#2823).
- Correction des tests E2E : Correction de tests end-to-end (#2806).
- Calcul des différences : Implémentation du calcul des différences entre les propositions de service d'un acteur et ses révisions (#2539).
- Fiabilisation des tests : Fiabilisation de la résolution du frame iframe dans les tests analytics (#2760).

### Autres changements
- Mise à jour de la documentation : Mise à jour des sites conformes (#2825).
- Nombreuses mises à jour de dépendances : Mises à jour de diverses dépendances (pydantic, django-import-export, urllib3, protobufjs, prettier, posthog-js, etc.) pour améliorer la sécurité et la stabilité. Ces mises à jour sont gérées par Dependabot et Renovate.
