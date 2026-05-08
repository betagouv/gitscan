## Changelog : ComparIA (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en matière de détection de spam, avec l'introduction d'un nouveau modèle basé sur Gemini. Plusieurs modèles de langage ont été ajoutés au catalogue (GPT-5.5, DeepSeek V4, Kimi K2.6, Gemma 4 26B A4B) et d'autres archivés. Des corrections et améliorations ont été apportées à la gestion de la base de données et à l'infrastructure, notamment pour simplifier l'installation via Docker. Des mises à jour de traduction ont également été intégrées.

### Évolutions fonctionnelles
- **Détection de spam améliorée:** Le système de détection de spam a été amélioré grâce à l'intégration du modèle Gemini, remplaçant l'approche basée sur des expressions régulières. [#398](https://github.com/betagouv/ComparIA/pull/398)
- **Ajout de nouveaux modèles de langage:**
    - Ajout de GPT-5.5 et GPT-5.5 Pro. [#461](https://github.com/betagouv/ComparIA/pull/461)
    - Ajout de DeepSeek V4 Pro et Flash. [#455](https://github.com/betagouv/ComparIA/pull/455)
    - Ajout de Kimi K2.6. [#425](https://github.com/betagouv/ComparIA/pull/425)
    - Ajout de Gemma 4 26B A4B. [#425](https://github.com/betagouv/ComparIA/pull/425)
- **Archivage de modèles obsolètes:** Plusieurs modèles de langage ont été archivés car ils ne sont plus disponibles ou ont été remplacés par des versions plus récentes (OLMO 3 32B Think, LFM2 8B A1B). [#426](https://github.com/betagouv/ComparIA/pull/426), [#428](https://github.com/betagouv/ComparIA/pull/428)
- **Amélioration de la gestion des classements:** Correction d'un problème lié aux intervalles de confiance dans le calcul des classements. [#470](https://github.com/betagouv/ComparIA/pull/470)
- **Amélioration de la robustesse du système de classement:** Gestion des modèles dégénérés dans le calcul du Bradley-Terry bootstrap. [#469](https://github.com/betagouv/ComparIA/pull/469)
- **Amélioration de l'accessibilité:** Amélioration du contraste des couleurs pour les boutons principaux afin d'améliorer l'accessibilité. [#460](https://github.com/betagouv/ComparIA/pull/460)

### Évolutions techniques
- **Refonte de la gestion de la base de données:**
    - Suppression de la journalisation des requêtes SQL pour améliorer les performances et la sécurité. [#454](https://github.com/betagouv/ComparIA/pull/454)
    - Nettoyage et refactorisation des requêtes SQL et des migrations de la base de données.
    - Ajout d'utilitaires en ligne de commande pour la gestion de la base de données (archivage, correction de données corrompues, etc.).
    - Persistance de la détection de spam dans la base de données. [#398](https://github.com/betagouv/ComparIA/pull/398)
- **Infrastructure:**
    - Simplification du processus d'installation avec une image Docker autonome utilisant Caddy comme reverse proxy. [#429](https://github.com/betagouv/ComparIA/pull/429)
    - Mise à jour des dépendances (npm, eslint, jsdom).
- **Correction de bugs:**
    - Correction d'erreurs de typage dans le code backend. [#473](https://github.com/betagouv/ComparIA/pull/473)
    - Correction de problèmes liés à l'injection d'ID de session hexadécimaux. [#453](https://github.com/betagouv/ComparIA/pull/453)
    - Correction de problèmes liés à la gestion des modèles OpenRouter et de leurs niveaux d'accès. [#461](https://github.com/betagouv/ComparIA/pull/461)

### Autres changements
- **Documentation:** Amélioration de la documentation concernant le processus d'initialisation de la base de données et l'installation via Docker.
- **Traduction:** Mises à jour des traductions en italien et en norvégien (Bokmål et Nynorsk). [#443](https://github.com/betagouv/ComparIA/pull/443)
- **Roadmap:** Mise à jour de la roadmap du projet. [#458](https://github.com/betagouv/ComparIA/pull/458)
- **Mise à jour des modèles:** Mise à jour de la liste des modèles de langage disponibles.
