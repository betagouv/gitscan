# Synthèse d'activité : gip-inclusion (du 26/06 au 17/09)

## Résumé de l'activité
L'activité récente est marquée par une forte dynamique de transformation de l'offre de services et de l'identité visuelle. Plusieurs plateformes ont entamé un rebranding majeur ( [les-emplois](/repos/gip-inclusion/les-emplois), [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) ) et ont considérablement enrichi leurs fonctionnalités de mise en relation, de recherche et de gestion ( [le-marche](/repos/gip-inclusion/le-marche), [data-inclusion](/repos/gip-inclusion/data-inclusion), [dora](/repos/gip-inclusion/dora), [immersion-facile](/repos/gip-inclusion/immersion-facile) ). Ces évolutions visent à offrir une expérience plus intuitive et pertinente pour les utilisateurs finaux, notamment via des outils de pilotage pour les employeurs et des moteurs de recherche plus intelligents.

Parallèlement, l'organisation a engagé des modernisations structurelles importantes pour garantir la scalabilité et la fiabilité des services, avec notamment le passage à des architectures serverless ( [fluo-proto](/repos/gip-inclusion/fluo-proto) ) et une mise à jour majeure des outils d'orchestration de données ( [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) ).

## Sécurité
- **Renforcement de l'authentification et des accès** : Intégration du SSO via Authentik ( [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil), [les-emplois](/repos/gip-inclusion/les-emplois) ), généralisation de l'authentification ProConnect ( [les-emplois](/repos/gip-inclusion/les-emplois) ) et amélioration de la gestion des clés d'API ( [autometa-jobs](/repos/gip-inclusion/autometa-jobs) ).
- **Protection des données et conformité** : Mise en place de pistes d'audit ( [les-emplois](/repos/gip-inclusion/les-emplois), [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav) ), renforcement des protocoles OIDC ( [inclusion-connect](/repos/gip-inclusion/inclusion-connect) ) et durcissement des politiques de sécurité web comme la CSP et les headers CORS ( [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) ).
- **Sécurisation des infrastructures** : Suppression des mots de passe codés en dur dans les prototypes ( [fluo-proto](/repos/gip-inclusion/fluo-proto) ) et restriction des téléchargements de données aux utilisateurs authentifiés ( [le-marche](/repos/gip-inclusion/le-marche) ).

## Autres changements notables
- **Migrations d'infrastructure majeures** : Passage à Airflow 3 ( [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) ) et transition vers un modèle de déploiement de conteneurs serverless ( [fluo-proto](/repos/gip-inclusion/fluo-proto) ).
- **Refontes d'interface et d'architecture** : Modernisation des interfaces d'administration ( [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil), [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms), [eures-beta](/repos/gip-inclusion/eures-beta) ) et optimisation des performances via l'ajout d'index SQL et de systèmes de cache ( [immersion-facile](/repos/gip-inclusion/immersion-facile), [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) ).
- **Intégrations de services tiers** : Activation des appels vers le service InterOps ( [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav) ) et configuration DNS pour l'intégration d'outils de gestion de relation client ( [infrastructure](/repos/gip-inclusion/infrastructure) ).

## Dépôts les plus actifs
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Migration majeure vers Airflow 3 et enrichissement massif des modèles de données métiers.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers "Match Europe" et optimisation complète des processus de matching et de candidatures.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Transition vers "La plateforme de l'inclusion" et déploiement de nouveaux outils de pilotage pour les employeurs.
- [dora](/repos/gip-inclusion/dora) : Amélioration de la précision de la recherche et automatisation des flux de données.
- [immersion-facile](/repos/gip-inclusion/immersion-facile) : Évolution des tableaux de bord et renforcement de l'architecture logicielle.
