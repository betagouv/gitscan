## Changelog : dora (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, l'activité a été principalement portée par une refonte de la gestion des données pour assurer une synchronisation fluide avec les plateformes externes (Data Inclusion). Le projet a également bénéficié d'améliorations de l'expérience utilisateur, notamment sur la recherche, la gestion des services et le système de notifications.

### Évolutions fonctionnelles
- **Recherche** : Ajout d'une fonctionnalité de recherche par communes et EPCI [#1340](https://github.com/gip-inclusion/dora/issues/1340).
- **Services** : Ajout du champ des horaires d'accueil et levée de la limite du nombre de catégories par service [#1289](https://github.com/gip-inclusion/dora/issues/1289).
- **Services** : Amélioration de la visibilité des détails des publics sur les pages de services [#1264](https://github.com/gip-inclusion/dora/issues/1264).
- **Filtres** : Correction de l'affichage des services "tous publics" lors de l'utilisation des filtres [#1261](https://github.com/gip-inclusion/dora/issues/1261).
- **Exports** : Intégration de l'identifiant FT dans les exports d'orientations reçues [#1290](https://github.com/gip-inclusion/dora/issues/1290).
- **Notifications** : Mise en place d'alertes Slack lors du passage d'une orientation en modération [#1296](https://github.com/gip-inclusion/dora/issues/1296).
- **Administration** : Correction des liens vers l'interface d'administration Django [#1295](https://github.com/gip-inclusion/dora/issues/1295) et accès facilité pour les GT aux pages d'administration des structures [#1286](https://github.com/gip-inclusion/dora/issues/1286).

### Évolutions techniques
- **Synchronisation de données** : Implémentation d'un nouveau framework de migration (`di_v1`) pour synchroniser les services et les structures avec Data Inclusion [#1345](https://github.com/gip-inclusion/dora/issues/1345), [913886b](https://github.com/gip-inclusion/dora/issues/913886b).
- **Cohérence des données** : Mise en place de la "double écriture" pour les conditions d'accès, les zones d'éligibilité et les descriptions afin de garantir la fiabilité des données synchronisées [#1318](https://github.com/gip-inclusion/dora/issues/1318), [5c65b5b](https://github.com/gip-inclusion/dora/issues/5c65b5b), [#1306](https://github.com/gip-inclusion/dora/issues/1306).
- **Refonte du modèle "Services"** : Restructuration majeure du modèle (renommage de champs, suppression de `ServiceKind`, fusion algorithmique des descriptions) [#1282](https://github.com/gip-inclusion/dora/issues/1282), [#1266](https://github.com/gip-inclusion/dora/issues/1266), [#1257](https://github.com/gip-inclusion/dora/issues/1257).
- **Performance** : Optimisation de la vitesse de chargement des pages d'édition via la parallélisation des appels [#1281](https://github.com/gip-inclusion/dora/issues/1281).
- **Automatisation** : Ajout d'une tâche mensuelle pour la mise à jour automatique de la base Sirene [#1310](https://github.com/gip-inclusion/dora/issues/1310).
- **Maintenance et Sécurité** : Ajout de commandes pour l'anonymisation des données [#1321](https://github.com/gip-inclusion/dora/issues/1321) et la normalisation des mots de passe [#1271](https://github.com/gip-inclusion/dora/issues/1271).

### Autres changements
- **Nettoyage** : Suppression de plusieurs commandes de gestion (management commands) et scripts obsolètes.
- **Nettoyage** : Retrait de colonnes et champs de données inutilisés (`orientation_reasons`, `use_inclusion_numerique_scheme`).
- **Documentation** : Amélioration de la documentation technique concernant les données d'orientation.
