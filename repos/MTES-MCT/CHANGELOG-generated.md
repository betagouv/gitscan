# Synthèse d'activité : MTES-MCT (du 23 mai au 23 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par une forte concentration sur l'amélioration de l'expérience utilisateur, la sécurité et la qualité des données. Plusieurs projets ont bénéficié de refontes d'interface, d'ajouts de fonctionnalités clés (comme l'authentification multi-facteurs pour Trackdéchets et l'importation massive de données pour MesADS) et de corrections de bugs.  Un effort important a également été consacré à la modernisation des infrastructures et des dépendances, notamment pour assurer la sécurité et la performance des applications. Les projets *Lucca*, *Dossier Facile* et *Ecobalyse* ont été particulièrement actifs, avec des mises à jour significatives sur de nombreux aspects.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :

*   **Trackdechets :** Implémentation de l'authentification multi-facteurs (MFA) avec gestion des réinitialisations et récupération de compte.
*   **Mesads :** Correction d'une faille de sécurité potentielle en utilisant `format_html` pour éviter l'exécution de JavaScript non intentionnel.
*   **Apilos :** Mise à jour de la dépendance `sentry-sdk` pour corriger des vulnérabilités.
*   **Carbure :** Correction de vulnérabilités de sécurité (CVE openssl) dans l'image de développement.

## Autres changements notables
*   **Zero-logement-vacant :** Migration vers React Router v7 et refonte de l'importation des données LOVAC avec DuckDB et Parquet pour une meilleure performance et scalabilité.
*   **Vizeau :** Nouvelle gestion complète des projets avec étapes, tags et documents associés.
*   **Verseau2 :** Ajout de la gestion des erreurs via Sentry et optimisation des requêtes avec une vue matérialisée.
*   **Trackdechets-vigiedechets :** Ajout de la possibilité de joindre plusieurs pièces jointes au formulaire de contact/assistance.
*   **Sparte :** Refonte de la page d'accueil et amélioration de la lisibilité des indicateurs.
*   **Potentiel :** Ajout de la possibilité pour les PP de corriger leur numéro d'identification.
*   **Monitorfish :** Migration vers les nouvelles versions de Spring Boot et Security.
*   **Docurba :** Intégration de Supabase pour l'authentification et remplacement de `wget` par `curl`.

## Dépôts les plus actifs
*   **Dossier-Facile-Frontend :** Amélioration de l'expérience utilisateur, correction de bugs et amélioration des tests E2E.
*   **Trackdechets :** Implémentation de l'authentification multi-facteurs et corrections de blocages critiques.
*   **Lucca :** Ajout de la gestion des adhérents et amélioration de l'interface d'administration.
*   **Mesads :** Ajout de l'importation massive de données et amélioration de la gestion des utilisateurs.
*   **Ecobalyse :** Ajout de nouvelles données pour les batteries, les emballages et les transports, ainsi que des améliorations techniques.
*   **Docurba :** Amélioration de l'affichage, ajout de fonctionnalités d'administration et migration vers Supabase.
*   **Potentiel :** Amélioration de l'interface et ajout de fonctionnalités pour les utilisateurs.
*   **Monitorfish :** Amélioration de l'interface et des fonctionnalités pour les contrôles en mer et à la débarque.
*   **Dialog :** Ajout de la gestion des cartes de densité et d'une procédure d'urgence.
*   **Apilos :** Amélioration de la génération de documents et correction de bugs.
