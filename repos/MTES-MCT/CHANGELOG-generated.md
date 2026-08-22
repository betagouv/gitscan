# Synthèse d'activité : MTES-MCT (du [Date de début] au [Date de fin])

## Résumé de l'activité
L'activité récente de l'organisation est marquée par un effort important sur l'accessibilité numérique (mise en conformité RGAA) et l'amélioration de l'expérience utilisateur via l'adoption des standards de design DSFR, notamment pour [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles), [vizeau](/repos/MTES-MCT/vizeau) et [fonds-vert-espace-laureat](/repos/MTES-MCT/fonds-vert-espace-laureat). Ces évolutions visent à rendre les services plus inclusifs et intuitifs pour les agents et les citoyens.

Parallèlement, de nouvelles capacités métier ont été déployées, comme la gestion des demandes de détachement dans [mobilic](/repos/MTES-MCT/mobilic) ou l'introduction de modes tutoriels dans [otelo](/repos/MTES-MCT/otelo). La fiabilité des données a également été renforcée par l'intégration de nouvelles sources (Matomo, API Enedis) et l'optimisation des processus de synchronisation pour [vigieau](/repos/MTES-MCT/vigieau) et [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration).

## Sécurité
- Renforcement de la gestion des accès et de la protection des données, notamment via l'implémentation de limites de requêtes (rate limiting) dans [histologe](/repos/MTES-MCT/histologe) et la restriction des accès aux impacts détaillés dans [ecobalyse](/repos/MTES-MCT/ecobalyse).
- Sécurisation des échanges de données (webhooks) pour [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) et correction de vulnérabilités de dépendances pour [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr).
- Mise en place d'une authentification par token pour sécuriser l'accès à l'API de [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à React 18 pour [partaj](/repos/MTES-MCT/partaj) et mise à jour vers Spring Boot 4.1.0 pour [rapportnav2](/repos/MTES-MCT/rapportnav2).
- **Modernisation des environnements** : Mise à jour globale vers R 4.6.0 pour la suite [parcours-r](/repos/MTES-MCT/parcours-r) et optimisation des workflows de déploiement (Scaleway, Scalingo) pour [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web) et [mobilic](/repos/MTES-MCT/mobilic).
- **Qualité logicielle et CI/CD** : Intégration d'outils de suivi de qualité (SonarQube, Codecov) et de tests automatisés renforcés pour [monitor-field](/repos/MTES-MCT/monitor-field) et [monitorenv](/repos/MTES-MCT/monitorenv).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte de la page de résultats et ajout d'un mode tutoriel guidé.
- [mobilic](/repos/MTES-MCT/mobilic) : Introduction de nouveaux processus métier (détachement, contestation) et amélioration des rapports.
- [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) : Évolutions majeures sur l'accessibilité et la gestion des sites favoris.
- [monitor-field](/repos/MTES-MCT/monitor-field) : Implémentation de la consultation des zones réglementaires et renforcement de la CI/CD.
- [dahlia](/repos/MTES-MCT/dahlia) : Améliorations de la gestion documentaire et des outils d'administration.
