## Changelog : fondation (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte architecturale majeure vers une approche "feature-first", améliorant la maintenabilité et l'évolutivité. Des améliorations significatives ont été apportées à la gestion des fichiers, des rapports et des observations, ainsi qu'à la sécurité et à la performance. L'ajout de Gotenberg comme générateur de PDF remplace Puppeteer, offrant une solution plus stable et performante.

### Évolutions fonctionnelles
- Ajout d'une page de détails du magistrat avec accès aux informations pertinentes. [#513](https://github.com/betagouv/fondation/issues/513)
- Possibilité de joindre des fichiers aux dossiers de nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Ajout d'une date d'audition pour les magistrats. [#463](https://github.com/betagouv/fondation/issues/463)
- Amélioration de l'affichage des observations des magistrats avec une refonte de l'interface et un panneau latéral dédié. [#474](https://github.com/betagouv/fondation/issues/474)
- Ajout d'un lien vers le propre rapport d'un membre dans l'en-tête du magistrat. [#500](https://github.com/betagouv/fondation/issues/500)
- Ajout d'un point d'accès M2M pour l'autorisation des magistrats. [#502](https://github.com/betagouv/fondation/issues/502)
- Possibilité de sauvegarder les éditions des rapports officiels des utilisateurs. [#510](https://github.com/betagouv/fondation/issues/510)
- Ajout d'un indicateur de commentaires sur les dossiers de nomination, tenant compte des résumés vides. [#408](https://github.com/betagouv/fondation/issues/408)
- Amélioration de la sélection de fichiers pour l'agenda. [#451](https://github.com/betagouv/fondation/issues/451)

### Évolutions techniques
- Refonte de l'architecture frontale vers une approche "feature-first" pour une meilleure organisation et maintenabilité du code.
- Remplacement de Puppeteer par Gotenberg pour la génération de PDF, améliorant la performance et la stabilité. [#520](https://github.com/betagouv/fondation/issues/520)
- Mise à jour de nombreuses dépendances, incluant React, NestJS, Prisma, TypeScript et d'autres.
- Migration des tests vers Vitest. [#437](https://github.com/betagouv/fondation/issues/437)
- Internalisation des enums et types partagés dans l'API pour une meilleure cohérence.
- Suppression des modèles partagés inutilisés.
- Amélioration de la sécurité avec des mises à jour de dépendances corrigeant des vulnérabilités.
- Ajout d'une vérification de la conformité des API lors des déploiements en environnement de développement. [#526](https://github.com/betagouv/fondation/issues/526)
- Ajout d'un favicon à l'application backend. [#521](https://github.com/betagouv/fondation/issues/521)

### Autres changements
- Correction de l'environnement variable Gotenberg pour la génération d'OpenAPI. [#524](https://github.com/betagouv/fondation/issues/524)
- Documentation corrigée concernant le rôle de relais SDV et l'ajout de Scaleway au diagramme d'architecture. [#509](https://github.com/betagouv/fondation/issues/509)
- Ajout de guides Storybook et mise à jour du fichier README principal. [#507](https://github.com/betagouv/fondation/issues/507)
- Préparation du domaine MTT. [#512](https://github.com/betagouv/fondation/issues/512)
- Correction de l'affichage du titre "Président" dans l'introduction. [#465](https://github.com/betagouv/fondation/issues/465)
- Amélioration de la gestion des numérotations dans les rapports.
- Correction de l'affichage des "de" avant les voyelles dans les documents générés. [#444](https://github.com/betagouv/fondation/issues/444)
- Suppression d'appels obsolètes à sheetjs.sh dans le build de Scalingo. [#501](https://github.com/betagouv/fondation/issues/501)
- Suppression du modal de rappel pour le suivi des observations lors de la définition du résultat. [#493](https://github.com/betagouv/fondation/issues/493)
- Correction d'un problème lié au cache de Vite lors des mises à jour de React DSFR. [#487](https://github.com/betagouv/fondation/issues/487)
