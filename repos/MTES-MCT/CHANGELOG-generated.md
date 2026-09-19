# Synthèse d'activité : MTES-MCT (du 01/09 au 15/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte dynamique de modernisation des interfaces utilisateur, notamment via l'intégration massive du Design System de l'État (DSFR) pour des projets comme [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) et [fonds-vert-espace-laureat](/repos/MTES-MCT/fonds-vert-espace-laureat). Ces évolutions visent à offrir une expérience plus cohérente, accessible et professionnelle aux agents et aux citoyens.

Parallèlement, l'organisation a considérablement enrichi ses capacités d'analyse et de pilotage. De nouveaux indicateurs de performance, des outils de reporting PDF améliorés et des capacités d'exportation de données plus poussées ont été déployés dans [vizeau](/repos/MTES-MCT/vizeau), [verseau2](/repos/MTES-MCT/verseau2) et [qualicharge](/repos/MTES-MCT/qualicharge). Enfin, l'automatisation de processus métiers, comme l'autovalidation des dossiers dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend), permet de gagner en efficacité opérationnelle tout en améliorant la fiabilité des données collectées.

## Sécurité
- Renforcement de la protection des données par l'anonymisation et le masquage des utilisateurs dans [mobilic-api](/repos/MTES-MCT/mobilic-api).
- Correction de vulnérabilités XSS et amélioration de l'API d'autorisation dans [envergo](/repos/MTES-MCT/envergo).
- Sécurisation des sessions et mise en place de mécanismes de limitation de débit (*rate limiting*) dans [boris](/repos/MTES-MCT/boris) et [histologe](/repos/MTES-MCT/histologe).
- Gestion plus fine des accès via le support de plusieurs clés API dans [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr).
- Correction de vulnérabilités potentielles dans les dépendances pour [vigieau](/repos/MTES-MCT/vigieau) et [potentiel](/repos/MTES-MCT/potentiel).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Inertia 3 pour [vizeau](/repos/MTES-MCT/vizeau), mise à jour vers React 18 pour [partaj](/repos/MTES-MCT/partaj), et montée de version vers Python 3.13 pour [fisheries-and-environment-data-warehouse](/repos/MTES-MCT/fisheries-and-environment-data-warehouse).
- **Modernisation de l'infrastructure** : Migration vers un stockage S3 pour [envergo](/repos/MTES-MCT/envergo) et adoption de MinIO pour [potentiel](/repos/MTES-MCT/potentiel).
- **Évolutions des environnements de formation** : Mise à jour massive des environnements R vers la version 4.6.0 pour l'ensemble des modules du [parcours-r](/repos/MTES-MCT/parcours-r).
- **Optimisation SIG** : Refactorisation de la gestion des données cartographiques (PMTiles) dans [vizeau](/repos/MTES-MCT/vizeau).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte de l'interface de résultats et introduction d'un assistant de simulation pas-à-pas.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation des dossiers et amélioration de l'analyse documentaire par IA.
- [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) : Modernisation complète de l'interface via le DSFR et amélioration de la cartographie.
- [mobilic](/repos/MTES-MCT/mobilic) : Ajout de notifications push et de nouvelles pages de suivi du schéma pluriannuel.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Fiabilisation de la saisie des rapports de contrôle et enrichissement des données de navigation.
- [envergo](/repos/MTES-MCT/envergo) : Amélioration de l'expérience cartographique et sécurisation de la plateforme.
