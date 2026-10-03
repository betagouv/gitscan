# Synthèse d'activité : MTES-MCT (du 01/09 au 15/09/2026)

## Résumé de l'activité
L'activité de l'organisation cette semaine est marquée par une dynamique intense sur trois axes majeurs : l'amélioration de l'expérience utilisateur (UI/UX), la montée en puissance de l'intelligence artificielle et la sécurisation des données. De nombreux projets, notamment dans les domaines de l'urbanisme et de l'environnement, ont bénéficié de refontes graphiques et d'une mise en conformité accrue avec les normes d'accessibilité (RGAA).

On observe également une transition technologique importante avec la mise à jour de nombreux environnements de calcul (passage à R 4.6 et Python 3.13) et l'intégration de fonctionnalités d'automatisation, comme l'autovalidation de dossiers dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) ou l'assistance par IA dans [dossierfacile-demo-cnh](/repos/MTES-MCT/dossierfacile-demo-cnh). Ces évolutions visent à simplifier les parcours métiers tout en garantissant une plus grande fiabilité des données collectées.

## Sécurité
Plusieurs mesures de renforcement de la sécurité et de la protection des données ont été déployées :
- **Authentification et accès** : Mise en place de l'authentification à deux facteurs (2FA) pour [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine), sécurisation de l'accès Metabase via OAuth2 pour [mobilic-metabase](/repos/MTES-MCT/mobilic-metabase), et introduction d'une authentification par token pour [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner).
- **Protection contre les attaques et vulnérabilités** : Protection de l'API GraphQL contre les attaques par déni de service (DoS) et correction de vulnérabilités de type BOLA pour [mobilic-api](/repos/MTES-MCT/mobilic-api). Renforcement des en-têtes de sécurité (CSP) pour [dahlia](/repos/MTES-MCT/dahlia) et sécurisation des accès aux fichiers privés pour [envergo](/repos/MTES-MCT/envergo).
- **Intégrité des données** : Prévention des injections SQL pour [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) et chiffrement de l'ID projet pour [potentiel](/repos/MTES-MCT/potentiel).
- **Maintenance corrective** : Résolution de vulnérabilités dans les dépendances pour [vigieau](/repos/MTES-MCT/vigieau) et [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Inertia 3 et Maplibre 6 pour [vizeau](/repos/MTES-MCT/vizeau), mise à jour vers React 18 pour [partaj](/repos/MTES-MCT/partaj), et montée de version vers Spring Boot 4.1 pour [rapportnav2](/repos/MTES-MCT/rapportnav2).
- **Évolutions des environnements de formation** : Mise à jour massive des environnements de calcul vers R 4.6 pour l'ensemble de la suite [parcours-r](/repos/MTES-MCT/parcours-r) et ses modules associés.
- **Optimisations de performance** : Amélioration du rendu cartographique via `ST_asMVT` pour [monitorenv](/repos/MTES-MCT/monitorenv) et optimisation des processus d'anonymisation par mise en cache Redis pour [mobilic-api](/repos/MTES-MCT/mobilic-api).
- **Refonte d'architecture** : Restructuration du parcours de scénarios pour [otelo](/repos/MTES-MCT/otelo) et passage à des fichiers LCI atomiques pour [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data).

## Dépôts les plus actifs
- [mobilic](/repos/MTES-MCT/mobilic) : Amélioration du suivi réglementaire des temps de repos et de l'expérience mobile.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Lancement de l'autovalidation des dossiers et renforcement du moteur d'IA documentaire.
- [otelo](/repos/MTES-MCT/otelo) : Refonte de l'interface et introduction d'un assistant de simulation pas-à-pas.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Fiabilisation de la saisie des rapports de contrôle et de l'auto-sauvegarde.
- [vigieau](/repos/MTES-MCT/vigieau) : Mise en conformité RGAA et gestion de la continuité des données historiques.
- [parcours-r](/repos/MTES-MCT/parcours-r) : Mise à jour de l'infrastructure de déploiement et des environnements Docker pour la formation.
