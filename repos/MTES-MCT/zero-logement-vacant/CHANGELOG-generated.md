## Changelog : zero-logement-vacant (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois a été marqué par une modernisation profonde de la plateforme, notamment via la migration vers un nouveau système d'authentification plus sécurisé et le passage à un moteur de base de données plus performant. Les fonctionnalités de gestion de campagnes ont été enrichies (ajout de documents, automatisation des statuts), tandis que l'expérience cartographique et l'accessibilité (conformité RGAA) ont été significativement améliorées pour les utilisateurs.

### Évolutions fonctionnelles
- **Gestion des campagnes** :
    - Possibilité d'enregistrer une campagne directement depuis un groupe [#1918](https://github.com/MTES-MCT/zero-logement-vacant/pull/1918).
    - Ajout de la gestion de documents au sein des campagnes (upload, liste et suppression) [#1919](https://github.com/MTES-MCT/zero-logement-vacant/pull/1919).
    - Automatisation du changement de statut des logements en fonction de la date d'envoi des campagnes.
- **Cartographie et SIG** :
    - Amélioration de la visualisation avec l'ajout de points pour les logements [#1937](https://github.com/MTES-MCT/zero-logement-vacant/pull/1937).
    - Nouvelle gestion de la visibilité des périmètres (affichage sous forme de contours).
- **Accessibilité (RGAA)** :
    - Mise en conformité importante sur plusieurs points : structure des documents, rôles des éléments de navigation (landmarks), gestion des erreurs de formulaires et étiquetage des tableaux [#1927](https://github.com/MTES-MCT/zero-logement-vacant/pull/1927), [#1931](https://github.com/MTES-MCT/zero-logement-vacant/pull/1931), [#1930](https://github.com/MTES-MCT/zero-logement-vacant/pull/1930).
- **Interface utilisateur** :
    - Stabilisation de la pagination des tableaux d'analyse et de la gestion du focus lors des changements de page.
    - Amélioration de la résilience du tableau de bord lors du chargement des cartes Metabase.

### Évolutions techniques
- **Sécurité et Authentification** :
    - Migration complète vers `Better Auth` pour une gestion des sessions plus robuste.
    - Renforcement de la sécurité avec l'ajout de l'authentification à deux facteurs (2FA) pour les administrateurs.
    - Correction de failles potentielles d'exposition de secrets dans les environnements de revue [#1958](https://github.com/MTES-MCT/zero-logement-vacant/pull/1958).
- **Base de données et API** :
    - Migration massive de la couche d'accès aux données de `Knex` vers `Kysely` pour une meilleure sécurité de type et des performances accrues.
    - Mise en place de la compression des réponses API pour optimiser les transferts de données.
- **Données et Analytics** :
    - Refonte des calculs d'enrichissement et des indicateurs d'usage ZLV pour plus de précision [#1952](https://github.com/MTES-MCT/zero-logement-vacant/pull/1952).
    - Optimisation des pipelines de calcul de localisation des propriétaires via Dagster.
- **Infrastructure et CI/CD** :
    - Accélération des tests de bout en bout (E2E) par l'exécution parallèle de Playwright et Cypress [#1955](https://github.com/MTES-MCT/zero-logement-vacant/pull/1955).
- **Outils de maintenance** :
    - Introduction d'un nouvel outil en ligne de commande (CLI) dédié aux opérations de réparation de données (Repair harness) [#1884](https://github.com/MTES-MCT/zero-logement-vacant/pull/1884).

### Autres changements
- **Documentation** :
    - Mise à jour exhaustive de la méthodologie de test RGAA.
    - Ajout de nombreux plans d'implémentation technique pour les nouvelles fonctionnalités et les migrations de base de données.
- **Nettoyage** : Suppression de nombreux composants et services d'authentification obsolètes.
