## Changelog : dictaphone (30 derniers jours, au 2026-05-21)

### Résumé
Cette période a été marquée par une série de corrections de bugs et d'améliorations de l'expérience utilisateur, tant sur le web que sur l'application mobile. Des fonctionnalités importantes comme la possibilité de relancer une transcription échouée et la gestion des erreurs d'upload ont été ajoutées. L'authentification mobile a été revue pour plus de robustesse et de sécurité. Plusieurs améliorations de l'interface utilisateur et de la gestion des fichiers ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de relancer une transcription échouée via l'interface web et l'API. [#fd9b751](https://github.com/suitenumerique/dictaphone/commit/fd9b751)
- Amélioration de la gestion des erreurs d'upload sur l'application mobile, avec des messages plus clairs pour l'utilisateur. [#dc7ca3f](https://github.com/suitenumerique/dictaphone/commit/dc7ca3f)
- Possibilité de télécharger l'application mobile directement depuis l'interface web. [#724c874](https://github.com/suitenumerique/dictaphone/commit/724c874)
- Ajout d'un lien vers la documentation dans l'application mobile. [#2f6f336](https://github.com/suitenumerique/dictaphone/commit/2f6f336)
- Amélioration de l'expérience utilisateur lors de la réinitialisation du mot de passe sur l'application mobile. [#c084838](https://github.com/suitenumerique/dictaphone/commit/c084838)
- Ajout d'une option pour contourner l'écran de connexion sur l'application mobile. [#16dd187](https://github.com/suitenumerique/dictaphone/commit/16dd187)
- Possibilité de sélectionner directement le texte transcrit sur l'application mobile. [#211908c](https://github.com/suitenumerique/dictaphone/commit/211908c) et [#1c8606b](https://github.com/suitenumerique/dictaphone/commit/1c8606b)
- Ajout d'un indicateur de progression lors de l'upload sur l'application mobile. [#6d46342](https://github.com/suitenumerique/dictaphone/commit/6d46342) et [#10dcb1f](https://github.com/suitenumerique/dictaphone/commit/10dcb1f)
- Amélioration de la gestion des fichiers : ajout d'une commande pour nettoyer les fichiers en attente et supprimés. [#f270029](https://github.com/suitenumerique/dictaphone/commit/f270029) et [#69a917b](https://github.com/suitenumerique/dictaphone/commit/69a917b)

### Évolutions techniques
- Migration de l'authentification mobile vers JWT et PKCE pour une meilleure sécurité. [#09702a1](https://github.com/suitenumerique/dictaphone/commit/09702a1) et [#1a44564](https://github.com/suitenumerique/dictaphone/commit/1a44564)
- Refonte de l'architecture d'authentification pour plus de robustesse. [#8b81751](https://github.com/suitenumerique/dictaphone/commit/8b81751)
- Mise à jour des dépendances backend et des fichiers Docker pour améliorer la sécurité. [#8a4ba91](https://github.com/suitenumerique/dictaphone/commit/8a4ba91)
- Amélioration du logging en cas d'échec de la transcription. [#b1a1451](https://github.com/suitenumerique/dictaphone/commit/b1a1451)
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code. [#27f5717](https://github.com/suitenumerique/dictaphone/commit/27f5717)
- Amélioration de la configuration de l'application avec la prise en compte de variables d'environnement pour `SECURE_SSL_REDIRECT`. [#338a90a](https://github.com/suitenumerique/dictaphone/commit/338a90a)

### Autres changements
- Mise à jour de la documentation et des fichiers README. [#2d7695d](https://github.com/suitenumerique/dictaphone/commit/2d7695d), [#4f34e13](https://github.com/suitenumerique/dictaphone/commit/4f34e13), [#dcb19c8](https://github.com/suitenumerique/dictaphone/commit/dcb19c8)
- Mise à jour des documents légaux. [#182a6a7](https://github.com/suitenumerique/dictaphone/commit/182a6a7) et [#e791c59](https://github.com/suitenumerique/dictaphone/commit/e791c59)
- Correction de typos et amélioration de la lisibilité du code. [#09e35de](https://github.com/suitenumerique/dictaphone/commit/09e35de)
- Amélioration de l'accessibilité de certains composants de l'application mobile. [#e8a970c](https://github.com/suitenumerique/dictaphone/commit/e8a970c)
- Diverses corrections de bugs et améliorations de l'interface utilisateur sur le web et l'application mobile.
