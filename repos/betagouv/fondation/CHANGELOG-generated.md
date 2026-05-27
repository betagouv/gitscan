## Changelog : fondation (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche et de la gestion des documents, notamment les fichiers de nomination et les pièces jointes aux observations. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des agendas, ainsi que des corrections de bugs pour une meilleure stabilité. Des efforts ont été réalisés pour moderniser l'infrastructure et améliorer la sécurité du projet.

### Évolutions fonctionnelles
- Amélioration de la présélection des fichiers d'agenda. [#359](https://github.com/betagouv/fondation/issues/359)
- Ajout de la possibilité de donner son avis. [#360](https://github.com/betagouv/fondation/issues/360)
- Ajout des membres absents dans le plan de présentation. [#358](https://github.com/betagouv/fondation/issues/358)
- Ajout d'un éditeur WYSIWYG pour les documents. [#352](https://github.com/betagouv/fondation/issues/352)
- Correction de l'affichage des erreurs lors de l'importation de fichiers. [#355](https://github.com/betagouv/fondation/issues/355)
- Ajout de la recherche en texte intégral dans les fichiers de nomination. [#336](https://github.com/betagouv/fondation/issues/336)
- Ajout de la possibilité de lier une pièce jointe à une observation. [#317](https://github.com/betagouv/fondation/issues/317)
- Récupération des présidents de formation. [#324](https://github.com/betagouv/fondation/issues/324)
- Ajout du statut des documents des fichiers de nomination. [#320](https://github.com/betagouv/fondation/issues/320)
- Correction du problème des fichiers suspendus qui continuaient de s'exécuter. [#338](https://github.com/betagouv/fondation/issues/338)
- Correction de l'affichage des combobox vides.
- Correction de la largeur du sélecteur de fichiers de nomination dans l'agenda.

### Évolutions techniques
- Mise en place d'un système de cache pour Playwright afin d'accélérer les tests. [#357](https://github.com/betagouv/fondation/issues/357)
- Refactorisation du modèle de date pour une meilleure gestion. [#332](https://github.com/betagouv/fondation/issues/332)
- Suppression des modèles partagés du frontend pour simplifier l'architecture. [#331](https://github.com/betagouv/fondation/issues/331)
- Suppression des migrations Drizzle. [#322](https://github.com/betagouv/fondation/issues/322)
- Introduction d'une utilitaire pour gérer les requêtes multipart JSON. [#318](https://github.com/betagouv/fondation/issues/318)
- Amélioration de la recherche des observations des magistrats. [#316](https://github.com/betagouv/fondation/issues/316)
- Suppression de la dépendance `fast-xml-parser`. [#323](https://github.com/betagouv/fondation/issues/323)
- Mise à jour de TailwindCSS. [#330](https://github.com/betagouv/fondation/issues/330)
- Intégration des outils d'analyse de code Oxlint et Oxfmt. [#329](https://github.com/betagouv/fondation/issues/329)

### Autres changements
- Mise à jour du fichier README. [#353](https://github.com/betagouv/fondation/issues/353)
- Configuration de Renovate pour limiter à une seule PR par mise à jour. [#350](https://github.com/betagouv/fondation/issues/350)
- Initialisation et configuration de Renovate pour la gestion des dépendances. [#334](https://github.com/betagouv/fondation/issues/334)
- Ajout d'une animation de recherche pour les fichiers. [#337](https://github.com/betagouv/fondation/issues/337)
- Correction d'un problème empêchant l'ingestion des sessions LOLFI. [#328](https://github.com/betagouv/fondation/issues/328)
- Ajout de tests d'acceptation. [#325](https://github.com/betagouv/fondation/issues/325)
- Correction d'un bug empêchant la sélection de l'agenda du rapport officiel.
- Correction d'un problème avec la session LOLFI.
- Correction de problèmes de style sur l'agenda.
- Audit de sécurité Zizmor. [#339](https://github.com/betagouv/fondation/issues/339)
