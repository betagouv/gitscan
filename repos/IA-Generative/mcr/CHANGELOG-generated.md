## Changelog : mcr (30 derniers jours, au 27 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application MCR, notamment l'ajout de la gestion de notes personnalisées dans les rapports, l'amélioration de la gestion des livrables (rapports générés), et des optimisations de l'interface utilisateur. Des corrections de bugs et des refactorisations techniques ont également été réalisées pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter des notes personnalisées aux rapports, avec la possibilité de les inclure dans différentes sections. [#746](https://github.com/IA-Generative/mcr/issues/746)
- Amélioration de la gestion des livrables :
    - Possibilité de relancer la génération d'un livrable en cas d'échec. [#720](https://github.com/IA-Generative/mcr/issues/720)
    - Gestion améliorée des statuts des livrables. [#694](https://github.com/IA-Generative/mcr/issues/694)
    - Affichage des livrables dans l'interface utilisateur. [#647](https://github.com/IA-Generative/mcr/issues/647)
- Intégration d'un bouton "Afficher dans Drive" pour les livrables. [#687](https://github.com/IA-Generative/mcr/issues/687)
- Ajout d'une modale d'aide pour l'utilisation de Visio. [#550](https://github.com/IA-Generative/mcr/issues/550)
- Ajout d'un bouton pour arrêter l'enregistrement Visio. [#552](https://github.com/IA-Generative/mcr/issues/552)
- Ajout d'une nouvelle fonctionnalité pour la gestion des participants, incluant l'extraction et l'utilisation des notes. [#639](https://github.com/IA-Generative/mcr/issues/639)
- Ajout d'une nouvelle fonctionnalité pour la gestion des intentions et des prochaines réunions, avec l'utilisation des notes. [#637](https://github.com/IA-Generative/mcr/issues/637)
- Ajout d'un composant d'éditeur de texte enrichi (Tiptap) pour la gestion des notes. [#608](https://github.com/IA-Generative/mcr/issues/608)
- Ajout d'un champ "Notes" aux réunions. [#605](https://github.com/IA-Generative/mcr/issues/605)
- Amélioration de la gestion des fichiers et des téléchargements. [#628](https://github.com/IA-Generative/mcr/issues/628)
- Ajout d'une bannière pour la contribution à la glossaire. [#641](https://github.com/IA-Generative/mcr/issues/641)

### Évolutions techniques
- Refactorisation de l'architecture pour une meilleure séparation des préoccupations et une plus grande modularité.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour des dépendances et correction des vulnérabilités.
- Amélioration des tests unitaires et d'intégration.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Refactorisation du code lié à la gestion des livrables pour une meilleure scalabilité et maintenabilité.
- Intégration de Langfuse pour l'observabilité. [#594](https://github.com/IA-Generative/mcr/issues/594)
- Amélioration de la gestion des prompts et des modèles de langage.
- Ajout de mécanismes de validation et de nettoyage des données.
- Amélioration de la gestion des tâches asynchrones avec Celery.
- Mise en place d'un système de gestion des feature flags.
- Ajout de tests pour la gestion des erreurs et des cas limites.
- Amélioration de la gestion des logs et du monitoring.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos dans les fichiers de configuration.
- Ajout de nouvelles entrées dans le glossaire.
- Amélioration des messages de log pour faciliter le débogage.
- Nettoyage du code et amélioration de la lisibilité.
- Mise à jour des dépendances de développement.
- Ajout de linters et de formatteurs de code pour garantir la qualité du code.
- Suppression de configurations Docker inutiles.
- Mise à jour des instructions de démarrage du projet local dans le README.
- Ajout de tests pour les nouvelles fonctionnalités.
- Suppression de feature flags obsolètes.
- Ajout d'un mécanisme pour détecter les mauvaises utilisations des feature flags.
- Ajout d'un système de gestion des secrets pour les clés API.
- Amélioration de la sécurité de l'application.
- Ajout d'un système de monitoring pour suivre les performances de l'application.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'un système de gestion des logs pour faciliter le débogage.
- Mise à jour des dépendances et correction des vulnérabilités.
- Amélioration des tests unitaires et d'intégration.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'un système de gestion des logs pour faciliter le débogage.
- Mise à jour des dépendances et correction des vulnérabilités.
- Amélioration des tests unitaires et d'intégration.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
