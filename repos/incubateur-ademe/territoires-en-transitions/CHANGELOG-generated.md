## Changelog : territoires-en-transitions (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois a été marqué par une restructuration majeure de la gestion des démarches (notamment le PCAET) et une transition importante vers les nouveaux référentiels. Les capacités d'analyse des collectivités ont été renforcées avec une meilleure gestion de la pertinence des leviers d'action. Parallèlement, le système de gestion documentaire a été profondément modernisé pour offrir plus de sécurité et de fiabilité lors des dépôts de fichiers.

### Évolutions fonctionnelles
- **Gestion des démarches (PCAET) :**
  - Amélioration du cycle d'instruction avec un suivi précis des avis, des notifications aux services et des étapes de validation.
  - Possibilité pour les services instructeurs de consulter des dossiers encore en cours d'élaboration.
  - Meilleure gestion des périmètres géographiques (EPCI, communes membres) et des dossiers de révision.
- **Référentiels et Bascule :**
  - Mise en œuvre de la transition vers le référentiel CR, incluant la gestion des commentaires, des scores et des actions d'origine.
  - Affichage des référentiels archivés dans la navigation avec un indicateur spécifique.
- **Analyse des collectivités et leviers :**
  - Les administrateurs peuvent désormais qualifier la pertinence des leviers et de leurs catégories.
  - Affichage détaillé des actions déjà rattachées à chaque levier et visualisation de la mobilisation par volet.
  - Introduction de la possibilité de déclarer un indicateur comme "non applicable".
- **Gestion documentaire :**
  - Amélioration du processus de dépôt de fichiers (gestion des signatures, détection des doublons et téléchargement sécurisé via le backend).
  - Possibilité de reclasser des documents directement depuis l'interface.
  - Amélioration de la visibilité des documents (gestion des fichiers confidentiels et des erreurs de lecture).
- **Interface utilisateur (UI) :**
  - Mise en conformité de la page des leviers avec les maquettes de design.
  - Améliorations de l'accessibilité (navigation au clavier pour les accordéons, tableaux plus lisibles et conformes au design system).

### Évolutions techniques
- **Architecture et Backend :**
  - Refactoring massif des services de gestion des documents, des plans et des indicateurs pour une meilleure modularité.
  - Optimisation du moteur de classification par IA (gestion des accents, découpage en lots pour plus de résilience).
  - Amélioration de la gestion des jetons (tokens) pour les appels LLM et les téléchargements de fichiers.
- **Infrastructure et CI/CD :**
  - Migration des processus de déploiement d'Earthly vers des Dockerfile natifs et des workflows GitHub Actions.
  - Mise en place de Nx Cloud pour optimiser les performances des tâches de CI.
  - Renforcement des workflows de maintenance de la base de données et de gestion des migrations (Sqitch).
- **Outils et Automatisation :**
  - Amélioration de l'intégration CRM/Crisp pour enrichir les conversations avec les données des collectivités et des utilisateurs.
  - Synchronisation quotidienne des groupes PostHog pour le suivi analytique.

### Autres changements
- **Documentation :** Mise à jour de plusieurs ADR (Architecture Decision Records) concernant la périodicité des indicateurs et les choix d'architecture.
- **Nettoyage :** Suppression complète de l'application "panier" et de ses dépendances techniques associées.
- **Qualité :** Augmentation de la couverture de tests (E2E et unitaires) sur les modules critiques (PCAET, documents, référentiels).
