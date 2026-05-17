## Changelog : labonnealternance (30 derniers jours, au 13 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur la recherche d'offres et la gestion des candidatures. Des optimisations ont également été apportées pour le suivi des performances et l'intégration avec des partenaires externes. De nombreuses corrections de bugs ont été implémentées pour améliorer la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Recherche & Candidature :** Amélioration de la navigation sur la page de résultats de recherche et affichage plus précis des candidatures spontanées [#2874](https://github.com/mission-apprentissage/labonnealternance/issues/2874).
- **Candidatures Partenaires :** Intégration de la candidature directe vers Taleez et amélioration de l'affichage de la modale de candidature externe [#2865](https://github.com/mission-apprentissage/labonnealternance/issues/2865) et [#2804](https://github.com/mission-apprentissage/labonnealternance/issues/2804).
- **XP Recruteurs :** Ajout du champ description et amélioration de l'affichage du détail des offres pour les recruteurs [#2881](https://github.com/mission-apprentissage/labonnealternance/issues/2881) et [#2890](https://github.com/mission-apprentissage/labonnealternance/issues/2890).
- **SEO :** Amélioration du SEO des pages diplômes et ajout de nouvelles pages villes optimisées pour le référencement [#2882](https://github.com/mission-apprentissage/labonnealternance/issues/2882) et [#2872](https://github.com/mission-apprentissage/labonnealternance/issues/2872).
- **Export de données :** Implémentation de l'export double flux CSV zippé vers France Travail [#2885](https://github.com/mission-apprentissage/labonnealternance/issues/2885).
- **Whitelist :** Ajout d'une whitelist pour les offres des entreprises GEIQ et des CFA d'entreprise [#2840](https://github.com/mission-apprentissage/labonnealternance/issues/2840).
- **Tracking :** Ajout du tracking Matomo pour les pages de recherche, découverte et candidature [#2871](https://github.com/mission-apprentissage/labonnealternance/issues/2871).

### Évolutions techniques
- **API :** Suppression de la route `/v1/application` et des schémas orphelins [#3137](https://github.com/mission-apprentissage/labonnealternance/issues/3137).
- **Matomo :** Activation du heartbeat timer et des heatmaps Matomo pour un meilleur suivi des performances [#3170](https://github.com/mission-apprentissage/labonnealternance/issues/3170).
- **Sentry :** Réduction du bruit dans Sentry en filtrant les erreurs externes [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947).
- **Authentification :** Utilisation de l'organizationId pour sélectionner le bon rôle utilisateur dans l'admin [#2877](https://github.com/mission-apprentissage/labonnealternance/issues/2877).
- **Node :** Mise à jour de Node caged [#2724](https://github.com/mission-apprentissage/labonnealternance/issues/2724).
- **Cache :** Amélioration de la gestion du cache de géolocalisation [#2884](https://github.com/mission-apprentissage/labonnealternance/issues/2884).

### Autres changements
- Mise à jour du token API apprentissage [#3138](https://github.com/mission-apprentissage/labonnealternance/issues/3138).
- Ajout d'assets pour les sprints 27 (tests, migration) et LBA-3203.
- Correction de fichiers d'assets corrompus (LBA-2631).
- Correction d'un oubli de report de données CFA [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887).
- Mise à jour des habilitations [#2878](https://github.com/mission-apprentissage/labonnealternance/issues/2878).
- Suppression des recruiters [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728).
