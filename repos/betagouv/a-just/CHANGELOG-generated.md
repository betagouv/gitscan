## Changelog : a-just (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la qualité du code, notamment au niveau des tests et de l'infrastructure. Des corrections ont été apportées pour assurer la propagation correcte des données de stock et des améliorations ont été faites sur l'interface utilisateur pour la visualisation des données. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Correction d'un bug concernant la propagation de la valeur du stock calculé lors de la suppression de la saisie sur un stock "à vérifier" hérité du mois précédent. [#522](https://github.com/betagouv/a-just/pull/522)
- Amélioration de la visualisation des dernières données dans le cockpit, notamment en forçant la recréation du canvas et en supprimant les doublons dans les tooltips.
- Correction de la date de fin d'historique.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Axios, Lodash, YAML, Karma, TypeScript, Angular, et les modules de base de données.
- Mise à jour des actions GitHub et du workflow GitHub Flow.
- Suppression de `babel-cli`, `esdoc` et `compodoc` pour alléger l'infrastructure.
- Refonte de la configuration de construction (build) pour le front-end.
- Amélioration de la gestion des fichiers `package-lock.json` et des versions des modules.
- Correction de tests API.
- Suppression de la configuration `precommit`.
- Modification des permissions des workflows GitHub.
- Suppression de la génération aléatoire de nombres pour la sécurité des mots de passe.
- Mise en place d'un `koa-smart` personnalisé.

### Autres changements
- Suppression de documentation temporaire.
- Nettoyage du code et suppression de commentaires inutiles.
- Ajout d'options et de packages optionnels.
- Ajout de la ventilation des dates par référentiel pour les enfants.
- Correction de la configuration de construction du front-end.
- Mise à jour des derniers modules côté front-end.
