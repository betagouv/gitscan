## Changelog : meet (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la transcription, à la gestion des enregistrements, à l'intégration SSO, et à l'expérience utilisateur globale. Des corrections de bugs et des mises à jour de dépendances ont également été intégrées pour améliorer la stabilité et la sécurité de la plateforme. L'ajout de la prise en charge des add-ins pour les calendriers partagés est également une nouveauté notable.

### Évolutions fonctionnelles
- Ajout d'un gradient de couleur pour les participants lorsque leur caméra est désactivée. [#1490](https://github.com/suitenumerique/meet/issues/1490)
- Possibilité de forcer l'affichage du nom SSO pour les utilisateurs authentifiés.
- Intégration d'outils d'add-in lors de la création de réunions dans les calendriers partagés.
- Amélioration de la gestion des enregistrements avec un fallback LiveKit pour l'événement `egress_ended`.
- Prise en charge de la recherche par email du propriétaire dans la table d'administration des enregistrements.
- Amélioration de l'accessibilité du panneau latéral avec un focus correct sur l'ouverture et la commutation des panneaux.
- Correction d'un bug qui empêchait l'interaction avec l'avertissement de partage d'écran en mode image dans l'image (PiP).
- Correction d'un crash du panneau d'informations pour les salles non enregistrées.
- Amélioration de la gestion des erreurs lors de l'utilisation de Whisper pour la transcription.

### Évolutions techniques
- Refactorisation de la gestion des variables d'environnement.
- Refactorisation des processeurs de fond pour utiliser la nouvelle API.
- Intégration de modules MediaPipe WASM en ligne pour éviter les chargements distants.
- Refactorisation du stockage du nom d'utilisateur.
- Mise en place d'un système d'analyse configurable avec PostHog.
- Mise à jour de l'image de base Alpine pour le service de résumé.
- Mise à jour de ffmpeg vers la version 8.1.2.
- Mise à jour de la version de Node.js pour la construction du frontend (Node 22).
- Mise à jour de l'image Docker pour nginx.
- Normalisation des clés d'objets S3 pour la compatibilité des notifications.
- Amélioration de la gestion des jetons LiveKit pour utiliser le nom complet comme nom d'affichage.
- Correction de la construction de l'application sur Scalingo.

### Autres changements
- Documentation : Correction du nom de la variable d'environnement CSS dans la documentation.
- Documentation : Ajout de Clever Cloud comme fournisseur SaaS de La Suite Meet.
- Documentation : Clarification des directives de contribution.
- Documentation : Précision de la généralisation française par le chef de produit.
- Suppression du code lié à la version 1 du service de résumé.
- Mise à jour des dépendances : `@mediapipe/tasks-vision`, `i18next`, `posthog-js`, `@tanstack/react-query`, `livekit-client`, `@pandacss/preset-panda`, `react-aria`, `react-aria-components`, `react-stately`.
- Publication de la version 1.24.0.
- Publication du chart Helm 0.0.27.
- Suppression du tag "beta" pour les add-ons.
- Correction d'un bug dans les tests d'attribution des intervenants pour la transcription.
- Mise à jour de la version du lockfile UV via le script de préparation de la release.
- Ajout d'instrumentation Sentry pour les agents LiveKit.
- Mise à jour de joserfc à la version 1.6.8 pour corriger une CVE.
- Mise à jour de mjml et @html-to/text-cli.
- Ajout de la prise en charge de la recherche des utilisateurs provisionnés en externe dans PostHog.
- Mise à jour de la documentation pour refléter les changements apportés à la compatibilité des clés S3.
- Mise à jour des dépendances Python.
- Correction de la déduplication des emails insensible à la casse dans la commande de fusion.
- Ajout de la prise en charge d'un domaine dédié pour l'API des flags de fonctionnalité PostHog.
- Rejet des jetons d'accès utilisateur sur l'API.
- Mise à jour de la documentation pour la personnalisation du favicon via un volume mount.
- Suppression de l'appel au flag de fonctionnalité `summary_enabled`.
- Mise à jour de l'image de base pour le service de résumé.
- Ajout de documentation pour les tests de l'analyseur S3.
- Ajout de tests pour couvrir les clés S3 encodées avec des signes plus.
- Mise à jour de la documentation du changelog.
