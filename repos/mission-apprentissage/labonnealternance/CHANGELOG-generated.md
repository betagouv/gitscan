## Changelog : labonnealternance (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du formulaire de prise de rendez-vous CFA et de la gestion des offres d'alternance. Des corrections ont également été apportées pour améliorer la fiabilité de la plateforme et optimiser les processus internes, comme l'export de données vers France Travail et la gestion des erreurs.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur du formulaire de prise de rendez-vous CFA. [#4773](https://github.com/mission-apprentissage/labonnealternance/issues/4773)
- Ajout de l'OPCO EP à la liste blanche pour éviter une classification erronée des offres en tant que CFA. [#4784](https://github.com/mission-apprentissage/labonnealternance/issues/4784)
- Suppression d'une fonte inutilisée (Marianne Medium) pour alléger le code et améliorer les performances. [#4762](https://github.com/mission-apprentissage/labonnealternance/issues/4762)
- Génération d'un fichier `llms.txt` à la racine du site, probablement pour des besoins de documentation ou de configuration liés à l'IA. [#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765)
- Ajout d'un mécanisme de protection pour éviter le double envoi de formulaires. [#4728](https://github.com/mission-apprentissage/labonnealternance/issues/4728)
- Correction de l'affichage du titre 1j1s sur la page recruteur. [#4744](https://github.com/mission-apprentissage/labonnealternance/issues/4744)
- Mise à jour du SMIC au 1er juin 2026 dans le simulateur d'alternance. [#4724](https://github.com/mission-apprentissage/labonnealternance/issues/4724)
- Amélioration des CTAs (Call To Action) sur la page de dépôt d'offre. [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136)
- Adaptation des CTAs "je postule" en fonction des partenaires. [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175)
- Ajout de questions au candidat lors de la création d'une offre. [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172)
- Ajout de pages SEO pour les diplômes. [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893)
- Mise à jour du bloc salaire sur les pages concernées. [#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213)
- Limitation à 10 métiers accessibles sur l'interface utilisateur. [#3211](https://github.com/mission-apprentissage/labonnealternance/issues/3211)
- Ajout de SIRET Handimatch. [#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171)

### Évolutions techniques
- Mise à jour de Next.js. [#4691](https://github.com/mission-apprentissage/labonnealternance/issues/4691)
- Suppression des scripts Biome redondants et mise à jour de la documentation. [#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761)
- Amélioration des notifications Slack pour les MEP et les releases (utilisation de Block Kit). [#4751](https://github.com/mission-apprentissage/labonnealternance/issues/4751)
- Ajout d'un garde-fou pour éviter un double envoi de données. [#4728](https://github.com/mission-apprentissage/labonnealternance/issues/4728)
- Correction de la signature de `onSuccessFunction` dans un plugin. [#4764](https://github.com/mission-apprentissage/labonnealternance/issues/4764)
- Correction d'un problème où `onSuccessFunction` n'était pas une fonction. [#4763](https://github.com/mission-apprentissage/labonnealternance/issues/4763)
- Configuration du merge driver SOPS pour les fichiers d'environnement chiffrés. [#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736)
- Suppression de Swagger et de ses dépendances de l'API v1. [#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717)
- Modernisation des templates d'issues et migration des références Jira vers GitHub Issues. [#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698)
- Correction d'un conflit `_id` lors de l'upsert des recruteurs. [#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708)
- Correction du fallback de géolocalisation France Travail sur le chef-lieu du département. [#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709)
- Ajout d'un heartbeat timer et de heatmaps Matomo pour le suivi de l'activité. [#4011](https://github.com/mission-apprentissage/labonnealternance/issues/4011)
- Suppression de la collection `eligible_trainings_for_appointments_histories` et refactorisation de la tâche de nettoyage. [#4725](https://github.com/mission-apprentissage/labonnealternance/issues/4725)
- Export double flux CSV zippé vers France Travail. [#3977](https://github.com/mission-apprentissage/labonnealternance/issues/3977)

### Autres changements
- Correction d'un problème de hardbounce Brevo qui empêchait la suppression des emails des recruteurs. [#4734](https://github.com/mission-apprentissage/labonnealternance/issues/4734)
- Validation des numéros d'issues pour éviter les erreurs GraphQL en cascade. [#4732](https://github.com/mission-apprentissage/labonnealternance/issues/4732)
- Correction d'un problème de graisse de police Marianne. [#4720](https://github.com/mission-apprentissage/labonnealternance/issues/4720)
- Envoi du changelog sur Slack après un déploiement en production. [#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723)
- Correction d'erreurs de mutation projet pour faciliter le diagnostic des mises à jour d'issues. [#4727](https://github.com/mission-apprentissage/labonnealternance/issues/4727)
- Ajout de nombreux assets d'issues pour la migration de sprint.
- Correction d'un problème de scrolling après la fermeture de la modale de désinscription. [#3179](https://github.com/mission-apprentissage/labonnealternance/issues/3179)
- Suppression de la route `/v1/application` et des schémas orphelins. [#4025](https://github.com/mission-apprentissage/labonnealternance/issues/4025)
- Mise à jour du token de l'API apprentissage. [#3138](https://github.com/mission-apprentissage/labonnealternance/issues/3138)
- Réduction du bruit Sentry sur les erreurs externes. [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947)
- Correction de l'utilisation du rôle utilisateur dans l'admin. [#3961](https://github.com/mission-apprentissage/labonnealternance/issues/3961)
- Correction d'un bug lié à l'affichage des offres créées par API. [#3169](https://github.com/mission-apprentissage/labonnealternance/issues/3169)
- Correction d'un problème de taille de police. [#3173](https://github.com/mission-apprentissage/labonnealternance/issues/3173)
- Correction d'un problème lié à l'oubli de report data CFA. [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887)
- Mise à jour de la liste des CFA blacklistées. [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689)
