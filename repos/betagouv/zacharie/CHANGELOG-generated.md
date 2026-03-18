## Changelog : zacharie (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives, notamment au niveau de l'interface d'administration, de la gestion des carcasses et de la synchronisation des données hors ligne. Des corrections de sécurité importantes ont également été apportées pour protéger les données des utilisateurs. Enfin, l'expérience utilisateur a été améliorée grâce à l'ajout d'une FAQ et d'une meilleure gestion de l'affichage sur mobile.

### Évolutions fonctionnelles
- Ajout d'une page FAQ avec des guides et des liens de navigation pour aider les utilisateurs. [#201](https://github.com/betagouv/zacharie/issues/201)
- Amélioration de l'interface d'administration pour une meilleure gestion des carcasses intermédiaires et des rôles circuit court. [#226](https://github.com/betagouv/zacharie/issues/226), [#230](https://github.com/betagouv/zacharie/issues/230), [#232](https://github.com/betagouv/zacharie/issues/232)
- Possibilité d'envoyer des carcasses à plusieurs destinataires. [#188](https://github.com/betagouv/zacharie/issues/188)
- Amélioration de la gestion de la transmission des carcasses, notamment en clôturant automatiquement les fiches circuit court lors de la transmission. [#200](https://github.com/betagouv/zacharie/issues/200)
- Amélioration de l'affichage sur mobile et adaptation de l'interface. [#184](https://github.com/betagouv/zacharie/issues/184)
- Possibilité d'éditer le nom de l'inspecteur. [#212](https://github.com/betagouv/zacharie/issues/212)
- Amélioration de la gestion des dates de mise à mort. [#221](https://github.com/betagouv/zacharie/issues/221)

### Évolutions techniques
- Correction de plusieurs vulnérabilités XSS pour améliorer la sécurité de l'application.
- Amélioration du chargement des entités et des utilisateurs pour optimiser les performances.
- Refonte de la synchronisation des données hors ligne. [#202](https://github.com/betagouv/zacharie/issues/202)
- Mise à jour des dépendances (minimatch, @getbrevo/brevo, ajv, tar).
- Amélioration de la structure du code et refactoring de certains composants.
- Ajout de tests pour améliorer la couverture et la qualité du code.
- Amélioration de la gestion du cache dans l'administration.

### Autres changements
- Simplification de l'importation de code CCG. [#234](https://github.com/betagouv/zacharie/issues/234)
- Correction de l'affichage des homonymes de villes.
- Amélioration de la formulation de certains textes dans l'interface utilisateur. [#216](https://github.com/betagouv/zacharie/issues/216), [#210](https://github.com/betagouv/zacharie/issues/210), [#205](https://github.com/betagouv/zacharie/issues/205), [#197](https://github.com/betagouv/zacharie/issues/197)
- Mise à jour de la documentation (README.md, CLAUDE.md).
- Correction de liens dupliqués et amélioration de la navigation.
- Suppression de code inutile et nettoyage général du code.
- Ajout d'une variable d'environnement pour la clé SENTRY.
- Correction de l'affichage des champs SVI.
- Correction de bugs divers liés à l'interface utilisateur et à la gestion des données.
