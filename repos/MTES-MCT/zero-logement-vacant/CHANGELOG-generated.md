## Changelog : zero-logement-vacant (30 derniers jours, au 21 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations techniques, notamment la refonte de la configuration du serveur avec l'utilisation de Zod pour la validation, la modernisation des outils de build et de test, et l'ajout d'une documentation OpenAPI complète pour l'API. Des améliorations fonctionnelles ont également été apportées, comme l'ajout de fonctionnalités pour les campagnes (affichage, téléchargement des destinataires) et la gestion des droits d'accès basés sur le périmètre géographique.

### Évolutions fonctionnelles
- Ajout de l'affichage de la liste des campagnes avec des options de tri améliorées.
- Possibilité de télécharger la liste des destinataires d'une campagne.
- Amélioration de l'affichage des informations relatives aux propriétaires (rang et droits de propriété).
- Correction de l'affichage des libellés dans l'onglet "Évolutions".
- Ajout d'une notification lors de la création d'une campagne et de la suppression d'un groupe.
- Amélioration de l'affichage des pourcentages et des nombres décimaux.
- Ajout d'un avertissement concernant les données sensibles sur les onglets "Notes" et "Documents".
- Correction de l'affichage des noms de filtres de périmètre.
- Correction du comportement du bouton de suppression d'une campagne.

### Évolutions techniques
- Refonte de la configuration du serveur : remplacement de `convict` par `Zod` pour une validation plus robuste et une meilleure gestion des schémas.
- Mise à jour de Vite en version 8 et des plugins associés.
- Ajout de documentation OpenAPI complète pour l'API, avec l'utilisation de Scalar au lieu de Swagger UI.
- Amélioration des tests : ajout de tests unitaires et d'intégration, correction de tests existants, et amélioration de la couverture de code.
- Refactorisation du code : suppression de code inutilisé, simplification de la logique, et amélioration de la lisibilité.
- Mise à jour des dépendances et des outils de build.
- Ajout de l'outil d'analyse de code Knip pour identifier les dépendances inutilisées.
- Implémentation de triggers pour optimiser les calculs de comptage des logements et des propriétaires dans les groupes.
- Utilisation de `p-memoize` pour optimiser les performances de l'API Geo.
- Migration vers une abstraction de fournisseur d'authentification pour gérer les droits d'accès basés sur le périmètre géographique.

### Autres changements
- Ajout de documentation pour les "superpowers" et les plans d'implémentation.
- Amélioration de la documentation technique (DAT, DE, DI) avec génération de PDF.
- Mise à jour des scripts de CI/CD pour améliorer l'efficacité et la fiabilité du processus de déploiement.
- Correction de problèmes mineurs d'interface utilisateur et de comportement.
- Ajout de commentaires et de documentation pour améliorer la maintenabilité du code.
- Correction de problèmes de compatibilité avec les navigateurs et les outils de développement.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Mise à jour des dépendances de sécurité.
- Amélioration de la configuration de Worktrunk.
- Ajout de la gestion des fichiers `.env` avec CleverCloud.
- Suppression de scripts et de dépendances inutiles.
- Correction de problèmes de performance.
