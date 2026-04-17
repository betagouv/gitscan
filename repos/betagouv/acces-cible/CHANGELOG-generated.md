## Changelog : acces-cible (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et la gestion des sites web, avec une attention particulière portée à la robustesse du traitement des fichiers CSV et à la détection des informations d'accessibilité. Des améliorations ont également été apportées à la visualisation des pages crawlées pour faciliter le débogage.

### Évolutions fonctionnelles
- Possibilité de télécharger un fichier CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Amélioration de la détection des liens externes. [#497](https://github.com/betagouv/acces-cible/issues/497)
- Extraction de l'adresse email de contact et du formulaire de contact sur les pages web. [#480](https://github.com/betagouv/acces-cible/issues/480)
- Correction de la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)
- Suppression du scope pour améliorer la détection du schéma et du plan d'accessibilité. [#491](https://github.com/betagouv/acces-cible/issues/491)

### Évolutions techniques
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518)
- Ajout d'une commande `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)
- Persistance de l'historique de la console Rails et du shell dans les conteneurs Docker.
- Ajout d'une fonctionnalité permettant de prévisualiser une page crawlée pour faciliter le débogage. [#487](https://github.com/betagouv/acces-cible/issues/487)

### Autres changements
- Amélioration de la gestion des fichiers CSV malformés lors de l'importation de sites. [#507](https://github.com/betagouv/acces-cible/issues/507), [#504](https://github.com/betagouv/acces-cible/issues/504), [#503](https://github.com/betagouv/acces-cible/issues/503)
- Ajustement de la configuration de Sentry et ajout de logs. [#498](https://github.com/betagouv/acces-cible/issues/498)
