## Changelog : a-just (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la maintenance du projet. Des corrections ont été apportées à la gestion des stocks, notamment lors de la propagation des données. Des mises à jour importantes des dépendances ont également été effectuées pour assurer la sécurité et la performance de l'application. Des améliorations ont été apportées à l'interface utilisateur, notamment au niveau de la visualisation des données et de la gestion des dates.

### Évolutions fonctionnelles
- Correction d'un bug concernant la propagation de la valeur du stock calculé lors de la confirmation d'un stock "à vérifier" hérité du mois précédent. [#522](https://github.com/betagouv/a-just/pull/522)
- Amélioration de la visualisation des dernières données dans le cockpit, avec une correction de l'affichage des données et suppression des doublons.
- Correction de la date de fin d'historique.
- Correction de l'importation des agents EAM.
- Correction de l'affichage des dates de début et de fin.

### Évolutions techniques
- Mise à jour des dépendances : Axios, lodash, yaml, karma, TypeScript, Angular (côté administration), et des modules de base de données.
- Suppression de Babel-cli, esdoc et compodoc pour alléger et simplifier l'environnement de développement.
- Refonte de la configuration de construction (build) du projet.
- Amélioration de la gestion des fichiers `package-lock.json` pour assurer la cohérence des dépendances.
- Suppression de `precommit` et remplacement par une configuration plus simple.
- Mise à jour des actions GitHub pour améliorer le workflow CI/CD.
- Suppression de la génération aléatoire de nombres pour renforcer la sécurité des mots de passe.
- Suppression de la configuration de formatage des données.
- Suppression de l'utilisation de `koa-smart` et création d'une version personnalisée.

### Autres changements
- Suppression de la documentation temporaire.
- Nettoyage du code et suppression des commentaires inutiles.
- Modification des permissions des workflows GitHub.
- Correction de la configuration Docker pour l'environnement d'end-to-end (E2E).
- Mise à jour de la configuration TypeScript pour les tests E2E.
- Modification de la méthode d'accès aux variables d'environnement dans les tests Cypress.
- Ajout d'options et de packages optionnels.
- Correction de la configuration de construction front-end.
- Ajout de tests lors des changements de script de construction.
- Mise à jour de la version du projet.
- Modification du template CA.
- Changement d'affectation de l'ATJ.
