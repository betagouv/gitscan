## Changelog : dictaphone (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en matière d'enregistrement et de gestion des fichiers audio et vidéo. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que l'ajout de nouvelles fonctionnalités comme la possibilité de régénérer les transcriptions et d'exporter les fichiers au format SRT. L'application mobile a bénéficié de nombreuses améliorations, notamment en matière de gestion des téléchargements et de l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout du support pour la plupart des formats audio et vidéo. [#c19d9ce](https://github.com/suitenumerique/dictaphone/commit/c19d9ce)
- Possibilité d'exporter les transcriptions au format SRT. [#f49ee75](https://github.com/suitenumerique/dictaphone/commit/f49ee75)
- Ajout de boutons pour copier le texte et ouvrir les fichiers dans le menu d'actions des fichiers. [#2252469](https://github.com/suitenumerique/dictaphone/commit/2252469)
- Affichage de la source du fichier audio et de sa durée en secondes dans l'interface d'administration Django. [#ac192c3](https://github.com/suitenumerique/dictaphone/commit/ac192c3)
- Amélioration de l'interface utilisateur pour la gestion des enregistrements, avec notamment un indicateur de progression du téléchargement sur mobile. [#d8c4f88](https://github.com/suitenumerique/dictaphone/commit/d8c4f88)
- Ajout d'une option pour n'autoriser le téléchargement que via Wi-Fi sur mobile. [#b350ff2](https://github.com/suitenumerique/dictaphone/commit/b350ff2)
- Possibilité de regénérer une transcription échouée. [#fd9b751](https://github.com/suitenumerique/dictaphone/commit/fd9b751)
- Ajout d'un bouton pour revenir à la liste des enregistrements après la suppression d'un fichier. [#66e5bf5](https://github.com/suitenumerique/dictaphone/commit/66e5bf5)
- Amélioration de l'accessibilité de l'application. [#1c59be1](https://github.com/suitenumerique/dictaphone/commit/1c59be1)
- Ajout d'un indicateur visuel du niveau sonore pendant l'enregistrement. [#c43f0b5](https://github.com/suitenumerique/dictaphone/commit/c43f0b5)
- Ajout d'un son de démarrage et d'arrêt de l'enregistrement. [#2605113](https://github.com/suitenumerique/dictaphone/commit/2605113)
- Possibilité de contourner l'écran de connexion sur mobile. [#16dd187](https://github.com/suitenumerique/dictaphone/commit/16dd187)

### Évolutions techniques
- Mise à jour de Python à la version 3.14.5 et de Django à la version 5.12.4. [#c41aac4](https://github.com/suitenumerique/dictaphone/commit/c41aac4)
- Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest`. [#4e8ce56](https://github.com/suitenumerique/dictaphone/commit/4e8ce56)
- Refonte de la logique d'enregistrement sur mobile, avec gestion des erreurs et amélioration de la robustesse. [#a61d16e](https://github.com/suitenumerique/dictaphone/commit/a61d16e)
- Ajout d'un script pour automatiser les releases sur mobile. [#3b401b6](https://github.com/suitenumerique/dictaphone/commit/3b401b6)
- Amélioration de la gestion des états et des conditions de course lors du téléchargement de fichiers. [#c27e4ce](https://github.com/suitenumerique/dictaphone/commit/c27e4ce)
- Optimisation de la gestion des imports et correction d'erreurs liées à Vite. [#7f23140](https://github.com/suitenumerique/dictaphone/commit/7f23140)
- Ajout d'une commande pour nettoyer les fichiers en attente et supprimés. [#f270029](https://github.com/suitenumerique/dictaphone/commit/f270029)
- Mise en place d'un cronjob pour exécuter la commande de nettoyage des fichiers. [#69a917b](https://github.com/suitenumerique/dictaphone/commit/69a917b)
- Amélioration de la robustesse de la logique JWT et PKCE. [#8b81751](https://github.com/suitenumerique/dictaphone/commit/8b81751)

### Autres changements
- Ajout d'un lien vers la salle Matrix dans le README. [#75733f8](https://github.com/suitenumerique/dictaphone/commit/75733f8)
- Activation du suivi des erreurs PostHog sur mobile. [#9218d75](https://github.com/suitenumerique/dictaphone/commit/9218d75)
- Mise à jour de la documentation et des fichiers de configuration. [#d640ad9](https://github.com/suitenumerique/dictaphone/commit/d640ad9)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Publication des versions v0.6.0, v0.6.1, v0.6.2, v0.7.0 et v0.7.1. [#cb55612](https://github.com/suitenumerique/dictaphone/commit/cb55612)
