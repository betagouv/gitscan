## Changelog : mcr (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout de nouvelles fonctionnalités comme la gestion de notes personnalisées dans les rapports, l'intégration de conseils pour l'enregistrement des réunions et une interface utilisateur améliorée pour la gestion des livrables. Des efforts importants ont également été consacrés à l'amélioration de la robustesse et de l'observabilité du système, notamment avec l'ajout d'une meilleure instrumentation Langfuse et la correction de plusieurs bugs.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter des notes personnalisées aux rapports générés [#746](https://github.com/IA-Generative/mcr/issues/746).
- Implémentation d'une nouvelle interface pour gérer les livrables, incluant la possibilité de relancer la génération d'un livrable en cas d'échec [#720](https://github.com/IA-Generative/mcr/issues/720).
- Ajout d'un composant pour afficher des conseils et des informations utiles pendant l'enregistrement des réunions [#554](https://github.com/IA-Generative/mcr/issues/554).
- Nouvelle interface pour afficher l'état de l'enregistrement en cours [#553](https://github.com/IA-Generative/mcr/issues/553).
- Intégration d'un modal pour afficher des conseils spécifiques à Visio [#551](https://github.com/IA-Generative/mcr/issues/551).
- Amélioration de l'affichage des livrables sur la page de réunion [#546](https://github.com/IA-Generative/mcr/issues/546).
- Ajout d'une bannière pour encourager la contribution à la glossaire [#641](https://github.com/IA-Generative/mcr/issues/641).

### Évolutions techniques
- Refactorisation de la logique d'extraction de notes pour une meilleure modularité et testabilité [#634](https://github.com/IA-Generative/mcr/issues/634).
- Amélioration de la gestion des erreurs et des retries dans le pipeline de génération de rapports [#594](https://github.com/IA-Generative/mcr/issues/594).
- Ajout d'une instrumentation Langfuse plus complète pour une meilleure observabilité des processus de génération [#595](https://github.com/IA-Generative/mcr/issues/595).
- Refactorisation du code pour supprimer les dépendances obsolètes et améliorer la maintenabilité [#685](https://github.com/IA-Generative/mcr/issues/685).
- Mise à jour de la validation de la plateforme de réunion [#732](https://github.com/IA-Generative/mcr/issues/732).
- Suppression de plusieurs feature flags obsolètes [#712](https://github.com/IA-Generative/mcr/issues/712).
- Refactorisation de la logique de gestion des livrables pour permettre un seul livrable par type [#616](https://github.com/IA-Generative/mcr/issues/616).
- Amélioration de la gestion des erreurs lors de la récupération des fichiers audio [#409](https://github.com/IA-Generative/mcr/issues/409).
- Implémentation d'un nouveau pipeline de map-reduce générique [#613](https://github.com/IA-Generative/mcr/issues/613).

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture [#637](https://github.com/IA-Generative/mcr/issues/637).
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Mise à jour des dépendances et des outils de développement.
- Correction de plusieurs typos et améliorations de la lisibilité du code.
- Ajout de nouveaux acronymes au glossaire [#642](https://github.com/IA-Generative/mcr/issues/642).
- Amélioration des instructions de démarrage du projet local dans le README [#663](https://github.com/IA-Generative/mcr/issues/663).
- Correction d'erreurs mypy [#654](https://github.com/IA-Generative/mcr/issues/654).
