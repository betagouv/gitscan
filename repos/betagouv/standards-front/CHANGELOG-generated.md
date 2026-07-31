## Changelog : standards-front (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives concernant la gestion des incubateurs, avec l'ajout d'une vue dédiée et d'informations plus détaillées. Des optimisations ont également été apportées à l'interface utilisateur, notamment pour l'affichage des tableaux et la simplification du menu principal. Enfin, des mises à jour de dépendances et de configuration ont été effectuées pour assurer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une vue pour les incubateurs, permettant de visualiser les incubateurs actifs et leurs évaluations. [#185](https://github.com/betagouv/standards-front/pulls/185)
- Affichage du nombre de services et d'évaluations actives pour chaque incubateur.
- Amélioration de l'affichage des tableaux avec l'introduction du composant `DsfrTableComponent`.
- Simplification du menu principal pour une meilleure expérience utilisateur.
- Formatage amélioré de la phase la plus récente des incubateurs.
- Suppression de la formulation "résumé" dans l'affichage des évaluations.

### Évolutions techniques
- Mise à jour de plusieurs dépendances :
    - `grape` vers la version 3.3.4
    - `solid_queue` vers la version 1.5.0
    - `actions/checkout` vers la version 7
    - `actions/cache` vers la version 6
    - `dsfr-view-components` (version non spécifiée)
- Intégration de `rack-mini-profiler` pour l'analyse des performances.
- Refonte de la configuration pour utiliser les nouvelles URL de staging.
- Mise à jour du schéma de la base de données `espace_membre`.
- Utilisation des étapes Cucumber partagées (`betagouv-cucumber-steps`).
- Refactorisation des fichiers de locales.
- Amélioration de la gestion de l'initialisation de `EspaceMembre::Startup`.
- Mise à jour de la gem `espace_membre-ruby` pour supporter le code `user.teams`.

### Autres changements
- Ajout d'une liste de résumé des composants de l'application sur la page d'accueil. [#190](https://github.com/betagouv/standards-front/pulls/190)
- Nettoyage du code et suppression d'informations inutiles.
- Correction de tests instables liés à la gem `espace_membre-ruby`.
- Ajout de la possibilité de personnaliser la description du titre d'un tableau.
