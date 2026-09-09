## Changelog : quefairedemesobjets (30 derniers jours, au 08 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'optimisation des performances du serveur et la stabilisation des environnements de déploiement. Des améliorations ont été apportées à l'interface utilisateur et à la qualité des données pour offrir une expérience plus fluide et fiable aux citoyens.

### Évolutions fonctionnelles
- Ajout d'un champ de localisation dans le formulaire de contact pour enrichir les données collectées [#3300](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3300).
- Amélioration de la qualité des données Open Data en interdisant les lignes vides dans les propositions de services [#3311](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3311).
- Personnalisation du texte d'aide (placeholder) de la barre de recherche [#3198](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3198).
- Correction d'un bug d'affichage d'objets manquants dans les fenêtres de partage des pages produits [#3174](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3174).

### Évolutions techniques
- **Performances & Infrastructure** :
    - Optimisation de la configuration Nginx et Gunicorn pour améliorer la réactivité du serveur [#3373](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3373).
    - Optimisation de la gestion des connexions à la base de données via l'application de `CONN_MAX_AGE` [#3364](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3364) et utilisation de workers `gthread` pour Gunicorn [#3362](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3362).
    - Mise à jour des outils d'infrastructure (Apache Airflow 3.3.1 et provider Scaleway pour Terragrunt) [#3351](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3351), [#3320](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3320).
- **Déploiement & CI/CD** :
    - Stabilisation des environnements de preview (gestion de l'URL de base, correction de la création de buckets et résolution d'erreurs de déploiement) [#3353](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3353), [#3367](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3367), [#3302](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3302).
- **Données & Sécurité** :
    - Renforcement de la sécurité via des correctifs et le passage des utilisateurs Metabase en lecture seule [#3350](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3350), [#3317](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3317).
    - Optimisation des pipelines de données (ordre des tâches de calcul et synchronisation des bases de données) [#3366](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3366), [#3363](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3363) et correction d'un problème d'import de dépendances dans les DAGs [#3318](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3318).
- **Qualité logicielle** :
    - Amélioration de la robustesse des tests de bout en bout (E2E) [#3294](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3294) et optimisation du contrôleur d'A/B testing [#3123](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3123).

### Autres changements
- Nettoyage du dépôt avec la suppression de fichiers `uv.lock` inutiles [#3270](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3270).
- Ajustements de configuration (exclusion de TypeScript dans Dependabot et gestion des fichiers de verrouillage) [#3375](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3375), [#3301](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3301), [#3299](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3299).
