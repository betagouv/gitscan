## Changelog : quefairedemesobjets (30 derniers jours, au 02 septembre 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur l'amélioration de l'expérience utilisateur (recherche et partage), le renforcement de la fiabilité des données et la stabilisation des processus techniques, notamment via l'amélioration des tests et des pipelines de données.

### Évolutions fonctionnelles
- **Amélioration de l'interface de recherche** : le texte d'aide (placeholder) du champ de recherche est désormais configurable [#3198](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3198).
- **Correction du partage de contenu** : résolution d'un bug où certains objets manquaient dans les fenêtres modales de partage des pages produits [#3174](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3174).
- **Qualité des données** : 
    - Mise en place de règles pour interdire les lignes vides dans les propositions de services du jeu de données OpenData [#3311](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3311).
    - Amélioration de la gestion des identifiants pour la CMA afin d'éviter les erreurs liées aux valeurs nulles [#3253](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3253).

### Évolutions techniques
- **Optimisation des pipelines de données** : 
    - Récupération des paramètres du DAG de clustering via API [#3246](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3246).
    - Correction de problèmes d'import de dépendances sur les DAGs suite à une mise à jour [#3318](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3318).
- **Qualité logicielle et tests** : 
    - Intégration de `sqlfluff` pour le contrôle de qualité du code SQL dans la plateforme de données [#3190](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3190).
    - Renforcement de la robustesse des tests de bout en bout (e2e) [#3294](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3294).
    - Amélioration du contrôleur dédié à l'A/B testing [#3123](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3123).
- **Maintenance infrastructure** : 
    - Automatisation de la recréation de la base de données de prévisualisation en cas de suppression [#3254](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3254).
    - Gestion et régénération des fichiers de verrouillage (lockfiles) pour la stabilité des dépendances [#3299](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3299).

### Autres changements
- **Nettoyage du dépôt** : suppression des fichiers `uv.lock` inutiles [#3270](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3270).
