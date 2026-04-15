## Changelog : a-just (30 derniers jours, au 15 avril 2026)

### Résumé
Les dernières mises à jour d'a-just se concentrent sur l'amélioration de la stabilité et de la correction de bugs, notamment concernant la gestion des stocks et l'affichage des données. Des efforts ont également été déployés pour moderniser les dépendances du projet et améliorer la sécurité. Des ajustements ont été faits sur l'interface utilisateur pour améliorer l'expérience utilisateur, notamment au niveau des informations contextuelles et des dates.

### Évolutions fonctionnelles
- Correction d'un bug concernant la propagation de la valeur du stock calculé lors de la suppression d'une saisie sur un stock "à vérifier" hérité du mois précédent. [#522](https://github.com/betagouv/a-just/pull/522)
- Amélioration de l'affichage des dernières données dans le cockpit, notamment en forçant la recréation du canvas et en supprimant les doublons dans les tooltips.
- Correction du calcul de l'EPT saisi.
- Correction de l'import des agents EAM.
- Correction de l'affichage de la date de fin d'historique.

### Évolutions techniques
- Mise à jour de nombreuses dépendances du projet (Node.js, PostgreSQL, Axios, TypeScript, Angular, Lodash, YAML, Karma, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Refonte de la configuration du build pour le front-end.
- Suppression de `babel-cli` et `esdoc` de `koa-smart`.
- Suppression de `precommit`.
- Mise à jour des actions GitHub.
- Suppression de la configuration de formatage des dates.
- Création d'un `koa-smart` personnalisé.
- Suppression de la documentation temporaire.
- Suppression de la configuration de sécurité avec un nombre aléatoire pour les mots de passe.
- Suppression de la configuration de `compodoc` et remplacement par des scripts en ligne.
- Suppression de la configuration de `vendor koa smart` pour la sandbox.

### Autres changements
- Modification des permissions des workflows GitHub.
- Ajout d'options et de packages optionnels.
- Mise à jour du fichier `package-lock.json`.
- Ajout d'une infobulle d'information pour les commentaires des agents.
- Correction des CGU.
- Amélioration des logs de débogage pour les tests E2E.
- Mise à jour de la configuration de TypeScript pour les tests E2E.
- Modification de la méthode d'accès aux variables d'environnement dans les tests Cypress.
- Correction du Dockerfile pour les tests E2E.
- Ajout de commentaires et corrections dans le Dockerfile pour les tests E2E.
