## Changelog : vizeau (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de Vizeau se concentrent sur l'amélioration de la gestion des projets, notamment avec l'ajout d'étapes de projet, la gestion des documents associés, et l'intégration de tags. Des améliorations ont également été apportées à l'interface utilisateur, à la cartographie et à la gestion des données, ainsi qu'à l'infrastructure technique du projet.

### Évolutions fonctionnelles
- Ajout de la gestion des étapes de projet : création, édition, suppression et validation. [#451](https://github.com/MTES-MCT/vizeau/pull/451)
- Possibilité d'ajouter des documents à chaque étape de projet. [#456](https://github.com/MTES-MCT/vizeau/pull/456)
- Implémentation de tags pour les étapes de projet. [#444](https://github.com/MTES-MCT/vizeau/pull/444)
- Affichage des projets sur les pop-ups de parcelle sur la carte. [#470](https://github.com/MTES-MCT/vizeau/pull/470)
- Ajout d'un bouton de navigation vers la sélection de parcelles lors de l'association de parcelles à un projet. [#452](https://github.com/MTES-MCT/vizeau/pull/452)
- Amélioration de l'affichage des titres pour éviter les troncatures. [#455](https://github.com/MTES-MCT/vizeau/pull/455)
- Correction de l'affichage des messages d'erreur d'authentification. [#472](https://github.com/MTES-MCT/vizeau/pull/472)
- Les commentaires de parcelle sont maintenant individuels à chaque utilisateur. [#474](https://github.com/MTES-MCT/vizeau/pull/474)

### Évolutions techniques
- Migration vers Adonis 7. [#470](https://github.com/MTES-MCT/vizeau/pull/470)
- Intégration du tracking Matomo pour l'analyse de l'utilisation de l'application. [#459](https://github.com/MTES-MCT/vizeau/pull/459)
- Optimisation de la requête de récupération des AAC et ajout d'un mode debug pour DuckDB. [#461](https://github.com/MTES-MCT/vizeau/pull/461)
- Raccourcissement des imports relatifs des types pour une meilleure organisation du code. [#442](https://github.com/MTES-MCT/vizeau/pull/442)
- Correction des erreurs de linter (imports de type).
- Génération de fichiers PMTiles. [#369](https://github.com/MTES-MCT/vizeau/pull/369)
- Scripts pour la génération de fiches AAC et d'analyses. [#460](https://github.com/MTES-MCT/vizeau/pull/460) et [#458](https://github.com/MTES-MCT/vizeau/pull/458)

### Autres changements
- Ajout d'un fichier `.env.sample` et mise à jour du fichier `.gitignore`.
- Amélioration de la documentation.
- Corrections de typos et de la mise en forme de la documentation.
- Suppression des logs de session non définis. [#444](https://github.com/MTES-MCT/vizeau/pull/444)
- Corrections diverses suite aux revues de code (Copilot).
- Corrections des différences livrable FIGMA.
- Correction des validations dans le validateur.
- Amélioration du texte des labels.
- Ajout de classes CSS pour améliorer la réactivité de la mise en page.
