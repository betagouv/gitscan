## Changelog : dictaphone (30 derniers jours, au 12 juin 2026)

### Résumé
Les dernières semaines ont été marquées par une amélioration significative de l'expérience utilisateur, en particulier sur l'application mobile. Des fonctionnalités importantes ont été ajoutées, comme la sélection de la langue de transcription avant l'enregistrement, la gestion des politiques de données, et une meilleure gestion des enregistrements hors ligne. Des corrections de bugs et des optimisations de performance ont également été apportées sur les applications web et mobile.

### Évolutions fonctionnelles
- Possibilité de sélectionner la langue de transcription avant de commencer un enregistrement, tant sur le web que sur le mobile. [#a030157](https://github.com/suitenumerique/dictaphone/pull/a030157) et [#3ddefed](https://github.com/suitenumerique/dictaphone/pull/3ddefed)
- Affichage et application des politiques de données sur le mobile, assurant la conformité et la transparence. [#67138e2](https://github.com/suitenumerique/dictaphone/pull/67138e2) et [#a7e14d2](https://github.com/suitenumerique/dictaphone/pull/a7e14d2)
- Gestion améliorée des enregistrements hors ligne sur le mobile : sauvegarde locale, synchronisation et suppression des fichiers audio après l'upload. [#c8eccc4](https://github.com/suitenumerique/dictaphone/pull/c8eccc4), [#6c2fd6e](https://github.com/suitenumerique/dictaphone/pull/6c2fd6e), [#4d9f77a](https://github.com/suitenumerique/dictaphone/pull/4d9f77a)
- Affichage d'une alerte sur le web lorsqu'un enregistrement est lancé depuis l'application mobile. [#1024be9](https://github.com/suitenumerique/dictaphone/pull/1024be9)
- Mode lecture seule pour les pages d'enregistrement. [#b64e23e](https://github.com/suitenumerique/dictaphone/pull/b64e23e)
- Amélioration de l'interface utilisateur pour la liste des enregistrements, avec un badge pour le statut de la transcription. [#aad2abd](https://github.com/suitenumerique/dictaphone/pull/aad2abd)
- Ajout de la possibilité de copier le texte de la transcription et d'ouvrir les documents associés. [#2252469](https://github.com/suitenumerique/dictaphone/pull/2252469)
- Ajout de sons de démarrage et d'arrêt lors de l'enregistrement sur mobile. [#fe272df](https://github.com/suitenumerique/dictaphone/pull/fe272df)
- Possibilité de télécharger un fichier non encore uploadé sur mobile. [#fe272df](https://github.com/suitenumerique/dictaphone/pull/fe272df)
- Amélioration de l'interface pour la sélection de la source audio lors de l'enregistrement. [#5d95a06](https://github.com/suitenumerique/dictaphone/pull/5d95a06)
- Ajout d'un indicateur visuel du niveau sonore pendant l'enregistrement. [#c43f0b5](https://github.com/suitenumerique/dictaphone/pull/c43f0b5)

### Évolutions techniques
- Mise à jour de Node.js en version 24 sur le frontend. [#62c7605](https://github.com/suitenumerique/dictaphone/pull/62c7605)
- Refonte de la gestion des enregistrements sur le frontend, avec une meilleure gestion des états et des performances. [#a61d16e](https://github.com/suitenumerique/dictaphone/pull/a61d16e)
- Amélioration de la robustesse de l'application mobile, notamment la gestion des autorisations et des erreurs. [#856b235](https://github.com/suitenumerique/dictaphone/pull/856b235) et [#6d7c112](https://github.com/suitenumerique/dictaphone/pull/6d7c112)
- Mise à jour des dépendances du backend (Python 3.14.5, Django 5.12.4). [#c41aac4](https://github.com/suitenumerique/dictaphone/pull/c41aac4)
- Mise en place de jobs cron pour la suppression des fichiers originaux et des fichiers supprimés. [#29854a4](https://github.com/suitenumerique/dictaphone/pull/29854a4)
- Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest`. [#3d7d025](https://github.com/suitenumerique/dictaphone/pull/3d7d025)
- Correction de vulnérabilités de sécurité via Snyk. [#cff3fce](https://github.com/suitenumerique/dictaphone/pull/cff3fce), [#7606de3](https://github.com/suitenumerique/dictaphone/pull/7606de3), [#060cc31](https://github.com/suitenumerique/dictaphone/pull/060cc31), [#25cb521](https://github.com/suitenumerique/dictaphone/pull/25cb521), [#1fbdb00](https://github.com/suitenumerique/dictaphone/pull/1fbdb00), [#c673daf](https://github.com/suitenumerique/dictaphone/pull/c673daf), [#f427600](https://github.com/suitenumerique/dictaphone/pull/f427600)

### Autres changements
- Mise à jour de la documentation et des mentions légales. [#182a6a7](https://github.com/suitenumerique/dictaphone/pull/182a6a7)
- Ajout d'un lien vers la salle Matrix. [#75733f8](https://github.com/suitenumerique/dictaphone/pull/75733f8)
- Améliorations de l'accessibilité sur le frontend. [#92d9ddb](https://github.com/suitenumerique/dictaphone/pull/92d9ddb), [#845e8f6](https://github.com/suitenumerique/dictaphone/pull/845e8f6), [#562d3e3](https://github.com/suitenumerique/dictaphone/pull/562d3e3), [#4448e09](https://github.com/suitenumerique/dictaphone/pull/4448e09), [#2e0ffc1](https://github.com/suitenumerique/dictaphone/pull/2e0ffc1), [#ba7e28a](https://github.com/suitenumerique/dictaphone/pull/ba7e28a), [#5d02804](https://github.com/suitenumerique/dictaphone/pull/5d02804), [#2400a0d](https://github.com/suitenumerique/dictaphone/pull/2400a0d), [#130ca0f](https://github.com/suitenumerique/dictaphone/pull/130ca0f)
- Nettoyage du code et suppression de code inutile. [#3e22d5b](https://github.com/suitenumerique/dictaphone/pull/3e22d5b), [#728986a](https://github.com/suitenumerique/dictaphone/pull/728986a), [#bbe4bb1](https://github.com/suitenumerique/dictaphone/pull/bbe4bb1)
