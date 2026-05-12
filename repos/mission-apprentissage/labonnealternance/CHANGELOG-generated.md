## Changelog : labonnealternance (30 derniers jours, au 11 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur plusieurs fronts. Des optimisations ont été apportées à la recherche et à l'export de données, notamment pour répondre aux besoins de France Travail. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de la plateforme, et des améliorations SEO ont été déployées pour les pages métiers et les pages de diplômes. Enfin, de nombreux assets (images, captures d'écran) ont été ajoutés pour faciliter le travail des équipes.

### Évolutions fonctionnelles

- **Recherche et Export :** Ajout de la possibilité d'exporter un double flux CSV zippé vers France Travail ([#2885](https://github.com/mission-apprentissage/labonnealternance/issues/2885)).
- **XP Recruteurs :** Amélioration du formulaire de candidatures pour l'espace recruteurs ([#2890](https://github.com/mission-apprentissage/labonnealternance/issues/2890)).
- **SEO :** Amélioration du SEO des pages diplômes (front et back) ([#2882](https://github.com/mission-apprentissage/labonnealternance/issues/2882)).
- **Import Flux :** Ajout de l'import des flux EDF et Enedis ([#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819)).
- **Candidature Spontanée :** Amélioration de la gestion des candidatures spontanées, notamment l'affichage du nombre de candidatures et la navigation sur la page de résultats ([#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861), [#2848](https://github.com/mission-apprentissage/labonnealternance/issues/2848)).
- **Taleez :** Intégration de la candidature directe vers Taleez et amélioration de l'affichage de la modale de candidature ([#2865](https://github.com/mission-apprentissage/labonnealternance/issues/2865), [#2804](https://github.com/mission-apprentissage/labonnealternance/issues/2804)).
- **Pages SEO Métiers :** Ajout de blocs salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération ([#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785)).
- **Pages Villes SEO :** Ajout de 10 nouvelles pages villes SEO.

### Évolutions techniques

- **Performance :** Optimisation des requêtes pour éliminer les problèmes de N+1 sur l'API `/api/traininglinks` ([#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841)).
- **Base de données :** Ajout de lectures MongoDB sur les secondaires pour la recherche ([#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849)).
- **Healthchecks :** Stabilisation des healthchecks et réduction de la pression sur le stream processor ([#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845)).
- **Cache :** Correction d'un bug lié à l'utilisation du cache de géolocalisation ([#2884](https://github.com/mission-apprentissage/labonnealternance/issues/2884)).
- **Monitoring :** Réduction du bruit de Sentry sur les erreurs externes ([#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947)).
- **Configuration :** Mise à jour des habilitations et correction de la configuration MongoDB.

### Autres changements

- **Documentation :** Correction d'erreurs et ajouts dans la documentation.
- **Assets :** Ajout de nombreux assets (images, captures d'écran) pour les issues et les tests.
- **Corrections :** Correction de l'oubli de report de données CFA ([#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887)).
- **Tracking :** Ajout du tracking Matomo pour la recherche, la découverte et la candidature ([#2871](https://github.com/mission-apprentissage/labonnealternance/issues/2871)).
