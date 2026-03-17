## Changelog : labonnealternance (30 derniers jours)

### Résumé
Les dernières mises à jour de la plateforme labonnealternance se concentrent sur l'amélioration de la stabilité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment l'authentification par token pour l'API Emploi Inclusion et l'importation de données Emploi Inclusion. Des optimisations ont également été apportées aux scripts de déploiement et à la gestion des ressources.

### Évolutions fonctionnelles
- Ajout de l'authentification par token pour l'API Emploi Inclusion, permettant une intégration plus sécurisée. [#2762](https://github.com/mission-apprentissage/labonnealternance/issues/2762)
- Importation des données Emploi Inclusion. [#2740](https://github.com/mission-apprentissage/labonnealternance/issues/2740)
- Mise à jour de la liste noire des CFA. [#2766](https://github.com/mission-apprentissage/labonnealternance/issues/2766)
- Amélioration de l'affichage des recruteurs actifs. [#2725](https://github.com/mission-apprentissage/labonnealternance/issues/2725)
- Ajout de pages SEO pour les métiers. [#2674](https://github.com/mission-apprentissage/labonnealternance/issues/2674)
- Activation du rappel annuel Affelnet. [#2712](https://github.com/mission-apprentissage/labonnealternance/issues/2712)
- Amélioration du wording des emails de déréférencement. [#2690](https://github.com/mission-apprentissage/labonnealternance/issues/2690)
- Ajout de normalisation du spacing DSFR. [#2694](https://github.com/mission-apprentissage/labonnealternance/issues/2694)

### Évolutions techniques
- Migration vers Biome pour le linting du code. [#2757](https://github.com/mission-apprentissage/labonnealternance/issues/2757)
- Mise à jour des versions des GitHub Actions et correction de sécurité pour le déploiement en preview. [#2777](https://github.com/mission-apprentissage/labonnealternance/issues/2777)
- Optimisation de l'utilisation de la mémoire lors des builds de preview. [#2716](https://github.com/mission-apprentissage/labonnealternance/issues/2716)
- Amélioration de la gestion des ressources pour les previews (MongoDB, serveurs). [#2715](https://github.com/mission-apprentissage/labonnealternance/issues/2715)
- Correction d'un problème d'OOM (Out Of Memory) lors du traitement des recruteurs. [#2699](https://github.com/mission-apprentissage/labonnealternance/issues/2699)
- Ajout d'un index 2dsphere dédié pour la recherche géographique des offres partenaires. [#2692](https://github.com/mission-apprentissage/labonnealternance/issues/2692)
- Décommissionnement des API offres v1 et v2. [#2686](https://github.com/mission-apprentissage/labonnealternance/issues/2686)
- Suppression de l'environnement de pentest. [#2720](https://github.com/mission-apprentissage/labonnealternance/issues/2720)

### Autres changements
- Correction de bugs divers (import Jobteaser, OPCO inconnu, statut des recruteurs, etc.).
- Nettoyage de scripts (static assets, closed companies).
- Ajustement des paramètres Sentry pour les cron jobs. [#2760](https://github.com/mission-apprentissage/labonnealternance/issues/2760)
- Mise à jour de la liste des partenaires. [#2691](https://github.com/mission-apprentissage/labonnealternance/issues/2691)
- Correction de typos et amélioration de la documentation.
- Suppression de références à des CFA obsolètes. [#2702](https://github.com/mission-apprentissage/labonnealternance/issues/2702)
- Amélioration de la gestion des erreurs et des logs.
- Correction de problèmes liés à l'indexation MongoDB.
