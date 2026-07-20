## Changelog : rapportnav2 (30 derniers jours, au 2026-07-17)

### Résumé
Cette version apporte des améliorations significatives à l'interface d'administration, notamment l'intégration des missions. Des corrections de performance ont été apportées pour optimiser l'affichage et la manipulation des données, en particulier pour les contrôles et infractions. De plus, la gestion des pays a été revue et des corrections ont été apportées à la validation des données et à l'affichage des informations.

### Évolutions fonctionnelles
- Ajout de la gestion des missions dans l'interface d'administration.
- Refonte de l'interface de gestion des équipages des missions PAM.
- Amélioration de l'affichage des contrôles et infractions (ajout de tabs pour les actions Fish).
- Ajout de la gestion des pays via l'API.
- Correction de l'affichage des options des radios multiples dans Fish [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033).
- Correction de l'affichage des valeurs dans l'interface.
- Suppression du bouton désactivé dans l'interface.

### Évolutions techniques
- Optimisation des performances lors du calcul du statut des actions en utilisant des données en mémoire plutôt que des requêtes répétées à la base de données.
- Utilisation de `@BatchSize` pour optimiser les requêtes liées aux agents, rôles d'agents, infractions et contrôles.
- Mise à jour de Spring Boot en version 4.1.0.
- Corrections et ajustements suite aux revues de code.

### Autres changements
- Correction de bugs divers liés à la validation des données.
- Correction de problèmes de duplication d'informations générales et de cibles.
- Correction de bugs liés à la suppression d'infractions sur Fish [#1412](https://github.com/MTES-MCT/rapportnav2/issues/1412) et [#1461](https://github.com/MTES-MCT/rapportnav2/issues/1461).
- Ajout de deux attributs à ActionFish.
- Corrections de tests et de build.
- Mises à jour de la documentation et de la configuration.
