## Changelog : fondation (30 derniers jours, au 05/08/2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes avec la refonte de la gestion des agendas et des rapports officiels, offrant ainsi de nouveaux outils d'édition et une meilleure gestion documentaire. L'expérience utilisateur a été fluidifiée par l'introduction de panneaux latéraux pour la consultation des données et de nouvelles pages de détails. En parallèle, une restructuration profonde de l'architecture technique a été réalisée pour améliorer la robustesse et la maintenabilité du système.

### Évolutions fonctionnelles
- **Gestion des rapports et agendas** : Mise en place d'un nouvel éditeur d'agenda frontend [#541](https://github.com/betagouv/fondation/issues/541), possibilité de sauvegarder les éditions de documents [#539](https://github.com/betagouv/fondation/issues/539) et augmentation de l'espace disponible pour les signatures dans les rapports [#547](https://github.com/betagouv/fondation/issues/547).
- **Expérience utilisateur et interface** : Création d'une page dédiée aux détails des magistrats [#513](https://github.com/betagouv/fondation/issues/513) et remplacement des fenêtres modales par des panneaux latéraux pour une consultation plus fluide des observations [#439](https://github.com/betagouv/fondation/issues/439), [#474](https://github.com/betagouv/fondation/issues/474).
- **Gestion des nominations et auditions** : Ajout de la possibilité de joindre des fichiers aux dossiers de nomination [#407](https://github.com/betagouv/fondation/issues/407), intégration de la date d'audition des magistrats [#463](https://github.com/betagouv/fondation/issues/463) et amélioration du suivi des dates d'audition [#508](https://github.com/betagouv/fondation/issues/508).
- **Alertes et sécurité** : Ajout d'une alerte en cas de juridiction exclue lors d'une affectation manuelle [#535](https://github.com/betagouv/fondation/issues/535) et mise en place d'un audit des points de terminaison (endpoints) publics [#526](https://github.com/betagouv/fondation/issues/526).

### Évolutions techniques
- **Architecture logicielle** : Migration massive du projet vers une architecture "feature-first" pour une meilleure organisation du code et une modularité accrue [#432](https://github.com/betagouv/fondation/issues/432).
- **Génération de documents** : Migration de la génération de PDF de Puppeteer vers Gotenberg pour plus de fiabilité [#520](https://github.com/betagouv/fondation/issues/520).
- **Qualité et Tests** : Migration vers Vitest [#437](https://github.com/betagouv/fondation/issues/437), ajout de tests unitaires frontend et renforcement de la validation des contrats OpenAPI dans la CI pour éviter les dérives de l'API [#472](https://github.com/betagouv/fondation/issues/472).
- **Mises à jour de l'infrastructure** : Montée de version majeure de TypeScript (v6) [#480](https://github.com/betagouv/fondation/issues/480) et de Prisma (v7) [#481](https://github.com/betagouv/fondation/issues/481).
- **Design System** : Alignement des espacements et des couleurs sur les tokens officiels du DSFR [#418](https://github.com/betagouv/fondation/issues/418).

### Autres changements
- **Documentation** : Mise à jour du README et ajout de guides Storybook pour faciliter le développement des composants [#507](https://github.com/betagouv/fondation/issues/507).
- **Nettoyage du code** : Suppression des anciens modèles partagés et internalisation de diverses énumérations et types (Rôles, Genre, Grades) pour simplifier la structure du projet.
