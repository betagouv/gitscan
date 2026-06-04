## Changelog : labonnealternance (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des bugs d'affichage et en optimisant les processus de gestion des offres et des recruteurs. Des améliorations techniques ont également été apportées pour moderniser l'infrastructure et faciliter le déploiement.

### Évolutions fonctionnelles
- Ajout d'un fichier `llms.txt` à la racine du site pour des besoins spécifiques. [#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765)
- Amélioration de l'affichage du titre sur la page recruteur (correction d'un bug). [#4744](https://github.com/mission-apprentissage/labonnealternance/issues/4744)
- Ajout d'un garde-fou pour éviter un double envoi de données. [#4728](https://github.com/mission-apprentissage/labonnealternance/issues/4728)
- Correction de l'affichage des erreurs de mutation projet pour faciliter le diagnostic des problèmes. [#4727](https://github.com/mission-apprentissage/labonnealternance/issues/4727)
- Amélioration des notifications Slack pour les MEP et les releases (utilisation de Block Kit). [#4751](https://github.com/mission-apprentissage/labonnealternance/issues/4751)
- Mise à jour du SMIC au 1er juin 2026 dans le simulateur alternant. [#4724](https://github.com/mission-apprentissage/labonnealternance/issues/4724)
- Ajout de questions au candidat lors de la création d'une offre. [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172)
- Ajout de 10 nouvelles pages métier SEO pour améliorer le référencement. [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893)
- Amélioration des CTAs (Call To Action) sur la page de dépôt d'offre. [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136)
- Adaptation du CTA "je postule" en fonction des partenaires. [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175)
- Rationalisation des blocs salaires pour le SEO. [#3177](https://github.com/mission-apprentissage/labonnealternance/issues/3177)
- Correction de l'encodage des entités HTML dans les titres d'offre et les noms de lieux de travail. [#3174](https://github.com/mission-apprentissage/labonnealternance/issues/3174)
- Correction du scrolling après la fermeture de la modale de désinscription. [#3179](https://github.com/mission-apprentissage/labonnealternance/issues/3179)
- Ajout de pages SEO pour les diplômes. [#2882](https://github.com/mission-apprentissage/labonnealternance/issues/2882)
- Mise à jour de la liste des CFA blacklistées. [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689)
- Amélioration du bloc salaire. [#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213)
- Limitation du nombre de métiers accessibles sur l'UI à 10. [#3211](https://github.com/mission-apprentissage/labonnealternance/issues/3211)

### Évolutions techniques
- Mise à jour de Next.js. [#4691](https://github.com/mission-apprentissage/labonnealternance/issues/4691)
- Suppression de Swagger et de ses dépendances de l'API v1. [#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717)
- Configuration du merge driver SOPS pour les fichiers d'environnement chiffrés. [#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736)
- Suppression de scripts Biome redondants et mise à jour de la documentation. [#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761)
- Suppression de la collection `eligible_trainings_for_appointments_histories` et refactoring de la tâche de nettoyage. [#4725](https://github.com/mission-apprentissage/labonnealternance/issues/4725)
- Suppression de la route `/v1/application` et des schémas orphelins. [#4025](https://github.com/mission-apprentissage/labonnealternance/issues/4025)
- Correction du conflit `_id` lors de l'upsert des recruteurs LBA. [#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708)
- Fallback de la géolocalisation France Travail sur le chef-lieu du département. [#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709)
- Ajout d'un "business error expired" pour tous les mappers. [#4740](https://github.com/mission-apprentissage/labonnealternance/issues/4740)
- Activation du heartbeat timer et des heatmaps Matomo. [#4011](https://github.com/mission-apprentissage/labonnealternance/issues/4011)
- Utilisation de l'organizationId pour sélectionner le bon rôle utilisateur dans l'admin. [#3961](https://github.com/mission-apprentissage/labonnealternance/issues/3961)

### Autres changements
- Modernisation des templates d'issues et migration des références Jira vers GitHub Issues. [#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698)
- Ajout d'assets d'issues pour la migration du sprint 27. (plusieurs commits)
- Correction de la graisse de la police Marianne. [#4720](https://github.com/mission-apprentissage/labonnealternance/issues/4720)
- Correction du problème de disparition d'une offre créée par API. [#3169](https://github.com/mission-apprentissage/labonnealternance/issues/3169)
- Correction d'un problème de taille de police. [#3173](https://github.com/mission-apprentissage/labonnealternance/issues/3173)
- Ajout du SIRET Handimatch. [#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171)
- Correction du hardbounce Brevo qui ne retirait pas l'email des recruteurs LBA. [#4734](https://github.com/mission-apprentissage/labonnealternance/issues/4734)
- Validation des numéros d'issues pour éviter les cascades d'erreurs GraphQL. [#4732](https://github.com/mission-apprentissage/labonnealternance/issues/4732)
- Envoi du changelog sur Slack après un déploiement en production. [#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723)
- Correction d'erreurs externes dans Sentry pour réduire le bruit. [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947)
- Correction de la gestion du report data CFA. [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887)
