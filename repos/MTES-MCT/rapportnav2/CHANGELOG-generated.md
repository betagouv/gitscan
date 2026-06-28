## Changelog : rapportnav2 (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment pour la gestion des actions et des ressources liées aux missions. Des corrections ont été apportées pour améliorer la validation des données et l'affichage des informations. L'intégration de Metabase permet désormais d'intégrer des tableaux de bord directement dans l'application.

### Évolutions fonctionnelles
- Ajout de la gestion des ressources associées aux actions de mission, incluant une nouvelle table `mission_action_resource` [#1390](https://github.com/MTES-MCT/rapportnav2/issues/1390).
- Refonte de l'interface pour la gestion des agents et des ressources, avec une page dédiée et des restrictions basées sur les rôles utilisateurs.
- Intégration d'un iframe Metabase pour l'affichage de tableaux de bord directement dans l'application.
- Amélioration de l'affichage des valeurs et du contrôle des actions "FISH" avec l'ajout de tabs.
- Correction de l'ordre des options dans les radios "FISH" [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033).
- Ajout de la possibilité de plonger (diving) dans les contrôles de navigation.

### Évolutions techniques
- Ajout de validations côté backend pour renforcer la cohérence des données.
- Générateur de documentation pour les règles de validation.
- Mise à jour des dépendances frontend (monitor-ui, undici).
- Amélioration des tests et correction de problèmes de build.
- Correction de la configuration du type de localisation (locationType) pour les contrôles.
- Refactoring du code frontend pour une meilleure organisation et maintenabilité.

### Autres changements
- Correction de dimensions du dialogue de création de mission.
- Ajustements de l'interface utilisateur suite aux retours produit.
- Suppression d'un bouton désactivé inutile.
- Ajout d'attributs à la classe `ActionFish`.
- Correction de problèmes liés aux snapshots des tests frontend.
- Mise à jour de la documentation et du playbook de déploiement.
