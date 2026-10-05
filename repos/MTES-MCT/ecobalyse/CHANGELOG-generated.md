## Changelog : ecobalyse (30 derniers jours, au 1er octobre 2026)

### Résumé
Ce mois-ci, ecobalyse a considérablement enrichi sa base de données avec l'ajout de nouveaux objets (moteurs électriques, piles) et de composants alimentaires. L'expérience utilisateur est améliorée par un nouvel éditeur de production, tandis que le système devient plus intelligent grâce à l'automatisation de la classification des matériaux.

### Évolutions fonctionnelles
- Nouvel éditeur modale pour la gestion des éléments de production [#2849](https://github.com/MTES-MCT/ecobalyse/pull/2849)
- Enrichissement de la base de données : moteurs électriques [#2846](https://github.com/MTES-MCT/ecobalyse/pull/2846), piles alcalines [#2828](https://github.com/MTES-MCT/ecobalyse/pull/2828), ingrédients Koch [#2836](https://github.com/MTES-MCT/ecobalyse/pull/2836), assemblages de laits végétaux [#2800](https://github.com/MTES-MCT/ecobalyse/pull/2800) et définition des catégories de consommation pour Veli [#2798](https://github.com/MTES-MCT/ecobalyse/pull/2798)
- Amélioration des rapports de hiérarchie des ingrédients [#2787](https://github.com/MTES-MCT/ecobalyse/pull/2787)
- Corrections de l'interface : gestion des noms d'éléments personnalisés [#2855](https://github.com/MTES-MCT/ecobalyse/pull/2855) et application des origines par défaut pour les composants [#2857](https://github.com/MTES-MCT/ecobalyse/pull/2857)

### Évolutions techniques
- Introduction d'une nouvelle API [#2792](https://github.com/MTES-MCT/ecobalyse/pull/2792)
- Automatisation de l'inférence des types de matériaux via la taxonomie, supprimant la saisie manuelle [#2779](https://github.com/MTES-MCT/ecobalyse/pull/2779)
- Optimisation des performances via l'utilisation d'insertions par lots (batch) en base de données [#2790](https://github.com/MTES-MCT/ecobalyse/pull/2790)
- Ajout d'un flag "betauser" pour le déploiement contrôlé de fonctionnalités expérimentales [#2832](https://github.com/MTES-MCT/ecobalyse/pull/2832)
- Correction des tests de bout en bout (E2E) [#2858](https://github.com/MTES-MCT/ecobalyse/pull/2858)
- Correction de l'exposition des détails d'étapes désactivées dans l'API textile [#2812](https://github.com/MTES-MCT/ecobalyse/pull/2812)

### Autres changements
- Documentation : ajout de guides sur les compléments [#2833](https://github.com/MTES-MCT/ecobalyse/pull/2833) et la création de nouveaux périmètres (scopes) [#2839](https://github.com/MTES-MCT/ecobalyse/pull/2839)
- Maintenance des données : mises à jour sur le transport des produits laitiers [#2856](https://github.com/MTES-MCT/ecobalyse/pull/2856), les processus de recyclage des batteries [#2825](https://github.com/MTES-MCT/ecobalyse/pull/2825) et les propriétés de l'eau [#2799](https://github.com/MTES-MCT/ecobalyse/pull/2799)
- Nettoyage des fichiers de métadonnées obsolètes [#2831](https://github.com/MTES-MCT/ecobalyse/pull/2831)
