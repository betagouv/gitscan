## Changelog : autometa (30 derniers jours, au 28 juillet 2026)

### Résumé
Les dernières mises à jour d'autometa se concentrent sur l'amélioration de l'expérience utilisateur avec une refonte de la navigation, l'ajout de nouvelles fonctionnalités comme la création de tableaux de bord et l'intégration de l'IA pour l'analyse des données via des embeddings de messages. Des optimisations de performance et des corrections de bugs ont également été apportées, ainsi que des améliorations de la qualité du code et des tests.

### Évolutions fonctionnelles
- Refonte complète de la navigation principale (sidebar et accueil) pour une meilleure expérience utilisateur. [#178]
- Ajout d'un bouton "Créer un tableau de bord" pour faciliter la création de rapports personnalisés. [#178]
- Rafraîchissement des conversations récentes dans la sidebar via htmx pour une mise à jour dynamique. [#172]
- Intégration de l'Accueil Plateforme preprod (site 226) au Tag Manager pour un suivi plus précis. [#179]
- Ajout d'un skill `zendesk_query` permettant d'interroger Zendesk en lecture seule. [#175]
- Création d'un glossaire BizDev pour une meilleure compréhension des termes métiers. [#169]
- Les erreurs détectées sont désormais enregistrées en base de données au lieu d'être signalées via Slack. [#170]
- Ajout de tooltips Bootstrap pour une meilleure accessibilité et information contextuelle sur les outils. [#175]

### Évolutions techniques
- Implémentation initiale des embeddings de messages avec model2vec pour l'analyse sémantique et l'IA. [#164]
- Optimisation de la récupération de la session S3 pour éviter les re-téléchargements redondants. [#161]
- Amélioration du selftest pour une meilleure fiabilité du système. [#165]
- Gestion des erreurs transitoires lors de la sauvegarde S3 pour éviter les interruptions de processus. [#160]
- Simplification de la gestion de l'environnement via un objet `Environment`. [#158]
- Simplification de la variable d'environnement `AUTOMETA_ENV`. [#156]
- Mise en place d'une série de phases pour améliorer la couverture des tests et la qualité du code :
    - Gel du plancher de couverture à 74.90% des branches. [#174]
    - Application d'une porte de couverture de diff à 90% sur les lignes modifiées. [#175]
    - Détection des tests creux (anti-slop). [#176]
    - Échec rapide des hooks lors des tests (ruff à l'édition + Stop lint-only). [#177]
- Mise à jour de la librairie Pillow en version 12.3.0 pour corriger des vulnérabilités de sécurité. [#175]

### Autres changements
- Anonymisation par défaut des NIR français dans les tickets Zendesk.
- Simplification du parsing des tickets et de la pagination de la recherche.
- Correction de bugs et amélioration de la couverture des tests.
- Ajout de configurations Dependabot pour la gestion des dépendances uvicorn et github-actions. [#163]
- Améliorations de l'interface utilisateur suite aux retours de revue (contraste, surlignage mobile, etc.).
- Correction de l'onglet Conversations qui pointait vers une URL incorrecte.
- Ajout de paramètres pour améliorer l'accessibilité.
