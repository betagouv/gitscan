# Synthèse d'activité : MTES-MCT (du 23 mai au 29 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par une forte concentration sur l'amélioration des applications existantes, avec des mises à jour significatives pour des outils clés comme Trackdéchets, Partageons l'eau, et les plateformes autour de l'accès au logement (Dossier Facile, Mon Devis Sans Oublis). Ces mises à jour incluent des améliorations de la sécurité (authentification multi-facteurs sur Trackdéchets, correction de vulnérabilités), de l'expérience utilisateur (nouvelles fonctionnalités, refonte d'interfaces), et de la performance (optimisation des requêtes, migration vers des technologies plus récentes).  Plusieurs dépôts ont bénéficié d'améliorations de la qualité du code et de l'automatisation des tests. L'intégration de nouvelles sources de données et l'ajout de fonctionnalités spécifiques à certains domaines (ICPE pour Envergo, gestion des ERP pour Acceslibre) témoignent d'une volonté de répondre aux besoins spécifiques des utilisateurs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   **Trackdéchets** : Implémentation de l'authentification multi-facteurs (MFA) avec journalisation des événements, gestion des réinitialisations et codes de récupération.
*   **Apilos** : Correction d'une vulnérabilité CVE.
*   **Keycloak-FranceConnect** : Activation de l'authentification à deux facteurs pour ProConnect.
*   **Docurba**: Mise en place d'un reverse proxy Nginx pour améliorer la sécurité.

## Autres changements notables
Plusieurs projets ont connu des évolutions techniques majeures :

*   **Zero-logement-vacant** : Migration vers React Router v7 et refonte de l'importation des données LOVAC avec DuckDB et Parquet pour une meilleure performance et scalabilité.
*   **Vizeau** : Ajout de la gestion des étapes de projet et d'une page "Mes territoires".
*   **Sparte** : Refonte de la page d'accueil et correction de problèmes de cache.
*   **Partaj** : Migration vers React 18 et mise à jour de plusieurs dépendances.
*   **Lucca-scripts** : Ajout d'une colonne 'parcelle' dans l'historique des statistiques.
*   **Docurba**: Intégration de l'authentification Supabase et refactorisation de l'architecture Django.

## Dépôts les plus actifs
*   **Trackdéchets** : Améliorations majeures de la sécurité avec l'implémentation de l'authentification multi-facteurs et corrections de bugs critiques.
*   **Partageons l'eau** : Amélioration de la gestion de l'environnement de sandbox et des workflows Git.
*   **Dossier Facile (frontend et backend)** : Nombreuses améliorations de l'interface utilisateur, de la gestion des données et de la sécurité.
*   **Envergo** : Ajout de nouvelles fonctionnalités pour la gestion des ICPE et refonte de l'interface utilisateur.
*   **Acceslibre** : Ajout de la gestion des ERP en RPA et amélioration de la collecte de données.
*   **Docurba**: Refonte de l'architecture et ajout de nouvelles fonctionnalités.
*   **Lucca**: Ajout de la gestion des adhérents et amélioration de l'importation des données.
*   **Aigle (frontend et api)** : Ajout de nouveaux statuts et amélioration de la gestion des données.
*   **Dahlia**: Intégration du SSO ProConnect et amélioration du scrapping.
