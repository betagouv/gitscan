## Changelog : labonnealternance (30 derniers jours, au 2026-05-30)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la plateforme, notamment des corrections de bugs, des optimisations de l'expérience utilisateur et des mises à jour techniques pour améliorer la performance et la maintenance du code. Des efforts ont également été déployés pour améliorer le SEO et l'intégration avec des services externes comme France Travail et Handimatch.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la suppression correcte des adresses email en "hardbounce" dans Brevo [#4734](https://github.com/mission-apprentissage/labonnealternance/issues/4734).
- Validation des numéros d'issues pour éviter des erreurs en cascade dans l'API GraphQL [#4732](https://github.com/mission-apprentissage/labonnealternance/issues/4732).
- Mise à jour du SMIC au 1er juin 2026 dans le simulateur d'alternance [#4724](https://github.com/mission-apprentissage/labonnealternance/issues/4724).
- Correction de l'affichage des erreurs de mutation projet pour faciliter le diagnostic des problèmes [#4727](https://github.com/mission-apprentissage/labonnealternance/issues/4727).
- Correction de l'affichage de la graisse de la police Marianne [#4720](https://github.com/mission-apprentissage/labonnealternance/issues/4720).
- Ajout de questions au candidat lors de la création d'une offre (via l'interface LBAC) [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172).
- Ajout des pages diplôme au sitemap principal pour améliorer le SEO [#3180](https://github.com/mission-apprentissage/labonnealternance/issues/3180).
- Mise à jour du bloc salaire [#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213).
- Limitation du nombre de métiers accessibles sur l'UI à 10 [#3211](https://github.com/mission-apprentissage/labonnealternance/issues/3211).
- Correction d'un problème de disparition d'offres créées via l'API [#3169](https://github.com/mission-apprentissage/labonnealternance/issues/3169).
- Ajout de 10 nouvelles pages métier pour le SEO [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893).
- Ajout du SIRET Handimatch [#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171).
- Modification des CTA (Call To Action) de dépôt d'offre [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136).
- Adaptation des CTA "je postule" en fonction des partenaires [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175).
- Rationalisation des blocs salaires pour le SEO [#3177](https://github.com/mission-apprentissage/labonnealternance/issues/3177).
- Correction de l'encodage des entités HTML dans le titre de l'offre et le nom du lieu de travail [#3174](https://github.com/mission-apprentissage/labonnealternance/issues/3174).
- Correction du scrolling après la fermeture de la modale de désinscription [#3179](https://github.com/mission-apprentissage/labonnealternance/issues/3179).
- Amélioration de l'expérience recruteur avec l'ajout d'un champ description et une revue de l'affichage des détails de l'offre [#2881](https://github.com/mission-apprentissage/labonnealternance/issues/2881).
- Ajout de la possibilité de réordonner les offres LBA selon le statut mandataire [#2888](https://github.com/mission-apprentissage/labonnealternance/issues/2888).
- Correction d'un bug lié à l'oubli du report data CFA [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887).
- Ajout de pages SEO pour les diplômes [#2882](https://github.com/mission-apprentissage/labonnealternance/issues/2882).
- Ajout de la recherche CLS sur la page métier [#2889](https://github.com/mission-apprentissage/labonnealternance/issues/2889).

### Évolutions techniques
- Mise à jour de Next.js [#4691](https://github.com/mission-apprentissage/labonnealternance/issues/4691).
- Suppression de la collection `eligible_trainings_for_appointments_histories` et refactorisation de la tâche de nettoyage [#4725](https://github.com/mission-apprentissage/labonnealternance/issues/4725).
- Suppression de Swagger et de ses dépendances de l'API v1 [#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717).
- Modernisation des templates d'issues et migration des références Jira vers GitHub Issues [#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698).
- Suppression de la route `/v1/application` et des schémas orphelins [#4025](https://github.com/mission-apprentissage/labonnealternance/issues/4025).
- Configuration du merge driver SOPS pour les fichiers d'environnement chiffrés [#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736).
- Envoi du changelog sur Slack après un déploiement en production [#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723).
- Correction du conflit `_id` lors de l'upsert des recruteurs LBA [#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708).
- Fallback de la géolocalisation France Travail sur le chef-lieu du département [#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709).
- Activation du heartbeat timer et des heatmaps Matomo [#4011](https://github.com/mission-apprentissage/labonnealternance/issues/4011).
- Utilisation de l'organizationId pour sélectionner le bon rôle utilisateur dans l'admin [#3961](https://github.com/mission-apprentissage/labonnealternance/issues/3961).
- Export double flux CSV zippé vers France Travail [#3977](https://github.com/mission-apprentissage/labonnealternance/issues/3977).
- Réduction du bruit Sentry sur les erreurs externes [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947).

### Autres changements
- Ajout d'assets (images, screenshots) pour la migration des issues vers GitHub.
- Mise à jour de la liste des CFA en blacklist [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689).
- Correction de fichiers d'assets corrompus.
