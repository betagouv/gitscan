## Changelog : data_pass (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se sont concentrées sur l'amélioration de l'expérience utilisateur, notamment en matière de recherche et de gestion des droits, ainsi que sur l'ajout de nouvelles fonctionnalités comme la gestion des clés API et l'intégration avec HubEE pour des démarches spécifiques. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la recherche d'utilisateurs et de la gestion des droits [#1608](https://github.com/etalab/data_pass/pull/1608).
- Ajout de la possibilité pour les développeurs de créer et supprimer leurs propres clés API [#1618](https://github.com/etalab/data_pass/pull/1618).
- Affichage des demandes validées dans les résultats de recherche par ID [#1619](https://github.com/etalab/data_pass/pull/1619).
- Mise à jour de la durée moyenne de réponse pour refléter le calcul statistique correct [#1622](https://github.com/etalab/data_pass/pull/1622).
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis révertée en raison de problèmes) [#1667](https://github.com/etalab/data_pass/pull/1667), [#1646](https://github.com/etalab/data_pass/pull/1646).
- Possibilité de définir plusieurs templates de cas d'usage pour un même formulaire [#1604](https://github.com/etalab/data_pass/pull/1604).
- Mise à jour du lien vers les CGU des services CISIRH [#1621](https://github.com/etalab/data_pass/pull/1621).
- Amélioration de la gestion de session avec une durée réduite à 12 heures et un plafonnement à 24 heures [#1679](https://github.com/etalab/data_pass/pull/1679).
- Ajout d'un message flash informant de l'expiration de la session lors de la déconnexion forcée [#1635](https://github.com/etalab/data_pass/pull/1635).
- Possibilité de s'inscrire facilement via un lien chiffré dans un email [#1606](https://github.com/etalab/data_pass/pull/1606).

### Évolutions techniques
- Ajout d'un module de gestion des *feature flags* centralisé [#1631](https://github.com/etalab/data_pass/pull/1631).
- Migration du scope TVA de VIES vers la DGFIP [#1629](https://github.com/etalab/data_pass/pull/1629).
- Refactorings et améliorations du code liés à l'intégration avec CNOUS [#1626](https://github.com/etalab/data_pass/pull/1626).
- Correction de problèmes de concurrence (races) dans les tests Cucumber [#1608](https://github.com/etalab/data_pass/pull/1608).
- Amélioration de la documentation concernant l'authentification ProConnect [#1622](https://github.com/etalab/data_pass/pull/1622).
- Mise à jour des dépendances (Docker, Actions GitHub, Faraday, Rubocop, etc.).

### Autres changements
- Correction de liens brisés vers la documentation Swagger [#1623](https://github.com/etalab/data_pass/pull/1623).
- Amélioration des wordings pour le cas d'usage EAJE [#1647](https://github.com/etalab/data_pass/pull/1647).
- Suppression d'une ligne de code inutile causant des problèmes de suppression de droits [#1634](https://github.com/etalab/data_pass/pull/1634).
- Amélioration de la gestion des erreurs et de la validation des données CNOUS [#1633](https://github.com/etalab/data_pass/pull/1633).
- Correction de la vocalisation et du focus sur les champs de saisie des codes INSEE pour une meilleure accessibilité [#1626](https://github.com/etalab/data_pass/pull/1626).
