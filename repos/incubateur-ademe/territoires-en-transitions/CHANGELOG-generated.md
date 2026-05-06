## Changelog : territoires-en-transitions (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la plateforme, notamment au niveau des sauvegardes et de la gestion des données. Des optimisations ont été apportées à la génération de rapports et à l'interface utilisateur, en particulier pour les plans d'actions et les indicateurs. L'équipe a également travaillé sur la personnalisation des référentiels et l'intégration avec des outils externes comme Calendly et Airtable.

### Évolutions fonctionnelles
- **Rapports :** Ajout de la dernière note dans les rapports et correction du tri des fiches. Les objectifs de la collectivité sont désormais inclus dans les graphes du PCAET. [#4258d03](https://github.com/incubateur-ademe/territoires-en-transitions/commit/4258d03)
- **Plans d'actions :** Les contributeurs pilotes peuvent désormais créer, modifier et supprimer des sous-actions. [#e2e6673](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e2e6673)
- **Personnalisation des référentiels :**  Implémentation de la personnalisation dans le backend, avec une interface de réponse remaniée et un bandeau intégré aux pages des sous-mesures. Les mesures désactivées par la personnalisation sont désormais masquées dans l'interface. [#c5a5e91](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c5a5e91)
- **Export PDF :** Génération des PDF désormais effectuée côté backend via tRPC. [#68aec1c](https://github.com/incubateur-ademe/territoires-en-transitions/commit/68aec1c)
- **Collectivités :** Correction de la recherche de collectivités. [#64956a6](https://github.com/incubateur-ademe/territoires-en-transitions/commit/64956a6)
- **Synchronisation Calendly/Airtable :** Amélioration de la synchronisation entre Calendly et Airtable. [#e110cf0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e110cf0)
- **Interface Utilisateur :** Amélioration de l'ergonomie de l'EDL avec l'utilisation d'un side panel. Correction de la pagination de la page Actualités.

### Évolutions techniques
- **Refactoring :** Refactorisation de l'historique des référentiels pour utiliser le backend plutôt qu'un accès direct à Supabase. [#8005748](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8005748)
- **Architecture :** Migration de certaines mutations de fiches et endpoints vers tRPC pour améliorer la performance et la maintenabilité. [#0ec6066](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0ec6066)
- **Base de données :** Ajout d'index sur les tables d'historique pour optimiser les requêtes. [#b9d106d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b9d106d)
- **Tests :** Amélioration de l'isolation des tests avec la création d'utilisateurs et collectivités de test, et parallélisation des tests. [#952f739](https://github.com/incubateur-ademe/territoires-en-transitions/commit/952f739)
- **CI/CD :** Ajout de scripts de backup et restore. [#89c01cf](https://github.com/incubateur-ademe/territoires-en-transitions/commit/89c01cf)
- **Déploiement :** Ajout du dashboard privé streamlit dans le healthcheck et création d'un cronjob pour vérifier la page des stats.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Configuration :** Mise à jour de l'adresse d'envoi d'email. [#1e2a780](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1e2a780)
- **Nettoyage de code :** Suppression de code obsolète et simplification de certaines parties du code.
- **Typographie :** Correction de typos. [#802d5f1](https://github.com/incubateur-ademe/territoires-en-transitions/commit/802d5f1)
- **Mise à jour des dépendances :** Suppression des dépendances inutiles et mise à jour des dépendances existantes.
