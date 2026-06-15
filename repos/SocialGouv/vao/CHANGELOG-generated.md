## Changelog : vao (30 derniers jours, au 11 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité et de la robustesse de l'application, notamment au niveau des formulaires de renouvellement d'agrément et de la gestion des représentants légaux. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des évolutions techniques pour améliorer la qualité du code et les tests.

### Évolutions fonctionnelles
- Correction de la validation de la date du certificat lors du renouvellement d'agrément [#1386](https://github.com/SocialGouv/vao/issues/1386).
- Amélioration de l'accessibilité de l'étape 1 du formulaire de renouvellement, notamment pour les erreurs liées aux représentants légaux [#1383](https://github.com/SocialGouv/vao/issues/1383).
- Correction du rafraîchissement du formulaire de renouvellement d'agrément [#1397](https://github.com/SocialGouv/vao/issues/1397).
- Ajout du contrôle des représentants légaux dans le processus de renouvellement d'agrément (OVA) [#1379](https://github.com/SocialGouv/vao/issues/1379).
- Correction d'un bug empêchant le bouton "fusager" d'être activé correctement dans certains cas [#1388](https://github.com/SocialGouv/vao/issues/1388).
- Normalisation des noms de fichiers uploadés en supprimant les caractères spéciaux [#1389](https://github.com/SocialGouv/vao/issues/1389).
- Correction d'un problème d'affichage des informations de la personne physique [#1388](https://github.com/SocialGouv/vao/issues/1388).
- Correction de la validation des étapes 3 et 4 du processus de renouvellement [#1381](https://github.com/SocialGouv/vao/issues/1381).
- Correction du renouvellement de procès-verbal [#1378](https://github.com/SocialGouv/vao/issues/1378).
- Ajout de la possibilité de renvoyer le code OTP et validation du nombre de tentatives [#1387](https://github.com/SocialGouv/vao/issues/1387) et [#1396](https://github.com/SocialGouv/vao/issues/1396).
- Correction d'un problème d'agrément valide après renouvellement [#1398](https://github.com/SocialGouv/vao/issues/1398).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : NestJS (10.4.22), Nodemailer (v8.0.7), Knex (v3.2.10), Axios (1.16.1), ts-jest (29.4.10), Multer (2.1.1), Nuxt (3.21.6), @aws-sdk/client-s3 (3.1045.0).
- Amélioration de la configuration des tests E2E, notamment avec des filtres pour assurer la visibilité des éléments testés [#1365](https://github.com/SocialGouv/vao/issues/1365), [#1364](https://github.com/SocialGouv/vao/issues/1364), [#1349](https://github.com/SocialGouv/vao/issues/1349).
- Refactoring du code et suppression de code dupliqué.
- Amélioration de la configuration ESLint et ajout de tests de couverture.
- Augmentation des ressources CPU et mémoire allouées au service PostgreSQL CNPG [#1362](https://github.com/SocialGouv/vao/issues/1362).
- Configuration du timeout des requêtes SQL sur CNPG PostgreSQL [#1363](https://github.com/SocialGouv/vao/issues/1363).
- Mise à jour de la configuration de build TypeScript.
- Utilisation de pnpm catalog.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes mineurs d'accessibilité (RGAA) sur différentes étapes des formulaires.
- Suppression de la catégorie de fichiers "MOTIVATION".
- Correction de problèmes de scroll sur l'onglet agrément DREETS.
- Mise à jour de la migration pour la suppression d'un enum.
