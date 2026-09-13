## Changelog : vizeau (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois a été marqué par l'enrichissement des capacités d'exportation de données (graphiques, projets et calendrier) et l'amélioration de la recherche textuelle. Parallèlement, une phase importante de stabilisation technique a été menée, incluant la migration vers Inertia 3 et l'optimisation de la gestion des données cartographiques (PMTiles).

### Évolutions fonctionnelles
- **Exportation de données** : Ajout de la possibilité d'exporter des graphiques (qualité de l'eau, assolements), des données de projet [#493](https://github.com/MTES-MCT/vizeau/pull/493) et des entrées de journal pour le calendrier au format ICS [#494](https://github.com/MTES-MCT/vizeau/pull/494).
- **Recherche** : Amélioration de l'expérience de recherche avec l'ajout de la recherche textuelle pour les substances [#499](https://github.com/MTES-MCT/vizeau/pull/499).
- **Corrections de bugs** :
    - Résolution de problèmes lors de l'affectation de parcelles aux projets [#508](https://github.com/MTES-MCT/vizeau/pull/508) et [#504](https://github.com/MTES-MCT/vizeau/pull/504).
    - Correction de la mise à jour des sous-entités de projets.
    - Correction des niveaux d'accessibilité [#505](https://github.com/MTES-MCT/vizeau/pull/505).
- **Contenu** : Correction de fautes de frappe dans les titres et descriptions des Aires d’Alimentation de Captage (AAC).

### Évolutions techniques
- **Migrations majeures** : Migration de la plateforme vers Inertia 3 [#491](https://github.com/MTES-MCT/vizeau/pull/491) et mise à jour vers Maplibre 6.
- **Optimisation SIG** : Refactorisation de la gestion des PMTiles [#498](https://github.com/MTES-MCT/vizeau/pull/498), incluant l'externalisation du générateur de fichiers.
- **Infrastructure & CI/CD** : 
    - Stabilisation de la chaîne de tests (CI) et correction des plantages.
    - Mise à jour des dépendances GitHub Actions et alignement de l'environnement de travail sur Node 24.
- **Architecture logicielle** :
    - Refactorisation de la structure de navigation du header.
    - Implémentation de contextes React pour les pages territoires/AAC [#493](https://github.com/MTES-MCT/vizeau/pull/493) et exploitations.
    - Mise à jour des schémas et des types (TypeScript).

### Autres changements
- Nettoyage de code et corrections suite aux revues de code (Copilot).
