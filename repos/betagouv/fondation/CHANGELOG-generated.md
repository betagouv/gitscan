## Changelog : fondation (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions de la fondation se sont concentrées sur l'amélioration de la gestion des documents, notamment des fichiers de nomination et des agendas, ainsi que sur l'ajout de nouvelles fonctionnalités de recherche et d'archivage des sessions. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la recherche en texte intégral dans les fichiers de nomination. [#336](https://github.com/betagouv/fondation/issues/336)
- Amélioration de la présélection des fichiers d'agenda. [#359](https://github.com/betagouv/fondation/issues/359)
- Ajout de la possibilité d'ajouter des membres absents au plan de présentation. [#358](https://github.com/betagouv/fondation/issues/358)
- Ajout d'un éditeur WYSIWYG pour les documents. [#352](https://github.com/betagouv/fondation/issues/352)
- Ajout de la fonctionnalité "Je donne mon avis". [#360](https://github.com/betagouv/fondation/issues/360)
- Ajout de la fonctionnalité d'archivage des sessions. [#361](https://github.com/betagouv/fondation/issues/361)
- Amélioration de l'affichage des erreurs lors de l'importation de fichiers. [#355](https://github.com/betagouv/fondation/issues/355)
- Ajout de la possibilité de récupérer les présidents de formation. [#324](https://github.com/betagouv/fondation/issues/324)
- Ajout du statut des documents des fichiers de nomination. [#320](https://github.com/betagouv/fondation/issues/320)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (axios, vite, @nestjs/core, postcss).
- Refactoring du modèle de date pour plus de clarté. [#332](https://github.com/betagouv/fondation/issues/332)
- Suppression des modèles partagés du front-end. [#331](https://github.com/betagouv/fondation/issues/331)
- Suppression des migrations Drizzle. [#322](https://github.com/betagouv/fondation/issues/322)
- Initialisation de Renovate pour la gestion des dépendances. [#334](https://github.com/betagouv/fondation/issues/334)
- Suppression de la librairie `fast-xml-parser`. [#323](https://github.com/betagouv/fondation/issues/323)
- Mise à jour de la librairie DSFR. [#321](https://github.com/betagouv/fondation/issues/321)
- Ajout de tests d'acceptation. [#325](https://github.com/betagouv/fondation/issues/325)
- Correction de la configuration de Renovate. [#343](https://github.com/betagouv/fondation/issues/343)

### Autres changements
- Mise à jour du fichier README. [#353](https://github.com/betagouv/fondation/issues/353)
- Ajout d'une animation de recherche de fichiers. [#337](https://github.com/betagouv/fondation/issues/337)
- Configuration d'un audit Zizmor. [#339](https://github.com/betagouv/fondation/issues/339)
- Application des règles de linter et de formateur de code Oxlint et Oxfmt. [#329](https://github.com/betagouv/fondation/issues/329)
- Correction de bugs mineurs liés à l'ingestion des sessions LOLFI et à l'affichage de l'interface utilisateur.
- Correction d'un problème empêchant l'affichage des sessions vides dans LOLFI. [#328](https://github.com/betagouv/fondation/issues/328)
- Correction de l'emplacement de la sélection de l'agenda du rapport officiel.
- Correction de styles sur la combobox vide.
- Correction de la largeur du résultat du sélecteur de fichier de nomination de l'agenda.
