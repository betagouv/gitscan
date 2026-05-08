## Changelog : data_pass (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de fonctionnalités pour la gestion des droits d'accès, l'amélioration de la navigation et la correction de bugs. Des efforts ont également été faits pour améliorer la documentation et la robustesse du code, ainsi que pour faciliter l'intégration avec d'autres systèmes via des webhooks.

### Évolutions fonctionnelles
- Ajout d'une interface pour bannir des utilisateurs ([#1508](https://github.com/etalab/data_pass/pull/1508)).
- Amélioration de l'affichage du statut des demandes (revendiqué/non revendiqué) [#1539](https://github.com/etalab/data_pass/pull/1539).
- Suppression du compteur de longlet "Demandes" pour les instructeurs [#1538](https://github.com/etalab/data_pass/pull/1538).
- Ajout d'un bouton "Précédent" à l'étape de traitement des données personnelles [#1542](https://github.com/etalab/data_pass/pull/1542).
- Amélioration du message affiché lors de la soumission sans modification [#1541](https://github.com/etalab/data_pass/pull/1541).
- Ajout d'informations sur les services CISIRH [#1546](https://github.com/etalab/data_pass/pull/1546), [#1545](https://github.com/etalab/data_pass/pull/1545), [#1543](https://github.com/etalab/data_pass/pull/1543).
- Amélioration de l'affichage des scopes et des groupes de scopes pour les services CISIRH.
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur [#1494](https://github.com/etalab/data_pass/pull/1494).
- Ajout d'un lien vers la création d'une demande dans la liste des demandes [#1487](https://github.com/etalab/data_pass/pull/1487).
- Amélioration du comportement de l'application lorsque les CGU sont vides [#1491](https://github.com/etalab/data_pass/pull/1491).
- Suppression de la ligne au-dessus des scopes sans groupes dans le formulaire [#1486](https://github.com/etalab/data_pass/pull/1486).
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API v1 [#1523](https://github.com/etalab/data_pass/pull/1523).
- Amélioration de la gestion des erreurs lors de la soumission d'une demande [#1505](https://github.com/etalab/data_pass/pull/1505).
- Ajout d'un accusé de réception de dépôt de demande [#1536](https://github.com/etalab/data_pass/pull/1536).
- Ajout de la possibilité de créer des demandes via l'API (écriture) [#1504](https://github.com/etalab/data_pass/pull/1504).

### Évolutions techniques
- Refactorisation de la gestion des événements et des changelogs.
- Amélioration des performances en corrigeant des requêtes N+1 sur le dashboard [#1506](https://github.com/etalab/data_pass/pull/1506).
- Ajout de webhooks pour les événements liés aux organisations (payload INSEE) [#1512](https://github.com/etalab/data_pass/pull/1512).
- Mise à jour de la gestion des slugs pour les HabilitationType [#1481](https://github.com/etalab/data_pass/pull/1481).
- Amélioration de la robustesse de l'application en gérant les erreurs de connexion [#1531](https://github.com/etalab/data_pass/pull/1531).
- Amélioration de la gestion des erreurs et des exceptions.
- Optimisation du CI/CD pour réduire le temps d'exécution des tests [#1503](https://github.com/etalab/data_pass/pull/1503).
- Mise à jour des dépendances (Rails Pulse, Rubocop, etc.).
- Ajout de tests contractuels pour garantir la cohérence des définitions.

### Autres changements
- Réorganisation de la documentation en sous-dossiers (technique, métier, API particulier) [#1549](https://github.com/etalab/data_pass/pull/1549).
- Ajout de la documentation du système HabilitationType dynamique [#1548](https://github.com/etalab/data_pass/pull/1548).
- Ajout de tutoriels pour les développeurs.
- Amélioration de la lisibilité du code et des messages d'erreur.
- Correction de typos et amélioration de la qualité de la documentation.
- Ajout de guidelines pour la co-authoring des commits.
- Mise à jour des wordings pour la tarification Eaje [#1497](https://github.com/etalab/data_pass/pull/1497).
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
