## Changelog : a-just (30 derniers jours, au 01 Juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout d'un système de feedback intégré, des améliorations de la gestion des dates et des corrections de bugs. Des efforts ont également été faits pour améliorer la stabilité des tests automatisés et la configuration de l'environnement de développement. Des améliorations ont été apportées au cockpit et à la gestion des données, notamment pour les référentiels et les effectifs.

### Évolutions fonctionnelles
- Ajout d'un système de feedback utilisateur permettant aux utilisateurs de donner une note (1 à 5 étoiles) et un commentaire sur l'application. Une pop-in de feedback s'affiche automatiquement après un mois d'utilisation. [#89024c55](https://github.com/betagouv/a-just/commit/89024c55)
- Amélioration de la gestion des dates dans la fonctionnalité "Situation à prendre en compte" : la date d'arrivée est désormais renseignée par défaut, tout en permettant une modification indépendante. [#aa0879f8](https://github.com/betagouv/a-just/commit/aa0879f8)
- Possibilité de saisir manuellement les dates via un champ de texte dans les composants `aj-date-select` et `aj-date-select-blue`, en complément du sélecteur de date. [#761752ed](https://github.com/betagouv/a-just/commit/761752ed)
- Amélioration de la duplication d'agents et de la synchronisation des origines. [#dd034c15](https://github.com/betagouv/a-just/commit/dd034c15)
- Ajout de la possibilité de dupliquer les situations actuelles. [#0f3dbfdc](https://github.com/betagouv/a-just/commit/0f3dbfdc)
- Mise à jour des fichiers de nomenclature. [#09f0d356](https://github.com/betagouv/a-just/commit/09f0d356)

### Évolutions techniques
- Refactorisation des tests E2E pour utiliser la nouvelle fonctionnalité de saisie manuelle de date. [#57939669](https://github.com/betagouv/a-just/commit/57939669)
- Mise à jour de la configuration Cypress pour utiliser `cy.env` au lieu de `Cypress.env`. [#e67c7077](https://github.com/betagouv/a-just/commit/e67c7077)
- Refactorisation du workflow GitHub Actions pour simplifier les étapes de déploiement. [#2ce96a06](https://github.com/betagouv/a-just/commit/2ce96a06)
- Correction de problèmes de type dans les requêtes Sequelize. [#ec31cd51](https://github.com/betagouv/a-just/commit/ec31cd51)
- Suppression de fichiers et de code inutilisés (sandbox, commentaires, logs). [#8223a9b1](https://github.com/betagouv/a-just/commit/8223a9b1), [#32a0f972](https://github.com/betagouv/a-just/commit/32a0f972), [#a9b5435b](https://github.com/betagouv/a-just/commit/a9b5435b)
- Mise à jour de l'extracteur-collecte. [#12fdf48f](https://github.com/betagouv/a-just/commit/12fdf48f)

### Autres changements
- Amélioration du style de la page d'administration des feedbacks. [#e64e5cd0](https://github.com/betagouv/a-just/commit/e64e5cd0)
- Correction de bugs mineurs et améliorations de la qualité du code. [#8a832abd](https://github.com/betagouv/a-just/commit/8a832abd), [#46580931](https://github.com/betagouv/a-just/commit/46580931), [#48fd46c5](https://github.com/betagouv/a-just/commit/48fd46c5), [#9ad62061](https://github.com/betagouv/a-just/commit/9ad62061)
- Ajout de tooltips au cockpit pour la visualisation des graphiques. [#ddffd4cb](https://github.com/betagouv/a-just/commit/ddffd4cb)
- Ajout de CSP security. [#88bcc8ef](https://github.com/betagouv/a-just/commit/88bcc8ef) et [#4cc7bcff](https://github.com/betagouv/a-just/commit/4cc7bcff)
- Corrections de textes et de traductions. [#76cde8dc](https://github.com/betagouv/a-just/commit/76cde8dc)
- Mise à jour du fichier excel extract collect 2026. [#216bf323](https://github.com/betagouv/a-just/commit/216bf323)
