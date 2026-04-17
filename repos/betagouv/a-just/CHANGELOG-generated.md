## Changelog : a-just (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la qualité du code, notamment via des mises à jour de dépendances et des corrections de bugs. Des améliorations ont également été apportées à l'interface utilisateur, en particulier concernant l'affichage des données et la gestion des stocks. Des ajustements de sécurité et de configuration ont également été effectués.

### Évolutions fonctionnelles
- Correction d'un bug concernant la propagation de la valeur du stock calculé lors de la suppression d'une saisie sur un stock "à vérifier" hérité du mois précédent. [#522](https://github.com/betagouv/a-just/pull/522)
- Amélioration de la visualisation des dernières données dans le cockpit.
- Correction du calcul de l'EPT saisi.
- Correction de l'importation des agents EAM.
- Ajout d'infobulles d'informations pour les alertes concernant les commentaires des agents.
- Correction de la date de fin d'historique.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Axios, TypeScript, divers modules Node.js (lodash, yaml, karma), Angular, et les dépendances de développement.
- Refonte de la configuration du build front-end.
- Suppression de Babel-cli et de Compodoc.
- Mise à jour des actions GitHub.
- Suppression de precommit.
- Amélioration de la gestion des fichiers `package-lock.json`.
- Suppression de `koa-smart` et création d'une version personnalisée.
- Suppression de la configuration de formatage des dates.
- Suppression des règles de sécurité inutiles.
- Modification des permissions des workflows GitHub.

### Autres changements
- Correction de la ventilation des dates par référentiel pour les enfants.
- Suppression de la documentation temporaire.
- Nettoyage du code `koa-smart`.
- Correction de la configuration du Dockerfile pour l'environnement E2E.
- Mise à jour de la version du projet.
- Amélioration des tests E2E (mise à jour de la méthode Cypress.env()).
- Correction de l'affichage des CGU.
- Suppression d'un nombre aléatoire utilisé pour la sécurité des mots de passe.
