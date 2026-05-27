## Changelog : labonnealternance (30 derniers jours, au 2026-05-25)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur la recherche d'offres, l'optimisation SEO et l'intégration de nouvelles fonctionnalités pour les recruteurs. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Enfin, des travaux préparatoires ont été réalisés pour les prochaines étapes de développement et de migration.

### Évolutions fonctionnelles
- **Recherche d'offres :** Limitation du nombre de métiers affichés dans l'interface de recherche à 10 pour améliorer la performance et la clarté [#3211](https://github.com/mission-apprentissage/labonnealternance/issues/3211).
- **Création d'offres :** Ajout de questions à poser aux candidats lors de la création d'une offre [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172).
- **SEO :** Ajout de 10 nouvelles pages métiers optimisées pour le référencement [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893) et ajout des pages diplômes au sitemap principal [#3180](https://github.com/mission-apprentissage/labonnealternance/issues/3180). Rationalisation des blocs salaires pour le SEO [#3177](https://github.com/mission-apprentissage/labonnealternance/issues/3177).
- **Handimatch :** Ajout du SIRET Handimatch lors de la création d'une offre [#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171) et correction des marges sur l'interface Handimatch [#3176](https://github.com/mission-apprentissage/labonnealternance/issues/3176).
- **Dépôt d'offre :** Modification des boutons d'appel à l'action (CTA) lors du dépôt d'offre [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136) et adaptation du bouton "Je postule" en fonction des partenaires [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175).
- **XP Recruteurs :** Ajout d'un champ description et amélioration de l'affichage du détail des offres pour les recruteurs [#2881](https://github.com/mission-apprentissage/labonnealternance/issues/2881).
- **Export double flux :** Implémentation de l'export du double flux CSV zippé vers France Travail [#2885](https://github.com/mission-apprentissage/labonnealternance/issues/2885).
- **Correction d'un bug :** Correction d'un problème de disparition d'une offre créée via l'API [#3169](https://github.com/mission-apprentissage/labonnealternance/issues/3169).
- **Correction d'un bug :** Correction d'un problème de tailles de polices [#3173](https://github.com/mission-apprentissage/labonnealternance/issues/3173).
- **Correction d'un bug :** Correction de l'encodage des entités HTML dans le titre de l'offre et le nom du lieu de travail [#3174](https://github.com/mission-apprentissage/labonnealternance/issues/3174).
- **Correction d'un bug :** Remise en état du scrolling après la fermeture de la modale de désinscription [#3179](https://github.com/mission-apprentissage/labonnealternance/issues/3179).
- **Correction d'un bug :** Correction d'un oubli de report de données CFA [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887).
- **Correction d'un bug :** Mise à jour de la liste des CFA en blacklist [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689).
- **Correction d'un bug :** Correction de la modification des champs utilisateur dans l'admin [#2869](https://github.com/mission-apprentissage/labonnealternance/issues/2869).

### Évolutions techniques
- **Tracking Matomo :** Ajout du tracking Matomo pour la recherche, la découverte et la candidature [#2871](https://github.com/mission-apprentissage/labonnealternance/issues/2871).
- **Suppression de routes obsolètes :** Suppression de la route `/v1/application` et des schémas de base de données orphelins [#3137](https://github.com/mission-apprentissage/labonnealternance/issues/3137).
- **Amélioration de la gestion des erreurs :** Réduction du bruit Sentry sur les erreurs externes [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947).
- **Heartbeat et Heatmaps :** Activation du heartbeat timer et des heatmaps Matomo [#3170](https://github.com/mission-apprentissage/labonnealternance/issues/3170).
- **Gestion des rôles utilisateurs :** Utilisation de l'organizationId pour sélectionner le bon rôle utilisateur dans l'admin [#2877](https://github.com/mission-apprentissage/labonnealternance/issues/2877).
- **Mise à jour du token API :** Mise à jour du token API d'apprentissage [#3138](https://github.com/mission-apprentissage/labonnealternance/issues/3138).

### Autres changements
- Mise à jour des modèles de tickets (issues)
- Ajout d'assets pour la migration des tickets
- Mise à jour du offer_history_status si réactivation par le flux.
- Correction de la documentation et des assets.
