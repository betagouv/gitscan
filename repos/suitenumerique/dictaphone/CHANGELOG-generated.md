## Changelog : dictaphone (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, l'équipe a déployé des améliorations significatives sur l'application mobile et le backend, notamment la gestion des erreurs, la possibilité de relancer les transcriptions échouées, l'intégration avec un service de documentation externe et des corrections d'interface utilisateur. L'application mobile a bénéficié d'une refonte de l'expérience utilisateur, avec l'ajout de fonctionnalités comme la suppression par glissement, la gestion des autorisations et l'intégration de l'authentification JWT/PKCE pour une sécurité accrue.

### Évolutions fonctionnelles
- Ajout de la possibilité de relancer une transcription échouée via l'interface utilisateur et l'API. [#fd9b751](https://github.com/suitenumerique/dictaphone/commit/fd9b751)
- Intégration avec un service de documentation externe pour l'ouverture directe des transcriptions. [#f125456](https://github.com/suitenumerique/dictaphone/commit/f125456)
- Amélioration de l'expérience utilisateur mobile :
    - Ajout de la possibilité de supprimer une transcription par glissement. [#7cabf2d](https://github.com/suitenumerique/dictaphone/commit/7cabf2d)
    - Amélioration de la gestion des erreurs et des états de chargement. [#7305190](https://github.com/suitenumerique/dictaphone/commit/7305190)
    - Ajout d'un indicateur de progression lors du téléchargement des fichiers. [#10dcb1f](https://github.com/suitenumerique/dictaphone/commit/10dcb1f)
    - Possibilité de contourner l'écran de connexion pour faciliter les tests. [#16dd187](https://github.com/suitenumerique/dictaphone/commit/16dd187)
- Limitation automatique de la durée d'enregistrement pour éviter les dépassements. [#4173509](https://github.com/suitenumerique/dictaphone/commit/4173509)
- Amélioration de la sélection de texte dans les transcriptions. [#642a018](https://github.com/suitenumerique/dictaphone/commit/642a018) et [#1c8606b](https://github.com/suitenumerique/dictaphone/commit/1c8606b)
- Ajout d'un lien pour supprimer son compte sur l'application mobile. [#377c8a2](https://github.com/suitenumerique/dictaphone/commit/377c8a2)

### Évolutions techniques
- Mise à jour de l'authentification mobile vers JWT avec PKCE pour une sécurité renforcée. [#09702a1](https://github.com/suitenumerique/dictaphone/commit/09702a1) et [#8b81751](https://github.com/suitenumerique/dictaphone/commit/8b81751)
- Refonte de l'architecture de l'application mobile pour une meilleure maintenabilité.
- Ajout d'un script pour automatiser le processus de publication de l'application mobile. [#3b401b6](https://github.com/suitenumerique/dictaphone/commit/3b401b6)
- Amélioration de la gestion des fichiers temporaires et des fichiers supprimés. [#f270029](https://github.com/suitenumerique/dictaphone/commit/f270029) et [#69a917b](https://github.com/suitenumerique/dictaphone/commit/69a917b)
- Mise à jour des dépendances du backend pour améliorer la sécurité et la stabilité. [#8a4ba91](https://github.com/suitenumerique/dictaphone/commit/8a4ba91)
- Amélioration des tests CI/CD et ajout de linting pour le code mobile. [#27f5717](https://github.com/suitenumerique/dictaphone/commit/27f5717)
- Amélioration de la gestion des logs et des erreurs. [#b1a1451](https://github.com/suitenumerique/dictaphone/commit/b1a1451)

### Autres changements
- Mise à jour de la documentation pour l'utilisation locale de l'environnement de développement. [#dcb19c8](https://github.com/suitenumerique/dictaphone/commit/dcb19c8) et [#211908c](https://github.com/suitenumerique/dictaphone/commit/211908c)
- Amélioration de la présentation du README. [#2d7695d](https://github.com/suitenumerique/dictaphone/commit/2d7695d) et [#8ac1961](https://github.com/suitenumerique/dictaphone/commit/8ac1961)
- Correction de typos et amélioration de la lisibilité du code. [#09e35de](https://github.com/suitenumerique/dictaphone/commit/09e35de)
- Correction de problèmes mineurs d'interface utilisateur.
- Suppression de code inutile et nettoyage du codebase.
