## Changelog : carbure (30 derniers jours, au 19/11/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes dans la précision et la fiabilité de la traçabilité des biocarburants. Les évolutions majeures concernent une refonte complète du processus d'invitation des utilisateurs, une amélioration significative de la gestion des unités et des matériaux (masse, volume, énergie), ainsi que l'ajout de fonctionnalités dédiées aux fournisseurs de biométhane. La sécurité des données a également été renforcée par l'automatisation de l'anonymisation lors des processus de sauvegarde.

### Évolutions fonctionnelles
- **Gestion de la traçabilité et des matériaux** :
    - Amélioration de la précision des données lors des imports Excel (gestion des décimales pour les émissions).
    - Nouvelle gestion des unités et des matériaux : possibilité de choisir entre masse, volume ou énergie, et intégration des propriétés physiques (PCI, densité) directement dans les actions.
    - Mise en place d'une matrice de statut pour mieux contrôler les transitions et les créations de données.
    - Importation du catalogue de matériaux via des fichiers CSV.
- **Biométhane** :
    - Création d'un espace dédié pour les fournisseurs de gaz permettant de visualiser les déclarations des producteurs liés par contrat.
    - Ajout de la possibilité de rouvrir les déclarations annuelles (via commande ou interface DREAL).
    - Amélioration de la gestion des types de collecte pour les résidus IAA.
- **Authentification et accès** :
    - Refonte du parcours d'invitation : création d'une page dédiée pour finaliser l'activation, meilleure gestion des liens expirés et des renvois de mails [#2431](https://github.com/MTES-MCT/carbure/issues/2431).
    - Amélioration de l'interface d'administration avec l'affichage du nombre total d'utilisateurs.
- **Interface utilisateur** :
    - Meilleure visibilité des unités et des décimales dans les champs de saisie en lecture seule.
    - Masquage (plutôt que suppression) de certains biocarburants spécifiques (ETBE) pour épurer l'interface.

### Évolutions techniques
- **Sécurité et protection des données** :
    - Mise en place de l'anonymisation automatique des données personnelles (mots de passe, emails) dans les sauvegardes, les réplicas SQL et les logs d'administration [#2350](https://github.com/MTES-MCT/carbure/issues/2350).
    - Ajout d'une confirmation utilisateur avant l'import de dumps sur la base de production [#2472](https://github.com/MTES-MCT/carbure/issues/2472).
    - Mise à jour des configurations CSP et correction de vulnérabilités (notamment sur `soupsieve`).
- **Performance et Infrastructure** :
    - Optimisation des requêtes de pagination et de filtrage sur le module Qualicharge [#2495](https://github.com/MTES-MCT/carbure/issues/2495).
    - Intégration de Trivy dans la CI pour le scan de sécurité des conteneurs.
    - Optimisation des pipelines CI pour éviter les exécutions inutiles.
- **Maintenance logicielle** :
    - Mise à jour majeure du backend et du frontend pour supporter les changements de versions de Django REST Framework, Pandas et React Router v7.

### Autres changements
- **Tests** : Amélioration de la robustesse des suites de tests, notamment sur les modules biométhane et TIRUERT, et correction de la persistance des données de test.
- **Documentation** : Mise à jour du schéma de l'API.
