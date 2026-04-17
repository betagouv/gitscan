## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la fonctionnalité de médiathèque, l'intégration des données scolaires, l'optimisation des performances des requêtes et diverses corrections de bugs et améliorations de l'interface utilisateur. L'objectif principal est d'offrir une expérience plus riche et plus performante aux utilisateurs de diagBruit.

### Évolutions fonctionnelles
- Ajout d'une page "Médiathèque" permettant de gérer et d'afficher des documents associés aux préconisations. Cela inclut la possibilité d'ajouter du contenu HTML enrichi et des images. [#56](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/56)
- Intégration des données scolaires (écoles) dans le système, avec ingestion de données OSM et association aux nuisances sonores. [#46](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/46)
- Ajout de champs "à retenir" et de points clés dans les préconisations, permettant une communication plus précise et structurée.
- Amélioration de la recherche avec un champ de recherche normalisé et un état initial vide.
- Ajout d'ancres dans le résumé des préconisations pour une navigation plus facile.
- Correction de l'affichage des cartes et des recommandations.
- Amélioration de la gestion des images dans l'éditeur HTML et correction des problèmes de taille.
- Correction de l'affichage des tableaux et de l'alignement des données.

### Évolutions techniques
- Optimisation de la requête `query_noisesource_intersecting_features` pour améliorer les performances.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise en place de loggers pour faciliter le débogage des APIs.
- Utilisation de pipelines CI/CD améliorés pour les déploiements.
- Correction de problèmes liés aux index géométriques.
- Mise à jour de la configuration de Strapi pour gérer correctement les emails.
- Suppression de code inutile et de collections Strapi non utilisées.
- Amélioration de la gestion des branches pour les déploiements en pré-production.

### Autres changements
- Correction de la documentation.
- Mise à jour des dépendances.
- Correction de problèmes de permissions sur Google Analytics.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes d'affichage sur différents navigateurs.
- Ajout de la possibilité d'envoyer des emails de feedback depuis la pré-production.
- Correction de problèmes liés à l'affichage des références de parcelles et de la validation dans la modale.
- Correction de problèmes liés à l'URL des logos.
- Correction de problèmes d'affichage du texte "Dernière mise à jour".
- Ajout de la configuration de Scalingo pour la branche `main` en pré-production.
