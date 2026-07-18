## Changelog : cdata (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, l'application cdata a bénéficié d'améliorations significatives en termes de suivi de publication, d'exploration tabulaire des données et de gestion des visualisations. De nouvelles pages ont été ajoutées pour le suivi HVD et l'édition des organisations. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une page de suivi HVD (Hypervision des Données) [#1166](https://github.com/datagouv/cdata/issues/1166).
- Amélioration de l'exploration tabulaire des données :
    - Correction de l'affichage de l'aperçu tabulaire en cas d'erreur de carte [#1165](https://github.com/datagouv/cdata/issues/1165).
    - Ajustements et corrections diverses [#1157](https://github.com/datagouv/cdata/issues/1157).
- Nouvelle page dédiée au suivi de publication [#1137](https://github.com/datagouv/cdata/issues/1137).
- Nouvelle page d'édition pour les organisations [#1132](https://github.com/datagouv/cdata/issues/1132).
- Possibilité de sauvegarder une image lors de la sauvegarde d'une visualisation [#1111](https://github.com/datagouv/cdata/issues/1111).
- Améliorations des graphiques et des visualisations [#1088](https://github.com/datagouv/cdata/issues/1088).
- Gestion améliorée des notifications : ajout de la possibilité de marquer les notifications comme lues localement et actualisation multi-pages [#1121](https://github.com/datagouv/cdata/issues/1121).

### Évolutions techniques
- Utilisation de la nouvelle API reuse v2 [#1155](https://github.com/datagouv/cdata/issues/1155).
- Correction de la gestion des réponses non-JSON par l'API [#1159](https://github.com/datagouv/cdata/issues/1159).
- Suppression du fichier `components.lockfile` [#1156](https://github.com/datagouv/cdata/issues/1156).
- Mise à jour des composants (v1.3) [#1150](https://github.com/datagouv/cdata/issues/1150).
- Désactivation de l'analyse imbriquée des champs dans l'éditeur tabulaire [#1164](https://github.com/datagouv/cdata/issues/1164).
- Suppression du filtrage heuristique de titre pour les bouquets de fiches dans l'API OpenAPI [#1151](https://github.com/datagouv/cdata/issues/1151).
- Ajout de mocks pour les tests [#1154](https://github.com/datagouv/cdata/issues/1154).
- Sharding des tests E2E pour améliorer la performance [#1152](https://github.com/datagouv/cdata/issues/1152).

### Autres changements
- Ajout de tests unitaires [#1136](https://github.com/datagouv/cdata/issues/1136) et E2E [#1139](https://github.com/datagouv/cdata/issues/1139).
- Améliorations générales du code et mises à jour de certaines dépendances [#1158](https://github.com/datagouv/cdata/issues/1158).
