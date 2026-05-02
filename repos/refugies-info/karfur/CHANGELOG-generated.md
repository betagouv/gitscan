## Changelog : karfur (30 derniers jours, au 2026-05-01)

### Résumé
Cette version apporte des corrections de bugs et des améliorations de performance, notamment au niveau de la gestion des traductions, de la sauvegarde des données et de la stabilité générale de l'application. Des mises à jour de sécurité ont également été intégrées pour corriger des vulnérabilités identifiées. Des améliorations ont été apportées à l'interface utilisateur, notamment pour corriger des problèmes d'affichage et d'accessibilité.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct des infocards (présence de tirets indésirables). [#3706](https://github.com/refugies-info/karfur/pull/3706)
- Correction d'un problème où les fiches traduites étaient envoyées incorrectement sur l'interface de traduction. [#3712](https://github.com/refugies-info/karfur/pull/3712)
- Correction d'un bug où le compteur de bénévoles était incorrectement initialisé à 0 sur la page de traduction. [#3736](https://github.com/refugies-info/karfur/pull/3736)
- Correction d'un problème d'affichage des dates et de formatage des nombres en français, évitant ainsi des erreurs. [#3735](https://github.com/refugies-info/karfur/pull/3735)
- Correction d'un bug lié à la gestion des opérateurs Agir, notamment au niveau des coordonnées de contact. [#3728](https://github.com/refugies-info/karfur/pull/3728) et [#3721](https://github.com/refugies-info/karfur/pull/3721)
- Correction d'un bug empêchant la sauvegarde correcte des participants. [#3722](https://github.com/refugies-info/karfur/pull/3722)

### Évolutions techniques
- Amélioration des performances de la récupération des statistiques de traduction en optimisant les requêtes. [#3711](https://github.com/refugies-info/karfur/pull/3711)
- Ajout d'index MongoDB pour améliorer les performances des requêtes sur les logs, les indicateurs et les dispositifs. [#3710](https://github.com/refugies-info/karfur/pull/3710)
- Refactor de la gestion des cartes (Map) Mongoose pour améliorer la robustesse et éviter les erreurs de sauvegarde. [#3725](https://github.com/refugies-info/karfur/pull/3725) et [#3721](https://github.com/refugies-info/karfur/pull/3721)
- Mise en place d'un hook pre-commit avec GitLeaks pour détecter les secrets potentiellement exposés dans le code. [#3699](https://github.com/refugies-info/karfur/pull/3699)
- Correction de plusieurs vulnérabilités de sécurité identifiées par Dependabot, notamment dans les dépendances `lodash`, `path-to-regexp` et `@smithy/config-resolver`. [#3694](https://github.com/refugies-info/karfur/pull/3694), [#3691](https://github.com/refugies-info/karfur/pull/3691) et [#3697](https://github.com/refugies-info/karfur/pull/3697)
- Simplification du pipeline de release. [#3698](https://github.com/refugies-info/karfur/pull/3698)

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés.
- Amélioration de la conformité RGAA (accessibilité) de l'application. [#3704](https://github.com/refugies-info/karfur/pull/3704)
- Suppression de suggestions invalides dans la collection `dispositifs_draft`. [#3718](https://github.com/refugies-info/karfur/pull/3718)
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs.
- Correction de problèmes liés à la gestion des variables d'environnement et des configurations.
- Nettoyage du code et refactoring de certaines parties de l'application.
