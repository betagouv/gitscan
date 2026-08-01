## Changelog : autometa (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, autometa a bénéficié d'améliorations significatives de l'interface utilisateur, notamment une refonte de la navigation et l'ajout de nouveaux boutons d'action. Des optimisations de performance ont été apportées pour réduire les temps de chargement et améliorer la stabilité. De plus, l'intégration avec Zendesk a été renforcée et des bases pour l'intégration de modèles de langage (embeddings) ont été posées.

### Évolutions fonctionnelles
- Refonte complète de la navigation principale (sidebar et page d'accueil) pour une meilleure expérience utilisateur. [#178]
- Ajout d'un bouton "Créer un tableau de bord" pour faciliter la création de rapports personnalisés. [#178]
- Rafraîchissement des conversations récentes dans la sidebar via htmx, corrigeant un bug existant. [#172]
- Ajout de tooltips (infobulles) pour les sections Jobs, Cron et Tag Manager pour une meilleure compréhension des fonctionnalités. [#115fa66]
- Intégration de l'Accueil Plateforme preprod (site 226) au Tag Manager pour un suivi plus précis. [#179]
- Ajout d'une skill Zendesk pour interroger les données de support client. [#c39199f]
- Anonymisation par défaut des numéros NIR français dans les tickets Zendesk pour la protection des données personnelles. [#f024047]
- Création d'un glossaire métier (bizdev) pour une meilleure compréhension des termes utilisés. [#169]

### Évolutions techniques
- Implémentation initiale des embeddings de messages avec le modèle model2vec, ouvrant la voie à l'utilisation de l'IA pour l'analyse sémantique. [#164]
- Optimisation de la récupération de session S3 pour éviter les re-téléchargements redondants et améliorer les performances. [#161]
- Amélioration de la gestion des erreurs lors de la sauvegarde S3, en traitant les erreurs temporaires sans interrompre le processus. [#160]
- Mise en place d'une configuration Dependabot pour la gestion automatique des mises à jour de `uv` et `github-actions`. [#163]
- Amélioration du selftest pour une meilleure détection des problèmes de configuration. [#165]
- Correction d'un problème empêchant le démarrage de l'application sur une base de données fraîche. [#166]
- Renforcement de la couverture de tests avec l'ajout de phases de tests progressives (gel du plancher de couverture, détection de tests creux, seuil de couverture sur les lignes modifiées). [#177, #176, #175, #174]
- Simplification de l'objet `Environment` pour une meilleure gestion de la configuration. [#158, #156]

### Autres changements
- Correction de bugs et amélioration de la qualité du code. [#55f3f74]
- Les erreurs détectées sont désormais enregistrées en base de données au lieu d'être envoyées sur Slack. [#170]
- Mise à jour de la librairie Pillow en version 12.3.0 pour corriger des vulnérabilités de sécurité. [#f14d3d5]
- Divers retours de revue implémentés pour améliorer l'interface utilisateur et corriger des problèmes d'accessibilité. [#620811a, #2f67103, #115fa66]
