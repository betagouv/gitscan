## Changelog : rapportnav2 (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des actions et des ressources, notamment pour les contrôles environnementaux. Des corrections et améliorations ont également été apportées à l'interface utilisateur, en particulier pour les formulaires et les dialogues, ainsi qu'à l'intégration de Metabase pour la visualisation de données. Des efforts ont été faits pour améliorer la validation des données et la sécurité.

### Évolutions fonctionnelles
- Ajout de la gestion des ressources des agents, avec une page dédiée et des restrictions de rôles. [#1380](https://github.com/MTES-MCT/rapportnav2/issues/1380) et [#1381](https://github.com/MTES-MCT/rapportnav2/issues/1381)
- Mise à jour de l'action "entretien des moyens" et ajout d'une nouvelle table `mission_action_resource`. [#1390](https://github.com/MTES-MCT/rapportnav2/issues/1390)
- Ajout de la possibilité de plonger (diving) dans les contrôles de navigation.
- Intégration d'un iframe Metabase pour l'affichage de rapports et de données.
- Amélioration de l'affichage des valeurs dans les formulaires.
- Correction de l'ordre des options dans les radios multi-sélection (Fish). [#1033](https://github.com/MTES-MCT/rapportnav2/issues/1033)
- Remplacement des champs de texte par des zones de texte pour les observations des contrôles environnementaux.
- Correction de l'affichage des dimensions des dialogues de création de mission.

### Évolutions techniques
- Refactorisation du code frontend pour une meilleure organisation et réutilisation.
- Ajout de validations côté backend pour renforcer la cohérence des données.
- Générateur de documentation pour les règles de validation.
- Mise à jour des dépendances frontend (Monitor-UI).
- Correction de problèmes de build et de tests.
- Amélioration des tests unitaires.
- Correction de problèmes liés à la gestion des types de localisation (GPS).

### Autres changements
- Correction de divers problèmes d'interface utilisateur et d'affichage.
- Amélioration de la gestion des snapshots pour les tests.
- Mise à jour des dépendances npm et yarn.
- Corrections de sécurité (audit npm).
- Mise à jour de la documentation.
- Corrections mineures et améliorations de code.
