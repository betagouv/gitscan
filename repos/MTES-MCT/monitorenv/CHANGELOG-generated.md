## Changelog : monitorenv (30 derniers jours, au 14 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout et l'amélioration de la gestion des "Zones de Vigilance" et des "Zones Réglementaires", avec une nouvelle interface utilisateur pour leur gestion, des filtres améliorés et une intégration plus poussée avec les données du CACEM. Des corrections et optimisations ont également été apportées au niveau de l'API et de la gestion des données des navires.

### Évolutions fonctionnelles
- **Zones de Vigilance :**
    - Ajout d'un filtre pour afficher les zones de vigilance récentes.
    - Mise à jour de l'interface utilisateur avec des lignes extensibles et un tri par date de création par défaut.
    - Ajout de colonnes épinglées pour une meilleure visibilité des informations clés.
    - Amélioration des filtres disponibles dans la vue de liste.
- **Zones Réglementaires :**
    - Création d'un nouveau flux de gestion des zones réglementaires, incluant un formulaire de création/modification.
    - Ajout d'une page de liste des zones réglementaires avec des filtres et une recherche.
    - Intégration des thèmes et tags dans le flux de gestion des zones réglementaires.
    - Amélioration de l'affichage des zones réglementaires dans le brief et sur la carte.
    - Possibilité d'exporter les données des zones réglementaires vers data.gouv.
- **AMP (Aires Marines Protégées) :**
    - Mise en évidence des nouveaux AMPs.
    - Correction du flux de données des AMPs.
    - Amélioration de l'affichage des AMPs sur la carte.
- **Navires :**
    - Ajout du tonnage brut UMS aux informations du navire.
    - Amélioration de la récupération des informations du navire par ID.

### Évolutions techniques
- **API :**
    - Ajout d'index sur les données d'identification pour améliorer les performances.
    - Refonte de la récupération des données des navires.
    - Ajout d'APIs pour la gestion des zones réglementaires (recherche, création, modification).
- **Base de données :**
    - Renommage du champ `sent_at` et refactoring de l'utilisation des timestamps.
    - Optimisation des requêtes pour la récupération des zones réglementaires.
- **Infrastructure :**
    - Mise à jour des dépendances (renouvellement des mises à jour automatiques avec un délai de 30 jours).
- **Tests :**
    - Correction des tests unitaires et E2E.
    - Ajout de tests pour les nouvelles fonctionnalités.
- **Sécurité :**
    - Vérification de la présence de la revendication `organizational_unit` pour renforcer la sécurité.

### Autres changements
- Correction de bugs divers liés à l'interface utilisateur et aux flux de données.
- Amélioration de la visibilité de l'environnement (intégration/pré-production).
- Suppression de fonctionnalités obsolètes et de fichiers inutiles.
- Mise à jour de la documentation.
- Ajout d'un bandeau d'information sur toutes les pages.
- Correction de l'URL de la favicon.
- Refactoring général du code pour améliorer la lisibilité et la maintenabilité.
