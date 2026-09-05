# Synthèse d'activité : gip-inclusion (du 26/06 au 02/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des outils de mise en relation et de recrutement, notamment via l'amélioration des processus de matching et de suivi des candidats dans [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) et [les-emplois](/repos/gip-inclusion/les-emplois). Ces évolutions permettent aux partenaires et aux employeurs de bénéficier de tableaux de bord plus précis et de workflows de gestion plus fluides.

Parallèlement, une modernisation profonde des infrastructures est en cours pour garantir la scalabilité et la stabilité des services. Cela se traduit par des migrations technologiques majeures vers de nouveaux frameworks pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow), ainsi que par une amélioration de l'intelligence de recherche dans [data-inclusion](/repos/gip-inclusion/data-inclusion) pour offrir des résultats plus pertinents aux utilisateurs.

## Sécurité
- Renforcement de la sécurité des accès via l'amélioration de la double authentification (MFA) et l'optimisation des scopes d'API dans [les-emplois](/repos/gip-inclusion/les-emplois).
- Restriction du téléchargement de listes de recherche aux seuls utilisateurs authentifiés dans [le-marche](/repos/gip-inclusion/le-marche).
- Sécurisation de la génération des URL par l'imposition du protocole HTTPS dans [la-communaute](/repos/gip-inclusion/la-communaute).
- Suppression des mots de passe en clair dans les configurations de base de données au profit de variables d'environnement dans [fluo-proto](/repos/gip-inclusion/fluo-proto).

## Autres changements notables
- Migration architecturale vers Django et refonte complète de la page d'accueil pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil).
- Mise à jour majeure de l'infrastructure vers Airflow 3 pour l'orchestration des données dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow).
- Transition identitaire vers "Match Europe" accompagnée d'une refonte de l'interface d'administration dans [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms).
- Migration de l'architecture de données vers le framework `di_v1` pour [dora](/repos/gip-inclusion/dora).
- Optimisation de la robustesse de l'infrastructure via l'amélioration des sauvegardes S3 et la mise en place de tests unitaires hermétiques dans [autometa](/repos/gip-inclusion/autometa).

## Dépôts les plus actifs
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding complet et amélioration majeure des fonctionnalités de matching et de suivi des candidatures.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte visuelle et migration technique vers une architecture Django robuste.
- [autometa](/repos/gip-inclusion/autometa) : Enrichissement des fonctionnalités de personnalisation et renforcement de la fiabilité de l'infrastructure.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Migration vers Airflow 3 et affinement des modèles de données pour les enquêtes.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Déploiement de nouveaux modules de gestion des orientations et de tableaux de bord analytiques.
