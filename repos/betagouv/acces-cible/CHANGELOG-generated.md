## Changelog : acces-cible (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives concernant l'importation de sites web via CSV, avec une meilleure gestion des erreurs et des fichiers malformés. Des corrections de traductions et des améliorations de la recherche ont également été apportées. Enfin, des outils de débogage ont été ajoutés pour faciliter l'analyse des pages crawlées.

### Évolutions fonctionnelles
- Possibilité de télécharger un fichier CSV filtré pour l'importation de sites web. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Amélioration de la détection des liens externes. [#497](https://github.com/betagouv/acces-cible/issues/497)
- Correction d'une erreur dans la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)
- Correction d'une erreur de traduction concernant les années. [#521](https://github.com/betagouv/acces-cible/issues/521)
- Ajout de la possibilité de prévisualiser une page crawlée pour faciliter le débogage. [#487](https://github.com/betagouv/acces-cible/issues/487)

### Évolutions techniques
- Ajout de la gem `i18-tasks` pour suivre les traductions inutilisées et supprimer celles qui le sont.
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518)
- Ajout de commandes `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)
- Persistance de l'historique de la console Rails et du shell dans les conteneurs Docker.
- Ajout des champs `url` et `normalized_url` aux données des sites. [#529](https://github.com/betagouv/acces-cible/issues/529)

### Autres changements
- Amélioration de la gestion des erreurs lors de l'importation de fichiers CSV malformés ou contenant des URL invalides. [#503](https://github.com/betagouv/acces-cible/issues/503), [#504](https://github.com/betagouv/acces-cible/issues/504), [#507](https://github.com/betagouv/acces-cible/issues/507)
- Ajustement de la configuration de Sentry et ajout de logs pour une meilleure surveillance. [#498](https://github.com/betagouv/acces-cible/issues/498)
- Suppression d'une fonctionnalité expérimentale ("upside down").
