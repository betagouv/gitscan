## Changelog : autometa (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, autometa a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment une refonte de la navigation, l'ajout de nouveaux outils (création de tableaux de bord) et une meilleure gestion des erreurs. Des optimisations techniques ont également été apportées pour améliorer la performance et la fiabilité du système, ainsi que des améliorations concernant les tests et la sécurité.

### Évolutions fonctionnelles
- Refonte complète de la navigation principale (sidebar et page d'accueil) pour une meilleure expérience utilisateur. [#178]
- Ajout d'un bouton "Créer un tableau de bord" pour faciliter la création de visualisations. [#178]
- Rafraîchissement des conversations récentes dans la sidebar via htmx pour une expérience plus fluide. [#172]
- Intégration du site "Accueil Plateforme preprod" (site 226) au Tag Manager. [#179]
- Ajout d'une nouvelle compétence `zendesk_query` permettant d'interagir avec Zendesk en lecture seule. [#174]
- Les erreurs détectées sont désormais enregistrées en base de données au lieu d'être envoyées sur Slack. [#170]
- Amélioration des tooltips avec l'utilisation de tooltips Bootstrap natifs. [#174]
- Ajout de tooltips sur les sections Jobs, Cron et Tag Manager pour une meilleure compréhension. [#174]
- Création d'un glossaire métier (bizdev). [#169]

### Évolutions techniques
- Ajout d'embeddings de messages initiaux avec le modèle `model2vec` pour améliorer la recherche sémantique. [#164]
- Optimisation de la récupération de session S3 pour éviter les re-téléchargements redondants. [#161]
- Amélioration du selftest pour une meilleure vérification de l'état du système. [#165]
- Correction d'un problème empêchant le démarrage de l'application sur une base de données fraîche. [#166]
- Gestion améliorée des erreurs transitoires lors de la sauvegarde S3. [#160]
- Mise en place d'une configuration Dependabot pour la gestion des mises à jour de dépendances (uv et github-actions). [#163]
- Amélioration de la gestion des tests avec l'ajout de phases pour renforcer la couverture et la qualité du code. [#177, #176, #175, #174]
- Anonymisation par défaut des NIR français dans les tickets Zendesk.
- Simplification de la gestion de l'environnement avec un objet `Environment`. [#158, #156]
- Correction d'un bug lié à la ré-architecture de la RPE du TDB. [#150]

### Autres changements
- Mise à jour de la librairie Pillow à la version 12.3.0 pour corriger des vulnérabilités identifiées par pip-audit. [#174]
- Diverses corrections et améliorations suite aux revues de code.
