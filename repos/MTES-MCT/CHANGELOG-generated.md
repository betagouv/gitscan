# Synthèse d'activité : MTES-MCT (du 10/09 au 17/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une modernisation profonde des interfaces et une montée en puissance des capacités d'analyse de données. L'intégration du Design System de l'État (DSFR) et les efforts de mise en conformité avec les normes d'accessibilité (RGAA) sur des projets comme [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) ou [vigieau](/repos/MTES-MCT/vigieau) améliorent significativement l'ergonomie et l'inclusion pour les utilisateurs finaux.

Parallèlement, de nouveaux usages émergent grâce à l'automatisation de processus clés, tels que l'autovalidation des dossiers dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) ou l'assistance pas-à-pas dans [otelo](/repos/MTES-MCT/otelo). Ces évolutions, couplées à des outils de reporting et de suivi enrichis ([vizeau](/repos/MTES-MCT/vizeau), [qualicharge](/repos/MTES-MCT/qualicharge)), offrent une meilleure aide à la décision pour les décideurs et les agents de terrain.

## Sécurité
- **Renforcement de l'authentification** : Mise en place de l'authentification à deux facteurs (2FA) dans [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine) et introduction d'une authentification par token pour [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner).
- **Correction de vulnérabilités critiques** : Résolution de failles de type XSS et d'autorisation dans [envergo](/repos/MTES-MCT/envergo), et correction de vulnérabilités de type BOLA et déni de service (DoS) dans [mobilic-api](/repos/MTES-MCT/mobilic-api).
- **Protection des données et des accès** : Sécurisation des webhooks dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) et amélioration de la gestion des clés API dans [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr).
- **Maintenance de sécurité** : Résolution de vulnérabilités dans les dépendances pour [vigieau](/repos/MTES-MCT/vigieau).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Inertia 3 et Maplibre 6 pour [vizeau](/repos/MTES-MCT/vizeau), migration vers React 18 pour [partaj](/repos/MTES-MCT/partaj), et mise à jour globale vers R 4.6.0 pour l'ensemble de la suite [parcours-r](/repos/MTES-MCT/parcours-r).
- **Refontes d'interface (DSFR)** : Modernisation massive des interfaces utilisateur via le Design System de l'État pour [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles), [mobilic](/repos/MTES-MCT/mobilic) et [fonds-vert-espace-laureat](/repos/MTES-MCT/fonds-vert-espace-laureat).
- **Intelligence Artificielle** : Déploiement du moteur de traitement documentaire DocIA (workflow v2) dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend).
- **Infrastructure et Cloud** : Migration du stockage vers Scaleway S3 pour [envergo](/repos/MTES-MCT/envergo) et optimisation des pipelines de déploiement pour [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web).

## Dépôts les plus actifs
- [vizeau](/repos/MTES-MCT/vizeau) : Enrichissement des capacités d'exportation et migrations techniques majeures.
- [mobilic](/repos/MTES-MCT/mobilic) : Renforcement du contrôle réglementaire et amélioration de l'expérience mobile.
- [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) : Modernisation de l'interface (DSFR) et optimisation de la cartographie.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation et de l'analyse documentaire par IA.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Fiabilisation de la saisie des rapports et enrichissement des données de navigation.
- [otelo](/repos/MTES-MCT/otelo) : Lancement d'un assistant de simulation (wizard) et refonte de l'administration.
- [parcours-r](/repos/MTES-MCT/parcours-r) : Mise à jour de l'infrastructure de formation et des environnements Docker.
- [vigieau](/repos/MTES-MCT/vigieau) : Mise en conformité RGAA et fiabilisation de la reconstitution des données historiques.
