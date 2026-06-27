## Changelog : pitchou (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des données, notamment en migrant les fichiers vers un nouveau stockage plus performant (Outscale Object Storage) et en optimisant la gestion des espèces protégées. Des améliorations significatives ont également été apportées aux statistiques et à l'administration, avec l'ajout de nouvelles fonctionnalités pour le suivi des indicateurs AARRI et la gestion des utilisateurs. Enfin, une refactorisation importante a été réalisée pour moderniser le code et préparer le projet pour l'avenir.

### Évolutions fonctionnelles
- Ajout d'un bouton "Retour" sur la page dossier. [#609](https://github.com/betagouv/pitchou/issues/609)
- Ajout d'un fil d'Ariane pour faciliter la navigation dans la documentation. [#610](https://github.com/betagouv/pitchou/issues/610)
- Amélioration de la section évolution des indicateurs AARRI dans les statistiques. [#597](https://github.com/betagouv/pitchou/issues/597)
- Ajout d'une page d'erreur 404 personnalisée. [#596](https://github.com/betagouv/pitchou/issues/596)
- Possibilité d'éditer le champ "enjeux" dans l'instruction. [#604](https://github.com/betagouv/pitchou/issues/604)
- Les dates de consultation du public sont désormais éditables dans l'onglet instruction. [#600](https://github.com/betagouv/pitchou/issues/600)
- Ajout de la possibilité de télécharger les événements utilisateurs pour les statistiques AARRI. [#591](https://github.com/betagouv/pitchou/issues/591)
- Ajout de la liste des espèces protégées en base de données, remplaçant le fichier CSV. [#589](https://github.com/betagouv/pitchou/issues/589)
- Ajout de nouveaux domaines autorisés pour l'authentification : indre-et-loire et guyane. [#579](https://github.com/betagouv/pitchou/issues/579) et ext.beta.gouv.fr [#601](https://github.com/betagouv/pitchou/issues/601)
- Ajout de *Cosentinia vellea* et du grand capricorne à la liste des espèces protégées. [#578](https://github.com/betagouv/pitchou/issues/578) et [#575](https://github.com/betagouv/pitchou/issues/575)
- Ajout d'une matrice d'impact à la page des statistiques. [#599](https://github.com/betagouv/pitchou/issues/599)

### Évolutions techniques
- Migration des fichiers vers Outscale Object Storage pour une meilleure performance et scalabilité. [#573](https://github.com/betagouv/pitchou/issues/573)
- Refactorisation du dépôt en monorepo. [#595](https://github.com/betagouv/pitchou/issues/595) et [#593](https://github.com/betagouv/pitchou/issues/593)
- Migration progressive vers TypeScript. [#568](https://github.com/betagouv/pitchou/issues/568) et [#567](https://github.com/betagouv/pitchou/issues/567)
- Correction du fuseau horaire des dates dans les dossiers. [#612](https://github.com/betagouv/pitchou/issues/612)
- Correction du chemin du schéma DS pour le worker. [#603](https://github.com/betagouv/pitchou/issues/603)
- Suppression des liens vers la démarche numérique dans les dossiers/avis d'expert. [#554cdc](https://github.com/betagouv/pitchou/commit/5554cde)
- Amélioration de la gestion des doublons de décisions administratives lors de la synchronisation. [#584](https://github.com/betagouv/pitchou/issues/584)
- Correction de l'affichage des fichiers espèces impactées après la migration vers Object Storage. [#590](https://github.com/betagouv/pitchou/issues/590)
- Correction d'une erreur 500 lors du téléchargement de fichiers. [#587](https://github.com/betagouv/pitchou/issues/587)
- Correction d'un bug empêchant le reset correct de l'état "vu" des notifications. [#592](https://github.com/betagouv/pitchou/issues/592)

### Autres changements
- Suppression de l'historique de la date d'envoi de la dernière contribution. [#615](https://github.com/betagouv/pitchou/issues/615)
- Ajout de pièces jointes aux seeds. [#614](https://github.com/betagouv/pitchou/issues/614)
- Enrichissement des seeds avec des dossiers plus réalistes. [#608](https://github.com/betagouv/pitchou/issues/608)
- Suppression du service tooling du Docker Compose. [#572](https://github.com/betagouv/pitchou/issues/572)
- Passage de `pgdata` en volume nommé dans le Docker Compose pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Ajout d'un bandeau sur l'environnement staging. [#574](https://github.com/betagouv/pitchou/issues/574)
- Documentation sur le suivi des événements utilisateurs. [#586](https://github.com/betagouv/pitchou/issues/586)
- Correction du format du fichier CSV pour les événements métriques AARRI. [#585](https://github.com/betagouv/pitchou/issues/585)
- Suppression de la synchronisation des "enjeux politique et écologique" depuis la démarche numérique. [#605](https://github.com/betagouv/pitchou/issues/605)
- Remplacement de `db-clear` par `data-clear` pour vider à la fois la base de données et le bucket S3.
