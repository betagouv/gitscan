# Synthèse d'activité : MTES-MCT (du 23/08 au 30/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte dynamique de modernisation des interfaces et une amélioration de l'accessibilité numérique (RGAA), notamment pour [vigieau](/repos/MTES-MCT/vigieau), [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) et [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant). Les utilisateurs bénéficient de nouvelles capacités de pilotage, de reporting et d'exportation de données ([vizeau](/repos/MTES-MCT/vizeau), [verseau2](/repos/MTES-MCT/verseau2), [qualicharge](/repos/MTES-MCT/qualicharge)), facilitant ainsi la prise de décision et la gestion des processus métier.

Parallèlement, des efforts importants ont été déployés pour fiabiliser les flux de données et moderniser les infrastructures. Cela inclut l'intégration de nouvelles sources statistiques ([fisheries-and-environment-data-warehouse](/repos/MTES-MCT/fisheries-and-environment-data-warehouse)) et une mise à jour majeure des environnements de formation vers R 4.6.0 ([parcours-r](/repos/MTES-MCT/parcours-r) et ses modules associés), garantissant la pérennité des outils pédagogiques.

## Sécurité
- Correction de vulnérabilités XSS et renforcement de la validation des entrées dans [envergo](/repos/MTES-MCT/envergo).
- Amélioration de la gestion des accès, de la rotation des jetons de session et de l'anonymisation des données dans [mobilic-api](/repos/MTES-MCT/mobilic-api) et [histologe](/repos/MTES-MCT/histologe).
- Mise en place d'une authentification par token pour [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner) et support de plusieurs clés API pour [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr).
- Correction de vulnérabilités liées aux webhooks dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend).

## Autres changements notables
- **Modernisation des frameworks et outils** : Migrations vers Inertia 3 ([vizeau](/repos/MTES-MCT/vizeau)), React 18 ([partaj](/repos/MTES-MCT/partaj)) et React Router 8 ([rapportnav2](/repos/MTES-MCT/rapportnav2)).
- **Évolutions infrastructurelles et DevOps** : Mise à jour globale des environnements de développement vers R 4.6.0 pour l'ensemble des modules de formation ([parcours-r](/repos/MTES-MCT/parcours-r) et ses modules) et automatisation des déploiements mobiles via EAS ([monitor-field](/repos/MTES-MCT/monitor-field)).
- **Optimisation de la donnée et des performances** : Refonte des pipelines d'ingestion et de stockage pour améliorer la performance et la traçabilité ([partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration), [qualicharge](/repos/MTES-MCT/qualicharge), [envergo](/repos/MTES-MCT/envergo)).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Introduction d'un assistant de simulation (wizard) et refonte de l'interface d'administration.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Mise en place de l'autovalidation des dossiers et amélioration du moteur de traitement documentaire par IA.
- [dialog](/repos/MTES-MCT/dialog) : Refonte complète du tableau de bord et enrichissement des fonctionnalités cartographiques.
- [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) : Amélioration de l'accessibilité et ajout de la gestion des sites favoris.
- [parcours-r](/repos/MTES-MCT/parcours-r) : Mise à jour majeure de l'infrastructure de formation vers R 4.6.0.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Évolutions sur la gestion des bordereaux et la visibilité du registre.
