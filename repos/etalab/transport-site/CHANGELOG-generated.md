## Changelog : transport-site (30 derniers jours, au 19 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur le renforcement de la validation des données de transport (notamment le format NeTEx) et l'amélioration de l'interface utilisateur. Des optimisations techniques ont également été apportées pour améliorer la sécurité, la stabilité et la maintenance de la plateforme.

### Évolutions fonctionnelles
- **Amélioration de la validation NeTEx** : sélection automatique de la version XSD selon la date de publication [#5602, #5600, #5599], affichage de la version utilisée [#5607], tri des erreurs par criticité décroissante [#5604] et correction de l'affichage en cas d'erreur de validation [#5606].
- **Interface utilisateur** : optimisation de la mise en page des réutilisations [#5623], correction de la hiérarchie des titres HTML pour l'accessibilité [#5624] et ajout de nouvelles variantes pour le composant `ColorfulButton` [#5603].
- **Données** : mise à jour de la logique de détection des opérateurs pour le format GBFS [#5626].

### Évolutions techniques
- **Sécurité** : mise en place du chiffrement des cookies [#5619].
- **Refactoring** : réduction de la duplication de code [#5618] et refonte de la page de détails des datasets [#5629].
- **Infrastructure et maintenance** : désactivation du polling IRVE dynamique sur les environnements de staging, de développement et sur le worker de production [#5621], mise à jour du fichier de protocole GTFS-RT [#5617], correction d'un bug d'affichage CSS lié à la minification [#5616] et résolution d'une erreur de suivi via Sentry [#5610].
