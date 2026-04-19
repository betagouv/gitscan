## Changelog : acces-cible (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et la gestion des sites web, ainsi que sur la correction de bugs liés à la lecture des fichiers CSV. De nouvelles fonctionnalités permettent également le téléchargement de CSV filtrés et la prévisualisation des pages crawlées pour faciliter le débogage.

### Évolutions fonctionnelles
- Possibilité de télécharger un fichier CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Amélioration de la détection des liens externes. [#497](https://github.com/betagouv/acces-cible/issues/497)
- Possibilité de prévisualiser une page crawlée pour faciliter le débogage. [#487](https://github.com/betagouv/acces-cible/issues/487)
- Correction de la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)

### Évolutions techniques
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518)
- Ajout d'une commande `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)
- Persistance de l'historique de la console Rails et du shell dans les conteneurs Docker.
- Amélioration de la gestion des erreurs lors de l'importation de fichiers CSV :
    - Gestion des URLs invalides. [#504](https://github.com/betagouv/acces-cible/issues/504)
    - Ignorer les lignes vides dans les fichiers CSV. [#503](https://github.com/betagouv/acces-cible/issues/503)
    - Gestion des fichiers CSV malformés. [#507](https://github.com/betagouv/acces-cible/issues/507)

### Autres changements
- Ajustement de la configuration de Sentry et ajout de logs. [#498](https://github.com/betagouv/acces-cible/issues/498)
- Une tentative d'inverser l'affichage a été annulée.
