## Changelog : catalogi (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de l'API, la provenance des données et l'expérience utilisateur. Des optimisations ont été apportées pour éviter les erreurs liées à Wikidata et améliorer la vitesse de chargement. L'interface utilisateur a été enrichie avec des informations sur la provenance des données et des corrections ont été apportées pour une meilleure compatibilité mobile.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la provenance des données dans l'interface utilisateur, avec une présentation sous forme de tableau comparatif dans la modale DSFR. [#2999e51](https://github.com/codegouvfr/catalogi/commit/2999e51)
- Ajout d'options pour les systèmes d'exploitation mobiles manquants et amélioration de la sécurité des types pour les systèmes d'exploitation. [#caffbcf](https://github.com/codegouvfr/catalogi/commit/caffbcf)
- Possibilité de configurer les sources via des fichiers. [#2415fc7](https://github.com/codegouvfr/catalogi/commit/2415fc7)
- Propagation de la nouvelle gestion de configuration via l'utilisation de fichiers. [#c081289](https://github.com/codegouvfr/catalogi/commit/c081289)
- Modification de la gestion des fonctionnalités du gateway. [#9af0faa](https://github.com/codegouvfr/catalogi/commit/9af0faa)

### Évolutions techniques
- Optimisation de la récupération des données Wikidata et des URLs des logos pour améliorer les performances de l'API. [#759cedb](https://github.com/codegouvfr/catalogi/commit/759cedb)
- Correction d'un problème de type dans Gitbeaker. [#75c22f7](https://github.com/codegouvfr/catalogi/commit/75c22f7)
- Refactorisation du type `SoftwareData` et suppression des colonnes `content` de la table `softwares`. [#4377664](https://github.com/codegouvfr/catalogi/commit/4377664)
- Utilisation de `Special:FilePath` pour les URLs des images Wikidata afin d'éviter les erreurs. [#e06c5c5](https://github.com/codegouvfr/catalogi/commit/e06c5c5)
- Renforcement de la sécurité du gateway Wikidata et mise en cache de l'autocomplétion pour éviter les erreurs 429. [#04a9455](https://github.com/codegouvfr/catalogi/commit/04a9455)
- Correction des dépendances pour les tests E2E. [#7273912](https://github.com/codegouvfr/catalogi/commit/7273912)
- Amélioration de la configuration CSP locale pour l'affichage des images. [#0e83b75](https://github.com/codegouvfr/catalogi/commit/0e83b75)
- Ajout de `worker-src` au CSP par défaut pour les workers Sentry. [#a7bcd62](https://github.com/codegouvfr/catalogi/commit/a7bcd62)
- Correction pour le suivi des changements de route SPA avec l'analytics, bloqués par le CSP. [#4c3d7b6](https://github.com/codegouvfr/catalogi/commit/4c3d7b6)

### Autres changements
- Documentation : Utilisation du CSP Vite dans l'environnement Vite. [#9058319](https://github.com/codegouvfr/catalogi/commit/9058319)
- Nettoyage des artefacts de provenance et de revue. [#5c7d400](https://github.com/codegouvfr/catalogi/commit/5c7d400)
- Correction des assertions dans les tests E2E pour éviter les collisions avec la provenance des sources. [#3297648](https://github.com/codegouvfr/catalogi/commit/3297648)
- Plusieurs mises à jour de version (build). [#94d3cf5, #2d13d03, #b3a645b, #cebe08f, #6e88656](https://github.com/codegouvfr/catalogi/commits)
