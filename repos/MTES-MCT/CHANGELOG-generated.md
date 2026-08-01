# Synthèse d'activité : MTES-MCT (du 22/05 au 30/07)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par des améliorations significatives sur plusieurs fronts.  De nombreuses mises à jour ont visé à renforcer la sécurité (notamment [trackdechets](/repos/MTES-MCT/trackdechets) avec l'authentification multi-facteurs et [keycloak-client-webhook](/repos/MTES-MCT/keycloak-client-webhook) avec l'ajout d'une authentification par token), à améliorer l'expérience utilisateur (par exemple, [vizeau](/repos/MTES-MCT/vizeau) avec l'affichage des projets sur la carte et [otelo](/repos/MTES-MCT/otelo) avec un mode tutoriel guidé), et à optimiser les processus internes (comme [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration) avec l'amélioration de l'ingestion de données). Plusieurs projets ont également bénéficié de refactorisations techniques et de mises à jour de dépendances pour une meilleure maintenabilité et performance.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- **Authentification multi-facteurs :** Implémentation de l'authentification multi-facteurs sur [trackdechets](/repos/MTES-MCT/trackdechets).
- **Gestion des clés API :** Ajout de la possibilité d'utiliser plusieurs clés API sur [keycloak-client-webhook](/repos/MTES-MCT/keycloak-client-webhook).
- **Mise à jour des dépendances :** Correction de vulnérabilités en mettant à jour les dépendances sur [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr) et [qualicharge](/repos/MTES-MCT/qualicharge).

## Autres changements notables
- **Migration vers Better Auth :** [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) a migré vers Better Auth pour une sécurité renforcée.
- **Refactorisation technique :** [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) a également entrepris une refactorisation importante avec Kysely.
- **Intégration de Matomo :** [vizeau](/repos/MTES-MCT/vizeau) a intégré Matomo pour le suivi analytique.
- **Migration vers AdonisJS 7 :** [vizeau](/repos/MTES-MCT/vizeau) a migré vers AdonisJS 7 pour des améliorations de performance et de sécurité.
- **Amélioration de l'infrastructure :** Plusieurs projets ont bénéficié d'améliorations de l'infrastructure de déploiement et de la gestion des données, notamment [dossierfacile-infra](/repos/MTES-MCT/dossierfacile-infra) et [fonds-prevention-argile](/repos/MTES-MCT/fonds-prevention-argile).

## Dépôts les plus actifs
- **zero-logement-vacant:** Améliorations de la sécurité, de l'authentification et refactorisation du code.
- **vizeau:** Ajout de nouvelles fonctionnalités, amélioration de l'expérience utilisateur et migration technique.
- **trackdechets:** Implémentation de l'authentification multi-facteurs et corrections de bugs.
- **otelo:** Amélioration de l'expérience utilisateur et ajout de nouvelles fonctionnalités.
- **dossierfacile-backend:** Amélioration de la gestion des pièces justificatives et corrections de bugs.
- **mobilic:** Ajout de la possibilité de contester une mission et de gérer les détachements.
- **ecobalyse:** Ajout de nouveaux ingrédients au catalogue LCI et amélioration de l'export au format Ecospold1.
- **apilos:** Amélioration de la génération de documents et mise à jour des dépendances.
- **aigle-frontend & aigle-api:** Amélioration des fonctionnalités d'administration et de la gestion des DDT.
