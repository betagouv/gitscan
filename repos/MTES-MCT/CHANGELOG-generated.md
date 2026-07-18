# Synthèse d'activité : MTES-MCT (du 25 mai au 22 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par une forte concentration sur l'amélioration de l'expérience utilisateur et la correction de bugs dans de nombreux dépôts. Plusieurs projets ont bénéficié de refontes d'interface (mobilic, ecobalyse-data, sparte, prelevements-deau-web), d'améliorations de la gestion des données (partageonsleau-orchestration, ecobalyse-method-tooling, trackdechets) et de l'ajout de nouvelles fonctionnalités (fonds-prevention-argile, dialog, histologe).  Une attention particulière a été portée à la sécurité avec des mises à jour de dépendances régulières et l'implémentation de nouvelles mesures de protection (otelo-backend, monitorfish).  Plusieurs dépôts ont également bénéficié d'optimisations de performance et de simplification des processus de déploiement (rapportnav2, verseau2, ecobalyse-runner).

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de sécurité :
- [otelo-backend](/repos/MTES-MCT/otelo-backend) : Mise à jour de la dépendance `sentry-sdk` pour corriger des vulnérabilités.
- [carbure](/repos/MTES-MCT/carbure) : Optimisation des requêtes en base de données pour améliorer la sécurité.
- [aigle-api](/repos/MTES-MCT/aigle-api) : Corrections et report de tests de sécurité.

## Autres changements notables
- **Refonte d'interfaces utilisateur:** [mobilic](/repos/MTES-MCT/mobilic), [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data), [sparte](/repos/MTES-MCT/sparte), [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web) ont bénéficié d'améliorations significatives de leur interface.
- **Amélioration des processus de déploiement:** [verseau2](/repos/MTES-MCT/verseau2) passe au déploiement via Terraform, [rapportnav2](/repos/MTES-MCT/rapportnav2) et [dossierfacile-infra](/repos/MTES-MCT/dossierfacile-infra) ont simplifié leurs processus de déploiement.
- **Intégration de nouvelles sources de données:** [dialog-integrations](/repos/MTES-MCT/dialog-integrations) intègre les données des préfectures de Nantes et Rennes.
- **Refactorisation et optimisation:** [trackdechets-data](/repos/MTES-MCT/trackdechets-data) améliore son environnement de sandbox, [ecobalyse-api](/repos/MTES-MCT/ecobalyse-api) refactorise la gestion des certificats d'électricité.
- **Nouvelles fonctionnalités:** [fonds-prevention-argile](/repos/MTES-MCT/fonds-prevention-argile) ajoute la gestion des garanties et la possibilité d'annuler des missions.

## Dépôts les plus actifs
- [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) : Amélioration de la cartographie et de l'analyse des données.
- [vizeau](/repos/MTES-MCT/vizeau) : Ajout de la gestion des étapes de projet et des tags.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Implémentation de l'authentification multi-facteurs et amélioration de la gestion des bordereaux.
- [trackdechets-vigiedechets](/repos/MTES-MCT/trackdechets-vigiedechets) : Amélioration de la gestion des contacts et de l'assistance.
- [qualicharge](/repos/MTES-MCT/qualicharge) : Ajout d'indicateurs de supervision et amélioration de la robustesse des calculs.
- [dialog](/repos/MTES-MCT/dialog) : Amélioration de la gestion des restrictions de circulation et de l'interface utilisateur.
- [histologe](/repos/MTES-MCT/histologe) : Amélioration de l'interface et de la gestion des signalements.
- [mobilic](/repos/MTES-MCT/mobilic) : Refonte de l'en-tête et du pied de page et amélioration de la gestion des activités.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Amélioration de l'analyse des documents et de la gestion des garants.
- [aigle-frontend](/repos/MTES-MCT/aigle-frontend) : Amélioration du tableau de bord DDT et de la gestion des statuts.
