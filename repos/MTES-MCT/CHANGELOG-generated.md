# Synthèse d'activité : MTES-MCT (du 22/05 au 22/06)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par une forte concentration sur l'amélioration de la qualité des données, la sécurité et l'expérience utilisateur de ses différentes applications. Plusieurs dépôts ont bénéficié de mises à jour significatives, notamment *trackdechets*, *vizeau*, *mon-devis-sans-oublis*, *dialog* et *acceslibre*. Ces améliorations se traduisent par de nouvelles fonctionnalités, des corrections de bugs, des optimisations de performance et une meilleure intégration avec d'autres services. L'accent mis sur la sécurité, avec des mises à jour de dépendances et des corrections de vulnérabilités, témoigne de l'engagement de l'organisation envers la protection des données et la fiabilité de ses services.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :

*   Correction d'une vulnérabilité dans `mesads` concernant l'authentification.
*   Mise à jour de la dépendance `sentry-sdk` dans `mon-devis-sans-oublis-backend-ocr` pour corriger des failles de sécurité.
*   Mise à jour de Twig et Symfony dans `dahlia` pour corriger des vulnérabilités de sécurité.
*   Correction de vulnérabilités dans les fichiers `uv.lock` de `ecobalyse-data`.

## Autres changements notables
*   **trackdechets:** Amélioration significative de l'interface utilisateur et correction de bugs, notamment sur les formulaires BSFF.
*   **vizeau:** Ajout de la gestion de projets avec étapes, attachement d'exploitations et de parcelles, et amélioration de la visualisation de la qualité de l'eau.
*   **dialog:** Ajout de la possibilité d'intégrer la cartographie via iframe et amélioration de la gestion des arrêtés.
*   **acceslibre:** Intégration de données APIDAE, ajout de nouvelles questions signalétiques et amélioration de la qualité des données.
*   **dahlia:** Passage d'une version initiale à une application fonctionnelle avec SSO ProConnect et scraping automatisé.
*   **carbuere:** Ajout de la gestion des entités DREAL et possibilité pour les DREAL d'accepter/refuser des utilisateurs.
*   **aigle-frontend & aigle-api:** Amélioration de l'administration, de la gestion des zones personnalisées et des performances.

## Dépôts les plus actifs
*   [trackdechets](/repos/MTES-MCT/trackdechets) : Corrections de bugs et améliorations de l'expérience utilisateur sur les formulaires BSFF.
*   [vizeau](/repos/MTES-MCT/vizeau) : Ajout de nouvelles fonctionnalités de gestion de projets et d'amélioration de la visualisation des données.
*   [dialog](/repos/MTES-MCT/dialog) : Amélioration de l'intégration cartographique et de la gestion des arrêtés.
*   [acceslibre](/repos/MTES-MCT/acceslibre) : Intégration de nouvelles données et amélioration de la qualité des informations sur l'accessibilité.
*   [dahlia](/repos/MTES-MCT/dahlia) : Développement d'une application fonctionnelle pour la gestion des dossiers DALO, DAHO et DAHU.
*   [mon-devis-sans-oublis-backend](/repos/MTES-MCT/mon-devis-sans-oublis-backend) : Amélioration de la gestion des droits et des fonctionnalités.
*   [boris](/repos/MTES-MCT/boris) : Amélioration du SEO et de la page de revente.
