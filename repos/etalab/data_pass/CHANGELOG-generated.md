## Changelog : data_pass (30 derniers jours, au 27 juillet 2026)

### Résumé
Les dernières mises à jour de DataPass se concentrent sur l'ajout de nouveaux éditeurs et formulaires API, l'amélioration de la gestion des autorisations FranceConnect, et des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et l'introduction d'un système de Feature Flags.

### Évolutions fonctionnelles
- Ajout de l'éditeur Hoptis Software et de ses deux formulaires API Particulier. [#1682](https://github.com/etalab/data_pass/issues/1682)
- Ajout d'un nouveau type de formulaire : API Particulier via Démarche numérique. [#1682](https://github.com/etalab/data_pass/issues/1682)
- Ajout de l’éditeur Familea et renommage de ses solutions logicielles (Diabolo et Mikado). [#1703](https://github.com/etalab/data_pass/issues/1703)
- Ajout de l'éditeur d'enfance et de petite enfance. [#1698](https://github.com/etalab/data_pass/issues/1698)
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis réversion en raison de problèmes). [#1667](https://github.com/etalab/data_pass/issues/1667)
- Ajout du scope `allocation_rentree_scolaire` pour les aides facultatives. [#1676](https://github.com/etalab/data_pass/issues/1676)
- Amélioration des wordings pour la proactivité concernant les étudiants boursiers. [#1697](https://github.com/etalab/data_pass/issues/1697)
- Correction d'une majuscule dans le nom "DDmariage". [#1699](https://github.com/etalab/data_pass/issues/1699)
- Amélioration de la gestion de la durée de vie des sessions FranceConnect, fixée à 12 heures. [#1657](https://github.com/etalab/data_pass/issues/1657)
- Ajout d'une page temporaire pour les emails de définition. [#1674](https://github.com/etalab/data_pass/issues/1674)
- Ajout de breadcrumbs pour une meilleure navigation. [#1673](https://github.com/etalab/data_pass/issues/1673)
- Amélioration de l'intro des services CISIRH. [#1685](https://github.com/etalab/data_pass/issues/1685)

### Évolutions techniques
- Introduction d'un système de Feature Flags centralisé avec documentation.
- Correction d'un problème de shadowing des requêtes UserAlertsComponent. [#1656](https://github.com/etalab/data_pass/issues/1656)
- Correction d'un bug lié au restore d'autorisation et au form_uid. [#1655](https://github.com/etalab/data_pass/issues/1655)
- Mise à jour de plusieurs dépendances (actions/cache, actions/checkout, rubocop, yard, aws-sdk-s3, rails_pulse, etc.).
- Mise à jour des actions GitHub (docker/build-push-action, docker/setup-buildx-action).

### Autres changements
- Refonte des cadres juridiques API Particulier pour une factorisation et une uniformisation. [#1605](https://github.com/etalab/data_pass/issues/1605)
- Nettoyage du code et amélioration de la configuration.
- Suppression de la purge de `france_connect_authorization_id` lors du retrait de la modalité FranceConnect.
- Correction du wording de la date de transmission pour CNOUS.
