# Synthèse d'activité : MTES-MCT (du 22 Avril au 22 Mai)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par une forte concentration sur l'amélioration de la qualité des données, la sécurité et l'expérience utilisateur de ses différentes applications. Plusieurs projets ont bénéficié de mises à jour significatives, notamment `trackdechets` avec l'ajout de la double authentification et l'amélioration de la gestion des déchets dangereux, `vizeau` avec de nouvelles fonctionnalités pour la visualisation des données agricoles, et `rapportnav2` avec des améliorations de la sécurité et de l'infrastructure.  De nombreux projets ont également reçu des corrections de bugs et des optimisations de performance.  L'intégration de nouvelles données et l'amélioration des API sont également des thèmes récurrents.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :

*   `trackdechets`: Implémentation de la double authentification (2FA).
*   `mobilic-api`: Ajout de la protection contre les attaques par complexité de requête GraphQL (DoS).
*   `acceslibre`: Correction de vulnérabilités identifiées lors de la mise à jour des dépendances.
*   `Dossier-Facile-Frontend`: Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (CVE).
*   `Keycloak-FranceConnect`: Activation de l'authentification à deux facteurs (2FA) pour l'identité ProConnect.

## Autres changements notables
*   `zero-logement-vacant`: Migration vers YAML pour la spécification OpenAPI et intégration de l'authentification SSO via Portail DF.
*   `rapportnav2`: Refonte du pipeline CI/CD avec gitlab-forge et mise à jour de l'image PostgreSQL.
*   `ecobalyse-schema`: Introduction de schémas spécifiques pour différents types de bâtiments et adoption du format *datapackage*.
*   `Docurba`: Refonte du menu d'authentification et ajout d'une bannière d'information sur la page de connexion.
*   `Lucca`: Ajout de la gestion des adhérents et possibilité de cloner un adhérent vers un autre département.

## Dépôts les plus actifs
*   `trackdechets`: Amélioration de la gestion des déchets dangereux et ajout de la double authentification.
*   `vizeau`: Ajout de nouvelles fonctionnalités pour la visualisation des données agricoles et corrections de bugs.
*   `rapportnav2`: Améliorations de la sécurité, de l'infrastructure et de la gestion des données.
*   `zero-logement-vacant`: Amélioration de la gestion des propriétaires et migration technique.
*   `Docurba`: Refonte de l'interface utilisateur et améliorations de l'API et des données.
*   `mobilic`: Ajout de la gestion des entités DREAL et amélioration de la gestion des plans d'approvisionnement.
*   `acceslibre`: Amélioration de la recherche et de la gestion des permissions utilisateurs.
*   `Dossier-Facile-Frontend`: Intégration d'une analyse documentaire intelligente (doc-ia) pour les bulletins de salaire.
*   `Lucca`: Ajout de la gestion des adhérents et possibilité de cloner un adhérent vers un autre département.
*   `ecobalyse`: Ajout de données pour de nouveaux ingrédients alimentaires et amélioration de l'explorateur.
