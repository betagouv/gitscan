## Changelog : meet (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des rôles des participants, notamment la possibilité de promouvoir des utilisateurs pendant une réunion. De nombreuses optimisations de performance ont été réalisées sur l'interface utilisateur, en particulier dans la gestion des participants et du chat. Des corrections de bugs et des mises à jour de dépendances ont également été intégrées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier le rôle d'un participant pendant une réunion (promotion d'un participant authentifié). [#1510](https://github.com/suitenumerique/meet/issues/1510)
- Affichage d'un badge "non authentifié" pour les participants non authentifiés.
- Amélioration de l'affichage du nom des participants dans la liste.
- Ajout d'un indicateur visuel pour les participants avec la caméra désactivée.
- Possibilité de configurer un lien vers la documentation.
- Ajout d'outils d'add-in lors de la création de réunions dans les calendriers partagés.
- Suppression du tag "beta" pour les add-ins.
- Amélioration de la gestion des erreurs et du reporting dans le module de transcription.

### Évolutions techniques
- Refactorisation importante du code du chat pour améliorer les performances et la maintenabilité.
- Optimisations de performance de l'interface utilisateur, notamment dans le rendu de la liste des participants, du carrousel, et des composants d'avatar.
- Virtualisation des messages du chat pour réduire la taille du DOM.
- Passage à Node 22 pour la construction de l'interface utilisateur.
- Mise à jour de plusieurs dépendances (livekit-client, posthog-js, @tanstack/react-query, etc.).
- Refactorisation du code pour isoler et optimiser les composants et les hooks.
- Amélioration de la gestion des événements et des abonnements pour réduire les re-rendus inutiles.
- Ajout d'un système d'analyse configurable basé sur des flags de fonctionnalités.
- Mise à jour de joserfc à la version 1.6.8 pour corriger une vulnérabilité.
- Amélioration de la gestion des permissions et de l'authentification.
- Ajout d'instrumentation Sentry pour les agents.

### Autres changements
- Mise à jour des termes de service.
- Ajout d'un fichier publiccode.yml.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests pour la gestion des clés S3.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour de la documentation.
- Correction de problèmes de focus dans le side panel.
- Correction de problèmes d'affichage dans le mode picture-in-picture.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour des images Docker.
