## Changelog : vao (30 derniers jours, au 30 avril 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives sur les parcours de renouvellement d'agrément, notamment au niveau de la gestion des fichiers, de la saisie d'informations et de l'envoi de notifications. Des corrections ont également été apportées pour améliorer l'accessibilité et la robustesse de l'application, ainsi que des évolutions sur le module Fusager.

### Évolutions fonctionnelles
- **Renouvellement d'agrément :** Amélioration de la gestion des fichiers lors du renouvellement d'agrément, notamment pour le casier judiciaire et les documents liés aux activités ([#1265](https://github.com/SocialGouv/vao/issues/1265), [#1256](https://github.com/SocialGouv/vao/issues/1256)).
- **Renouvellement d'agrément :** Correction de bugs et amélioration de la saisie d'adresse et des informations de bilan dans le formulaire de renouvellement ([#1282](https://github.com/SocialGouv/vao/issues/1282), [#1279](https://github.com/SocialGouv/vao/issues/1279), [#1259](https://github.com/SocialGouv/vao/issues/1259), [#1258](https://github.com/SocialGouv/vao/issues/1258)).
- **Notifications :** Implémentation de l'envoi de mails de confirmation pour les demandes d'agrément ([#1286](https://github.com/SocialGouv/vao/issues/1286)).
- **Fusager :** Ajout de nouvelles fonctionnalités et corrections pour le module Fusager, incluant la gestion des messages, des listes JDMA et l'affichage des dossiers d'agrément ([#1268](https://github.com/SocialGouv/vao/issues/1268), [#1269](https://github.com/SocialGouv/vao/issues/1269), [#1248](https://github.com/SocialGouv/vao/issues/1248), [#1249](https://github.com/SocialGouv/vao/issues/1249)).
- **Interface utilisateur :** Amélioration de l'accessibilité (RGAA) des boutons et labels, notamment pour les représentants légaux ([#1281](https://github.com/SocialGouv/vao/issues/1281), [#1266](https://github.com/SocialGouv/vao/issues/1266)).
- **OVA :** Correction de l'affichage des dates et du statut dans l'interface OVA ([#1294](https://github.com/SocialGouv/vao/issues/1294)).
- **OVA :** Correction de l'inversion du nom et prénom des personnes morales ([#1273](https://github.com/SocialGouv/vao/issues/1273)).

### Évolutions techniques
- **Tests :** Ajout de tests unitaires et E2E pour améliorer la couverture et la qualité du code.
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans le cadre des corrections RGAA.
- **Typescript :** Migration de certaines parties du code en Typescript.
- **Suppression de code inutile :** Nettoyage du code dans le module `shared-ui` ([#1234](https://github.com/SocialGouv/vao/issues/1234)).

### Autres changements
- Correction de divers bugs et améliorations mineures de l'interface utilisateur.
- Mise à jour de la documentation.
- Amélioration de la gestion des doublons de fichiers ([#1295](https://github.com/SocialGouv/vao/issues/1295)).
- Correction de la sauvegarde du dossier de candidature ([#1296](https://github.com/SocialGouv/vao/issues/1296)).
- Correction de l'accès à la liste des usages ([#1293](https://github.com/SocialGouv/vao/issues/1293)).
- Correction d'un problème de formatage d'adresse ([#1284](https://github.com/SocialGouv/vao/issues/1284)).
- Suppression de documents "zombies" ([#115cfdc1](https://github.com/SocialGouv/vao/commit/115cfdc1)).
