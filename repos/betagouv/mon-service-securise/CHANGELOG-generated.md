## Changelog : mon-service-securise (30 derniers jours, au 2026-07-17)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'expérience utilisateur, notamment l'ajout de fonctionnalités liées aux référentiels externes (ISO2700X, ReCyf, AE2690) et une refonte de l'interface avec l'intégration de composants DSFR pour une meilleure accessibilité et cohérence visuelle. Des corrections et des améliorations techniques ont également été apportées, notamment autour des tests d'accessibilité et de la gestion des risques.

### Évolutions fonctionnelles
- Ajout d'une case à cocher pour le consentement au pixel de suivi lors de l'inscription et gestion du consentement via un webhook.
- Intégration des données des référentiels externes (ISO2700X, ReCyf, AE2690) dans la liste des mesures.
- Possibilité de filtrer les mesures par référentiel externe.
- Affichage des mesures du référentiel AE2690.
- Ajout d'une page publique répertoriant toutes les mesures du référentiel V2.
- Amélioration de l'affichage des mesures spécifiques et ajout d'une colonne indiquant le nombre de services associés sans statut.
- Ajout d'une notification pour les référentiels externes.
- Refonte de l'interface utilisateur avec l'intégration de composants DSFR (boutons, tableaux, onglets, etc.).
- Ajout de boîtes d'informations pour les indices cyber, les mesures par niveau de criticité et par catégorie.
- Ajout de l'annexe des risques V1 et V2 au PDF.
- Ajout d'une indication de fichier généré sur la sélection des vecteurs et des matrices.
- Possibilité de surcharger la gravité d'un risque général V2.
- Ajout de la gestion des risques spécifiques V2 dans le tiroir.

### Évolutions techniques
- Conversion de plusieurs modèles métier en TypeScript (ElementsFabricables, ItemsAvecDescription, fabriquePartiePrenante, ActeurHomologation, RolesResponsabilites, PartiesPrenantes, ActeursHomologation, PartiePrenante).
- Refactorisation du code pour supprimer les dépendances obsolètes et le code inutilisé.
- Amélioration de la gestion des erreurs et des validations.
- Mise à jour de plusieurs dépendances (axe-core, eslint, playwright, typescript, etc.).
- Amélioration des tests d'accessibilité avec l'ajout de tests pour de nouvelles fonctionnalités et la correction de problèmes existants.
- Utilisation d'un serveur de test dédié pour les tests d'accessibilité.
- Ajout d'un adaptateur de persistance mémoire avec des données pour les tests d'accessibilité.
- Amélioration de la performance et de la robustesse du code.
- Suppression de code obsolète et simplification de la configuration.

### Autres changements
- Documentation de la conversion des modèles métier en TypeScript.
- Correction de coquilles et amélioration de la lisibilité du code.
- Mise à jour des illustrations et des textes.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Amélioration du système de notification.
- Ajout de logs pour faciliter le débogage.
- Suppression de la page "activation".
- Ajout d'un fichier robots.txt et d'un sitemap.
- Ajout de tracking Matomo pour la navigation dans la SPA.
- Suppression des tests de l'admin.
- Suppression du POC Typst.
