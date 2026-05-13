## Changelog : ComparIA (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en matière de détection de spam, d'ajout de nouveaux modèles de langage (GPT-5.5, DeepSeek V4, Kimi K2.6, Grok 4.20, Qwen 3.6 Plus, MiniMax M2.7, LFM2 24B A2B, GLM 5.1) et d'archivage de modèles obsolètes. Des efforts importants ont également été consacrés à la maintenance de la base de données, avec l'ajout d'outils pour l'archivage, la correction et la gestion des données corrompues. Enfin, des mises à jour de traduction ont été intégrées grâce à la communauté Weblate.

### Évolutions fonctionnelles
- **Nouveaux modèles de langage:** Ajout de plusieurs nouveaux modèles de langage pour les tests et comparaisons : GPT-5.5, DeepSeek V4 Pro et Flash, Kimi K2.6, Grok 4.20, Qwen 3.6 Plus, MiniMax M2.7, LFM2 24B A2B et GLM 5.1. [#444](https://github.com/betagouv/ComparIA/pull/444), [#445](https://github.com/betagouv/ComparIA/pull/445), [#455](https://github.com/betagouv/ComparIA/pull/455), [#456](https://github.com/betagouv/ComparIA/pull/456), [#461](https://github.com/betagouv/ComparIA/pull/461)
- **Archivage de modèles:** Archivage de 12 modèles de langage obsolètes. [#449](https://github.com/betagouv/ComparIA/pull/449)
- **Amélioration de la détection de spam:** Renforcement de la détection de spam grâce à la reconnaissance de schémas d'injection de code et de faux identifiants de session. [#467](https://github.com/betagouv/ComparIA/pull/467), [#468](https://github.com/betagouv/ComparIA/pull/468), [#472](https://github.com/betagouv/ComparIA/pull/472), [#473](https://github.com/betagouv/ComparIA/pull/473)
- **Mises à jour de traduction:** Intégration de mises à jour de traduction pour l'italien et le norvégien grâce à la communauté Weblate. [#443](https://github.com/betagouv/ComparIA/pull/443), [#459](https://github.com/betagouv/ComparIA/pull/459)

### Évolutions techniques
- **Refactoring base de données:** Refactorings importants de la base de données, incluant la suppression de colonnes obsolètes, la correction de données corrompues et l'amélioration des requêtes. [#454](https://github.com/betagouv/ComparIA/pull/454)
- **Outils de gestion de la base de données:** Ajout d'une interface en ligne de commande (CLI) pour la gestion de la base de données, incluant des outils pour l'archivage, la correction et l'analyse des données.
- **Suppression de la journalisation de la base de données:** Suppression de la journalisation de la base de données pour améliorer les performances. [#454](https://github.com/betagouv/ComparIA/pull/454)
- **Docker:** Simplification de l'installation via Docker. [#429](https://github.com/betagouv/ComparIA/pull/429)
- **Utilisation d'OpenRouter:** Passage à OpenRouter pour l'analyse LLM, abandonnant Vertex AI.
- **Amélioration de l'accessibilité:** Amélioration du contraste des couleurs pour une meilleure accessibilité. [#460](https://github.com/betagouv/ComparIA/pull/460)

### Autres changements
- Mise à jour de la documentation et du fichier README avec la feuille de route du projet. [#458](https://github.com/betagouv/ComparIA/pull/458)
- Mises à jour de dépendances mineures.
