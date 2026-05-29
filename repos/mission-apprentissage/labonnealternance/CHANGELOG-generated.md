## Changelog : labonnealternance (30 derniers jours, au 28 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment des corrections de bugs affectant l'affichage et le fonctionnement de certaines fonctionnalités. Des optimisations techniques ont également été réalisées, incluant la suppression de composants obsolètes et la migration vers un système de gestion des issues plus moderne. Enfin, des mises à jour de données et des améliorations SEO ont été implémentées.

### Évolutions fonctionnelles
- **Recherche :** Amélioration de la géolocalisation, avec un fallback sur le chef-lieu du département en cas d'échec de la géolocalisation France Travail [#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709).
- **Offres d'apprentissage :**
    - Correction d'un bug empêchant l'affichage correct des offres créées via l'API [#3169](https://github.com/mission-apprentissage/labonnealternance/issues/3169).
    - Ajout de questions au candidat lors de la création d'une offre [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172).
    - Amélioration de l'affichage des blocs salaires [#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213).
    - Limitation du nombre de métiers accessibles dans l'interface à 10 pour améliorer la performance [#3211](https://github.com/mission-apprentissage/labonnealternance/issues/3211).
    - Mise à jour de la liste des CFA blacklistées [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689).
- **Expérience Recruteur :**
    - Ajout du champ description et amélioration de l'affichage des détails d'une offre dans l'espace recruteur [#2881](https://github.com/mission-apprentissage/labonnealternance/issues/2881).
    - Ajout de la possibilité de réactiver une offre via le flux.
- **SEO :**
    - Ajout de 10 nouvelles pages métier pour améliorer le référencement [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893).
    - Ajout des pages diplôme au sitemap principal [#3180](https://github.com/mission-apprentissage/labonnealternance/issues/3180).
    - Rationalisation des blocs salaires pour le SEO [#3177](https://github.com/mission-apprentissage/labonnealternance/issues/3177).
- **Handimatch :** Ajout du SIRET Handimatch [#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171) et correction de marges [#3176](https://github.com/mission-apprentissage/labonnealternance/issues/3176).
- **CTAs :** Modification des CTAs de dépôt d'offre et adaptation du CTA "je postule" en fonction des partenaires [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136) et [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175).

### Évolutions techniques
- **Gestion des issues :** Modernisation des templates d'issues et migration des références Jira vers GitHub Issues [#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698).
- **API :** Suppression de Swagger et de ses dépendances de l'API v1 [#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717). Suppression de la route /v1/application et des schémas orphelins [#4025](https://github.com/mission-apprentissage/labonnealternance/issues/4025).
- **Monitoring :** Activation du heartbeat timer et des heatmaps Matomo [#4011](https://github.com/mission-apprentissage/labonnealternance/issues/4011).
- **Automatisation :** Implémentation de l'envoi du changelog sur Slack après un déploiement en production [#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723).
- **Correction de bugs :**
    - Correction du conflit `_id` lors de l'upsert des recruteurs [#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708).
    - Correction de l'encodage des entités HTML dans `offer_title` et `workplace_name` [#3934](https://github.com/mission-apprentissage/labonnealternance/issues/3934).
    - Correction d'un problème de graisse de la police Marianne [#4720](https://github.com/mission-apprentissage/labonnealternance/issues/4720).
    - Correction du scrolling après fermeture de la modale de désinscription [#4035](https://github.com/mission-apprentissage/labonnealternance/issues/4035).
    - Correction d'un bug lié à la disparition d'une offre créée par API [#3948](https://github.com/mission-apprentissage/labonnealternance/issues/3948).
    - Correction d'un problème de taille de police [#3963](https://github.com/mission-apprentissage/labonnealternance/issues/3963).
    - Correction d'un bug lié à l'oublie de report data CFA [#3836](https://github.com/mission-apprentissage/labonnealternance/issues/3836).
- **Export :** Implémentation de l'export double flux CSV zippé vers France Travail [#3977](https://github.com/mission-apprentissage/labonnealternance/issues/3977).

### Autres changements
- Mise à jour de la liste des CFA blacklistées.
- Ajout d'assets pour la migration des sprints (plusieurs commits).
- Réduction du bruit Sentry sur les erreurs externes [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947).
- Mise à jour du token API-apprentissage [#3138](https://github.com/mission-apprentissage/labonnealternance/issues/3138).
