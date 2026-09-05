# Synthèse d'activité : MTES-MCT (du 25/08 au 03/09)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une double dynamique de modernisation des interfaces et de fiabilisation des données. Les utilisateurs bénéficient de refontes visuelles et ergonomiques majeures sur des plateformes clés comme [otelo](/repos/MTES-MCT/otelo) ou [dialog](/repos/MTES-MCT/dialog), ainsi que d'une mise en conformité accrue avec les normes d'accessibilité (RGAA) sur [vigieau](/repos/MTES-MCT/vigieau) et [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).

Parallèlement, des avancées significatives ont été réalisées sur les infrastructures de données et l'intelligence artificielle, notamment avec l'amélioration du traitement documentaire de [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) et l'optimisation des pipelines d'ingestion pour [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration). Ces évolutions renforcent la robustesse et la précision des outils mis à disposition des acteurs publics et privés.

## Sécurité
- **Corrections de vulnérabilités (XSS, webhooks, dépendances) :** [envergo](/repos/MTES-MCT/envergo), [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend), [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr) et [potentiel](/repos/MTES-MCT/potentiel).
- **Renforcement de l'authentification et de la protection des données :** [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner) (authentification par token), [mobilic-api](/repos/MTES-MCT/mobilic-api) (rotation des jetons et anonymisation), [histologe](/repos/MTES-MCT/histologe) (rate limiting et régénération de jetons) et [vigieau](/repos/MTES-MCT/vigieau) (restauration des certifications).
- **Amélioration de la sécurité du typage et de la gestion des accès :** [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) (migration vers Kysely) et [verseau2](/repos/MTES-MCT/verseau2) (tests de contrôle d'accès).

## Autres changements notables
- **Modernisation des frameworks et environnements :** [vizeau](/repos/MTES-MCT/vizeau) (migration vers Inertia 3), [partaj](/repos/MTES-MCT/partaj) (passage à React 18) et la suite [parcours-r](/repos/MTES-MCT/parcours-r) (mise à jour vers R 4.6.0).
- **Évolutions majeures de l'infrastructure et des pipelines :** [vigieau](/repos/MTES-MCT/vigieau) (système de backfill de données), [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration) (nouveaux connecteurs de données) et [monitor-field](/repos/MTES-MCT/monitor-field) (automatisation des builds Android).
- **Intelligence artificielle et gestion des données :** [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) (migration vers le moteur DocIA v2) et [ecobalyse](/repos/MTES-MCT/ecobalyse) (transition vers un nouveau système de taxonomie).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte complète de l'expérience utilisateur (assistant, tutoriel) et de l'affichage des résultats.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation et amélioration du traitement documentaire par IA.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Optimisation de la fiabilité des rapports de contrôle et de l'interface de saisie.
- [mobilic](/repos/MTES-MCT/mobilic) : Déploiement des notifications push et optimisation du parcours de création de mission.
- [parcours-r](/repos/MTES-MCT/parcours-r) : Mise à jour globale des environnements de formation (R 4.6.0 et Docker).
