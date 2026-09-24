## Changelog : dig-dig-doc (30 derniers jours, au 24 septembre 2026)

### Résumé
Le projet a connu une progression massive, passant d'un socle initial à une plateforme fonctionnelle et structurée. Les utilisateurs disposent désormais d'une interface moderne basée sur le design système DSFR, de capacités d'intelligence artificielle avancées (chat en streaming, choix du modèle LLM, extraction d'entités) et d'outils complets pour l'analyse et le reporting de documents.

### Évolutions fonctionnelles
- **Intelligence Artificielle & Chat :**
    - Interface de chat interactive avec support du streaming de texte, rendu Markdown et citation des sources.
    - Possibilité de sélectionner le modèle LLM utilisé pour les conversations et les agents.
    - Nouvelles fonctionnalités d'analyse : classification automatique, extraction d'entités et génération de rapports.
    - Affichage de jauges de confiance pour les résultats d'analyse.
- **Traitement Documentaire :**
    - Amélioration de l'extraction de texte ([#4](https://github.com/IA-Generative/dig-dig-doc/issues/4)) incluant la détection des blocs de mise en page (bounding boxes).
    - Visualisation enrichie des résultats via des carrousels de cartes et des onglets dédiés par type d'analyse.
    - Gestion des métadonnées de documents et partage d'analyses.
- **Interface Utilisateur (UI) :**
    - Refonte complète de l'interface utilisateur basée sur le socle DSFR (Design Système de l'État).
    - Navigation optimisée avec une barre latérale (sidebar) rétractable, gestion du profil et pagination des listes.
    - Mise en place d'une page d'accueil et d'une organisation structurée pour les dossiers et les analyses.

### Évolutions techniques
- **Infrastructure & Déploiement :**
    - Création de charts Helm incluant la gestion des dépendances (Redis, PostgreSQL) et les jobs de migration.
    - Automatisation complète du cycle de vie (CI/CD) via GitHub Actions et GitLab (publication d'images, gestion des versions).
    - Ajout de Docker-compose pour faciliter l'environnement de développement local.
- **Architecture Backend :**
    - Intégration de l'authentification Keycloak pour le Backend-for-Frontend (BFF).
    - Implémentation de Server-Sent Events (SSE) pour la communication en temps réel.
    - Renforcement de la robustesse avec des health checks étendus (PostgreSQL, S3) et un système de jetons d'application.
    - Refonte du modèle de données pour optimiser la gestion des analyses, des dossiers et des coordonnées de mise en page.

### Autres changements
- Correction de fichiers de migration en doublon.
- Mise en place de l'étape de linting et de tests unitaires dans le workflow de pré-commit.
- Nettoyage et optimisation de la configuration Docker.
