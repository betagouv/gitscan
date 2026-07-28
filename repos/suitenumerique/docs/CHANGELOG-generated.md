## Changelog : docs (30 derniers jours, au 23 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur, notamment dans la présentation de documents et la gestion des utilisateurs. Des corrections de bugs et des optimisations techniques ont également été réalisées pour améliorer la stabilité et la performance de l'application. La documentation a été enrichie avec des informations sur la configuration et l'utilisation de certaines fonctionnalités.

### Évolutions fonctionnelles
- Possibilité d'ouvrir et de partager une présentation à une diapositive spécifique. [#2508](https://github.com/suitenumerique/docs/issues/2508)
- Ajout d'un menu utilisateur.
- Nouvelle interface utilisateur pour le panneau latéral, avec des animations Lottie.
- Amélioration de l'interface utilisateur du panneau latéral.
- Restauration du lien "Passer au contenu" après la refonte de l'en-tête.
- Ajout de la gestion de nouvelles langues (zh_CN, eo_PL, zh_TW). [#2486](https://github.com/suitenumerique/docs/issues/2486)
- Possibilité de réinitialiser un document via une commande de gestion.
- Amélioration de la recherche de documents.
- Ajout d'une commande pour réinitialiser un document.
- Possibilité de quitter un document.

### Évolutions techniques
- Adaptation de la commande de build pour tenir compte d'une mise à jour de `tsc-alias`.
- Mise à jour de la sécurité de Next.js (v16.2.11).
- Correction d'une erreur de pointeur nul dans la liste des tâches de fond (backend_conjob_list).
- Correction de problèmes de focus sur les diapositives de la présentation.
- Capture des erreurs de gestionnaire de conversion dans Sentry.
- Refonte de l'architecture de la présentation pour une meilleure réutilisation des composants.
- Amélioration de la gestion des connexions de collaboration.
- Mise à jour de la configuration du déploiement pour gérer les certificats CA personnalisés.
- Suppression d'un backend d'authentification inutilisé.
- Correction de bugs liés au drag and drop dans Firefox.
- Correction de problèmes de redirection après suppression de document.

### Autres changements
- Mise à jour de la documentation avec des informations sur la configuration du format de conversion et l'utilisation de S3.
- Mise à jour des modèles de formulaires pour les issues. [#2207](https://github.com/suitenumerique/docs/issues/2207)
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Correction de problèmes de tests E2E pour l'export.
- Amélioration de la sémantique des éléments HTML (utilisation de `<p>` au lieu de `<div>`).
- Mise à jour des chaînes de traduction.
- Ajout de la gestion des erreurs dans le fournisseur Yjs.
- Suppression de fichiers de configuration inutiles.
- Correction de problèmes de tests unitaires.
