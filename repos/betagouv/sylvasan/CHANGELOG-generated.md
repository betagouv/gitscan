## Changelog : sylvasan (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les évolutions de SylvaSan se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de la connexion via l'authentification DSF, l'implémentation d'un champ carte sur mobile et web, et des améliorations de la gestion des vocabulaires. Des corrections de bugs et des optimisations ont également été apportées, notamment concernant l'affichage des noms longs, la gestion des erreurs et la validation des données.

### Évolutions fonctionnelles
- Implémentation de la connexion via l'authentification DSF pour le web et le mobile. [#287](https://github.com/betagouv/sylvasan/pull/287)
- Ajout d'un champ carte fonctionnel sur mobile et web, permettant la visualisation et la manipulation de données géographiques. [#227](https://github.com/betagouv/sylvasan/pull/227)
- Synchronisation des pôles depuis DSF. [#261](https://github.com/betagouv/sylvasan/pull/261)
- Possibilité de filtrer les réponses par enquête. [#288](https://github.com/betagouv/sylvasan/pull/288)
- Ajout d'une page "Mon compte" avec les informations de l'utilisateur et sa source d'authentification.
- Amélioration de l'affichage des champs avec des noms longs. [#342](https://github.com/betagouv/sylvasan/pull/342)
- Ajout de la gestion des conditions d'affichage des champs (visibilité selon les valeurs d'autres champs). [#281](https://github.com/betagouv/sylvasan/pull/281)
- Ajout de la possibilité de supprimer une observation non sauvegardée.
- Amélioration de l'affichage des labels pour les vocabulaires web.
- Ajout de la pagination dans la vue des réponses.

### Évolutions techniques
- Mise à jour des dépendances : Django, boto3, vue-router, vue-tsc, jsdom, ionic, capacitor, etc. (voir les commits pour la liste complète).
- Refactorisation du code pour l'implémentation du champ carte.
- Amélioration de la gestion des erreurs et de la validation des données.
- Ajout de tests unitaires pour les nouvelles fonctionnalités.
- Mise à jour de la documentation.
- Utilisation de Django Storages pour la gestion des fichiers. [#285](https://github.com/betagouv/sylvasan/pull/285)
- Correction de bugs et amélioration de la performance.

### Autres changements
- Ajout d'un fichier `.keep` pour les builds Android.
- Mise à jour de la version Android (0.0.8 et 0.0.10).
- Correction de warnings Typescript.
- Amélioration de la structure du code et de la lisibilité.
- Ajout de logging pour le débogage de l'authentification Oauth.
- Mise à jour des variables d'environnement pour l'authentification Oauth.
- Ajout de spinners pour améliorer l'expérience utilisateur pendant les chargements.
- Ajout d'un ADR pour le champ image.
- Amélioration de la gestion des sessions après un redémarrage.
- Correction de bugs liés à la position des onglets et de l'authentification.
