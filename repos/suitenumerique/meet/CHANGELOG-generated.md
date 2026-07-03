## Changelog : meet (30 derniers jours, au 2026-07-02)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout d'outils d'analyse pour mieux comprendre l'utilisation de la plateforme, l'amélioration de la gestion des fichiers et des corrections de bugs pour une expérience utilisateur plus fluide. Des améliorations de l'accessibilité et des mises à jour de sécurité ont également été apportées. L'addon Outlook a été amélioré avec de nouvelles fonctionnalités.

### Évolutions fonctionnelles
- Ajout d'un système d'analyse configurable (PostHog) pour suivre les événements, notamment la génération de liens de réunion. [#1383](https://github.com/suitenumerique/meet/issues/1383)
- Amélioration de l'addon Outlook : ajout d'un lien de feedback, support de l'internationalisation et amélioration de la gestion des liens.
- Ajout d'un sondage de satisfaction optionnel en bas de la page de résumé.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Possibilité de désactiver la connexion silencieuse via un paramètre d'URL.
- Amélioration de la gestion des effets vidéo pour une meilleure accessibilité.
- Amélioration de la pagination dans la vue PiP (Picture-in-Picture) avec une meilleure accessibilité.
- Ajout d'un administrateur spécifique pour la gestion des fichiers.
- Ajout d'une commande pour nettoyer les fichiers en attente et supprimés.
- Amélioration du bruit de fond avec un pipeline de traitement audio BBBA.

### Évolutions techniques
- Intégration du SDK PostHog dans le backend.
- Normalisation des clés d'objets S3 pour la compatibilité avec les notifications.
- Refactorisation de la gestion des variables d'environnement.
- Mise à jour de plusieurs dépendances (eslint, react-i18next, aiohttp, urllib3, posthog-js).
- Amélioration de la robustesse du processus de suppression de fichiers.
- Utilisation de `ReturnType<typeof setTimeout>` pour une meilleure typage.
- Amélioration de la gestion de l'état des fichiers dans la base de données.
- Lazy loading de `@libreaudio/la-call` pour optimiser les performances.
- Mise à jour des librairies libcrypto3 et libssl3.
- Passage à ESLint 9.
- Mise à jour de la configuration CSP pour corriger une régression.
- Mise à jour du chart Helm.

### Autres changements
- Ajout de Clever Cloud comme fournisseur SaaS pour La Suite Meet dans la documentation.
- Clarification des directives de contribution dans la documentation.
- Ajout de l'instance email.eu à la liste des instances connues.
- Ajout d'un badge DPG au README.
- Documentation de la personnalisation du favicon via un volume mount.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de dépendances inutiles.
- Correction de problèmes d'accessibilité sur les effets vidéo.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes liés à l'audio (canal gauche uniquement).
- Correction de problèmes liés à la collecte de métadonnées.
- Correction d'un bug dans le collecteur d'agents.
- Mise à jour des migrations de base de données.
