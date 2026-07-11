## Changelog : catalogi (30 derniers jours, au 18 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des données externes, notamment pour les références ROR et RNSR, et introduit une nouvelle fonctionnalité de protection des logiciels configurable via l'interface utilisateur. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer l'affichage des protections des logiciels via l'interface utilisateur, avec un message d'administration associé. [#523](https://github.com/codegouvfr/catalogi/issues/523)
- Affichage des protections des logiciels dans une modale dédiée.
- Amélioration de la sélection des logiciels sur la page d'accueil, avec une configuration possible via `ui-config`.
- Ajout de la récupération de l'organisation pour les références ROR et RNSR. [#523](https://github.com/codegouvfr/catalogi/issues/523)
- Réintégration des métadonnées de dépôt sur GitHub pour les données externes. [#547](https://github.com/codegouvfr/catalogi/issues/547)
- Blocage de l'API de création de logiciels lorsque l'utilisation de la fonctionnalité "ajouter un logiciel ou service" est désactivée.
- Correction de l'ordre des migrations. [#523](https://github.com/codegouvfr/catalogi/issues/523)

### Évolutions techniques
- Optimisation de la requête SQL pour filtrer les données, déplaçant le filtre du traitement des résultats vers la requête elle-même. [#516](https://github.com/codegouvfr/catalogi/issues/516)
- Mise en place d'un ordre déterministe pour les données externes des logiciels afin d'assurer la cohérence des tests.
- Mise à jour de la méthode de mise à jour des données par source et en parallèle. [#516](https://github.com/codegouvfr/catalogi/issues/516)
- Correction d'un test live.
- Ajout d'un test et correction de la fermeture des pull requests GitHub.

### Autres changements
- Amélioration de l'espacement entre le héros de la page d'accueil et la sélection des logiciels.
- Mises à jour des dépendances via Renovate.
- Augmentation du numéro de version.
