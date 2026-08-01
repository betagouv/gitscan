## Changelog : meet (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance, notamment au niveau du rendu de l'interface utilisateur et de la gestion des participants. De nouvelles fonctionnalités ont été ajoutées concernant la gestion des rôles des participants et l'intégration d'outils externes. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour améliorer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier le rôle d'un participant pendant une réunion. [#1234](https://github.com/suitenumerique/meet/issues/1234)
- Affichage d'un badge indiquant si un participant est authentifié.
- Amélioration du rendu du nom des participants dans la liste.
- Possibilité de promouvoir des participants authentifiés en administrateurs.
- Ajout d'un indicateur visuel pour les participants avec l'appareil photo désactivé.
- Ajout d'un lien configurable vers la documentation.
- Intégration d'outils externes lors de la création de réunions dans les calendriers partagés.
- Amélioration de l'affichage des initiales dans les avatars.
- Ajout d'un gradient de couleur pour les participants dans l'avatar.

### Évolutions techniques
- Refactorisation importante du code du chat pour optimiser les performances.
- Virtualisation des messages du chat pour réduire la taille du DOM.
- Optimisation du rendu des métadonnées des participants.
- Amélioration de la gestion des événements liés aux participants.
- Refactorisation du code pour isoler et optimiser différents composants de l'interface utilisateur.
- Mise à jour de plusieurs dépendances (LiveKit, React Query, PostHog, etc.).
- Mise à jour de l'image Docker pour utiliser nginx-unprivileged:1.30.3-alpine3.23.
- Mise à jour de la version de Node.js pour le build frontend à la version 22.
- Mise à jour de la version de Python pour les agents.
- Refactorisation du système d'authentification backend.
- Ajout d'un système d'analytics configurable basé sur PostHog.
- Amélioration de la gestion des erreurs et des webhooks pour le service de résumé.
- Mise à jour des dépendances Python.
- Normalisation des clés S3 pour la compatibilité avec les notifications.

### Autres changements
- Mise à jour des termes de service.
- Ajout d'un fichier `publiccode.yml`.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests unitaires.
- Amélioration de la documentation.
- Correction de problèmes liés au centrage des initiales dans les avatars.
- Suppression de code obsolète.
- Correction de problèmes de focus dans l'interface utilisateur.
- Correction de problèmes liés à la gestion des états du chat.
- Amélioration de la gestion des erreurs dans le service de résumé.
- Correction d'un bug lié à la détection des tentatives de nouvelles tentatives.
- Correction d'un bug lié à la gestion des métadonnées d'enregistrement.
- Correction d'un bug lié à la gestion des erreurs dans le service de résumé.
- Correction d'un bug lié à la gestion des clés S3.
