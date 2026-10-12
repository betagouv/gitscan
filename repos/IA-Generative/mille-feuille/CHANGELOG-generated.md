## Changelog : mille-feuille (30 derniers jours, au 11 octobre 2026)

### Résumé
Le projet a connu une transformation majeure ce mois-ci, marquée par son passage de "dig-dig-doc" à son identité actuelle, **mille-feuille**. La plateforme est passée d'un outil d'extraction à une solution complète de gestion documentaire assistée par IA. Les utilisateurs peuvent désormais non seulement analyser des documents, mais aussi interagir avec eux via un chat intelligent, générer automatiquement des documents officiels (PDF/ODT) et suivre l'avancement de leurs dossiers via un tableau de bord complet.

### Évolutions fonctionnelles
- **Intelligence Artificielle & Chat :**
    - Mise en place d'une interface de chat moderne (type ChatGPT) avec support du streaming, rendu Markdown et sélection de modèles LLM ([#8b08ebe](https://github.com/IA-Generative/mille-feuille/commit/8b08ebe)).
    - Capacité de l'assistant à citer ses sources : les réponses incluent des liens cliquables permettant d'ouvrir directement la page et le passage surligné dans le document source ([#a842f9b](https://github.com/IA-Generative/mille-feuille/commit/a842f9b)).
    - L'assistant peut désormais ajouter des notes internes directement dans le dossier via des outils dédiés ([#86e7802](https://github.com/IA-Generative/mille-feuille/commit/86e7802b9bbf06a76c052479cec8befe68119bb5)).
- **Génération de documents :**
    - Création automatisée de documents ODT et PDF à partir de modèles et de données extraites par l'IA ([#872cfee](https://github.com/IA-Generative/mille-feuille/commit/872cfee)).
    - Interface de revue de brouillons permettant de visualiser les valeurs de champs et de prévisualiser le rendu final ([#cbb2b77](https://github.com/IA-Generative/mille-feuille/commit/cbb2b77)).
- **Gestion des dossiers et analyses :**
    - Nouveau tableau de bord de suivi avec gestion des échéances, des statuts et des seuils de couleur pour prioriser les tâches ([#89d6267](https://github.com/IA-Generative/mille-feuille/commit/89d6267), [#89de67](https://github.com/IA-Generative/mille-feuille/commit/89d6267)).
    - Amélioration de l'expérience d'analyse : pagination des éléments et des notes, et possibilité de relancer une analyse ou de générer un résumé via un bouton dédié ([#057f7d6](https://github.com/IA-Generative/mille-feuille/commit/057f7d6), [#3eeb5b1](https://github.com/IA-Generative/mille-feuille/commit/3eeb5b1a867a79d2d0e8605578ed16c6b296d4b9)).
    - Ajout d'un historique complet des événements par dossier ([#6ae067b](https://github.com/IA-Generative/mille-feuille/commit/6ae067b)).
- **Interface Utilisateur :**
    - Modernisation de l'interface globale respectant les standards DSFR (logo Marianne, thèmes officiels) ([#f4fec37](https://github.com/IA-Generative/mille-feuille/commit/f4fec37)).

### Évolutions techniques
- **Architecture & Workers :**
    - Déploiement d'un worker spécialisé pour le rendu de documents via LibreOffice ([#90e2c64](https://github.com/IA-Generative/mille-feuille/commit/90e2c64)).
    - Introduction du mode "Éphémère" permettant des analyses rapides et temporaires avec nettoyage automatique des données ([#2753f5f](https://github.com/IA-Generative/mille-feuille/commit/2753f5f)).
    - Implémentation d'un serveur MCP (Model Context Protocol) pour étendre les capacités des agents ([#6e1068b](https://github.com/IA-Generative/mille-feuille/commit/6e1068b)).
- **Infrastructure & Déploiement :**
    - Mise en place complète de Helm charts incluant la gestion de Redis, Postgres et S3, avec autoscaling via KEDA ([#f2b0044](https://github.com/IA-Generative/mille-feuille/commit/f2b0044)).
    - Optimisation des processus de migration de base de données lors du déploiement.
- **Développement & SDK :**
    - Création de SDK Python (standard et éphémère) pour faciliter l'intégration de la plateforme ([#81049c3](https://github.com/IA-Generative/mille-feuille/commit/81049c3)).
    - Renforcement de la sécurité avec l'intégration de Keycloak pour la gestion des rôles et des accès par groupe ([#76c7689](https://github.com/IA-Generative/mille-feuille/commit/76c7689)).

### Autres changements
- **Rebranding :** Renommage complet du projet de `dig-dig-doc` vers `mille-feuille`.
- **Documentation :** Mise à jour massive de la documentation, incluant des exemples de dossiers types (contentieux, sécurité routière, etc.) et des guides d'utilisation des nouveaux agents ([#a21e6c7](https://github.com/IA-Generative/mille-feuille/commit/a21e6c7)).
- **Qualité de code :** Intégration de Ruff pour le linting et de Gitleaks pour la détection de secrets dans la CI.
