## Changelog : ComparIA (30 derniers jours, au 2026-04-15)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de déploiement, de robustesse et de fonctionnalités. L'installation via Docker a été simplifiée et documentée. Des corrections ont été apportées pour résoudre des problèmes de configuration et de stabilité, notamment au niveau de la base de données et du reverse proxy. L'évaluation des modèles a été améliorée avec l'ajout de nouveaux modèles (Gemma 4) et une nouvelle approche pour la détection de spam.

### Évolutions fonctionnelles
- Ajout des modèles Gemma 4 26B A4B et Gemma 4 31B au catalogue de modèles disponibles. [#425](https://github.com/betagouv/ComparIA/pull/425) [#418](https://github.com/betagouv/ComparIA/pull/418)
- Implémentation d'un système de limitation de débit (rate limiting) pour la sélection de modèles personnalisés afin de prévenir les abus. [#384](https://github.com/betagouv/ComparIA/pull/384)
- Amélioration de la détection de spam et de contenu inapproprié en utilisant le modèle Gemini au lieu d'expressions régulières, et en persistant la détection dans la base de données. [#398](https://github.com/betagouv/ComparIA/pull/398)
- Ajout d'un captcha Altcha pour les endpoints de l'arène afin de limiter le spam. [#414](https://github.com/betagouv/ComparIA/pull/414)
- Mise à jour des modèles disponibles : archivage de Olmo-3-32b-think, LFM 2 8B A1B et Gemini 3 Pro. [#428](https://github.com/betagouv/ComparIA/pull/428) [#426](https://github.com/betagouv/ComparIA/pull/426) [#424](https://github.com/betagouv/ComparIA/pull/424)
- Ajout de nouveaux modèles Mistral Small 4 (119B MoE) et GPT 5.4 Mini et Nano.

### Évolutions techniques
- Simplification du processus d'installation avec Docker et ajout de documentation détaillée. [#429](https://github.com/betagouv/ComparIA/pull/429)
- Refonte de l'architecture de calcul des classements des modèles, avec stockage en cache Redis pour améliorer les performances.
- Amélioration de la gestion des erreurs et ajout de logs plus précis, notamment avec l'intégration de Loki.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité, notamment au niveau de la gestion des données et des requêtes à la base de données.
- Mise à jour des dépendances du frontend (jsdom, eslint) et du backend (pip).
- Correction de problèmes de configuration liés à PostgreSQL et Caddy.
- Amélioration de la gestion des pipelines CI/CD.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés.
- Corrections de traductions dans l'interface utilisateur (Estonien, Danois).
- Nettoyage du code et suppression de fichiers inutilisés.
- Mise à jour des modèles de données.
- Ajout de badges DeepWiki pour l'auto-rafraîchissement de la page.
