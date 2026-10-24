# Synthèse d'activité : MTES-MCT (du 20/09 au 27/09/2026)

## Résumé de l'activité
L'activité de cette période est marquée par une volonté de moderniser l'expérience utilisateur et de renforcer la fiabilité des outils métier. De nombreux projets ont bénéficié de refontes graphiques majeures ([sparte](/repos/MTES-MCT/sparte), [otelo](/repos/MTES-MCT/otelo)) ou de l'introduction de nouveaux modes d'accompagnement, tels que des assistants de simulation et des tutoriels interactifs, pour faciliter la prise en main des plateformes.

Parallèlement, l'organisation a concentré ses efforts sur l'exploitation des données, avec une amélioration notable des capacités d'exportation (rapports PDF, graphiques, OpenData) et une automatisation accrue des processus de collecte et de validation. Ces évolutions visent à offrir des outils plus précis et plus simples pour les agents et les citoyens, tout en garantissant une meilleure conformité aux standards d'accessibilité (RGAA).

## Sécurité
- **Renforcement de l'authentification** : Généralisation de l'authentification à deux facteurs (2FA) pour sécuriser les accès critiques ([otelo](/repos/MTES-MCT/otelo), [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine), [oilhi-cms](/repos/MTES-MCT/oilhi-cms), [histologe](/repos/MTES-MCT/histologe), [mobilic-metabase](/repos/MTES-MCT/mobilic-metabase)).
- **Protection des données et des API** : Mise en place de mesures contre les attaques par déni de service (DoS), les fuites de données (BOLA) et les injections (SSRF) ([trackdechets](/repos/MTES-MCT/trackdechets), [mobilic-api](/repos/MTES-MCT/mobilic-api), [dahlia](/repos/MTES-MCT/dahlia)).
- **Conformité et audit** : Amélioration de la protection de la vie privée via des processus d'anonymisation renforcés ([mobilic-api](/repos/MTES-MCT/mobilic-api)) et mise en place de logs d'audit pour la traçabilité des actions ([dahlia](/repos/MTES-MCT/dahlia), [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles)).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Inertia 3 pour [vizeau](/repos/MTES-MCT/vizeau), mise à jour vers React 18 pour [partaj](/repos/MTES-MCT/partaj) et montée de version vers Spring Boot 4.1 pour [rapportnav2](/repos/MTES-MCT/rapportnav2).
- **Modernisation des environnements de formation** : Mise à jour globale des environnements de développement et de déploiement vers R 4.6.0 pour l'ensemble des modules du [parcours-r](/repos/MTES-MCT/parcours-r).
- **Évolutions d'infrastructure** : Migration vers le stockage S3 pour la gestion des fichiers privés ([envergo](/repos/MTES-MCT/envergo)) et optimisation des pipelines d'ingestion de données ([partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration)).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte complète de l'interface de résultats, ajout de tutoriels et renforcement de la sécurité.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Enrichissement massif de la base de données et automatisation de la classification des matériaux.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Introduction de l'autovalidation des dossiers et amélioration de l'analyse documentaire par IA.
- [mobilic-api](/repos/MTES-MCT/mobilic-api) : Travaux importants sur l'anonymisation des données, la protection contre les attaques et la gestion des alertes.
- [parcours-r](/repos/MTES-MCT/parcours-r) : Mise à jour des environnements Docker et optimisation des workflows de déploiement pour la formation.
