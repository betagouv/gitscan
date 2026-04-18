# Synthèse d'activité : datagouv (derniers 7 jours)

## Résumé de l'activité
L'organisation datagouv a connu une activité soutenue au cours des dernières semaines, avec des mises à jour touchant de nombreux dépôts. Les efforts se sont concentrés sur l'amélioration de la qualité des données (cadastre, découpage administratif), l'optimisation des performances et de la robustesse des APIs (api-geo, api-meteo, api-tabular, hydra), et l'ajout de nouvelles fonctionnalités pour faciliter l'utilisation des outils et des données (hubee, passemarche, cdata, apistration).  Une migration technique majeure a également été entreprise sur `ouverture.data.gouv.fr` avec l'adoption de PNPM pour la gestion des dépendances.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité, notamment `datagouv-mcp` avec l'ajout de la surveillance via Sentry et `passemarche` avec l'ajout d'un filigrane et d'une bannière d'environnement sur les PDF générés en dehors de la production.  `datagouv_client` a également mis à jour ses dépendances pour corriger des alertes de sécurité.

## Autres changements notables
La migration vers PNPM sur `ouverture.data.gouv.fr` est un changement d'infrastructure majeur.  `hydra` a implémenté des vérifications de type statique avec `mypy` pour améliorer la qualité du code.  `apistration` a refactorisé la gestion de la configuration et des identifiants sensibles, et prépare une publication open source de la partie SIADE.  `fr-format` a effectué une mise à jour significative avec le remplacement de la validation SIRET par un interactor et la migration vers ActionMailer.

## Dépôts les plus actifs
*   [albert-api-client-playground](/repos/datagouv/albert-api-client-playground) : Amélioration de l'interface utilisateur pour afficher les alias des modèles.
*   [api-geo](/repos/datagouv/api-geo) : Correction d'un bug de normalisation des chaînes de caractères pour une meilleure reconnaissance des noms de lieux.
*   [api-meteo](/repos/datagouv/api-meteo) : Correction de bugs liés à la gestion des années dans les requêtes.
*   [api-tabular](/repos/datagouv/api-tabular) : Intégration continue améliorée avec la construction et la publication de l'image Docker.
*   [apistration](/repos/datagouv/apistration) : Ajout de nouvelles fonctionnalités et refactorisation de la gestion de la configuration.
*   [cadastre](/repos/datagouv/cadastre) : Mise à jour des données de découpage administratif pour 2026.
*   [cdata](/repos/datagouv/cdata) : Amélioration de la recherche et de l'interface utilisateur, migration vers Nuxt 4.
*   [datagouvfr_data_pipelines](/repos/datagouv/datagouvfr_data_pipelines) : Amélioration de la robustesse des pipelines et ajout de support pour les pétitions du Sénat.
*   [fr-format](/repos/datagouv/fr-format) : Ajout du format IdRNB et modernisation du code.
*   [hydra](/repos/datagouv/hydra) : Optimisation de la conversion CSV vers Parquet et ajout du support OGC WMS.
*   [passemarche](/repos/datagouv/passemarche) : Amélioration de l'authentification, de la gestion des lots et ajout de catégories.
*   [roles.data](/repos/datagouv/roles.data) : Ajout d'informations sur les organisations et les administrateurs des groupes.
