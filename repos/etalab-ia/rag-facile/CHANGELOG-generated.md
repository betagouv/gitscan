## Changelog : rag-facile (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par d'importantes améliorations de la plateforme rag-facile, notamment l'ajout de l'authentification et de la persistance des conversations via Supabase, une refonte de l'architecture interne pour une meilleure modularité, et l'ajout de nouvelles fonctionnalités comme l'intégration de l'IA Inspect pour l'évaluation de la qualité des réponses et un système de compétences pour l'agent conversationnel. De nombreuses corrections de bugs et améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'authentification via Supabase et persistance des conversations. Les utilisateurs peuvent maintenant se connecter et retrouver leurs conversations précédentes.
- Intégration de l'IA Inspect pour l'évaluation de la qualité des réponses (précision, rappel, fidélité).
- Système de compétences pour l'agent conversationnel, permettant d'étendre ses capacités.
- Amélioration de l'interface utilisateur avec l'ajout d'un thème DSFR (Design Système Français).
- Ajout d'un nouveau flux d'installation avec une interface plus conviviale et la possibilité de choisir la langue.
- Possibilité de configurer et de personnaliser le système via des commandes CLI.
- Ajout de la gestion des collections de documents (ajout, suppression, activation/désactivation).
- Amélioration de la recherche avec l'ajout de l'expansion de requête et de stratégies HyDE.
- Ajout de la possibilité d'utiliser des collections publiques Albert.

### Évolutions techniques
- Refonte de l'architecture interne pour une meilleure modularité et maintenabilité, avec l'extraction de packages pour l'ingestion, le contexte, le reranking et l'orchestration.
- Utilisation de `uv` pour la gestion des dépendances et des environnements virtuels.
- Amélioration du système de tests avec l'ajout de tests d'intégration et de tests unitaires.
- Mise à jour des dépendances vers les dernières versions stables.
- Ajout d'un système de tracing pour le débogage et l'analyse des performances.
- Utilisation de worktrees pour un développement plus efficace.
- Amélioration du script d'installation pour une meilleure compatibilité avec différents systèmes d'exploitation.
- Ajout de la gestion des secrets via des variables d'environnement.
- Utilisation de git pour la gestion des sessions et la persistance des données.

### Autres changements
- Ajout de documentation sur l'utilisation de la plateforme et le développement.
- Amélioration des messages d'erreur et des messages d'aide.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'un guide pour les contributeurs.
- Ajout d'un fichier `.gitignore` pour ignorer les fichiers inutiles.
- Mise à jour des badges de version et des liens vers les dépôts.
