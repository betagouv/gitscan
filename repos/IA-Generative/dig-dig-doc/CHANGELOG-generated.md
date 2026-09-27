## Changelog : dig-dig-doc (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a marqué une étape majeure avec l'introduction de l'**Agent Helper**, un assistant intelligent capable d'interagir avec l'utilisateur via une interface de chat pour faciliter les analyses. La plateforme a également gagné en flexibilité grâce aux **analyses éphémères** (pour des tests rapides) et à l'automatisation des **résumés de documents et de dossiers**. L'interface utilisateur a été largement modernisée pour offrir une expérience plus fluide, plus intuitive et conforme aux standards du design système DSFR.

### Évolutions fonctionnelles
- **Assistant Intelligent (Agent Helper) :**
  - Mise en place d'une interface de chat interactive pour l'agent ([#50](https://github.com/IA-Generative/dig-dig-doc/issues/50)).
  - Possibilité de choisir le modèle LLM utilisé pour les conversations et les agents.
  - Ajout d'indicateurs visuels pour le suivi de la progression des tâches de l'agent.
  - Support du protocole MCP pour étendre les capacités de l'assistant ([#50](https://github.com/IA-Generative/dig-dig-doc/issues/50)).
- **Analyses Éphémères :** Création d'un mode d'analyse temporaire permettant de lancer des processus rapides avec suppression automatique des données et nettoyage du stockage S3 ([#22](https://github.com/IA-Generative/dig-dig-doc/issues/22), [#23](https://github.com/IA-Generative/dig-dig-doc/issues/23), [#24](https://github.com/IA-Generative/dig-dig-doc/issues/24)).
- **Gestion Documentaire Intelligente :**
  - Génération automatique de résumés pour les documents et les dossiers avec système de versioning ([#52](https://github.com/IA-Generative/dig-dig-doc/issues/52)).
  - Fonctionnalité « Dossier à ranger » proposant des suggestions d'analyse basées sur les résumés existants ([#54](https://github.com/IA-Generative/dig-dig-doc/issues/54)).
- **Expérience Utilisateur & Interface :**
  - **Profil & Statistiques :** Nouvelle page profil avec statistiques d'utilisation et respect du thème DSFR ([#61](https://github.com/IA-Generative/dig-dig-doc/issues/61)).
  - **Navigation :** Modernisation de la page d'accueil, ajout d'une barre latérale (sidebar) rétractable, et réorganisation du menu utilisateur (déplacement du bouton Tâches) ([#62](https://github.com/IA-Generative/dig-dig-doc/issues/62)).
  - **Aide & Tutoriels :** Intégration d'un système de tutoriels avec suivi de la progression de l'utilisateur.
  - **Monitoring :** Ajout d'un accès direct aux tâches en cours et d'un tableau de bord de statistiques plateforme ([#60](https://github.com/IA-Generative/dig-dig-doc/issues/60)).

### Évolutions techniques
- **Intelligence Artificielle :**
  - Intégration de **LangGraph** pour la gestion des workflows de l'agent helper ([#50](https://github.com/IA-Generative/dig-dig-doc/issues/50)).
  - Optimisation de la compatibilité avec les modèles **Scaleway AI** (gestion des appels d'outils parallèles).
- **Architecture Backend :**
  - Implémentation du modèle de données et des API REST pour la gestion des conversations de l'agent ([#50](https://github.com/IA-Generative/dig-dig-doc/issues/50)).
  - Refactoring des composants d'administration pour une meilleure modularité.
- **Infrastructure & DevOps :**
  - Mise en place de charts **Helm** incluant la gestion de l'autoscaling avec KEDA et des probes de santé.
  - Renforcement des pipelines CI/CD via GitHub Actions et GitLab CI.
  - Amélioration de l'authentification **Keycloak** (mapping des rôles et gestion des profils).
- **Qualité du code :** Nettoyage et formatage massif du code via **Ruff** pour le backend et le worker.

### Autres changements
- **Conformité :** Mise en place de conditions générales d'utilisation (CGU) versionnées avec blocage de l'accès en cas de non-acceptation ([#58](https://github.com/IA-Generative/dig-dig-doc/issues/58)).
- **Design :** Mise à jour de l'identité visuelle avec l'intégration du logo officiel Marianne (DSFR).
- **Documentation :** Amélioration de la documentation de l'API OpenAPI et ajout de guides pour l'utilisation du serveur MCP.
