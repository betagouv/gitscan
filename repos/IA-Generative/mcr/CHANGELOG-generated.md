## Changelog : mcr (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la refactorisation de l'architecture de l'application, en particulier autour des routes et des use cases, pour une meilleure organisation et maintenabilité.  De nombreuses améliorations ont été apportées à la gestion des transcriptions, des rapports et des notes, avec un accent sur la robustesse et l'expérience utilisateur. Des corrections de bugs et des améliorations de la documentation ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger l'audio des réunions [#757](https://github.com/IA-Generative/mcr/issues/757).
- Amélioration de l'accessibilité du modal de feedback [#831](https://github.com/IA-Generative/mcr/issues/831).
- Ajout d'une page de maintenance pour signaler les interruptions de service [#799](https://github.com/IA-Generative/mcr/issues/799).
- Possibilité de relancer la génération d'un rapport [#720](https://github.com/IA-Generative/mcr/issues/720).
- Ajout de la possibilité d'ajouter des notes personnalisées aux sections des rapports [#726](https://github.com/IA-Generative/mcr/issues/726), [#727](https://github.com/IA-Generative/mcr/issues/727).
- Ajout d'un bouton "Voir dans Drive" pour accéder directement aux fichiers sur Google Drive [#687](https://github.com/IA-Generative/mcr/issues/687).
- Amélioration de la gestion des erreurs et des validations pour le feedback des utilisateurs [#831](https://github.com/IA-Generative/mcr/issues/831).
- Ajout d'une fonctionnalité pour gérer les tâches de transcription des réunions supprimées [#807](https://github.com/IA-Generative/mcr/issues/807).

### Évolutions techniques
- Refactorisation majeure de l'architecture en utilisant des "use cases" pour gérer la logique métier, remplaçant les routes directes [#828](https://github.com/IA-Generative/mcr/issues/828), [#840](https://github.com/IA-Generative/mcr/issues/840), [#838](https://github.com/IA-Generative/mcr/issues/838), [#833](https://github.com/IA-Generative/mcr/issues/833), [#820](https://github.com/IA-Generative/mcr/issues/820), [#770](https://github.com/IA-Generative/mcr/issues/770), [#755](https://github.com/IA-Generative/mcr/issues/755), [#790](https://github.com/IA-Generative/mcr/issues/790), [#712](https://github.com/IA-Generative/mcr/issues/712), [#722](https://github.com/IA-Generative/mcr/issues/722).
- Suppression de code obsolète et de fonctionnalités non utilisées [#828](https://github.com/IA-Generative/mcr/issues/828), [#770](https://github.com/IA-Generative/mcr/issues/770), [#685](https://github.com/IA-Generative/mcr/issues/685).
- Amélioration de la gestion des logs et suppression des préfixes inutiles [#511](https://github.com/IA-Generative/mcr/issues/511).
- Mise en place d'un linter pour l'architecture des use cases [#814](https://github.com/IA-Generative/mcr/issues/814).
- Migration vers une organisation basée sur le "trunk-based development" [#796](https://github.com/IA-Generative/mcr/issues/796).
- Amélioration de la gestion des erreurs et des exceptions dans les use cases [#823](https://github.com/IA-Generative/mcr/issues/823).
- Refactorisation du code pour une meilleure séparation des préoccupations et une plus grande modularité.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour des dépendances et de l'infrastructure.

### Autres changements
- Mise à jour de la documentation pour refléter les changements récents [#760](https://github.com/IA-Generative/mcr/issues/760), [#703](https://github.com/IA-Generative/mcr/issues/703).
- Ajout d'un script pour installer facilement les dépendances locales [#834](https://github.com/IA-Generative/mcr/issues/834).
- Mise à jour de la configuration de Slack pour refléter les changements d'équipe [#834](https://github.com/IA-Generative/mcr/issues/834).
- Suppression de configurations Docker inutiles [#686](https://github.com/IA-Generative/mcr/issues/686).
- Ajout d'une commande `make install` pour faciliter la configuration de l'environnement de développement [#834](https://github.com/IA-Generative/mcr/issues/834).
