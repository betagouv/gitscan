## Changelog : quefairedemesobjets (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois a été marqué par une optimisation majeure des performances de l'infrastructure et une amélioration de la stabilité de la plateforme. Les utilisateurs bénéficieront d'une navigation plus fluide (notamment sur mobile et via les cartes) et de corrections sur plusieurs fonctionnalités de partage, de recherche et de gestion des données.

### Évolutions fonctionnelles
- **Expérience utilisateur & Interface** :
    - Simplification des boutons de partage de l'assistant [#3354](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3354).
    - Amélioration de l'autocomplétion sur mobile iOS pour un meilleur positionnement des suggestions [#3380](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3380).
    - Affichage d'une carte directement dans une fenêtre modale [#3071](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3071).
    - Personnalisation du texte d'aide (placeholder) dans le champ de recherche [#3198](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3198).
    - Correction des modales de partage pour les pages produits [#3174](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3174).
- **Contenu & Données** :
    - Amélioration de l'orientation des visiteurs sur les pages de contenu "Sites Conformes" [#3238](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3238).
    - Ajout d'un champ de localisation dans le formulaire de contact [#3300](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3300).
    - Nettoyage des données Open Data pour interdire les lignes vides dans les propositions de services [#3311](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3311).
- **Corrections** :
    - Résolution d'une erreur 500 lors de la gestion des redirections de synonymes [#3200](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3200).
    - Correction de l'affichage de la carte suite à la mise à jour de MapLibre [#3383](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3383).

### Évolutions techniques
- **Performances & Optimisations** :
    - Optimisation des performances Docker pour les bases de données PostGIS [#3376](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3376).
    - Fine-tuning de la configuration Nginx et Gunicorn [#3373](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3373).
    - Utilisation des workers `gthread` pour Gunicorn afin d'améliorer la réactivité [#3362](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3362).
    - Optimisation de la gestion des connexions à la base de données via `CONN_MAX_AGE` [#3364](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3364).
- **Infrastructure & DevOps** :
    - Mise à jour d'Apache Airflow vers la version 3.3.1 [#3351](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3351).
    - Migration et déploiement de bases de données Airflow et de Metabase sur Scaleway [#3384](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3384).
    - Amélioration de l'infrastructure avec OpenTofu et mise à jour du provider Scaleway pour Terragrunt [#3387](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3387) [#3320](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3320).
    - Mise en place d'un monitoring pour le proxy Posthog via un nouveau DAG [#3374](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3374).
    - Amélioration de la gestion des environnements de preview (URL de base et déploiement) [#3353](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3353) [#3302](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3302).
    - Renforcement de la sécurité via une procédure de rotation des mots de passe [#3382](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3382).
- **Architecture & Data Pipeline** :
    - Réorganisation du modèle `base_action` dans le pipeline dbt [#3386](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3386).
    - Correction de l'ordre d'exécution des tâches pour le calcul des acteurs [#3366](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3366).
    - Refactoring des fichiers Airflow pour éviter l'utilisation de fonctions utilitaires à la racine [#3271](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3271).

### Autres changements
- Nettoyage du dépôt (suppression de fichiers `uv.lock` inutiles [#3270](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3270) et ajout de `.parcel-cache` au `.gitignore`).
- Ajustement de la configuration de Dependabot pour exclure certaines versions de TypeScript [#3375](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3375).
