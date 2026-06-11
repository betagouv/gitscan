## Changelog : docs (30 derniers jours, au 2026-06-10)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment en matière d'accessibilité, de recherche et de présentation de documents. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. L'ajout du mode présentateur et l'amélioration de la recherche sont des fonctionnalités clés pour les utilisateurs.

### Évolutions fonctionnelles
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches dans les documents. [#2407](https://github.com/suitenumerique/docs/issues/2407)
- Ajout d'un mode présentateur pour faciliter la présentation des documents. [#2321](https://github.com/suitenumerique/docs/issues/2321)
- Amélioration de la recherche : affichage du document parent pour les sous-documents. [#1952](https://github.com/suitenumerique/docs/issues/1952)
- Ajout d'une fonctionnalité permettant de quitter un document. [#2365](https://github.com/suitenumerique/docs/issues/2365)
- Ajout d'une fonctionnalité permettant de supprimer les accès et invitations lors du déplacement d'un document si le scope change.
- Ajout d'une fonctionnalité permettant de capturer des événements pour l'analyse (PostHog) lors de diverses actions sur les documents (création, suppression, favoris, etc.).
- Ajout d'une fonctionnalité permettant de capturer des événements pour l'analyse lors de l'utilisation des actions d'IA.
- Ajout d'une fonctionnalité permettant de capturer des événements pour l'analyse lors de la connexion des utilisateurs.
- Ajout d'une fonctionnalité permettant de capturer des événements pour l'analyse lors de la création et suppression de documents.
- Ajout d'un breadcrumb dans les résultats de recherche. [#2310](https://github.com/suitenumerique/docs/issues/2310)
- Ajout d'un panneau latéral pour les commentaires. [#2279](https://github.com/suitenumerique/docs/issues/2279)
- Ajout d'un panneau latéral pour la table des matières.

### Évolutions techniques
- Amélioration de l'accessibilité des composants de recherche. [#2390](https://github.com/suitenumerique/docs/issues/2390)
- Amélioration de l'accessibilité du mode présentateur (lecture d'écran, navigation au clavier). [#2383](https://github.com/suitenumerique/docs/issues/2383)
- Amélioration de l'accessibilité du titre du document. [#2380](https://github.com/suitenumerique/docs/issues/2380)
- Refactorisation de la gestion des modals pour utiliser `ModalDefaultVariantProps`.
- Mise à jour de Blocknote à la version 0.51.4. [#2373](https://github.com/suitenumerique/docs/issues/2373)
- Suppression d'un job de test E2E obsolète. [#2404](https://github.com/suitenumerique/docs/issues/2404)
- Suppression du code de masquage des documents.
- Amélioration de la gestion des connexions à la base de données pour éviter les erreurs lors des tests.
- Utilisation de runners ARM64 pour la construction des images.
- Ajout d'une analyse de vulnérabilités avec Trivy.
- Suppression de paramètres inutilisés dans la classe Paginator.
- Amélioration de la configuration de PostHog.
- Amélioration de la configuration de l'environnement Helm.
- Ajout de support pour le déploiement sur PaaS (Scalingo).
- Correction d'un problème de fuite de mémoire dans les tests.
- Correction d'un problème d'ordre des éléments dans la corbeille.
- Correction d'un problème de streaming de contenu de document sous ASGI.
- Correction d'un problème de validation d'ID de document.

### Autres changements
- Mise à jour des chaînes de traduction.
- Ajout de la configuration manquante `CONVERSION_UPLOAD_ENABLED` dans la documentation.
- Ajout de la configuration manquante `POSTHOG_HOST` dans la documentation.
- Ajout d'un nouveau paramètre de configuration `DOCUMENT_ALL_ENDPOINT_ENABLED`.
- Correction de problèmes de mise en page et de style.
- Correction de problèmes de compatibilité avec Cunningham.
- Suppression de code obsolète.
- Correction de problèmes de focus dans l'interface utilisateur.
- Mise à jour des dépendances JavaScript.
- Correction de problèmes de flakiness dans les tests E2E.
- Ajout de tests unitaires pour les hooks du mode présentateur.
- Ajout de tests E2E pour le mode présentateur.
- Correction de problèmes de superposition d'éléments dans le menu déroulant.
- Correction de problèmes d'affichage des titres longs dans la table des matières.
- Correction d'un bug empêchant la fermeture du panneau latéral.
- Correction d'un bug lié à l'affichage des emojis dans les PDF.
- Correction d'un crash lié à l'utilisation de GTranslate et du zoom.
- Correction de problèmes liés à l'affichage du panneau latéral sur les tablettes.
- Correction de problèmes liés à l'affichage des icônes dans l'en-tête du panneau latéral.
- Suppression des commentaires dans la fonction print.
- Amélioration de la gestion des erreurs.
- Amélioration de la documentation.
