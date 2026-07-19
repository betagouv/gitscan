## Changelog : docs (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec une refonte de l'en-tête, l'ajout d'un menu utilisateur, et des corrections de bugs pour une meilleure stabilité. Des améliorations de l'accessibilité ont également été apportées, ainsi que des optimisations de la recherche et de la gestion des documents.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des paramètres [#2463](https://github.com/suitenumerique/docs/issues/2463).
- Refonte de l'en-tête avec une barre flottante pour une navigation plus intuitive [#2471](https://github.com/suitenumerique/docs/issues/2471).
- Possibilité de créer des sous-documents directement depuis l'interface [#2423](https://github.com/suitenumerique/docs/issues/2423).
- Amélioration de la recherche de documents en utilisant l'ID du document au lieu du chemin [#2501](https://github.com/suitenumerique/docs/issues/2501).
- Ajout d'une commande de gestion pour réinitialiser un document [#1882](https://github.com/suitenumerique/docs/issues/1882).
- Possibilité de quitter un document [#2410](https://github.com/suitenumerique/docs/issues/2410).
- Amélioration de la recherche pour les utilisateurs non authentifiés [#2407](https://github.com/suitenumerique/docs/issues/2407).

### Évolutions techniques
- Mise à jour de la bibliothèque PyJWT pour corriger une vulnérabilité de sécurité [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Refactorisation de la suppression d'utilisateurs pour une meilleure gestion des relations [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Amélioration de la gestion des connexions de collaboration pour une meilleure cascade de suppression [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Configuration de la journalisation avec la propagation activée pour une meilleure traçabilité [#2481](https://github.com/suitenumerique/docs/issues/2481).
- Capture des erreurs de gestionnaire de conversion Yjs dans Sentry pour une meilleure surveillance [#2516](https://github.com/suitenumerique/docs/issues/2516).
- Utilisation de l'ID utilisateur au lieu de la relation utilisateur dans le module de partage [#2437](https://github.com/suitenumerique/docs/issues/2437).

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3 [#2481](https://github.com/suitenumerique/docs/issues/2481).
- Ajout d'un badge DPG au fichier README [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Mise à jour des modèles de formulaires pour les issues [#2207](https://github.com/suitenumerique/docs/issues/2207).
- Correction de typos dans le guide de contribution [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Mise à jour des chaînes de caractères traduites [#2510](https://github.com/suitenumerique/docs/issues/2510).
- Ajout d'un mécanisme de protection pour la collaboration [#2481](https://github.com/suitenumerique/docs/issues/2481).
- Renommage du dossier "docs" dans la documentation.
