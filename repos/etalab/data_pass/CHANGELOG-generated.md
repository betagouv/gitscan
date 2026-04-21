## Changelog : data_pass (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de la gestion des utilisateurs (ajout de bannissement, gestion des droits), l'enrichissement des fonctionnalités pour les formulaires (Extenso, API Particulier, Solis) et des corrections de bugs pour une meilleure stabilité et expérience utilisateur. Des améliorations techniques ont également été apportées, notamment au niveau des tests et de l'infrastructure.

### Évolutions fonctionnelles
- **Gestion des utilisateurs :** Ajout de la possibilité de bannir un utilisateur administrateur, bloquant ainsi son accès à l'application et aux sessions actives. [#1508](https://github.com/etalab/data_pass/pull/1508)
- **Formulaire Extenso :** Ajout du bloc "modalités" au formulaire Extenso, permettant une configuration plus fine des habilitations. [#1467](https://github.com/etalab/data_pass/pull/1467), [#1472](https://github.com/etalab/data_pass/pull/1472)
- **API Particulier :** Activation des scopes `men_statut_boursier` et `men_echelon_bourse` pour le formulaire API Particulier. [#1473](https://github.com/etalab/data_pass/pull/1473)
- **Formulaire Solis :** Rendre les scopes `cnaf_adresse` et `cnaf_enfants` cochables pour le formulaire Solis. [#1502](https://github.com/etalab/data_pass/pull/1502)
- **Notifications :** Les managers reçoivent désormais les notifications de messages. [#1468](https://github.com/etalab/data_pass/pull/1468)
- **Amélioration des URLs :** Utilisation des IDs numériques des autorisations dans les URLs pour une meilleure lisibilité et performance. [#1498](https://github.com/etalab/data_pass/pull/1498)
- **Gestion des droits :** Possibilité de retirer entièrement les droits d'un utilisateur disposant déjà de droits. [#1484](https://github.com/etalab/data_pass/pull/1484)
- **CGU :** Correction de l'affichage de la checkbox CGU pour les types d'habilitation dynamiques. [#1491](https://github.com/etalab/data_pass/pull/1491)

### Évolutions techniques
- **CI/CD :** Optimisation de la configuration CI pour accélérer l'exécution des tests (parallélisation, utilisation de caches). [#1503](https://github.com/etalab/data_pass/pull/1503), [#1513](https://github.com/etalab/data_pass/pull/1513)
- **Refactoring :** Refactorisation de la suppression de `HabilitationType` pour utiliser un interactor. [#1462](https://github.com/etalab/data_pass/pull/1462)
- **Mise à jour Rails :** Mise à jour de Rails vers la version 8.1.2.1. [#1460](https://github.com/etalab/data_pass/pull/1460)
- **Historique :** Ajout d'un type d'événement d'historique pour les mises à jour. [#1493](https://github.com/etalab/data_pass/pull/1493)
- **Traces :** Ajout d'AdminChange pour tracer les changements faits par des admins. [#1494](https://github.com/etalab/data_pass/pull/1494)
- **Tests :** Ajout d'un test de non-régression pour la boucle de redirection sur dates d'homologation identiques.

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant les rôles. [#1471](https://github.com/etalab/data_pass/pull/1471)
- **Documentation Webhooks :** Ajout d'une page de documentation sur les webhooks.
- **Amélioration des emails :** Rendre les URLs cliquables dans les emails et envoyer des emails à des personnes spécifiques pour les approbations DGFIP. [#1511](https://github.com/etalab/data_pass/pull/1511), [#1505](https://github.com/etalab/data_pass/pull/1505)
- **Correction de typos :** Correction de typos dans les sujets des emails. [#1506](https://github.com/etalab/data_pass/pull/1506)
- **Correction de bug :** Correction d'une boucle de redirection sur les dates d'homologation. [#1469](https://github.com/etalab/data_pass/pull/1469)
- **Correction de bug :** Correction d'un problème de chargement de documents API PFC. [#1464](https://github.com/etalab/data_pass/pull/1464)
- **Correction de bug :** Correction d'un problème de N+1 queries sur le dashboard. [#1499](https://github.com/etalab/data_pass/pull/1499)
- **Correction de bug :** Correction d'un problème de silent 422 sur la soumission de la requête d'autorisation depuis la page de résumé. [#1505](https://github.com/etalab/data_pass/pull/1505)
