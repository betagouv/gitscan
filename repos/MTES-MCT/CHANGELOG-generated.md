# Synthèse d'activité : MTES-MCT (du 01/09 au 04/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une forte dynamique de modernisation des interfaces et un renforcement de l'accessibilité numérique (RGAA), notamment sur les projets [vigieau](/repos/MTES-MCT/vigieau) et [verseau2](/repos/MTES-MCT/verseau2). Les efforts se sont concentrés sur l'enrichissement des capacités d'analyse de données et de reporting pour des outils comme [ecobalyse](/repos/MTES-MCT/ecobalyse) et [otelo](/repos/MTES-MCT/otelo), offrant ainsi des outils de décision plus précis aux utilisateurs.

Parallèlement, plusieurs plateformes ont franchi des étapes clés en matière d'automatisation, comme l'autovalidation des dossiers dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) ou la gestion automatisée des bordereaux dans [trackdechets](/repos/MTES-MCT/trackdechets). Ces évolutions visent à fluidifier les parcours métiers et à accroître la fiabilité des données collectées.

## Sécurité
- **Renforcement de l'authentification** : Déploiement de l'authentification à deux facteurs (2FA) pour sécuriser les accès dans [otelo](/repos/MTES-MCT/otelo), [oilhi-cms](/repos/MTES-MCT/oilhi-cms) et [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine).
- **Correction de vulnérabilités critiques** : 
    - Protection contre les injections SQL dans [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles).
    - Correction de failles de type SSRF dans [trackdechets](/repos/MTES-MCT/trackdechets).
    - Sécurisation contre les attaques par déni de service (DoS) et les fuites de données (BOLA) dans [mobilic-api](/repos/MTES-MCT/mobilic-api).
- **Protection des données personnelles** : Amélioration des processus d'anonymisation et de la protection des données sensibles (PII) dans [mobilic-api](/repos/MTES-MCT/mobilic-api) et [trackdechets](/repos/MTES-MCT/trackdechets).

## Autres changements notables
- **Migrations technologiques majeures** : 
    - Passage à Inertia 3 pour [vizeau](/repos/MTES-MCT/vizeau).
    - Mise à jour vers React 18 pour [partaj](/repos/MTES-MCT/partaj).
    - Montée de version de Spring Boot pour [rapportnav2](/repos/MTES-MCT/rapportnav2).
    - Mise à jour globale des environnements de formation vers R 4.6.0 pour le [parcours-r](/repos/MTES-MCT/parcours-r).
- **Évolutions d'infrastructure** : 
    - Migration vers des systèmes de stockage S3 et Keycloak pour [potentiel](/repos/MTES-MCT/potentiel) et [envergo](/repos/MTES-MCT/envergo).
    - Automatisation des processus de build Android via EAS pour [monitor-field](/repos/MTES-MCT/monitor-field).
- **Optimisation des performances** : Amélioration du rendu cartographique (SIG) dans [monitorenv](/repos/MTES-MCT/monitorenv) et optimisation des requêtes SQL pour [fisheries-and-environment-data-warehouse](/repos/MTES-MCT/fisheries-and-environment-data-warehouse).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte de l'expérience de simulation et ajout de nouveaux outils d'analyse démographique.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Enrichissement massif de la base de données et automatisation de la classification des matériaux.
- [mobilic-api](/repos/MTES-MCT/mobilic-api) : Travaux intensifs sur la conformité réglementaire, la sécurité et l'anonymisation des données.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Implémentation de l'autovalidation des dossiers assistée par IA.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Sécurisation de la plateforme et automatisation de la gestion des bordereaux.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Amélioration de l'expérience de saisie des rapports et de la navigation.
