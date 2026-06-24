## Changelog : dictaphone (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, l'équipe a déployé plusieurs améliorations significatives pour l'application web, l'application mobile et le backend. Les utilisateurs bénéficieront d'une meilleure estimation de la durée de traitement des fichiers, d'une interface utilisateur plus intuitive pour la gestion des enregistrements, et d'une plus grande robustesse de l'application mobile. Des corrections de bugs et des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'informations sur la durée de traitement des fichiers sur mobile [#50cf735](https://github.com/suitenumerique/dictaphone/commit/50cf735).
- Affichage d'une estimation de la durée de traitement en cours sur l'interface web [#e21d89c](https://github.com/suitenumerique/dictaphone/commit/e21d89c).
- Ajout de boutons pour ajuster la vitesse de lecture sur l'interface web [#d41ab07](https://github.com/suitenumerique/dictaphone/commit/d41ab07).
- Amélioration de l'expérience utilisateur pour la sélection de la langue de transcription, avec une option précoce de sélection et une gestion des erreurs améliorée [#70c4bce](https://github.com/suitenumerique/dictaphone/commit/70c4bce), [#a030157](https://github.com/suitenumerique/dictaphone/commit/a030157), [#83eca2b](https://github.com/suitenumerique/dictaphone/commit/83eca2b).
- Ajout d'une alerte sur mobile lors du premier lancement concernant l'optimisation de la batterie [#4262b3a](https://github.com/suitenumerique/dictaphone/commit/4262b3a).
- Possibilité de télécharger un fichier non encore uploadé sur mobile [#fe272df](https://github.com/suitenumerique/dictaphone/commit/fe272df).
- Ajout de sons de démarrage et d'arrêt pour l'enregistrement sur mobile [#6762996](https://github.com/suitenumerique/dictaphone/commit/6762996).
- Amélioration de l'interface pour la liste des enregistrements sur le frontend [#6cc6254](https://github.com/suitenumerique/dictaphone/commit/6cc6254).
- Ajout d'options d'export avancées pour les transcriptions, notamment au format SRT [#f49ee75](https://github.com/suitenumerique/dictaphone/commit/f49ee75).
- Ajout d'actions "Copier le texte" et "Ouvrir dans Docs" au menu des fichiers [#2252469](https://github.com/suitenumerique/dictaphone/commit/2252469).
- Affichage de la source et de la durée des fichiers audio dans l'interface d'administration Django [#ac192c3](https://github.com/suitenumerique/dictaphone/commit/ac192c3).

### Évolutions techniques
- Mise à jour de Node vers la version 24 sur le frontend [#62c7605](https://github.com/suitenumerique/dictaphone/commit/62c7605).
- Amélioration de l'estimation de la durée de traitement des fichiers sur le backend [#efad892](https://github.com/suitenumerique/dictaphone/commit/efad892), [#dd3fd17](https://github.com/suitenumerique/dictaphone/commit/dd3fd17).
- Refonte du calcul de la durée de traitement pour une meilleure précision [#2efacaf](https://github.com/suitenumerique/dictaphone/commit/2efacaf).
- Amélioration de la gestion des jobs Celery pour une estimation plus précise du temps de traitement [#50cf735](https://github.com/suitenumerique/dictaphone/commit/50cf735).
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité [#7606de3](https://github.com/suitenumerique/dictaphone/commit/7606de3), [#060cc31](https://github.com/suitenumerique/dictaphone/commit/060cc31), [#25cb521](https://github.com/suitenumerique/dictaphone/commit/25cb521), [#1fbdb00](https://github.com/suitenumerique/dictaphone/commit/1fbdb00), [#c673daf](https://github.com/suitenumerique/dictaphone/commit/c673daf), [#f427600](https://github.com/suitenumerique/dictaphone/commit/f427600).
- Mise à jour de Python vers la version 3.14.5 et Django vers la version 5.12.4 [#c41aac4](https://github.com/suitenumerique/dictaphone/commit/c41aac4).
- Ajout de jobs cron pour la suppression des fichiers originaux et des données obsolètes [#29854a4](https://github.com/suitenumerique/dictaphone/commit/29854a4).
- Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest` [#4e8ce56](https://github.com/suitenumerique/dictaphone/commit/4e8ce56).
- Ajout de logs plus détaillés pour faciliter le débogage des problèmes d'authentification mobile [#600e899](https://github.com/suitenumerique/dictaphone/commit/600e899).

### Autres changements
- Correction de bugs divers sur le frontend et le mobile [#ee0b5cc](https://github.com/suitenumerique/dictaphone/commit/ee0b5cc), [#61c1623](https://github.com/suitenumerique/dictaphone/commit/61c1623), [#bd4bec3](https://github.com/suitenumerique/dictaphone/commit/bd4bec3), [#b681b4d](https://github.com/suitenumerique/dictaphone/commit/b681b4d), [#c293117](https://github.com/suitenumerique/dictaphone/commit/c293117), [#6d7c112](https://github.com/suitenumerique/dictaphone/commit/6d7c112), [#53905c6](https://github.com/suitenumerique/dictaphone/commit/53905c6), [#3677d59](https://github.com/suitenumerique/dictaphone/commit/3677d59), [#0ac2d87](https://github.com/suitenumerique/dictaphone/commit/0ac2d87), [#4f2a60c](https://github.com/suitenumerique/dictaphone/commit/4f2a60c).
- Amélioration de l'accessibilité de l'interface web [#f427600](https://github.com/suitenumerique/dictaphone/commit/f427600), [#92d9ddb](https://github.com/suitenumerique/dictaphone/commit/92d9ddb), [#845e8f6](https://github.com/suitenumerique/dictaphone/commit/845e8f6), [#562d3e3](https://github.com/suitenumerique/dictaphone/commit/562d3e3), [#4448e09](https://github.com/suitenumerique/dictaphone/commit/4448e09), [#2400a0d](https://github.com/suitenumerique/dictaphone/commit/2400a0d), [#130ca0f](https://github.com/suitenumerique/dictaphone/commit/130ca0f).
- Ajout d'un lien vers la salle Matrix dans le README [#75733f8](https://github.com/suitenumerique/dictaphone/commit/75733f8).
- Correction d'un problème de réhydratation des stores sur mobile [#6762996](https://github.com/suitenumerique/dictaphone/commit/6762996).
- Mise en place de PostHog pour le suivi des erreurs sur mobile [#9218d75](https://github.com/suitenumerique/dictaphone/commit/9218d75).
- Ajout de la configuration de logging depuis la documentation [#9ac99e9](https://github.com/suitenumerique/dictaphone/commit/9ac99e9).
- Correction d'une vulnérabilité Dockerfile [#cff3fce](https://github.com/suitenumerique/dictaphone/commit/cff3fce).
