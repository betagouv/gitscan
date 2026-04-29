## Changelog : karfur (30 derniers jours, au 22 avril 2026)

### Résumé
Cette période a été marquée par des corrections de bugs et des améliorations de la stabilité, notamment concernant la gestion des données des opérateurs AGIR, des dispositifs et des traductions. Des efforts ont également été déployés pour améliorer la sécurité en corrigeant des vulnérabilités et en ajoutant des outils de détection de secrets. Enfin, des optimisations de performance ont été apportées à la base de données.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'envoi des fiches à traduire. [#3712](https://github.com/refugies-info/karfur/pull/3712)
- Correction de l'affichage des tirets dans les infocards. [#3706](https://github.com/refugies-info/karfur/pull/3706)
- Correction de l'affichage des validations et publications dans l'interface de traduction. [#3721](https://github.com/refugies-info/karfur/pull/3721)
- Correction d'un bug lié aux coordonnées des opérateurs AGIR. [#3728](https://github.com/refugies-info/karfur/pull/3728)
- Correction d'un bug lié aux informations de contact de l'AFND dans le département de la Marne. [#3731](https://github.com/refugies-info/karfur/pull/3731)
- Amélioration de la gestion des participants nuls pour éviter les erreurs. [#3722](https://github.com/refugies-info/karfur/pull/3722)

### Évolutions techniques
- Mise à jour de React en version 19.1.0 et mise à jour des snapshots. [#3650](https://github.com/refugies-info/karfur/pull/3650)
- Ajout d'un outil de détection de secrets (GitLeaks) au pre-commit hook. [#3699](https://github.com/refugies-info/karfur/pull/3699)
- Correction de vulnérabilités de sécurité dans les dépendances (next, axios, vite, lodash). [#3714](https://github.com/refugies-info/karfur/pull/3714), [#3694](https://github.com/refugies-info/karfur/pull/3694), [#3691](https://github.com/refugies-info/karfur/pull/3691)
- Ajout d'index MongoDB pour améliorer les performances des requêtes sur les logs, indicateurs et dispositifs. [#3710](https://github.com/refugies-info/karfur/pull/3710)
- Optimisation de la récupération du nombre de traducteurs actifs. [#3711](https://github.com/refugies-info/karfur/pull/3711)
- Refactoring de la gestion des Mongoose Maps pour éviter les erreurs d'autosave. [#3725](https://github.com/refugies-info/karfur/pull/3725), [#3721](https://github.com/refugies-info/karfur/pull/3721)
- Simplification du pipeline de release. [#3698](https://github.com/refugies-info/karfur/pull/3698)

### Autres changements
- Mise à jour de la déclaration d'accessibilité pour indiquer une conformité partielle. [#3686](https://github.com/refugies-info/karfur/pull/3686)
- Amélioration de la documentation et du code pour la gestion des erreurs.
- Correction de problèmes de typage et de formatage du code.
- Mise à jour des commentaires et de la documentation.
- Suppression de code inutile et nettoyage du code.
- Ajout d'un skill pour l'investigation des erreurs serveur. [#3670](https://github.com/refugies-info/karfur/pull/3670)
