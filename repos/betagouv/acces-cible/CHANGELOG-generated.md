## Changelog : acces-cible (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de l'application, notamment lors de l'importation de données via des fichiers CSV. De nouvelles fonctionnalités ont été ajoutées pour faciliter le téléchargement de données filtrées et améliorer la détection des liens externes. Des corrections de bugs et des améliorations de la sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger un fichier CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Amélioration de la détection des liens externes. [#497](https://github.com/betagouv/acces-cible/issues/497)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les logiciels de tableur. [#520](https://github.com/betagouv/acces-cible/issues/520)
- Correction de la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)

### Évolutions techniques
- Sécurisation du rendu des URLs externes pour prévenir les attaques XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518)
- Mise à jour de plusieurs dépendances mineures. [#523](https://github.com/betagouv/acces-cible/issues/523)
- Ajout de la gem `i18-tasks` pour la gestion des traductions et suppression des traductions inutilisées.
- Ajout de commandes `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)
- Persistance de l'historique de la console Rails et du shell dans les environnements Docker.
- Ajout des champs `url` et `normalized_url` aux données des sites. [#529](https://github.com/betagouv/acces-cible/issues/529)

### Autres changements
- Amélioration de la configuration de Sentry et ajout de logs pour faciliter le monitoring et le débogage. [#498](https://github.com/betagouv/acces-cible/issues/498)
- Correction de la gestion des erreurs lors de l'importation de fichiers CSV malformés ou contenant des lignes vides. [#503](https://github.com/betagouv/acces-cible/issues/503), [#504](https://github.com/betagouv/acces-cible/issues/504), [#507](https://github.com/betagouv/acces-cible/issues/507)
- Correction d'une erreur de traduction pour les années invalides. [#521](https://github.com/betagouv/acces-cible/issues/521)
- Suppression d'une fonctionnalité expérimentale ("upside down") qui n'était pas stable.
