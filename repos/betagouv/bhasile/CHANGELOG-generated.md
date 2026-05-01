## Changelog : bhasile (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la recherche et du filtrage des données, notamment pour les CPOM et les structures. Des améliorations significatives ont été apportées à l'interface utilisateur, notamment pour la gestion des opérateurs et des indicateurs de qualité. Des corrections de bugs et des optimisations de performance ont également été réalisées pour améliorer la stabilité et la réactivité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de rechercher des structures par code DNA/FINESS [#1112](https://github.com/betagouv/bhasile/issues/1112).
- Amélioration de l'interface utilisateur pour l'importation d'adresses [#1206](https://github.com/betagouv/bhasile/issues/1206).
- Ajout de la possibilité d'étendre la date de fin des avenants [#1211](https://github.com/betagouv/bhasile/issues/1211).
- Nouvelle interface utilisateur pour la gestion des opérateurs, incluant la recherche et la mise à jour [#1148](https://github.com/betagouv/bhasile/issues/1148), [#1159](https://github.com/betagouv/bhasile/issues/1159), [#1168](https://github.com/betagouv/bhasile/issues/1168).
- Ajout d'indicateurs de qualité pour les actes administratifs [#1218](https://github.com/betagouv/bhasile/issues/1218).
- Amélioration du filtre et du tri des CPOM [#1095](https://github.com/betagouv/bhasile/issues/1095).
- Ajout de la possibilité d'ajouter plusieurs adresses collectives [#1160](https://github.com/betagouv/bhasile/issues/1160).
- Ajout de notes [#1146](https://github.com/betagouv/bhasile/issues/1146).
- Ajout de la gestion des filiales [#1145](https://github.com/betagouv/bhasile/issues/1145), [#1153](https://github.com/betagouv/bhasile/issues/1153).
- Ajout de la gestion des rôles et permissions [#1050](https://github.com/betagouv/bhasile/issues/1050).
- Ajout d'un modal de confirmation lors de la modification d'un formulaire [#1179](https://github.com/betagouv/bhasile/issues/1179).

### Évolutions techniques
- Refactorisation de l'architecture vers une structure à 3 niveaux [#1219](https://github.com/betagouv/bhasile/issues/1219).
- Ajout de routage côté client pour la transformation [#1216](https://github.com/betagouv/bhasile/issues/1216).
- Suppression des indicateurs financiers du schéma de budget [#1205](https://github.com/betagouv/bhasile/issues/1205).
- Déplacement de la logique de détermination de `isSubventionee` et `isAutorisee` côté serveur [#1188](https://github.com/betagouv/bhasile/issues/1188).
- Amélioration de la performance du pipeline [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1171](https://github.com/betagouv/bhasile/issues/1171), [#1172](https://github.com/betagouv/bhasile/issues/1172).
- Séparation du schéma Prisma [#1142](https://github.com/betagouv/bhasile/issues/1142).
- Normalisation des dates [#1136](https://github.com/betagouv/bhasile/issues/1136).
- Suppression de champs inutiles pour UserAction [#1128](https://github.com/betagouv/bhasile/issues/1128).

### Autres changements
- Correction de bugs concernant l'affichage de la qualité des structures [#1220](https://github.com/betagouv/bhasile/issues/1220).
- Correction de bugs d'affichage et de construction de la carte [#1192](https://github.com/betagouv/bhasile/issues/1192), [#1212](https://github.com/betagouv/bhasile/issues/1212).
- Correction d'un problème de z-index de la table par rapport à l'en-tête [#1171](https://github.com/betagouv/bhasile/issues/1171).
- Amélioration du style des statistiques de l'opérateur [#1213](https://github.com/betagouv/bhasile/issues/1213).
- Corrections cosmétiques de la carte [#1214](https://github.com/betagouv/bhasile/issues/1214).
- Ajout de tests unitaires et E2E [#1178](https://github.com/betagouv/bhasile/issues/1178), [#1184](https://github.com/betagouv/bhasile/issues/1184), [#1197](https://github.com/betagouv/bhasile/issues/1197), [#1202](https://github.com/betagouv/bhasile/issues/1202), [#1203](https://github.com/betagouv/bhasile/issues/1203).
- Mise à jour de la documentation et des dépendances.
- Nettoyage du code et corrections de typos.
- Correction de l'affichage des documents financiers [#1137](https://github.com/betagouv/bhasile/issues/1137), [#1181](https://github.com/betagouv/bhasile/issues/1181).
- Amélioration de l'accessibilité et du design [#1108](https://github.com/betagouv/bhasile/issues/1108).
