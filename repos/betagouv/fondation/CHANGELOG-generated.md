## Changelog : fondation (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a déployé de nombreuses améliorations pour faciliter la gestion des affectations, des observations et des fichiers. Les utilisateurs bénéficieront d'une interface plus intuitive, de nouvelles fonctionnalités comme l'ingestion de données LOLLI, et de corrections de bugs pour une meilleure expérience globale. Des améliorations techniques ont également été apportées pour optimiser la performance et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un manuel utilisateur pour faciliter la prise en main [#261](https://github.com/betagouv/fondation/issues/261).
- Possibilité de trier les résultats dans les listes (outcomes, reporters affectés) [#259](https://github.com/betagouv/fondation/issues/259), [#258](https://github.com/betagouv/fondation/issues/258), [#260](https://github.com/betagouv/fondation/issues/260).
- Gestion de plusieurs priorités pour les tâches [#259](https://github.com/betagouv/fondation/issues/259).
- Ajout d'indicateurs visuels pour les commentaires et descriptions d'observations [#265](https://github.com/betagouv/fondation/issues/265), [#257](https://github.com/betagouv/fondation/issues/257).
- Possibilité d'ajouter plusieurs pièces jointes à une session [#254](https://github.com/betagouv/fondation/issues/254).
- Ajout de deux nouveaux types de résultats de fichiers [#255](https://github.com/betagouv/fondation/issues/255).
- Amélioration de la gestion des identifiants de connexion (insensibilité à la casse) [#253](https://github.com/betagouv/fondation/issues/253).
- Possibilité de définir un nombre minimal de reporters requis [#256](https://github.com/betagouv/fondation/issues/256).
- Ajout d'alertes en cas de position requise avec pièce jointe [#192](https://github.com/betagouv/fondation/issues/192).
- Amélioration de l'affichage des candidatures avec un badge indiquant le total [#190](https://github.com/betagouv/fondation/issues/190).
- Affichage de l'acronyme du poste pour les magistrats [#172](https://github.com/betagouv/fondation/issues/172).
- Ajout de l'âge dans la carte récapitulative [#180](https://github.com/betagouv/fondation/issues/180).
- Ajout de la version de l'application dans le pied de page [#197](https://github.com/betagouv/fondation/issues/197).
- Possibilité d'exclure des membres lors de l'affectation automatique [#189](https://github.com/betagouv/fondation/issues/189).
- Déplacement du bloc des observateurs dans les détails du magistrat [#188](https://github.com/betagouv/fondation/issues/188).
- Ajout d'un indicateur de suivi pour les observations [#198](https://github.com/betagouv/fondation/issues/198).
- Ajout de la description des observations [#193](https://github.com/betagouv/fondation/issues/193).
- Ajout de la position actuelle [#218](https://github.com/betagouv/fondation/issues/218).

### Évolutions techniques
- Intégration de Sentry pour le suivi des erreurs HTTP [#249](https://github.com/betagouv/fondation/issues/249).
- Amélioration de la requête pour les détails des sessions des membres [#251](https://github.com/betagouv/fondation/issues/251).
- Optimisation du filtrage des rapports par statut [#250](https://github.com/betagouv/fondation/issues/250).
- Refactorisation de l'affectation automatique dans plusieurs fichiers [#236](https://github.com/betagouv/fondation/issues/236).
- Amélioration de la gestion de l'affectation automatique (gestion des exclusions, arrondis, distribution arithmétique, affectation unique) [#235](https://github.com/betagouv/fondation/issues/235), [#226](https://github.com/betagouv/fondation/issues/226), [#225](https://github.com/betagouv/fondation/issues/225), [#223](https://github.com/betagouv/fondation/issues/223).
- Mise à jour des dépendances API et client [#240](https://github.com/betagouv/fondation/issues/240), [#238](https://github.com/betagouv/fondation/issues/238).
- Ajout de tests full-stack de base [#187](https://github.com/betagouv/fondation/issues/187).
- Suppression de Lodash [#202](https://github.com/betagouv/fondation/issues/202).
- Mise à jour de React Router [#183](https://github.com/betagouv/fondation/issues/183).
- Ajout d'un module HTTP [#205](https://github.com/betagouv/fondation/issues/205).

### Autres changements
- Ajout de scripts pour les fichiers XSD [#252](https://github.com/betagouv/fondation/issues/252).
- Amélioration des instructions Copilot [#230](https://github.com/betagouv/fondation/issues/230).
- Suppression de Dependabot [#252](https://github.com/betagouv/fondation/issues/252).
- Ajout de tags aux utilisateurs lors des notifications de changelog [#227](https://github.com/betagouv/fondation/issues/227).
- Correction d'un problème empêchant l'importation en double [#233](https://github.com/betagouv/fondation/issues/233).
- Prévention des bursts d'observations [#264](https://github.com/betagouv/fondation/issues/264).
- Correction d'un bug d'affichage de l'icône de commentaire [#265](https://github.com/betagouv/fondation/issues/265).
- Correction d'un problème lié à la récupération de la charge de travail sur une version non publiée [#222](https://github.com/betagouv/fondation/issues/222).
- Correction d'un problème de connexion (insensibilité à la casse) [#253](https://github.com/betagouv/fondation/issues/253).
- Amélioration des permissions CI en production [#186](https://github.com/betagouv/fondation/issues/186), [#184](https://github.com/betagouv/fondation/issues/184).
- Corrections mineures de typographie et d'affichage.
