## Changelog : dora (30 derniers jours, au 1er octobre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une refonte de l'expérience pour les gestionnaires de territoires et d'une simplification importante de la gestion des structures et des services. Les outils de recherche et d'export de données ont également été enrichis pour faciliter le travail des professionnels.

### Évolutions fonctionnelles
- **Gestion des structures** : Simplification des fiches et des formulaires d'édition [#1383], fusion de la présentation et du résumé en une description unique [#1384], possibilité de rattacher une structure à un réseau porteur [#1382] et ajout d'une option vide pour la typologie des structures [#1398].
- **Gestion des services** : Ajout du champ des horaires d'accueil, amélioration de la synchronisation avec les modèles [#1370], correction des conflits de noms de formulaires [#1354] et correction de l'initialisation des données lors de la création via un modèle [#1390].
- **Tableaux de bord et Recherche** : Refonte du tableau de bord et création d'une nouvelle page d'accueil pour les gestionnaires de territoires [#1339, #1349], nouvelle route de recherche pour les communes et les EPCI [#1340], et enrichissement des exports de données (orientations [#1361] et champs pour data.inclusion [#1345]).
- **Interface et Expérience utilisateur** : Support du Markdown pour les bandeaux d'avertissement [#1404] et la comparaison de descriptions [#1364], gestion améliorée des erreurs de formulaires [#1392] et mise en place de la double écriture des conditions d'accès [#1318].

### Évolutions techniques
- **Infrastructure et Sécurité** : Migration vers SeaweedFS pour le stockage local S3 [#1376], mise à jour de l'image MinIO en CI [#1355], correction de la génération du token d'authentification ProConnect [#1363] et sécurisation des données via le masquage du lien de mobilisation interne [#1360].
- **Maintenance et Performance** : Suppression des workflows de modération pour les services et les structures [#1378, #1380], optimisation du chargement des structures pour le personnel [#1353] et nettoyage global du code (suppression de commandes de gestion obsolètes, de pages admin inutilisées et de colonnes de base de données inutilisées [#1377, #1317]).
- **Monitoring et Compatibilité** : Migration vers le SDK Sentry v11 [#1397] et amélioration de la compatibilité de la pagination avec les navigateurs sans helpers d'itérateur [#1391].
- **Outils** : Ajout d'une commande d'anonymisation des données [#1321].

### Autres changements
- Mise à jour de la configuration CSP pour autoriser Matomo [#1409] et actualisation de l'URL de Dora dans les scripts SQL [#1357].
