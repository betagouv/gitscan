## Changelog : drive (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration de WOPI pour une meilleure compatibilité avec les suites bureautiques en ligne, l'amélioration de la prévisualisation des fichiers (notamment PDF et images), et l'ajout de fonctionnalités liées aux droits et aux conditions d'utilisation. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la prévisualisation des fichiers PDF : affichage à la bonne dimension et ajout de tests E2E pour les PDF avec des tailles de page mixtes.
- Ajout d'un modal de consentement pour les conditions d'utilisation (entitlement disclaimers).
- Possibilité de configurer la durée de validité des invitations via une variable d'environnement.
- Amélioration de l'expérience utilisateur lors de la suppression de dossiers parents pendant un chargement de fichiers : l'upload est annulé.
- Intégration de WOPI : remplacement de l'ID de version par l'ETag pour une meilleure gestion des fichiers avec les applications WOPI.
- Ajout d'indicateurs de performance pour l'utilisation de l'organisation via l'API.
- Possibilité de configurer l'utilisation de PKCE pour l'authentification SSO.
- Ajout d'événements de suivi (PostHog) pour le duplicata d'éléments et les changements de type de colonne.

### Évolutions techniques
- Refactorisation du code de prévisualisation des fichiers pour utiliser les composants de l'UI Kit.
- Déplacement des imports MIME vers l'UI Kit.
- Amélioration de la gestion des transactions lors de la duplication de fichiers.
- Refactorisation du code lié aux droits (entitlements) dans un package backend dédié.
- Mise à jour de plusieurs dépendances : Django (v5.2.14), urllib3 (v2.7.0), pytest (v9.0.3), vite (v6.4.2), Next.js (v15.5.15).
- Suppression de la fonctionnalité de mirroring.
- Amélioration de la gestion des erreurs et des logs pour l'action `get_file_content` WOPI.
- Modification de la façon dont les fichiers WOPI sont ouverts : ils s'ouvrent désormais dans un nouvel onglet.
- Optimisation des tests E2E et ajout de tests pour les nouvelles fonctionnalités.
- Utilisation de variables d'environnement pour configurer la durée de validité des invitations et les URLs JWKS.

### Autres changements
- Mise à jour de la documentation (changelog).
- Nettoyage du code et suppression de code inutilisé.
- Correction de problèmes de style et d'affichage dans l'interface utilisateur.
- Ajout de traductions pour les nouveaux messages et fonctionnalités.
- Amélioration de la stabilité des tests E2E.
- Correction de sélecteurs E2E pour les tests PDF.
- Ajout de tests E2E pour les prévisualisations audio et vidéo.
- Correction de bugs liés à l'affichage du menu "+ New" dans les dossiers en lecture seule.
- Correction d'un bug de blocage de la sélection de plage dans les dossiers volumineux.
