## Changelog : quefairedemesobjets (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'améliorations significatives visant à rendre la plateforme plus rapide et plus stable. L'expérience utilisateur a été enrichie par de nouveaux outils de navigation (cartes, formulaires) et des corrections de bugs, tandis que l'infrastructure technique a été renforcée pour garantir une meilleure sécurité et une gestion des données plus efficace.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités et UX :**
    - Intégration d'une carte personnalisée dans une fenêtre modale [#3071](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3071).
    - Amélioration de l'orientation des visiteurs sur les pages de contenu "Sites Conformes" [#3238](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3238).
    - Ajout d'un champ de localisation dans le formulaire de contact [#3300](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3300).
    - Possibilité de configurer le texte d'aide (placeholder) du champ de recherche [#3198](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3198).
    - Optimisation du contrôleur d'A/B testing [#3123](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3123).
- **Corrections de bugs :**
    - Résolution d'une erreur 500 lors de la redirection d'un synonyme [#3200](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3200).
    - Correction d'un objet manquant dans les modales de partage des pages produits [#3174](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3174).
    - Interdiction des lignes vides dans les propositions de services du jeu de données Open Data pour garantir la qualité des données [#3311](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3311).

### Évolutions techniques
- **Performances :**
    - Optimisation de la configuration Nginx et Gunicorn [#3373](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3373).
    - Amélioration de la gestion des connexions à la base de données via l'application de `CONN_MAX_AGE` [#3364](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3364).
    - Utilisation de workers `gthread` pour Gunicorn afin d'améliorer la gestion des requêtes [#3362](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3362).
- **Infrastructure et DevOps :**
    - Migration des bases de données Airflow et création d'une instance Metabase sur Scaleway [#3384](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3384).
    - Mise à jour d'Apache Airflow vers la version 3.3.1 [#3351](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3351).
    - Amélioration de la stabilité et de la configuration des environnements de preview (déploiement, URL de base, gestion des buckets) [#3302](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3302) [#3353](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3353) [#3367](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3367).
    - Mise à jour du provider Scaleway pour Terragrunt [#3320](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3320).
- **Sécurité :**
    - Mise en place d'une procédure de rotation des mots de passe [#3382](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3382).
    - Restriction des accès Metabase avec la création d'utilisateurs en lecture seule [#3317](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3317).
    - Application de divers correctifs de sécurité [#3350](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3350).
- **Données et Monitoring :**
    - Ajout d'un DAG de monitoring pour le proxy Posthog [#3374](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3374).
    - Résolution de problèmes d'ordre d'exécution des tâches pour le calcul des acteurs [#3366](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3366).
    - Correction d'erreurs d'importation de dépendances dans les DAGs suite à une mise à jour [#3318](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3318).
- **Tests :**
    - Amélioration de la robustesse des tests de bout en bout (E2E) [#3294](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3294).

### Autres changements
- Nettoyage du dépôt avec la suppression de fichiers inutiles (`uv.lock`) [#3270](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3270).
- Mise à jour des configurations Git (ajout de `.parcel-cache` au `.gitignore`) et de Dependabot.
