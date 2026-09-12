# Synthèse d'activité : MTES-MCT (du 25/08 au 03/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une modernisation profonde des outils de gestion et de suivi. Les évolutions majeures concernent l'amélioration de l'expérience utilisateur via des interfaces refondues ([otelo](/repos/MTES-MCT/otelo), [dialog](/repos/MTES-MCT/dialog), [vizeau](/repos/MTES-MCT/vizeau)) et l'intégration de l'intelligence artificielle pour l'automatisation des processus documentaires ([dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend)). 

Les efforts de fiabilisation des données, de conformité à l'accessibilité numérique (RGAA) et de sécurisation des échanges sont également prédominants sur l'ensemble des domaines d'intervention, notamment pour les secteurs de l'eau, de l'environnement et du logement ([vigieau](/repos/MTES-MCT/vigieau), [mobilic-api](/repos/MTES-MCT/mobilic-api), [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant)).

## Sécurité
- **Protection des données et des accès** : Renforcement de l'anonymisation des données ([mobilic-api](/repos/MTES-MCT/mobilic-api)), sécurisation des sessions et mise en place du rate limiting ([boris](/repos/MTES-MCT/boris), [histologe](/repos/MTES-MCT/histologe)), et introduction de l'authentification par token ([ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner)).
- **Corrections de vulnérabilités** : Résolution de failles XSS ([envergo](/repos/MTES-MCT/envergo)), correction de vulnérabilités liées aux webhooks ([dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend)) et mises à jour de dépendances critiques pour corriger des failles de sécurité ([potentiel](/repos/MTES-MCT/potentiel), [vigieau](/repos/MTES-MCT/vigieau)).

## Autres changements notables
- **Modernisation des frameworks** : Migrations importantes vers des versions récentes de frameworks et bibliothèques pour améliorer la réactivité et la maintenance ([vizeau](/repos/MTES-MCT/vizeau), [partaj](/repos/MTES-MCT/partaj), [rapportnav2](/repos/MTES-MCT/rapportnav2)).
- **Optimisation de l'infrastructure et de la CI/CD** : Amélioration des processus de déploiement automatisés, notamment pour les environnements mobiles et cloud ([monitor-field](/repos/MTES-MCT/monitor-field), [parcours-r](/repos/MTES-MCT/parcours-r), [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web)) et refonte de la gestion des pipelines de données ([monitorenv](/repos/MTES-MCT/monitorenv)).

## Dépôts les plus actifs
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation des dossiers et de l'analyse documentaire par IA.
- [otelo](/repos/MTES-MCT/otelo) : Mise en place d'un assistant de simulation (wizard) et refonte de la page de résultats.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Amélioration de la saisie des rapports de contrôle et de l'expérience utilisateur.
- [dialog](/repos/MTES-MCT/dialog) : Refonte du tableau de bord et enrichissement des capacités cartographiques.
- [mobilic](/repos/MTES-MCT/mobilic) : Mise en place des notifications push et optimisation du parcours de création de mission.
- [dahlia](/repos/MTES-MCT/dahlia) : Amélioration de la gestion des dossiers et de la manipulation des pièces jointes.
- [histologe](/repos/MTES-MCT/histologe) : Automatisation de la clôture des dossiers et enrichissement de l'interface d'administration.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Automatisation de la classification des matériaux et enrichissement du catalogue de données.
- [potentiel](/repos/MTES-MCT/potentiel) : Optimisation des processus d'import et de la gestion des règles métier.
- [vizeau](/repos/MTES-MCT/vizeau) : Modernisation de l'infrastructure technique et nouvelles capacités d'exportation.
