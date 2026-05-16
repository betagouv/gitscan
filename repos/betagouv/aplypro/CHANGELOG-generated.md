## Changelog : aplypro (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des corrections d'allocations, la pagination des rapports et la robustesse du système. Des corrections de bugs ont été apportées à la page de rectification, notamment concernant les adresses et les validations. Une nouvelle fonctionnalité permet de relancer les corrections en cas d'échec.

### Évolutions fonctionnelles
- Amélioration de la gestion des codes d'extension de voie autorisés par l'ASP, en lien avec l'issue [#1951](https://github.com/betagouv/aplypro/issues/1951).
- Pagination ajoutée à la page d'index des rapports pour une meilleure expérience utilisateur [#1956](https://github.com/betagouv/aplypro/issues/1956).
- Possibilité de relancer l'envoi des corrections en cas de rejet, avec un mécanisme de retry [#1953](https://github.com/betagouv/aplypro/issues/1953).
- Amélioration de la page de rectification :
    - Masquage du numéro IBAN pour plus de sécurité.
    - Corrections de plusieurs bugs mineurs [#1947](https://github.com/betagouv/aplypro/issues/1947).
    - Amélioration des validations et affichage des erreurs [#1948](https://github.com/betagouv/aplypro/issues/1948).
    - Correction de bugs liés aux mises à jour d'adresse [#1944](https://github.com/betagouv/aplypro/issues/1944).

### Évolutions techniques
- Centralisation de la définition de la méthode `overpaid?` pour une meilleure maintenabilité.
- Pré-calcul du validateur sur la page de rectification pour optimiser les performances.
- Ajout de tests unitaires et de tests fonctionnels pour améliorer la couverture et la qualité du code.
- Refactoring et nettoyage du code, notamment suppression de conditions inutiles et nettoyage de l'abbreviator.

### Autres changements
- Mise à jour de la version de l'application à 2.10.1 et 2.10.0.
- Correction du titre de la page de rectification.
- Bump de version à 2.9.4.
