# Synthèse d'activité : gip-inclusion (du 24 juin au 24 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation gip-inclusion a été marquée par des améliorations significatives sur plusieurs fronts. Les plateformes "Le Marché de l'Inclusion" et "Traiteurs Engagés" ont bénéficié d'améliorations fonctionnelles pour les utilisateurs, notamment en termes de gestion des devis et de sécurité.  Plusieurs projets ont également mis l'accent sur la modernisation de l'infrastructure et l'automatisation des processus, comme l'intégration de Dependabot dans de nombreux dépôts et la migration vers des architectures serverless. L'intégration de nouvelles sources de données et l'amélioration de la qualité des données sont également des thèmes récurrents, notamment dans les projets "pilotage-airflow" et "data-inclusion".

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [le-marche](/repos/gip-inclusion/le-marche) : Le téléchargement de listes de recherche est désormais restreint aux utilisateurs authentifiés.
- [authentik-sso](/repos/gip-inclusion/authentik-sso) : Mise en place de l'infrastructure initiale pour un système d'authentification centralisé.
- [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav) : Implémentation de l'authentification par token et ajout d'une configuration Content Security Policy (CSP).

## Autres changements notables
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte majeure de la page d'accueil avec passage à Django et mise en place d'un pipeline CI/CD.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Refactorisation des modèles DBT et intégration de nouvelles sources de données (DORA, RDV-I, FAGERH, ESAT).
- [autometa](/repos/gip-inclusion/autometa) : Refonte de la navigation, ajout de nouveaux outils et améliorations de la gestion des erreurs.
- [data-inclusion-schema](/repos/gip-inclusion/data-inclusion-schema) : Amélioration de l'accès aux valeurs des énumérations.

## Dépôts les plus actifs
- [rdv-insertion](/repos/gip-inclusion/rdv-insertion) : Amélioration des performances, correction de bugs et ajout de nouvelles fonctionnalités pour le suivi des parcours d'accompagnement.
- [le-marche](/repos/gip-inclusion/le-marche) : Amélioration de l'expérience utilisateur pour les acheteurs et renforcement de la sécurité.
- [traiteurs-engages-app](/repos/gip-inclusion/traiteurs-engages-app) : Amélioration de la gestion des devis et ajout de la possibilité de joindre des pièces jointes sécurisées.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Intégration de nouvelles sources de données et refactorisation des modèles DBT.
- [autometa](/repos/gip-inclusion/autometa) : Refonte de l'interface utilisateur et amélioration de la performance.
