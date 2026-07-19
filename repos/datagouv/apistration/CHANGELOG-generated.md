## Changelog : apistration (30 derniers jours, au 2026-07-17)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité, notamment la correction de nombreux problèmes identifiés par des audits RGAA. Des fonctionnalités ont été ajoutées pour faciliter l'intégration des éditeurs et améliorer la gestion des tokens. Plusieurs corrections et améliorations ont également été apportées aux API, notamment concernant les données TVA et les informations sur les établissements scolaires.

### Évolutions fonctionnelles
- Ajout de la gestion des tokens éditeur en self-service (création, prolongation, révocation) [#252](https://github.com/datagouv/apistration/pull/252).
- Implémentation d'un webhook pour l'API Particulier, permettant la gestion des démarches numériques [#266](https://github.com/datagouv/apistration/pull/266).
- Amélioration de la documentation pour les intégrations éditeur et les tokens éditeur [#178](https://github.com/datagouv/apistration/pull/178).
- Ajout d'un filtre de statut pour les habilitations dans le tableau de bord des fournisseurs.
- Affichage de l'ID interne de l'utilisateur sur la page de son compte.
- Ajout de l'endpoint CNAV ARS (Allocation Rentrée Scolaire) [#164](https://github.com/datagouv/apistration/pull/164).
- Refonte de l'intégration des données Simplifions avec l'ajout de nouvelles fonctionnalités et corrections.
- Mise en place d'un système de création automatique de délégations pour les éditeurs via un formulaire Typeform [#249](https://github.com/datagouv/apistration/pull/249).

### Évolutions techniques
- Corrections de sécurité concernant le tabnapping et les XSS sur les liens DataPass [#240](https://github.com/datagouv/apistration/pull/240).
- Amélioration de la robustesse des tests et correction de tests aléatoires.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (Rubocop, Ruby, etc.).
- Amélioration de la gestion des erreurs et des réponses HTTP pour l'API DJEPVA.
- Optimisation de la gestion du cache pour l'API TVA.
- Mise en place d'un système de gestion des incidents via Hyperping.
- Amélioration de la gestion des erreurs et des validations pour les tokens éditeur.

### Autres changements
- Amélioration significative de l'accessibilité du site web, avec correction de nombreux problèmes identifiés par des audits RGAA.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et corrections.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de jeux de données de test pour le service CNous.
- Nettoyage du code et suppression de code obsolète.
- Amélioration des messages d'erreur et des logs.
- Correction de problèmes de linting.
- Ajout de tests unitaires et d'intégration.
