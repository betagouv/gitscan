## Changelog : playground (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des versions des ingéstions de données, l'amélioration de la gestion des utilisateurs et des permissions, ainsi que la correction de bugs et l'optimisation de la sécurité. Des améliorations ont également été apportées à l'intégration avec Letta Cloud et à l'automatisation des tests.

### Évolutions fonctionnelles
- Ajout de l'affichage de la version d'ingestion dans l'interface utilisateur, permettant de suivre l'historique des données. [#250](https://github.com/refugies-info/playground/pull/250)
- Possibilité d'assigner une fiche à un utilisateur pour le suivi et la collaboration. [#242](https://github.com/refugies-info/playground/pull/242)
- Correction d'un bug empêchant la sauvegarde des fiches Bomo. [#243](https://github.com/refugies-info/playground/pull/243)
- Correction d'un bug lié à l'affichage des titres des fiches RCO en langage clair. [#252](https://github.com/refugies-info/playground/pull/252)
- Correction d'un bug concernant les métadonnées avec des coordonnées GPS. [#253](https://github.com/refugies-info/playground/pull/253)
- Ajout d'un bouton "Enregistrer" même pour les fiches archivées. [#237](https://github.com/refugies-info/playground/pull/237)
- Amélioration de l'affichage du statut de publication des fiches. [#240](https://github.com/refugies-info/playground/pull/240)
- Mise en place d'une auto-sauvegarde des fiches Bomo. [#247](https://github.com/refugies-info/playground/pull/247)

### Évolutions techniques
- Intégration d'une action Letta Code Review dans le workflow CI/CD. [#268](https://github.com/refugies-info/playground/pull/268)
- Refactorisation de la gestion des versions d'ingestion pour une meilleure robustesse et clarté. [#271](https://github.com/refugies-info/playground/pull/271)
- Mise à jour des types Supabase générés automatiquement. [#258](https://github.com/refugies-info/playground/pull/258)
- Migration de l'identifiant `author_id` vers `assignee_id` dans les tables de la base de données. [#238](https://github.com/refugies-info/playground/pull/238)
- Correction de la migration de la base de données pour assurer sa rejouabilité. [#272](https://github.com/refugies-info/playground/pull/272)
- Suppression des paramètres Claude inutilisés. [#266](https://github.com/refugies-info/playground/pull/266)
- Archivage des anciens assets RCO. [#260](https://github.com/refugies-info/playground/pull/260)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. [#262](https://github.com/refugies-info/playground/pull/262)
- Ajout d'une commande pour migrer la base de données. [#251](https://github.com/refugies-info/playground/pull/251)

### Autres changements
- Ajout de nouveaux traducteurs et agents de traduction.
- Amélioration de la documentation concernant l'inventaire Letta Cloud. [#259](https://github.com/refugies-info/playground/pull/259)
- Correction d'un test Storybook bloquant la CI. [#239](https://github.com/refugies-info/playground/pull/239)
- Suppression d'un workflow de création d'enregistrements inutiles.
- Ajout de Camille et Jérémy au seed des utilisateurs pour le débogage. [#258](https://github.com/refugies-info/playground/pull/258)
- Suppression d'un workflow de traduction obsolète.
- Mise à jour du workflow de dépendances. [#236](https://github.com/refugies-info/playground/pull/236)
