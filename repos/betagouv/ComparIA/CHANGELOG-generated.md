## Changelog : ComparIA (30 derniers jours, au 08 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en matière de détection de spam, de gestion des modèles de langage (ajout, archivage, mises à jour) et d'infrastructure. Des corrections ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme, notamment au niveau de la gestion de la base de données et de l'installation via Docker. L'accessibilité a également été améliorée avec des ajustements de contraste.

### Évolutions fonctionnelles
- **Détection de spam améliorée :** La détection de spam a été renforcée grâce à l'intégration du modèle Gemini pour une identification plus précise des contenus indésirables et des bots. Les détections de spam sont désormais persistées dans la base de données, comme les données PII. [#398](https://github.com/betagouv/ComparIA/pull/398)
- **Ajout de nouveaux modèles de langage :** Les modèles Gemma 4 26B A4B et 31B, Kimi K2.6, DeepSeek V4 Pro et Flash, et GPT-5.5 ont été ajoutés au catalogue de modèles disponibles.
- **Archivage de modèles obsolètes :** Les modèles Olmo-3-32b-think, LFM2 8B A1B et Gemini 3 Pro ont été archivés en raison de leur obsolescence ou d'indisponibilité.
- **Amélioration de l'accessibilité :** Le contraste de la couleur violette primaire a été amélioré pour une meilleure accessibilité. [#460](https://github.com/betagouv/ComparIA/pull/460)
- **Gestion des intervalles de confiance du classement :** Correction d'un problème empêchant le calcul des intervalles de confiance du classement. [#470](https://github.com/betagouv/ComparIA/pull/470)

### Évolutions techniques
- **Refonte de l'infrastructure Docker :** Une nouvelle infrastructure Docker a été mise en place pour simplifier l'installation et le déploiement de ComparIA, incluant un reverse proxy Caddy.
- **Optimisation de la base de données :** Plusieurs optimisations ont été apportées à la base de données, notamment la suppression de colonnes obsolètes, la correction de requêtes et l'ajout d'index pour améliorer les performances.
- **Amélioration de la gestion des logs :** La journalisation des actions sur la base de données a été améliorée pour faciliter le débogage et la surveillance.
- **Mise à jour des dépendances :** Plusieurs dépendances ont été mises à jour vers leurs dernières versions stables, notamment jsdom, eslint et les paquets npm/yarn.
- **Correction de bugs et améliorations diverses :** Correction de plusieurs bugs mineurs et améliorations diverses de la qualité du code.
- **Intégration de Weblate :** Intégration des dernières traductions depuis Weblate. [#443](https://github.com/betagouv/ComparIA/pull/443)

### Autres changements
- **Documentation :** Amélioration de la documentation concernant l'installation via Docker et le processus d'initialisation de la base de données.
- **Roadmap :** Mise à jour de la roadmap du projet. [#458](https://github.com/betagouv/ComparIA/pull/458)
- **Corrections de typos et améliorations de la lisibilité du code.**
- **Mise à jour des traductions italiennes et norvégiennes.**
