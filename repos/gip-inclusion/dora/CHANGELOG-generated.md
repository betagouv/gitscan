## Changelog : dora (30 derniers jours, au 02 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de la structure des données (migration vers le framework DI_v1) afin d'optimiser la gestion des services, des structures et des publics. Parallèlement, l'expérience utilisateur a été enrichie par de nouvelles notifications, une recherche plus fluide et des informations plus détaillées dans l'interface.

### Évolutions fonctionnelles
- **Notifications & Alertes** : Mise en place de notifications Slack lors du passage d'une orientation en modération [#1296](https://github.com/gip-inclusion/dora/issues/1296).
- **Recherche** : Amélioration de l'expérience de recherche avec une limitation du nombre de résultats pour plus de clarté [#1245](https://github.com/gip-inclusion/dora/issues/1245) et réactivation de la recherche textuelle [#1254](https://github.com/gip-inclusion/dora/issues/1254).
- **Interface & UX** : 
    - Affichage des précisions concernant les publics sur les pages de détail des services [#1264](https://github.com/gip-inclusion/dora/issues/1264).
    - Suppression de la limite du nombre de catégories par service [#1289](https://github.com/gip-inclusion/dora/issues/1289).
    - Accès facilité aux pages d'administration des structures pour les Groupes Territoriaux (GT) [#1286](https://github.com/gip-inclusion/dora/issues/1286).
- **Exports** : Ajout de la colonne "Identifiant FT" dans l'export des orientations reçues [#1290](https://github.com/gip-inclusion/dora/issues/1290).
- **Corrections** : 
    - Correction des URLs vers l'administration Django [#1295](https://github.com/gip-inclusion/dora/issues/1295).
    - Correction du filtrage des services "tous-publics" [#1261](https://github.com/gip-inclusion/dora/issues/1261).
    - Correction de l'utilisation des labels de financement [#1309](https://github.com/gip-inclusion/dora/issues/1309).
    - Garantie de l'unicité des critères d'admission [#1243](https://github.com/gip-inclusion/dora/issues/1243).

### Évolutions techniques
- **Architecture de données** : Migration massive vers le nouveau framework de données `di_v1`, impactant les services, les structures et les champs de mobilisation.
- **Refactoring** : 
    - Simplification de la gestion des "Publics" et des "Types de services" (passage de relations Many-to-Many à des champs plus performants comme `ArrayField` ou des colonnes uniques).
    - Refonte et fusion des descriptions de services pour une meilleure cohérence des données.
- **Performance** : Optimisation de la vitesse de chargement des pages d'édition de services et de modèles via la parallélisation des appels de données [#1281](https://github.com/gip-inclusion/dora/issues/1281).
- **Automatisation** : Ajout d'une tâche mensuelle automatique pour la mise à jour de la base de données Sirene [#1310](https://github.com/gip-inclusion/dora/issues/1310).
- **Maintenance & Infrastructure** : 
    - Rollback de la version de Django vers la 6.0.8 pour assurer la stabilité [#1313](https://github.com/gip-inclusion/dora/issues/1313).
    - Nettoyage de plusieurs colonnes et commandes d'importation obsolètes.

### Autres changements
- **Documentation** : Amélioration de la documentation technique concernant les données d'orientation.
