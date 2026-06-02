## Changelog : fondation (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des sessions, des rapports officiels et de la recherche de documents. Des correctifs ont été apportés pour améliorer la stabilité et l'expérience utilisateur, notamment en corrigeant des bugs liés à l'affichage des informations et à l'archivage des sessions. L'équipe a également travaillé sur de nouvelles fonctionnalités comme l'avis sur les documents et l'intégration d'un éditeur WYSIWYG.

### Évolutions fonctionnelles
- Ajout de la possibilité de donner un avis sur les documents. [#360](https://github.com/betagouv/fondation/issues/360)
- Intégration d'un éditeur WYSIWYG pour les documents. [#352](https://github.com/betagouv/fondation/issues/352)
- Ajout de la possibilité d'afficher les membres absents dans le plan de présentation. [#358](https://github.com/betagouv/fondation/issues/358)
- Amélioration de la présélection des fichiers d'ordre du jour. [#359](https://github.com/betagouv/fondation/issues/359)
- Ajout du statut des sessions. [#362](https://github.com/betagouv/fondation/issues/362)
- Implémentation de l'archivage des sessions. [#361](https://github.com/betagouv/fondation/issues/361) et [#364](https://github.com/betagouv/fondation/issues/364)
- Correction de l'affichage des rapports officiels sans ordre du jour dans la liste des documents. [#366](https://github.com/betagouv/fondation/issues/366)
- Correction de l'inclusion du résultat supprimé dans le statut de la session signalée. [#368](https://github.com/betagouv/fondation/issues/368)
- Correction du tri des membres par nom. [#384](https://github.com/betagouv/fondation/issues/384)
- Correction du formatage de l'heure en HH:mm. [#384](https://github.com/betagouv/fondation/issues/384)
- Correction de l'affichage du secrétaire du rapport officiel. [#367](https://github.com/betagouv/fondation/issues/367)

### Évolutions techniques
- Refactorisation du modèle de date pour une meilleure cohérence. [#332](https://github.com/betagouv/fondation/issues/332)
- Suppression du module `shared-models` du front-end. [#331](https://github.com/betagouv/fondation/issues/331)
- Intégration des outils d'analyse de code Oxlint et Oxfmt. [#329](https://github.com/betagouv/fondation/issues/329)
- Mise en place d'un workflow de publication (release workflow). [#327](https://github.com/betagouv/fondation/issues/327)
- Ajout de la recherche en texte intégral dans les fichiers de nomination. [#336](https://github.com/betagouv/fondation/issues/336)
- Suppression de `@tailwindcss/postcss`. [#345](https://github.com/betagouv/fondation/issues/345)

### Autres changements
- Mise à jour de la documentation README. [#353](https://github.com/betagouv/fondation/issues/353)
- Configuration de Renovate pour la gestion des dépendances. [#334](https://github.com/betagouv/fondation/issues/334), [#343](https://github.com/betagouv/fondation/issues/343) et [#350](https://github.com/betagouv/fondation/issues/350)
- Ajout d'une animation de recherche de fichiers. [#337](https://github.com/betagouv/fondation/issues/337)
- Correction de bugs mineurs liés à l'importation de fichiers et à l'ingestion des sessions LOLFI. [#326](https://github.com/betagouv/fondation/issues/326), [#328](https://github.com/betagouv/fondation/issues/328) et [#338](https://github.com/betagouv/fondation/issues/338)
- Correction de problèmes de style et d'affichage.
- Correction de l'empêchement de l'envoi de sessions vides depuis LOLFI.
