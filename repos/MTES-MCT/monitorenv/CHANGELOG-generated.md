## Changelog : monitorenv (30 derniers jours, au 3 août 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de la gestion des zones réglementaires, incluant la création de groupes et la simplification des formulaires de saisie. Les capacités de recherche et la précision des données cartographiques ont été renforcées, tandis que la fiabilité du suivi des missions et des rapports de données a été améliorée pour offrir une meilleure aide à la décision.

### Évolutions fonctionnelles
- **Gestion des zones réglementaires** : introduction de groupes réglementaires, simplification des processus de création (informations minimales requises) et amélioration de la recherche par localisation et par requête.
- **Suivi des missions** : correction de l'affichage des dates dans les listes, prévention de la sélection de doublons pour les unités de contrôle et possibilité de mettre à jour les missions via rapportnav.
- **Reporting** : fiabilisation de l'affichage des dates dans les rapports et correction des problèmes de fuseaux horaires (UTC).
- **Cartographie et SIG** : amélioration de la précision des coordonnées (arrondi de la longitude) et correction de la création de points sur la carte.
- **Gestion des navires** : ajout de la possibilité d'associer des fichiers et des informations complémentaires aux navires.
- **Expérience utilisateur (UX/UI)** : corrections ergonomiques sur les boutons, les menus de sélection (CheckTreePicker) et l'affichage des options de recherche.

### Évolutions techniques
- **Données et SIG** : refactorisation du concept de "facade" en "seafront", amélioration de la validité spatiale des objets et séparation des noms de couches et des localisations pour résoudre les problèmes de caractères spéciaux.
- **Architecture** : transition d'une gestion par énumérations vers une récupération de données via API pour les zones de façade et intégration de composants UI partagés (FileUploader).
- **Tests et Qualité** : stabilisation importante de la suite de tests de bout en bout (E2E/Cypress) et des tests unitaires, ainsi qu'un nettoyage du code (linting et formatage).

### Autres changements
- Corrections de fautes de frappe dans l'interface utilisateur.
