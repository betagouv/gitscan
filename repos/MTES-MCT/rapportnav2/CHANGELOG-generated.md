## Changelog : rapportnav2 (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface de gestion des équipages de mission (PAM), notamment une refonte de l'interface utilisateur. De plus, la gestion des pays a été améliorée avec l'intégration d'une source de données via API. Plusieurs corrections de bugs et optimisations de performance ont également été implémentées, notamment concernant l'affichage et la gestion des infractions et des contrôles.

### Évolutions fonctionnelles
- Refonte de l'interface utilisateur pour la gestion des équipages de mission (PAM) [#1436](https://github.com/MTES-MCT/rapportnav2/issues/1436).
- Intégration d'une source de données pays via API, permettant une gestion plus dynamique et à jour des pays [#1441](https://github.com/MTES-MCT/rapportnav2/issues/1441).
- Amélioration de l'affichage des contrôles et infractions, avec l'implémentation d'un système d'onglets pour une meilleure organisation [#1343](https://github.com/MTES-MCT/rapportnav2/issues/1343).
- Ajout de deux nouveaux attributs à ActionFish.
- Correction de l'ordre des options dans les MultiRadio de Fish [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033).

### Évolutions techniques
- Optimisation des performances lors du calcul du statut des actions, en utilisant les données en mémoire plutôt que de requêter la base de données à chaque fois.
- Amélioration des performances des requêtes sur les infractions et les contrôles grâce à l'utilisation de `@BatchSize`.
- Mise à jour de Spring Boot vers la version 4.1.0.

### Autres changements
- Correction de règles de validation.
- Prévention de la duplication d'informations générales et de cibles.
- Correction de bugs mineurs et ajustements de l'interface utilisateur.
- Suppression d'une dépendance obsolète (npm audit).
