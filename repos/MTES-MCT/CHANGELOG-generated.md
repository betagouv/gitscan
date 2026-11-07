# Synthèse d'activité : MTES-MCT (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une modernisation profonde des interfaces utilisateurs à travers de nombreux projets, visant à améliorer l'ergonomie et la clarté des données pour les agents et les citoyens (notamment pour [otelo](/repos/MTES-MCT/otelo), [sparte](/repos/MTES-MCT/sparte) et [dahlia](/repos/MTES-MCT/dahlia)). Ces refontes visent une prise en main plus intuitive grâce à des parcours guidés et des tableaux de bord enrichis.

Parallèlement, un effort majeur a été déployé sur la fiabilité et la sécurité des plateformes. L'intégration de l'intelligence artificielle pour l'analyse documentaire ([dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend)), le renforcement de l'authentification et la stabilisation des pipelines de données garantissent des outils plus robustes et sécurisés pour les utilisateurs finaux.

## Sécurité
- **Renforcement de l'authentification** : Généralisation de l'authentification à deux facteurs (2FA) pour sécuriser les accès administratifs : [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine), [otelo](/repos/MTES-MCT/otelo), [oilhi-cms](/repos/MTES-MCT/oilhi-cms) et [mobilic-metabase](/repos/MTES-MCT/mobilic-metabase).
- **Protection des données et correctifs critiques** : Correction de vulnérabilités (SSRF, protection des données personnelles, correctifs Node.js/npm) : [trackdechets](/repos/MTES-MCT/trackdechets), [vigieau](/repos/MTES-MCT/vigieau), [mobilic](/repos/MTES-MCT/mobilic), [ecobalyse](/repos/MTES-MCT/ecobalyse) et [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend).
- **Contrôle des accès et détection de menaces** : Mise en place de mécanismes de détection de bots et de limitations de débit (rate limiting) : [envergo](/repos/MTES-MCT/envergo), [dahlia](/repos/MTES-MCT/dahlia) et [potentiel](/repos/MTES-MCT/potentiel).

## Autres changements notables
- **Migrations technologiques majeures** : Modernisation des architectures vers des versions récentes de frameworks et langages (Inertia 3, Nuxt 4, React 18, Spring Boot 4, Python 3.13) : [vizeau](/repos/MTES-MCT/vizeau), [vigieau](/repos/MTES-MCT/vigieau), [partaj](/repos/MTES-MCT/partaj), [rapportnav2](/repos/MTES-MCT/rapportnav2) et [fisheries-and-environment-data-warehouse](/repos/MTES-MCT/fisheries-and-environment-data-warehouse).
- **Optimisation des Systèmes d'Information Géographique (SIG)** : Amélioration des performances de rendu cartographique et de la gestion des données spatiales : [vizeau](/repos/MTES-MCT/vizeau), [monitorenv](/repos/MTES-MCT/monitorenv) et [qualicharge-carto](/repos/MTES-MCT/qualicharge-carto).
- **Évolutions d'infrastructure et de stockage** : Migration vers de nouveaux services de stockage (MinIO) et d'authentification (Keycloak), et optimisation des déploiements (Scaleway) : [potentiel](/repos/MTES-MCT/potentiel), [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web) et [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte majeure de l'expérience utilisateur (wizard, tutoriel) et des outils d'analyse.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation des dossiers et amélioration du traitement documentaire par IA.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Renforcement de la sécurité et automatisation de la gestion des bordereaux.
- [dahlia](/repos/MTES-MCT/dahlia) : Refonte de l'interface et nouveaux outils de gestion des litiges et des accès.
- [vizeau](/repos/MTES-MCT/vizeau) : Modernisation de l'architecture et enrichissement des capacités d'exportation de données.
- [fonds-vert-espace-laureat](/repos/MTES-MCT/fonds-vert-espace-laureat) : Refonte du module de gestion des métriques et des anomalies.
