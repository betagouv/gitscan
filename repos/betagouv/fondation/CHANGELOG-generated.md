## Changelog : fondation (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur une refonte architecturale majeure vers une approche "feature-first", améliorant la maintenabilité et l'évolutivité du projet. Des améliorations fonctionnelles ont été apportées à la gestion des fichiers, des observations et des dates d'audition. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Possibilité d'enregistrer les éditions des utilisateurs pour les rapports officiels [#510](https://github.com/betagouv/fondation/issues/510).
- Ajout d'un message de statut lors de la sauvegarde d'une date d'audition, avec possibilité de modifier les dates passées après confirmation [#508](https://github.com/betagouv/fondation/issues/508).
- Ajout d'un bouton "+" pour ajouter des observations [#497](https://github.com/betagouv/fondation/issues/497).
- Possibilité d'attacher des fichiers à un dossier de candidature [#407](https://github.com/betagouv/fondation/issues/407).
- Ajout de la possibilité de définir une date d'audition pour les magistrats [#463](https://github.com/betagouv/fondation/issues/463).
- Amélioration de la sélection des fichiers d'agenda [#451](https://github.com/betagouv/fondation/issues/451).
- Remplacement du modal "Magistrat" par un panneau latéral pour une meilleure expérience utilisateur [#439](https://github.com/betagouv/fondation/issues/439).
- Ajout d'étiquettes de résultat de dossier de nomination provenant de l'API [#473](https://github.com/betagouv/fondation/issues/473).

### Évolutions techniques
- Refonte de l'architecture frontale vers une approche "feature-first" pour une meilleure organisation et maintenabilité.
- Migration des tests vers Vitest [#437](https://github.com/betagouv/fondation/issues/437).
- Suppression des modèles partagés au profit d'une architecture plus modulaire [#496](https://github.com/betagouv/fondation/issues/496), [#495](https://github.com/betagouv/fondation/issues/495), [#494](https://github.com/betagouv/fondation/issues/494), [#491](https://github.com/betagouv/fondation/issues/491), [#486](https://github.com/betagouv/fondation/issues/486), [#485](https://github.com/betagouv/fondation/issues/485), [#483](https://github.com/betagouv/fondation/issues/483).
- Mise à jour de Prisma vers la version 7 [#481](https://github.com/betagouv/fondation/issues/481).
- Mise à jour de TypeScript vers la version 6 [#480](https://github.com/betagouv/fondation/issues/480).
- Amélioration de la gestion des dépendances et des caches pour optimiser les performances.
- Ajout d'un point de terminaison d'autorisation M2M pour les magistrats [#502](https://github.com/betagouv/fondation/issues/502).
- Internalisation des enums et types pour une meilleure cohérence [#492](https://github.com/betagouv/fondation/issues/492), [#490](https://github.com/betagouv/fondation/issues/490).
- Suppression des observers legacy [#464](https://github.com/betagouv/fondation/issues/464).

### Autres changements
- Correction de la documentation concernant le rôle de relais SDV et ajout de Scaleway au diagramme d'architecture [#509](https://github.com/betagouv/fondation/issues/509).
- Ajout de guides Storybook et mise à jour du fichier README principal [#507](https://github.com/betagouv/fondation/issues/507).
- Correction de l'appel supprimé à sheetjs.sh dans le build Scalingo [#501](https://github.com/betagouv/fondation/issues/501).
- Suppression du modal de rappel de suivi des observations lors de la définition du résultat [#493](https://github.com/betagouv/fondation/issues/493).
- Refonte des stories MagistratObservations autour d'un terrain de jeu à carte unique [#488](https://github.com/betagouv/fondation/issues/488).
- Correction d'un problème lié au cache Vite lors de la mise à jour des icônes react-dsfr [#487](https://github.com/betagouv/fondation/issues/487).
- Amélioration de la gestion des requêtes Storybook pour éviter les problèmes de réseau [#479](https://github.com/betagouv/fondation/issues/479).
- Suppression d'une étape obsolète de sheetjs du workflow Storybook [#478](https://github.com/betagouv/fondation/issues/478).
- Déploiement de Storybook sur Scalingo [#477](https://github.com/betagouv/fondation/issues/477).
- Ajout de la prise en charge de xlsx dans le projet [#476](https://github.com/betagouv/fondation/issues/476).
- Ajout de tests d'intégration API [#441](https://github.com/betagouv/fondation/issues/441).
- Mise en place d'une vérification OpenAPI lors du push sur la branche de développement [#475](https://github.com/betagouv/fondation/issues/475).
- Mise en place d'un système de validation des clients OpenAPI générés [#472](https://github.com/betagouv/fondation/issues/472).
- Correction de l'affichage des nombres LOFLI [#480](https://github.com/betagouv/fondation/issues/480).
- Plusieurs corrections de sécurité et mises à jour de dépendances.
