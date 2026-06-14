## Changelog : karfur (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la gestion des données, notamment l'amélioration de la détection des doublons, la structuration des données pour l'Agent Knowledge et la correction de bugs liés à l'affichage et à la sauvegarde des données. Des améliorations ont également été apportées à l'interface utilisateur, en particulier sur les fiches RCO pour les plateformes mobiles.

### Évolutions fonctionnelles
- Correction de bugs d'affichage sur les fiches RCO sur Android et iOS [#3792](https://github.com/refugies-info/karfur/pull/3792).
- Correction d'un bug empêchant la prévisualisation des fiches [#3798](https://github.com/refugies-info/karfur/pull/3798).
- Correction d'un problème de connexion et de réinitialisation de mot de passe [#3789](https://github.com/refugies-info/karfur/pull/3789).
- Amélioration de l'affichage des adresses postales sur les fiches RCO, notamment sur mobile [#3778](https://github.com/refugies-info/karfur/pull/3778).
- Correction de l'affichage des accents dans le moteur de recherche [#3769](https://github.com/refugies-info/karfur/pull/3769).
- Mise à jour des mentions légales sur le site et l'application [#3785](https://github.com/refugies-info/karfur/pull/3785).
- Ajout de la possibilité de supprimer les contenus RCO de l'interface de traduction pour éviter les erreurs [#3780](https://github.com/refugies-info/karfur/pull/3780).

### Évolutions techniques
- Implémentation d'un endpoint pour la détection de doublons d'agents [#3754](https://github.com/refugies-info/karfur/pull/3754).
- Structuration des données pour le corpus documentaire de l'Agent Knowledge (création de la structure, exportation et normalisation des ressources documentaires, configuration de l'indexation QMD) [#3788](https://github.com/refugies-info/karfur/pull/3788), [#3786](https://github.com/refugies-info/karfur/pull/3786), [#3782](https://github.com/refugies-info/karfur/pull/3782), [#3779](https://github.com/refugies-info/karfur/pull/3779).
- Amélioration de la gestion des erreurs et des valeurs nulles dans le code serveur.
- Mise à jour des dépendances et correction de vulnérabilités de sécurité.
- Ajout de tests et de validations pour améliorer la qualité du code.
- Amélioration de la performance et de la robustesse de l'application.

### Autres changements
- Documentation des structures de données et des nouveaux endpoints.
- Nettoyage du code et refactoring de certaines parties de l'application.
- Corrections de coquilles et améliorations de la lisibilité du code.
- Ajout de hooks GitLeaks pour la détection de secrets dans le code.
- Mise à jour de la version de l'application à 2.8.0.
