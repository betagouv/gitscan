## Changelog : potentiel (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant le module de raccordement, la gestion des candidatures et des données, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations ont également été apportées à la gestion des permissions et à la sécurité.

### Évolutions fonctionnelles
- Intégration complète du module de raccordement au menu principal et ajout de fonctionnalités de téléchargement et de suppression de documents liés au raccordement. [#4476, #4413, #4368]
- Amélioration du détail des candidatures avec l'ajout des données relatives aux procès-verbaux (PV). [#4400]
- Ajout de la possibilité pour un cocontractant de corriger une date d'achèvement réel. [#4440]
- Possibilité d'ajouter la date de l'accord de recours au formulaire. [#4352]
- Ajout de l'information du volume réservé dans la page lauréat et dans l'export. [#4474]
- Ajout d'un badge et d'un wording pour indiquer l'état de raccordement. [#4459]
- Ajout d'un lien vers le jeu de données dans le footer. [#4442]
- Ajout de la possibilité d'exporter une liste de candidats non notifiés. [#4406]
- Ajout de la possibilité d'exporter un PDF des candidats lauréats d'une nouvelle période. [#4409]
- Modification de l'intitulé "démarches simplifiées" en "Démarche Numérique". [#4403]
- Amélioration de l'affichage et de la gestion des filtres utilisateurs. [#4465, #4477]
- Ajout d'une indication sur l'environnement (warning prod) pour les administrateurs. [#4450]

### Évolutions techniques
- Mise à jour de Keycloak en version 26.7.0. [#4439]
- Vérification des permissions sur les routes Next.js pour renforcer la sécurité. [#4420]
- Refactorisation du code du module de raccordement. [#4368]
- Amélioration du script de restauration de la base de données pour les review apps. [#4405]
- Mise à jour des dépendances (npm audit) et ajout des dépendances manquantes. [#4457]
- Correction de bugs liés à la reconstruction du projector et de l'historique. [#4447]
- Correction de routes de téléchargement de documents mainlevée. [#4426]
- Monitoring du CRON datagouv. [#4418]

### Autres changements
- Correction de bugs visuels et d'erreurs diverses dans l'interface utilisateur. [#4482, #4461, #4469, #4472, #4473, #4475]
- Harmonisation des données des candidatures PV ayant des trackers. [#4483]
- Suppression d'animations inutiles dans le menu. [#4468, #4482, #4478]
- Correction de problèmes liés aux caractères non autorisés dans les chemins de documents. [#4437]
- Ajout d'un email de contact dans le corps du mail de désignation. [#4473]
- Correction de l'export CSV des candidats (colonnes en doublon). [#4454]
- Correction de l'affichage de la puissance cumulée par période d'AO. [#4475]
- Correction de l'accès aux mainlevées rejetées. [#4414]
- Correction de la qualification de la DCR. [#4408]
- Ajout d'un bloc d'information pour les PP avant de demander la mainlevée des gfs. [#4410]
- Suppression d'alertes liées à Notice. [#4445]
- Correction de l'ouverture des liens internes dans un nouvel onglet. [#4431]
- Correction de l'affichage des erreurs lors de la correction des données. [#4449]
- Ajout de la gestion des permissions dans les pages. [#4467]
- Correction de l'autorisation de téléchargement des MES pour les GRD. [#4462]
- Correction de la recherche dans la liste des utilisateurs. [#4461]
- Mise à jour du dump de la base de données. [#4443]
- Ajout de la vérification des données EDF OA (date achèvement réel). [#4433]
- Ajout d'un script pour harmoniser les données des candidatures PV. [#4483]
