## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 03/09/2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une amélioration majeure de la fiabilité de l'indexation documentaire grâce à une refonte du traitement OCR. L'expérience utilisateur est enrichie par de nouveaux outils de pilotage des évaluations et une meilleure visibilité sur les erreurs de traitement. Enfin, une campagne de mise à jour a permis de corriger plusieurs vulnérabilités de sécurité critiques.

### Évolutions fonctionnelles
- **Évaluation** : Ajout d'une interface dédiée permettant de lancer et de gérer les processus d'évaluation.
- **Visibilité Backoffice** : Amélioration du suivi avec l'affichage des pages non indexées et la remontée explicite des erreurs (lors de l'indexation ou de la création de collections).
- **Interface Utilisateur** : Optimisation de l'affichage pour les chemins de sections trop longs et ajout de la possibilité de sélectionner une collection à modifier.

### Évolutions techniques
- **Sécurité** : Correction de plusieurs vulnérabilités critiques (High/Moderate) via la mise à jour de dépendances clés ([#149](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/149), [#150](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/150), [#141](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/141), etc.).
- **Moteur d'indexation (OCR)** : Refonte complète du convertisseur OCR JSON pour une gestion plus fine des structures complexes (tableaux, listes, titres) et de la continuité entre les pages.
- **Résilience** : Amélioration de la robustesse du pipeline pour permettre l'indexation de documents même si des erreurs surviennent sur certaines pages OCR.
- **Optimisation & Refactoring** : Refactorisation du domaine PDF, réduction de la fréquence de suivi de l'indexation et nettoyage important des tests et des pipelines obsolètes.

### Autres changements
- Mise à jour de la documentation (README).
