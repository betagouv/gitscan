## Changelog : quefairedemesobjets (30 derniers jours, au 17/09/2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié de nouveaux contenus et de portails dédiés, ainsi que d'améliorations significatives de l'expérience utilisateur, notamment sur mobile et via l'interface cartographique. Un effort majeur a également été consacré à l'optimisation des performances du serveur et à la stabilisation de l'infrastructure de données et de déploiement.

### Évolutions fonctionnelles
- **Nouveaux contenus et portails** : Mise en ligne du nouveau portail [SINOE](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3312) et ajout de la nouvelle entité [LEKO](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3401).
- **Améliorations de l'expérience utilisateur (UX)** :
    - Simplification des boutons de partage de l'assistant [#3354](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3354).
    - Intégration de cartes sur mesure dans des fenêtres modales [#3071](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3071).
    - Correction du positionnement des suggestions d'autocomplétion sur mobile iOS [#3380](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3380).
    - Ajout d'un champ de localisation dans le formulaire de contact [#3300](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3300).
    - Rendu du placeholder de recherche configurable [#3198](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3198).
- **Corrections de bugs** :
    - Résolution d'un problème d'affichage de la carte suite à la mise à jour de MapLibre [#3383](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3383).
    - Correction d'une erreur 500 lors de l'ajout de redirections de synonymes [#3200](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3200).
    - Correction d'objets manquants dans les modales de partage de produits [#3174](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3174).
    - Rectification du mapping des sous-catégories CMA [#3399](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3399).

### Évolutions techniques
- **Optimisation des performances** :
    - Fine-tuning de la configuration Nginx et Gunicorn (utilisation de workers `gthread`) [#3373](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3373) [#3362](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3362).
    - Optimisation de la gestion des connexions à la base de données (application de `CONN_MAX_AGE`) [#3364](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3364).
    - Amélioration des performances Docker pour les bases de données PostGIS [#3376](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3376).
- **Infrastructure et CI/CD** :
    - Mise à jour d'Apache Airflow vers la version 3.3.1 [#3351](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3351).
    - Amélioration de la gestion des environnements de preview (déploiement et configuration des URLs) [#3302](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3302) [#3353](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3353) [#3367](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3367).
    - Mise à jour et optimisation des outils d'infrastructure (OpenTofu, provider Scaleway pour Terragrunt) [#3387](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3387) [#3320](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3320).
    - Migration des instances de base de données Airflow et Metabase [#3398](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3398) [#3384](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3384).
- **Données et Backend** :
    - Migration des produits legacy de Django vers Wagtail [#3160](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3160).
    - Réorganisation des modèles dbt et des pipelines de données [#3386](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3386) [#3366](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3366).
    - Amélioration de la qualité des données OpenData (nettoyage des lignes vides) [#3311](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3311).
    - Correction des dépendances d'importation dans les DAGs Airflow [#3318](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3318).
- **Sécurité et Qualité** :
    - Mise en place d'une procédure de rotation des mots de passe [#3382](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3382).
    - Application de correctifs de sécurité [#3350](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3350).
    - Renforcement de la robustesse des tests de bout en bout (E2E) [#3397](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3397) [#3294](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3294).
    - Restriction des accès Metabase en mode lecture seule [#3317](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3317).

### Autres changements
- **Nettoyage et configuration** :
    - Suppression de fichiers inutiles (`uv.lock`) [#3270](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3270).
    - Mise à jour du `.gitignore` pour inclure le cache Parcel.
    - Ajustement de la configuration Dependabot pour TypeScript [#3375](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3375).
