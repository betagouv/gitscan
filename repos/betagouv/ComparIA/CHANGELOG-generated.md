## Changelog : ComparIA (30 derniers jours, au 2026-04-15)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de déploiement, de robustesse et de fonctionnalités. L'installation via Docker a été simplifiée, la détection de spam a été améliorée, de nouveaux modèles de langage ont été ajoutés et des optimisations ont été apportées au calcul des classements. Des efforts importants ont également été consacrés à la maintenance et à la modernisation de l'infrastructure.

### Évolutions fonctionnelles
- **Installation simplifiée :** Une nouvelle méthode d'installation via Docker avec Caddy a été ajoutée, facilitant le déploiement de ComparIA. [#429](https://github.com/betagouv/ComparIA/pull/429)
- **Détection de spam améliorée :** La détection de spam et de contenu inapproprié a été améliorée en utilisant le modèle Gemini, remplaçant l'ancienne méthode basée sur des expressions régulières.  La détection de spam est maintenant persistée en base de données, comme les données personnelles. [#398](https://github.com/betagouv/ComparIA/pull/398)
- **Nouveaux modèles de langage :** Plusieurs nouveaux modèles de langage ont été ajoutés au catalogue, notamment Gemma 4 26B A4B, Gemma 4 31B, et Mistral Small 4 (119B MoE). Certains modèles obsolètes (Gemini 3 Pro, LFM 2 8B A1B, olmo-3-32b-think) ont été archivés. [#425](https://github.com/betagouv/ComparIA/pull/425), [#426](https://github.com/betagouv/ComparIA/pull/426), [#416](https://github.com/betagouv/ComparIA/pull/416), [#418](https://github.com/betagouv/ComparIA/pull/418), [#422](https://github.com/betagouv/ComparIA/pull/422)
- **Limitation du taux de requêtes :** Une limitation du taux de requêtes a été ajoutée pour la sélection personnalisée de modèles, afin de prévenir les abus. [#384](https://github.com/betagouv/ComparIA/pull/384)
- **Captcha Altcha :** Ajout d'un captcha Altcha pour les endpoints de l'arène. [#414](https://github.com/betagouv/ComparIA/pull/414)

### Évolutions techniques
- **Refonte du calcul des classements :** Le calcul des classements a été refactorisé pour utiliser Redis comme cache, améliorant ainsi les performances et réduisant la dépendance aux fichiers statiques. Les données de classement sont maintenant calculées en interne à partir de la base de données.
- **Amélioration de l'infrastructure DevOps :** Simplification des pipelines Jenkins et GitHub Actions, suppression de tâches inutiles et amélioration de la configuration Docker.
- **Logging amélioré :** Ajout de logging basé sur Loki pour une meilleure traçabilité et surveillance.
- **Mise à jour des dépendances :** Mise à jour de plusieurs dépendances, notamment eslint, jsdom, et les paquets npm.
- **Refactorisation du code :** Refactorisation de plusieurs parties du code, notamment les requêtes à la base de données et la gestion des modèles.
- **Correction de bugs :** Correction de plusieurs bugs liés à la configuration de PostgreSQL, aux erreurs Caddy, et à la gestion des timeouts.

### Autres changements
- **Documentation :** Amélioration de la documentation concernant l'installation via Docker et le processus d'initialisation de la base de données.
- **Traduction :** Mise à jour des traductions en estonien et en danois via Weblate.
- **Archivage de modèles :** Archivage de modèles de langage obsolètes pour maintenir la pertinence du catalogue.
- **Configuration Dependabot :** Configuration de Dependabot pour des mises à jour groupées moins fréquentes.
- **Suppression de scripts inutiles :** Suppression de scripts de mise à jour des classements et de vérification d'images.
