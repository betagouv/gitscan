## Changelog : labonnealternance (30 derniers jours, au 13 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la plateforme, notamment l'ajout de nouvelles fonctionnalités pour les recruteurs (gestion des candidatures), l'optimisation du SEO pour les pages de diplômes et de villes, et l'amélioration de l'export de données vers France Travail. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Expérience Recruteur :** Ajout d'un formulaire de gestion des candidatures pour les recruteurs [#2890](https://github.com/mission-apprentissage/labonnealternance/issues/2890).
- **SEO :** Amélioration du SEO des pages de diplômes (front et back) [#2882](https://github.com/mission-apprentissage/labonnealternance/issues/2882).
- **SEO :** Ajout de 10 nouvelles pages ville pour le SEO [#2872](https://github.com/mission-apprentissage/labonnealternance/issues/2872) et [#2875](https://github.com/mission-apprentissage/labonnealternance/issues/2875).
- **Export de données :** Implémentation de l'export de données en double flux CSV zippé vers France Travail [#2885](https://github.com/mission-apprentissage/labonnealternance/issues/2885).
- **Candidatures Partenaires :** Possibilité de candidatures directes vers Taleez [#2804](https://github.com/mission-apprentissage/labonnealternance/issues/2804) et tracking des candidatures partenaires externes [#2862](https://github.com/mission-apprentissage/labonnealternance/issues/2862).
- **Navigation Recherche :** Amélioration de la navigation sur la page de résultats de recherche [#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861).
- **Simulation :** Ajout du tracking Matomo sur la page de simulation [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832).
- **Landing Page Candidat 1J1S :** Création d'une landing page pour le programme "1 Jeune 1 Solution" [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834).
- **Flux Import :** Intégration des flux import d'EDF et d'Enedis [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819).

### Évolutions techniques
- **Matomo :** Activation du heartbeat timer et des heatmaps Matomo pour un meilleur suivi de l'activité utilisateur [#3170](https://github.com/mission-apprentissage/labonnealternance/issues/3170).
- **Gestion des rôles :** Utilisation de l'organizationId pour sélectionner le bon rôle utilisateur dans l'admin [#2877](https://github.com/mission-apprentissage/labonnealternance/issues/2877).
- **Suppression de routes obsolètes :** Suppression de la route /v1/application et des schémas de base de données orphelins [#3137](https://github.com/mission-apprentissage/labonnealternance/issues/3137).
- **Optimisation MongoDB :** Amélioration de la configuration de MongoDB (maxPoolSize, secondary helper) pour une meilleure performance [#2856](https://github.com/mission-apprentissage/labonnealternance/issues/2856).
- **Synchronisation Stats :** Ajout d'un job de resynchronisation des statistiques LBA [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846).
- **Healthchecks :** Stabilisation des healthchecks et réduction de la pression du stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
- **Cache Géolocalisation :** Optimisation de l'utilisation du cache de géolocalisation pour éviter les erreurs [#2884](https://github.com/mission-apprentissage/labonnealternance/issues/2884).

### Autres changements
- **Documentation :** Ajout d'assets pour les issues des sprints 27 (tests et migrations).
- **Corrections Sentry :** Réduction du bruit des erreurs Sentry liées à des erreurs externes [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947).
- **Correction CFA :** Correction d'un oubli de report de données CFA [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887).
- **Mise à jour API Apprentissage :** Mise à jour du token de l'API apprentissage [#3138](https://github.com/mission-apprentissage/labonnealternance/issues/3138).
- **Correction Assets :** Correction de plusieurs assets corrompus.
