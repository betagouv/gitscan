# Synthèse d'activité : MTES-MCT (du 01/09 au 31/10)

## Résumé de l'activité
L'activité récente de l'organisation a été marquée par une modernisation profonde des interfaces utilisateurs et une amélioration significative de la fiabilité des données. Des projets majeurs comme [otelo](/repos/MTES-MCT/otelo), [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) et [sparte](/repos/MTES-MCT/sparte) ont bénéficié de refontes ergonomiques visant à simplifier la prise en main des outils et à enrichir les capacités d'analyse pour les utilisateurs finaux.

Parallèlement, l'organisation a intensifié ses efforts sur l'automatisation des processus métier et l'ingestion de données multi-sources, notamment via [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration) et [vizeau](/repos/MTES-MCT/vizeau). Ces évolutions permettent une gestion plus fluide des flux d'informations et une meilleure exploitation des indicateurs de suivi pour les décideurs.

## Sécurité
- **Renforcement de l'authentification** : Généralisation de l'authentification à deux facteurs (2FA) sur [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine), [oilhi-cms](/repos/MTES-MCT/oilhi-cms) et [histologe](/repos/MTES-MCT/histologe).
- **Correction de vulnérabilités critiques** : Résolution de failles de type SSRF, injections et fuites de données sur [trackdechets](/repos/MTES-MCT/trackdechets), [mobilic-api](/repos/MTES-MCT/mobilic-api) et [ecobalyse](/repos/MTES-MCT/ecobalyse).
- **Protection des données et des accès** : Mise en place de logs d'audit, de mécanismes de limitation de débit (rate limiting) et de détection de bots sur [dahlia](/repos/MTES-MCT/dahlia), [otelo](/repos/MTES-MCT/otelo), [boris](/repos/MTES-MCT/boris) et [envergo](/repos/MTES-MCT/envergo).
- **Sécurisation des infrastructures** : Amélioration du contrôle des tokens, du chiffrement des identifiants et de la gestion des accès aux fichiers sur [stop-punaises](/repos/MTES-MCT/stop-punaises), [potentiel](/repos/MTES-MCT/potentiel) et [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Inertia 3 pour [vizeau](/repos/MTES-MCT/vizeau), Nuxt 4 pour [vigieau](/repos/MTES-MCT/vigieau), React 18 pour [partaj](/repos/MTES-MCT/partaj) et Spring Boot 4.1.0 pour [rapportnav2](/repos/MTES-MCT/rapportnav2).
- **Évolutions d'infrastructure et CI/CD** : Mise à jour des environnements Docker (passage à R 4.6.0) pour les projets du [parcours-r](/repos/MTES-MCT/parcours-r), déploiement automatisé sur Scaleway pour [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web) et migration vers de nouveaux services de stockage (MinIO/Keycloak) pour [potentiel](/repos/MTES-MCT/potentiel).
- **Optimisations SIG et performance** : Amélioration des performances de rendu cartographique via l'utilisation de `ST_asMVT` sur [monitorenv](/repos/MTES-MCT/monitorenv) et optimisation de la gestion des tuiles PMTiles pour [vizeau](/repos/MTES-MCT/vizeau).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte complète de la page de résultats, ajout de tutoriels interactifs et renforcement de la sécurité.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation des dossiers et amélioration de l'analyse documentaire par IA.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Sécurisation de la plateforme contre les injections et automatisation de la gestion des bordereaux.
- [mobilic-api](/repos/MTES-MCT/mobilic-api) : Normalisation des immatriculations, optimisation des performances et corrections de sécurité suite à audit.
- [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration) : Amélioration de l'ingestion et de la normalisation des données provenant de multiples connecteurs.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Enrichissement de la base de données et nouveaux outils d'édition en masse des articles de production.
- [monitorenv](/repos/MTES-MCT/monitorenv) : Optimisation de la cartographie et enrichissement des outils d'administration du backoffice.
