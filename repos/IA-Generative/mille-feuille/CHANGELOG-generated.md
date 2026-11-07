## Changelog : mille-feuille (30 derniers jours, au 05/11/2026)

### Résumé
Ce mois-ci, mille-feuille a franchi une étape majeure en renforçant l'intelligence et l'autonomie de ses agents. Les utilisateurs bénéficient désormais d'un moteur de recherche beaucoup plus puissant, de la possibilité d'ajouter des sources de connaissances externes et d'une interface modernisée incluant un mode sombre/clair. Le système est devenu plus robuste grâce à une migration de plusieurs processus critiques vers le backend.

### Évolutions fonctionnelles
- **Chat & Agents** : 
    - Amélioration de l'interaction avec les agents (possibilité de les appeler via `@Nom`, réponses en streaming, et affichage de l'agent qui répond).
    - Introduction d'un système d'outils pour les agents (calculatrice, gestion des dates, et support du protocole MCP pour des outils externes).
    - Nouveau système d'autorisation permettant de valider ou refuser l'utilisation d'un outil par l'assistant.
    - Amélioration de la citation des sources dans le chat avec un affichage précis par ligne.
- **Recherche & Connaissances** :
    - Mise en place d'une recherche hybride (combinant recherche textuelle et sémantique) pour des résultats plus pertinents.
    - Ajout d'une fonctionnalité de "Base de connaissances" permettant d'intégrer des sources externes via URL.
    - Nouveaux réglages de recherche permettant de gérer l'indexation et la reconstruction des données.
- **Analyse & Documents** :
    - Amélioration de l'extraction de données (entités, classification visuelle via CLIP, et extraction de texte par page).
    - Gestion des dossiers enrichie : ajout de fichiers après coup, génération de résumés automatiques et visualisation des zones d'extraction directement sur les pages.
    - Possibilité de modifier ou de supprimer des analyses existantes.
- **Interface Utilisateur** :
    - Introduction du mode clair et mode sombre.
    - Refonte visuelle du tableau de bord, de la page de profil et du pied de page.
    - Optimisation de l'affichage des calendriers et des dates.

### Évolutions techniques
- **Architecture & Backend** :
    - Migration des tâches lourdes (agents d'analyse, indexation de recherche, et exécution des outils) du worker vers le backend pour une meilleure stabilité.
    - Suppression du worker `agent_execution` au profit d'une gestion centralisée.
- **Moteur de recherche** :
    - Intégration de Qdrant pour la gestion des index et de la recherche hybride.
    - Implémentation d'une stratégie de reconstruction d'index "blue/green" pour permettre des mises à jour sans interruption de service.
- **IA & Traitement de documents** :
    - Optimisation des pods OCR avec l'intégration de PaddleOCR (layout, table, vision).
    - Amélioration du stockage des données textuelles pour conserver la position précise (lignes/mots) des éléments extraits.
- **Infrastructure & Déploiement** :
    - Mise à jour majeure des charts Helm (intégration de Qdrant, gestion des secrets via Vault, et optimisation des ressources).
    - Amélioration de la CI/CD (nettoyage des processus GitLab au profit de GitHub Actions).

### Autres changements
- Renommage officiel du projet de `dig-dig-doc` à `mille-feuille`.
- Mise à jour de la documentation technique (Helm, agents, et guides d'utilisation de l'API éphémère).
