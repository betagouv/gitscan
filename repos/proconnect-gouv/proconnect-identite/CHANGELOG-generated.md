## Changelog : proconnect-identite (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en simplifiant l'inscription pour certaines organisations et en affinant les messages d'erreur. Des travaux ont également été réalisés pour moderniser l'infrastructure et améliorer la sécurité, avec notamment la migration progressive des emails et la gestion des clients d'authentification.

### Évolutions fonctionnelles
- Simplification de l'inscription : Les petites organisations civiles et agricoles disposant d'une adresse email gratuite ne sont plus soumises à la modération lors de l'inscription. [#1972](https://github.com/proconnect-gouv/proconnect-identite/issues/1972)
- Amélioration des messages d'erreur : Ajout d'une description plus précise des erreurs OIDC renvoyées à PCF, facilitant le débogage.
- Gestion des motifs de rejet : Suppression du motif de rejet "autre" et remplacement par un message invitant l'utilisateur à consulter son email pour plus d'informations.
- Précision de l'expéditeur d'email : Ajout du nom de l'expéditeur aux emails envoyés.
- Migration des emails : Début de la migration des emails envoyés depuis MonComptePro.
- Gestion des services publics : Ajout d'une nouvelle fonction pour déterminer si une entité est un service public, avec un nouvel algorithme.

### Évolutions techniques
- Refactorisation des tests E2E : Utilisation de `before hook` pour initialiser la base de données dans les tests E2E, améliorant la performance et la fiabilité.
- Mise à jour des dépendances : Plusieurs dépendances ont été mises à jour, notamment `axios`, `moment-timezone`, `prettier`, `systeminformation`, `uuid`, `hono`, `redis`, `cypress-io/github-action` et `actions/labeler`.
- Gestion des clients d'authentification : Création d'un client d'authentification dédié pour l'environnement de pré-production PCF et mise à jour des identifiants correspondants.
- Publication du package RNE : Le package RNE est maintenant public.
- Amélioration de la compatibilité : Ajout d'une compatibilité ascendante pour l'algorithme `is-service-public`.
- Correction de types : Correction d'un problème d'importation de types pour PostgreSQL dans les contextes.
- Formatage des données : Amélioration du formatage des données issues du script Grist.
- Correction d'un bug d'apostrophe : Correction d'un bug lié à l'apostrophe.
- Correction d'un bug lié à l'URL : Ajout de `encodeURIComponent` pour améliorer la concaténation d'URL.

### Autres changements
- Documentation : Mise à jour de la documentation pour refléter les changements apportés.
- Workflow CI/CD : Ajout d'un workflow dispatch pour faciliter l'exécution manuelle des tâches.
- Ajout d'un script pour mettre à jour la liste des administrations depuis Grist.
- Ajout d'un script pour exécuter localement la mise à jour des données de l'annuaire des entreprises.
- Correction d'un problème de versionnement des packages.
- Revert d'une mise à jour de Node.js qui causait des problèmes.
