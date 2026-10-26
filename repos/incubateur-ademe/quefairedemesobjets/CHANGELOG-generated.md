## Changelog : quefairedemesobjets (30 derniers jours, au 25 octobre 2026)

### Résumé
Ce mois-ci a été marqué par une refonte majeure de l'interface d'administration des "Suggestions", qui adopte désormais une architecture moderne combinant Django et React. Parallèlement, l'expérience utilisateur a été enrichie par l'amélioration de la recherche d'objets et le déploiement progressif de l'Assistant V2.

### Évolutions fonctionnelles
- **Assistant V2** : Redirection automatique des utilisateurs existants vers la nouvelle version [#3480](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3480) et correction de la gestion des synonymes [#3497](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3497).
- **Gestion des Suggestions (Admin)** : Mise en place d'une nouvelle interface de gestion incluant des actions de masse [#3493](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3493), une validation ligne par ligne [#3492](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3492), et une gestion par cohortes et groupes [#3489](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3489), [#3490](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3490).
- **Recherche & Navigation** : Amélioration du scoring de la recherche d'objets pour plus de pertinence [#3388](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3388) et correction de la navigation (bouton précédent) dans les formulaires [#3433](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3433).
- **Interface utilisateur** : Ajustements visuels de l'administration (largeur des menus déroulants [#3496](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3496)) et rendu des informations de tri plus discret par défaut [#3403](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3403).

### Évolutions techniques
- **Architecture** : Implémentation du nouveau socle architectural Django + React pour le module de suggestions [#3488](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3488) et mise à jour de la structure pour gérer les suggestions de clusters [#3536](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3536).
- **Pipeline de données (Airflow & DBT)** : Migration des processus d'enrichissement (DAGs) vers la nouvelle architecture de suggestions [#3530](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3530), correction du processus DBT pour l'enrichissement SIRET/SIREN [#3532](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3532) et amélioration de la précision des logs Airflow [#3522](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3522).
- **Infrastructure & DevOps** : Suppression de l'infrastructure Metabase en préproduction [#3409](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3409), optimisation du nettoyage des environnements de preview [#3385](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3385) et renforcement de la sécurité via l'utilisation de variables d'environnement pour les commandes de base de données [#3448](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3448).
- **Refactoring** : Déplacement des paramètres des workers vers le module API [#3463](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3463) et correction de la gestion du cache Nginx pour l'Assistant [#3486](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3486).

### Autres changements
- **Documentation** : Ajout de la documentation relative aux nouvelles fonctionnalités de suggestion dans l'administration [#3494](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3494).
