## Changelog : mobilic-api (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions de l'API Mobilic se sont concentrées sur l'amélioration de la sécurité et de la conformité des données, notamment via l'anonymisation des informations sensibles et la correction de vulnérabilités. Des améliorations ont également été apportées à la gestion des exports de données, ainsi qu'à la correction de bugs liés à l'authentification et à la validation des missions. Enfin, une mise à jour de la version de Flask a été effectuée, suivie d'un retour en arrière pour éviter des impacts trop importants.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la validation automatique des missions en raison d'un problème avec l'identification de l'entreprise soumettant la mission. [#692](https://github.com/MTES-MCT/mobilic-api/pull/692)
- Correction du format d'affichage du poids des véhicules dans les bulletins de contrôle (Bdc) pour utiliser une virgule décimale. [#691](https://github.com/MTES-MCT/mobilic-api/pull/691)
- Amélioration de la gestion de la connexion des agents (AgentConnect) en corrigeant des problèmes liés aux redirections et à la synchronisation de l'unité organisationnelle. [#687](https://github.com/MTES-MCT/mobilic-api/pull/687), [#686](https://github.com/MTES-MCT/mobilic-api/pull/686)
- Ajout d'une nouvelle fonctionnalité d'anonymisation des données des Bdc pour le Ministère de l'Intérieur. [#688](https://github.com/MTES-MCT/mobilic-api/pull/688)
- Mise à jour de l'étiquette de vérification de la réglementation "sans permis de conduire". [#684](https://github.com/MTES-MCT/mobilic-api/pull/684)
- Ajout d'un endpoint de validation pour les exports.
- Ajout de stratégies d'export vers Sentry.

### Évolutions techniques
- Mise à jour de Flask et des dépendances pipenv pour corriger des vulnérabilités de sécurité, suivie d'un retour à une version antérieure pour éviter des changements trop importants. [#686](https://github.com/MTES-MCT/mobilic-api/pull/686)
- Refactoring du code pour améliorer la qualité et la conformité aux règles SonarCloud.
- Amélioration de la gestion des exports de données :
    - Ajout de règles pour la gestion des chunks.
    - Tri des fichiers dans les archives zip.
    - Gestion des exports pour les données vides.
- Suppression du contexte des accès aux données d'activité pour améliorer la sécurité. [#693](https://github.com/MTES-MCT/mobilic-api/pull/693)
- Renommage de variables pour respecter les conventions de nommage (snake_case).
- Synchronisation de l'unité organisationnelle lors de la reconnexion d'AgentConnect.

### Autres changements
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la documentation.
- Correction de bugs mineurs et nettoyage du code.
- Ajout de logs pour faciliter le débogage.
- Tri des fichiers d'export par ordre alphabétique.
- Ajout des noms des employés lors de l'export de données vides.
- Correction de l'ordre de tri des dates dans les exports.
