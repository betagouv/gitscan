## Changelog : ComparIA (30 derniers jours, au 28 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la plateforme ComparIA, notamment l'ajout de nouveaux modèles de langage (GPT-5.5, DeepSeek V4, Gemma 4), des corrections de bugs et des optimisations de performance, en particulier au niveau de la base de données.  Des efforts significatifs ont également été déployés pour améliorer la robustesse de la plateforme, notamment en matière de détection de spam et de gestion des erreurs. Enfin, l'infrastructure de déploiement a été simplifiée avec l'ajout d'une installation Docker simplifiée.

### Évolutions fonctionnelles
- Ajout des modèles de langage GPT-5.5 et GPT-5.5 Pro pour l'évaluation.
- Ajout des modèles de langage DeepSeek V4 Pro et Flash.
- Ajout du modèle Gemma 4 26B et 31B.
- Amélioration de la détection de spam grâce à l'utilisation du modèle Gemini et à la persistance des résultats dans la base de données.
- Implémentation d'un système de limitation de débit (rate limiting) pour l'utilisation des modèles personnalisés, afin de prévenir les abus.
- Ajout d'un captcha Altcha pour protéger les endpoints de l'arène.
- Ajout d'une commande CLI pour l'archivage des données corrompues.
- Ajout d'une commande CLI pour l'export des datasets.
- Ajout de la possibilité de construire des datasets pour un pays spécifique.

### Évolutions techniques
- Refactorisation importante de la gestion de la base de données, incluant la suppression de colonnes obsolètes et l'optimisation des requêtes.
- Amélioration de la gestion des logs et des erreurs, avec une dégradation gracieuse en cas de problème avec le service Loki.
- Simplification de l'infrastructure de déploiement avec l'ajout d'une installation Docker simplifiée.
- Refactorisation des scripts Jenkins pour une meilleure maintenabilité.
- Utilisation de `cyclopts` pour la gestion des arguments en ligne de commande dans les scripts de dataset.
- Mise à jour des dépendances npm et pip.
- Amélioration de la gestion des erreurs et des timeouts pour les appels à l'API Ordbogen.
- Utilisation de `huggingface-hub` pour l'upload des datasets.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'infrastructure.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Traduction de nouvelles chaînes de caractères en estonien via Weblate.
- Suppression de modèles de langage obsolètes (OLMO 3.32B, LFM2 8B).
- Archivage du modèle Gemini 3 Pro.
- Suppression de l'utilisation de Vertex AI pour l'analyse LLM, au profit d'OpenRouter.
- Suppression des jobs de vérification d'images dans Jenkins et GitHub.
- Ajout de variables d'environnement pour la configuration de Hugging Face.
- Suppression des logs PostgreSQL.
