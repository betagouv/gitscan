## Changelog : potentiel (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du module de raccordement, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la gestion des données et des workflows, notamment concernant les candidatures, les mainlevées et les informations relatives aux projets. Des améliorations ont également été apportées à l'export de données et à la gestion des permissions.

### Évolutions fonctionnelles
- Possibilité pour l'administration de corriger le numéro d'identification d'un projet. [#4498](https://github.com/MTES-MCT/potentiel/issues/4498)
- La DGEc peut accorder un recours pour un projet éliminé avec une date d'accord identique à la date de désignation. [#4497](https://github.com/MTES-MCT/potentiel/issues/4497)
- Intégration du module de raccordement au menu principal, avec des améliorations de l'interface et des corrections de bugs. [#4476](https://github.com/MTES-MCT/potentiel/issues/4476) et [#4492](https://github.com/MTES-MCT/potentiel/issues/4492)
- Ajout de la possibilité de supprimer un document de raccordement. [#4413](https://github.com/MTES-MCT/potentiel/issues/4413)
- Ajout de données PV (Procès Verbal) dans le détail d'une candidature. [#4400](https://github.com/MTES-MCT/potentiel/issues/4400)
- Ajout de l'export CSV des candidats non notifiés. [#4406](https://github.com/MTES-MCT/potentiel/issues/4406)
- Ajout du volume réservé à l'instruction des candidatures. [#4429](https://github.com/MTES-MCT/potentiel/issues/4429) et [#4474](https://github.com/MTES-MCT/potentiel/issues/4474)
- Un cocontractant peut corriger une date d'achèvement réel. [#4440](https://github.com/MTES-MCT/potentiel/issues/4440)
- Ajout d'un lien vers le jeu de données dans le footer. [#4442](https://github.com/MTES-MCT/potentiel/issues/4442)
- Possibilité pour les administrateurs de corriger la date d'achèvement réel. [#4352](https://github.com/MTES-MCT/potentiel/issues/4352)
- Qualification des fichiers PTF/CR/CRD. [#4372](https://github.com/MTES-MCT/potentiel/issues/4372) et [#4672](https://github.com/MTES-MCT/potentiel/issues/4672)

### Évolutions techniques
- Mise à jour de Keycloak en version 26.7.0. [#4439](https://github.com/MTES-MCT/potentiel/issues/4439)
- Amélioration de la vérification des permissions sur les routes Next.js. [#4420](https://github.com/MTES-MCT/potentiel/issues/4420)
- Refactoring du module de raccordement côté front-end. [#4368](https://github.com/MTES-MCT/potentiel/issues/4368)
- Script pour harmoniser les données des candidatures PV ayant des trackers. [#4483](https://github.com/MTES-MCT/potentiel/issues/4483)
- Script de vérification des données EDF OA (date achèvement réel). [#4433](https://github.com/MTES-MCT/potentiel/issues/4433)
- Ajout d'un garde-fou pour la synchronisation des buckets (limite à 2000 objets modifiés). [#4446](https://github.com/MTES-MCT/potentiel/issues/4446)
- Amélioration de la gestion des erreurs et des validations (caractères non autorisés dans les paths de documents). [#4437](https://github.com/MTES-MCT/potentiel/issues/4437)
- Ajout de la/les typologie d'installation du projet dans l'endpoint API achevement. [#4486](https://github.com/MTES-MCT/potentiel/issues/4486)
- Ajout de la liste des emails porteurs rattachés au projet dans l'endpoint API EDF OA V1. [#4484](https://github.com/MTES-MCT/potentiel/issues/4484)
- Ajout de l'information du volume réservé dans la page lauréat et l'export. [#4474](https://github.com/MTES-MCT/potentiel/issues/4474)
- Ajout de trackers dans le retour de l'endpoint /achevements/a-transmettre. [#4479](https://github.com/MTES-MCT/potentiel/issues/4479)

### Autres changements
- Correction de divers bugs d'interface et de comportement.
- Amélioration du wording de certains messages et formulaires. [#4488](https://github.com/MTES-MCT/potentiel/issues/4488) et [#4496](https://github.com/MTES-MCT/potentiel/issues/4496)
- Mise à jour des dépendances (npm audit). [#4457](https://github.com/MTES-MCT/potentiel/issues/4457)
- Suppression des alertes liées à Notice. [#4445](https://github.com/MTES-MCT/potentiel/issues/4445)
- Ajout d'une indication sur l'environnement (warning prod) pour les administrateurs. [#4450](https://github.com/MTES-MCT/potentiel/issues/4450)
- Suppression de l'animation du menu. [#4468](https://github.com/MTES-MCT/potentiel/issues/4468) et [#4482](https://github.com/MTES-MCT/potentiel/issues/4482)
- Simplification des filtres utilisateurs. [#4465](https://github.com/MTES-MCT/potentiel/issues/4465)
- Suppression de la note minimale pour les lauréats du volume réservé. [#4485](https://github.com/MTES-MCT/potentiel/issues/4485)
- Correction de l'affichage des dates d'accord de recours. [#4497](https://github.com/MTES-MCT/potentiel/issues/4497)
- Correction des routes de téléchargement des documents de mainlevée. [#4426](https://github.com/MTES-MCT/potentiel/issues/4426)
- Correction des puissances appelées P11 éolien et P12 bat. [#4423](https://github.com/MTES-MCT/potentiel/issues/4423)
- Correction du prix moyen pondéré en euros/MWh. [#4421](https://github.com/MTES-MCT/potentiel/issues/4421)
- Ajout de monitoring du CRON datagouv. [#4418](https://github.com/MTES-MCT/potentiel/issues/4418)
