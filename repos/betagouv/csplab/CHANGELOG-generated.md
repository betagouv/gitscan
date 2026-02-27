## Changelog : csplab (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à csplab au cours des 30 derniers jours. Les principales évolutions concernent l'ingestion et le traitement des offres d'emploi et des CV, avec des améliorations significatives sur l'interface utilisateur et les fonctionnalités de recherche et de correspondance. Des efforts importants ont également été consacrés à la maintenance technique et à l'amélioration de l'infrastructure.

### Évolutions fonctionnelles
- Amélioration de la page de traitement des CV (candidats) avec de nouveaux styles (#223, #219).
- Ajout de détails en cas d'erreur lors de l'analyse JSON (#217).
- Implémentation de la correspondance entre les CV et les offres d'emploi (#167, #183).
- Ajout d'une page de résultats de CV simple avec une fonctionnalité de filtrage basique via HTMX (#180, #182, #204).
- Mise en place d'un système de polling pour la mise à jour des résultats de CV (#162, #165).
- Gestion des erreurs de CV dans le flux candidat (#164).
- Amélioration de la page d'accueil de Tycho avec de nouveaux styles (#180).
- Correction d'un bug empêchant le chargement correct des offres (#168).
- Correction d'un bug lié au remplacement de contenu lors du polling (#165).
- Correction d'un problème d'unicité dans le modèle VectorizedDocumentModel (#233).
- Correction de l'affichage des propriétés des cartes concours (#231).

### Évolutions techniques
- Refactorisation du dépôt de documents composites en un dépôt de documents et une passerelle de documents (#212).
- Simplification de la configuration pour les environnements (#215).
- Remplacement des ID d'entités par des UUID (#201).
- Mise à jour de la configuration de Sentry (#192).
- Remplacement de la vérification du format de commit par la vérification du titre de PR (#190).
- Mise à jour de la configuration pour permettre l'utilisation d'endpoints tiers personnalisés en mode développement et la définition de valeurs factices pour les tests (#188).
- Ajout de la Django Debug Toolbar en mode développement (#186).
- Séparation des paramètres de configuration en fonction de l'environnement et configuration de la collecte des fichiers statiques (#159).
- Refactorisation des administrateurs Django pour rendre certains champs en lecture seule (#184).
- Mise à jour de Django vers la version 6.0.1 (#143).
- Mise à jour de psycopg vers la version 3.3.2 (#144).
- Implémentation de la vectorisation des offres (#166).
- Amélioration de l'ingestion des offres avec la possibilité de traiter les documents par lots (#208).
- Amélioration de la robustesse de l'ingestion des offres (#138).
- Amélioration de l'ingestion des offres en permettant de charger des documents (#120).
- Mise en place d'une authentification JWT pour toutes les API (#2ce7d1).
- Alignement de la configuration du hook git avec la nouvelle configuration des emojis cz (#222, #221).
- Alignement de la configuration de djlint entre VSCode et la CLI (#220).
- Mise à jour des styles de la page de traitement des CV (#223).
- Mise à jour des styles de la page de téléchargement des CV (#219).
- Suppression de la verbosité excessive des tests (#199).
- Suppression des contraintes excessives dans les docstrings (#205).
- Ajout de la journalisation des messages dans la console (#194).

### Autres changements
- Mise à jour du fichier CHANGELOG.md pour les versions 0.1.3 et 0.1.2 (#185, #131).
- Nettoyage du code du repository (#211).
- Mise à jour des dépendances (#137, #136).
- Amélioration technique de l'ingestion des offres (#107).
- Correction de la configuration de Tycho avec Django 6 (#151).
- Correction de la localisation et du nettoyage des références (#154).
- Ajout de l'initialisation des métadonnées de CV (#182).
