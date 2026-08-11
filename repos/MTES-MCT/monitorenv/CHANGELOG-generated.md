## Changelog : monitorenv (30 derniers jours, au 05 août 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de la gestion des zones réglementaires avec l'introduction de la notion de "groupes réglementaires". Parallèlement, des efforts importants ont été consacrés à la fiabilisation des données cartographiques et à la stabilisation de l'application via le renforcement des tests automatisés. L'expérience utilisateur a également été affinée, notamment sur les modules de missions et de reporting.

### Évolutions fonctionnelles
- **Gestion des zones réglementaires** : 
    - Introduction des "groupes réglementaires" avec de nouveaux formulaires de saisie.
    - Amélioration de la recherche de zones par localisation.
    - Simplification de la saisie (les tags ne sont plus obligatoires, tandis que le type et la localisation du groupe deviennent requis).
- **Missions et Reporting** :
    - Correction de l'affichage des dates dans les listes de missions et les rapports.
    - Sécurisation de la saisie des missions (impossibilité de sélectionner deux fois la même unité de contrôle).
    - Correction des erreurs de calcul de dates (gestion UTC) dans les rapports.
- **Cartographie et Interface** :
    - Amélioration de la précision des coordonnées lors de la création de points sur la carte.
    - Optimisation de l'ergonomie de recherche (affichage des options incluses dans la requête).
    - Corrections UI sur les boutons transparents et les sélecteurs d'arborescence (CheckTreePicker).
    - Clarification des libellés (passage de "facade" à "seafront").

### Évolutions techniques
- **Données et SIG** :
    - Refonte de la structure des données pour les zones réglementaires (séparation du nom de la couche et de la localisation pour éviter les caractères spéciaux).
    - Amélioration de la validité des données géospatiales (utilisation de `ST_MakeValid` pour les façades maritimes).
    - Correction des flux de migration de données et de l'upload de données ouvertes (open data).
- **Architecture et Refactoring** :
    - Migration de la gestion des façades maritimes d'une énumération statique vers un appel API dynamique.
    - Optimisation de la gestion des identifiants pour les nouveaux groupes (gestion des IDs > 1 000 000).
- **Qualité et Tests** :
    - Programme intensif de correction et de stabilisation des tests de bout en bout (E2E avec Cypress) et des tests unitaires.

### Autres changements
- Maintenance du code : mise à jour du formatage (Prettier), correction du linting et nettoyage de diverses coquilles (typos).
