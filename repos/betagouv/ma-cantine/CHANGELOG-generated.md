## Changelog : ma-cantine (30 derniers jours)

### Résumé
Les dernières mises à jour de ma-cantine améliorent l'Observatoire avec de nouveaux filtres et corrections d'affichage, optimisent les performances de l'application, notamment au niveau des requêtes et des imports, et ajoutent de nouvelles fonctionnalités pour la gestion des télédéclarations et des données géographiques. Des améliorations sont également apportées à l'interface utilisateur, notamment sur le tableau de bord et dans l'administration des cantines.

### Évolutions fonctionnelles
- Amélioration des filtres dans l'Observatoire avec une recherche plus performante ([#6465](https://github.com/betagouv/ma-cantine/issues/6465)).
- Ajout d'un bouton pour accéder directement au bilan depuis le tableau de bord, remplaçant l'ancien badge "À compléter" ([#6492](https://github.com/betagouv/ma-cantine/issues/6492)).
- Ajout de phrases explicatives pour les champs géographiques et le code INSEE dans l'administration des cantines ([#6493](https://github.com/betagouv/ma-cantine/issues/6493)).
- Ajout d'une phrase d'explication pour le champ `declaration_donnees_2025` dans l'administration des cantines ([#6495](https://github.com/betagouv/ma-cantine/issues/6495)).
- Ajout de la possibilité d'exporter les cantines enregistrées via SIREN ([#6409](https://github.com/betagouv/ma-cantine/issues/6409)).
- Ajout de nouveaux supports pour le webinaire grandes collectivités ([#6470](https://github.com/betagouv/ma-cantine/issues/6470)).
- Ajout d'un nouveau tableauleur xlsx pour le suivi des achats ([#6426](https://github.com/betagouv/ma-cantine/issues/6426)).
- Ajout d'une nouvelle page dédiée aux imports de bilans détaillés ([#6397](https://github.com/betagouv/ma-cantine/issues/6397)).
- Ajout d'un fichier dédié à la création de cantines pour les gestionnaires ([#6383](https://github.com/betagouv/ma-cantine/issues/6383)).
- Ajout d'un fichier dédié à la modification des cantines ([#6407](https://github.com/betagouv/ma-cantine/issues/6407)).
- Ajout d'un fichier dédié à la création de cantines ([#6395](https://github.com/betagouv/ma-cantine/issues/6395)).
- Ajout d'un nouvel import via ID de cantine ([#6393](https://github.com/betagouv/ma-cantine/issues/6393)).

### Évolutions techniques
- Simplification du code d'inscription à la newsletter ([#6486](https://github.com/betagouv/ma-cantine/issues/6486)).
- Refactor de l'ETL pour afficher la durée d'insertion des données avec Pandas et améliorer le nom du dataset ([#6485](https://github.com/betagouv/ma-cantine/issues/6485)).
- Amélioration des performances en ajoutant un `prefetch_related` sur `annotate_with_is_managed_by_user` ([#6487](https://github.com/betagouv/ma-cantine/issues/6487)).
- Mise à jour de Django (5.1.15 à 5.2.11) et des dépendances associées (DRF, Wagtail) ([#6390](https://github.com/betagouv/ma-cantine/issues/6390)).
- Correction de tests flaky en améliorant le mocking ([#6457](https://github.com/betagouv/ma-cantine/issues/6457)).
- Ajout de tests parallèles pour accélérer l'exécution des tests ([#6483](https://github.com/betagouv/ma-cantine/issues/6483)).
- Ajout d'un script pour récupérer les communes avec leur code EPCI ([#6476](https://github.com/betagouv/ma-cantine/issues/6476)).
- Correction de la pagination du suivi des achats, augmentée de 10 à 500 ([#6489](https://github.com/betagouv/ma-cantine/issues/6489)).
- Correction d'un bug d'arrondi des décimales dans le gaspillage alimentaire ([#6449](https://github.com/betagouv/ma-cantine/issues/6449)).
- Correction d'un bug empêchant l'affichage de la modale de succès après un import échoué ([#6448](https://github.com/betagouv/ma-cantine/issues/6448)).
- Correction d'un problème de vérification des champs de cantine lors de la revendication ([#6388](https://github.com/betagouv/ma-cantine/issues/6388)).
- Correction d'un bug lié à l'annulation des télédéclarations et la suppression des snapshots ([#6423](https://github.com/betagouv/ma-cantine/issues/6423)).
- Amélioration de la gestion du timeout de Celery ([#6444](https://github.com/betagouv/ma-cantine/issues/6444)).
- Ajout de champs pour stocker les pourcentages bio, egalim et objectifs egalim atteints dans les télédéclarations ([#6481](https://github.com/betagouv/ma-cantine/issues/6481)).
- Ajout d'un champ pour indiquer la raison de la non prise en compte des bilans dans les statistiques ([#5753](https://github.com/betagouv/ma-cantine/issues/5753)).

### Autres changements
- Mise à jour de la documentation des télédéclarations ([#6401](https://github.com/betagouv/ma-cantine/issues/6401)).
- Suppression du bandeau rappel conso dans l'en-tête ([#6384](https://github.com/betagouv/ma-cantine/issues/6384)).
- Suppression de l'import admin des cantines ([#6387](https://github.com/betagouv/ma-cantine/issues/6387)).
- Ajout d'instructions pour Claude et Github Copilot ([#6419](https://github.com/betagouv/ma-cantine/issues/6419)).
- Ajout d'un filtre pour les armées dans les diagnostics ([#6453](https://github.com/betagouv/ma-cantine/issues/6453)).
- Suppression des tests nécessitant une connexion internet ([#6459](https://github.com/betagouv/ma-cantine/issues/6459)).
- Ajout de la possibilité de ne pas lancer les tests pour les changements de fichiers .md ou .pdf ([#6459](https://github.com/betagouv/ma-cantine/issues/6459)).
- Ajout de la gestion des erreurs Sentry pour les nouveaux imports de cantines ([#6412](https://github.com/betagouv/ma-cantine/issues/6412)).
- Amélioration du schéma d'import des bilans ([#6398](https://github.com/betagouv/ma-cantine/issues/6398)).
- Correction du lien vers le fichier d'exemple d'import des bilans détaillés ([#6404](https://github.com/betagouv/ma-cantine/issues/6404)).
