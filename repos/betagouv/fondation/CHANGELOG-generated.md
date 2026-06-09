## Changelog : fondation (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des documents, notamment les agendas et les rapports officiels, ainsi que sur la gestion des sessions et des archives. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience globale.

### Évolutions fonctionnelles
- Amélioration de la sélection des fichiers d'agenda et verrouillage des fichiers lors de leur publication officielle [#384](https://github.com/betagouv/fondation/issues/384).
- Ajout de l'heure de fin dans les rapports officiels [#379](https://github.com/betagouv/fondation/issues/379).
- Possibilité d'ajouter une renonciation aux plans de présentation [#378](https://github.com/betagouv/fondation/issues/378).
- Ajout de la possibilité de donner son avis (fonction "Je donne mon avis") [#360](https://github.com/betagouv/fondation/issues/360).
- Ajout des membres absents dans les plans de présentation [#358](https://github.com/betagouv/fondation/issues/358).
- Ajout de la gestion du statut des sessions [#362](https://github.com/betagouv/fondation/issues/362).
- Implémentation de l'archivage des sessions [#361](https://github.com/betagouv/fondation/issues/361) et [#364](https://github.com/betagouv/fondation/issues/364).
- Ajout de la recherche en texte intégral dans les fichiers de nomination [#336](https://github.com/betagouv/fondation/issues/336).
- Amélioration de la présentation des plans dans la liste [#386](https://github.com/betagouv/fondation/issues/386).
- Amélioration de la sélection des fichiers d'agenda [#384](https://github.com/betagouv/fondation/issues/384).

### Évolutions techniques
- Refactorisation du modèle de date pour plus de cohérence [#332](https://github.com/betagouv/fondation/issues/332).
- Mise en place d'un système de CI/CD avec Renovate pour la gestion des dépendances et l'automatisation des mises à jour.
- Optimisation de la configuration de Renovate pour limiter le nombre de PRs ouverts simultanément [#343](https://github.com/betagouv/fondation/issues/343).
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (axios, vite, @nestjs/core, postcss) [#346](https://github.com/betagouv/fondation/issues/346), [#347](https://github.com/betagouv/fondation/issues/347), [#356](https://github.com/betagouv/fondation/issues/356).
- Ajout d'une animation de recherche pour les fichiers [#337](https://github.com/betagouv/fondation/issues/337).

### Autres changements
- Correction de l'affichage des badges de documentation [#389](https://github.com/betagouv/fondation/issues/389).
- Correction de l'affichage des plans de présentation [#386](https://github.com/betagouv/fondation/issues/386).
- Correction de l'affectation de la version dans la préparation de la documentation [#382](https://github.com/betagouv/fondation/issues/382).
- Correction de l'affichage des pièces jointes pour les observateurs [#375](https://github.com/betagouv/fondation/issues/375).
- Correction de la normalisation des grades lors de l'importation des magistrats [#373](https://github.com/betagouv/fondation/issues/373).
- Correction de l'archivable des sessions avec un résultat nul [#376](https://github.com/betagouv/fondation/issues/376).
- Correction de l'affichage des rapports officiels sans agenda dans la liste des documents [#366](https://github.com/betagouv/fondation/issues/366).
- Mise à jour de la documentation README [#353](https://github.com/betagouv/fondation/issues/353).
- Correction de l'affichage des erreurs lors de l'importation [#355](https://github.com/betagouv/fondation/issues/355).
- Correction de la duplication des observateurs [#354](https://github.com/betagouv/fondation/issues/354).
- Correction du comportement des fichiers suspendus [#338](https://github.com/betagouv/fondation/issues/338).
- Ajout d'un audit de sécurité avec Zizmor [#339](https://github.com/betagouv/fondation/issues/339).
- Correction du pré-sélection des fichiers d'agenda [#359](https://github.com/betagouv/fondation/issues/359).
- Correction du feedback des rapports officiels [#341](https://github.com/betagouv/fondation/issues/341).
- Correction du préfixe des commits Renovate [#393](https://github.com/betagouv/fondation/issues/393).
- Correction du nom de l'agenda dans la liste des plans [#391](https://github.com/betagouv/fondation/issues/391).
- Correction du design des boutons de sélection des fichiers d'agenda [#390](https://github.com/betagouv/fondation/issues/390).
- Correction de l'utilisation du rôle utilisateur pour le bouton JDMA [#388](https://github.com/betagouv/fondation/issues/388).
- Correction du comptage des fichiers par statut [#371](https://github.com/betagouv/fondation/issues/371).
- Correction du rendu PDF après pagination [#370](https://github.com/betagouv/fondation/issues/370).
- Correction du tri des membres par nom [#384](https://github.com/betagouv/fondation/issues/384) et [#4570f02](https://github.com/betagouv/fondation/commit/4570f02196986180449197899976676065961411).
- Correction du formatage de l'heure [#0050199](https://github.com/betagouv/fondation/commit/0050199c7f3f14846011962c6116a1f73136379a).
- Ajout de vendor avant la migration [#83bfc54](https://github.com/betagouv/fondation/commit/83bfc54f18342f74f328693b4824334341264a16).
- Migration avec sheetjs [#38db17b](https://github.com/betagouv/fondation/commit/38db17b86f4558063742916272c6469684861221).
- Build API avec sheetjs [#33a44b3](https://github.com/betagouv/fondation/commit/33a44b3824461819f4697130944f165986660754).
