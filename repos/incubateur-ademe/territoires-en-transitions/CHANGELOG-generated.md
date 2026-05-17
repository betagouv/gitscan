## Changelog : territoires-en-transitions (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la gestion des fiches actions et des plans, avec une migration vers une nouvelle architecture technique (tRPC) pour plus de performance et de robustesse. Des corrections de bugs et des optimisations ont également été apportées, notamment au niveau de l'import de plans et de la synchronisation des données. L'ajout d'une page publique "matrice d'impact" permet une meilleure communication sur les résultats.

### Évolutions fonctionnelles
- Ajout d'une page publique "matrice d'impact" pour présenter les résultats du projet. [#58db5f8](https://github.com/incubateur-ademe/territoires-en-transitions/commit/58db5f8)
- Amélioration de la gestion des invitations et correction d'un problème de feedback d'erreur. [#3778c2a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/3778c2a)
- Les contributeurs pilotes peuvent désormais créer, modifier et supprimer des sous-actions. [#e2e6673](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e2e6673)
- Possibilité d'ajouter la dernière note dans les rapports. [#6f4471d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6f4471d)
- Amélioration de l'interface de personnalisation des référentiels avec la gestion des questions/réponses et un bandeau intégré. [#c5a5e91](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c5a5e91)
- Correction de l'affichage des tâches dans les sous-mesures. [#bc1d278](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bc1d278)
- Amélioration de la synchronisation Calendly/Airtable. [#e110cf0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e110cf0)
- Ajout de la possibilité d'évaluer un feature flag à partir de l'ID de collectivité côté serveur. [#0ddca9d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0ddca9d)
- Correction de la recherche de collectivités. [#64956a6](https://github.com/incubateur-ademe/territoires-en-transitions/commit/64956a6)

### Évolutions techniques
- Migration des ressources partagées (départements, régions, types de plan) vers tRPC pour améliorer les performances. [#c056905](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c056905), [#33cd35f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/33cd35f)
- Migration des mutations de fiche de Supabase vers tRPC. [#a60468f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a60468f)
- Refactoring de l'import de plans pour optimiser les performances et sécuriser la création de fiches. [#2b7ae1a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2b7ae1a)
- Utilisation du backend pour l'historisation des référentiels au lieu d'un accès direct à Supabase. [#8005748](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8005748)
- Ajout d'index sur les tables d'historique pour améliorer les performances. [#b9d106d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b9d106d)
- Mise en place d'une stratégie de backup et restore de la base de données. [#d30baa5](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d30baa5)
- Amélioration de l'isolation des tests et parallélisation. [#952f739](https://github.com/incubateur-ademe/territoires-en-transitions/commit/952f739)

### Autres changements
- Mise à jour de la configuration Tailwind. [#885e682](https://github.com/incubateur-ademe/territoires-en-transitions/commit/885e682)
- Correction de typos et amélioration de la documentation. [#802d5f1](https://github.com/incubateur-ademe/territoires-en-transitions/commit/802d5f1), [#a002502](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a002502)
- Remplacement de Stonly par une bannière gérée en propre. [#6ba2da0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6ba2da0)
- Amélioration de la robustesse des tests du service d'envoi de mails. [#07b123b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/07b123b)
- Suppression de code inutile et nettoyage du code. [#bb61d02](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bb61d02), [#4258d03](https://github.com/incubateur-ademe/territoires-en-transitions/commit/4258d03)
