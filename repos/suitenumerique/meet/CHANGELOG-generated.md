## Changelog : meet (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, la Suite Meet a bénéficié d'améliorations significatives en termes de fonctionnalités, notamment l'intégration d'outils additionnels lors de la création de réunions, l'amélioration de la gestion des noms d'utilisateurs SSO, et des corrections de bugs pour une meilleure stabilité. Des mises à jour de sécurité et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'afficher des outils additionnels lors de la création de réunions dans les calendriers partagés.
- Amélioration de la gestion des noms d'utilisateurs SSO : possibilité de forcer l'affichage du nom complet pour les utilisateurs authentifiés.
- Correction d'un bug empêchant l'affichage correct des informations dans le panneau d'informations pour les salles non enregistrées.
- Amélioration de l'accessibilité : focus du conteneur du panneau latéral lors de son ouverture et restauration du focus lors du changement de panneau.
- Correction d'un bug empêchant l'assignation correcte des locuteurs lors de la transcription.
- Ajout d'un gradient de couleur pour les participants lorsque leur caméra est désactivée.
- Priorisation de l'affichage du partage d'écran en mode Picture-in-Picture.
- Utilisation du layout "focus" pour le partage d'écran en Picture-in-Picture.
- Correction d'un bug empêchant l'activation du bouton de partage d'écran en mode Picture-in-Picture.

### Évolutions techniques
- Mise à jour de plusieurs dépendances frontend (livekit-client, @tanstack/react-query, posthog-js, i18next, @mediapipe/tasks-vision).
- Refactorisation de l'organisation des packages JavaScript frontend.
- Intégration des poids des modèles MediaPipe directement dans le code pour éviter les chargements distants.
- Installation de `vite-plugin-static-copy` pour les assets WASM de MediaPipe.
- Refactorisation des processeurs de fond pour utiliser la nouvelle API.
- Mise à jour de la base d'image Alpine pour le service de résumé.
- Mise à jour de la version de ffmpeg.
- Mise à jour de la version de joserfc pour corriger une vulnérabilité CVE-2026-49852.
- Mise en place d'un système d'analyse configurable avec PostHog.
- Ajout de la traçabilité des événements de génération de liens de réunion.
- Amélioration de la gestion des variables d'environnement.
- Mise à jour de l'image Docker pour nginx.
- Mise à jour de la version de Node.js utilisée pour la construction du frontend.
- Correction d'un bug dans le script de construction des emails.
- Normalisation des clés d'objets S3 pour la compatibilité avec les notifications.

### Autres changements
- Documentation : correction du nom de la variable d'environnement CSS dans la documentation.
- Documentation : ajout de Clever Cloud comme fournisseur SaaS pour La Suite Meet.
- Documentation : clarification des directives de contribution.
- Documentation : ajout d'une note concernant la suppression de la version v1 du résumé.
- Suppression du tag "beta" pour les add-ons.
- Ajout du badge DPG au README.
- Mise à jour du fichier `CHANGELOG.md`.
- Correction de la gestion des emails nuls dans les analyses.
- Mise à jour du fichier Helm chart.
- Correction de la configuration de Tilt pour le mapping des noms complets et courts.
- Ajout de l'instrumentation Sentry pour les agents LiveKit.
- Suppression du code lié à la version v1 du résumé.
- Correction de la déduplication des emails (insensible à la casse) dans la commande de fusion.
- Ajout de la prise en charge des cas d'utilisation Visio pour les routes v2 du résumé.
- Refactorisation de l'authentification basée sur les tokens Bearer.
- Ajout de la possibilité de rechercher les enregistrements par email du propriétaire.
- Amélioration de l'espacement des vignettes en Picture-in-Picture.
- Amélioration de l'accessibilité du contrôle de pagination.
- Utilisation de "Avancé" au lieu de "Premium" dans le panneau latéral.
- Ajout de la prise en charge d'un domaine dédié pour l'API des feature flags.
- Rejet des tokens d'accès utilisateur sur l'API.
- Mise à jour de la documentation pour la personnalisation du favicon via un volume mount.
- Ajout de la compatibilité avec les clés S3 encodées avec des signes plus.
- Ajout de docstrings pour les tests de parser.
- Ajout de tests pour couvrir les clés S3 encodées avec des signes plus.
- Mise à jour de l'image de base Alpine.
- Mise à jour de la version de cryptography.
