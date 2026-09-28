## Changelog : ecobalyse (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'un enrichissement significatif de sa base de données environnementale, notamment avec l'ajout de nouveaux produits et une meilleure classification des ingrédients via une nouvelle structure de taxonomie. L'expérience utilisateur a été améliorée par l'ajout de nouveaux éléments visuels et d'exemples dans le simulateur, tandis que l'infrastructure a été optimisée pour gagner en performance et en sécurité.

### Évolutions fonctionnelles
- **Enrichissement des données :**
    - Ajout de nouveaux éléments de données : piles alcalines ([#2828](https://github.com/MTES-MCT/ecobalyse/issues/2828)), assemblage de lait végétal ([#2800](https://github.com/MTES-MCT/ecobalyse/issues/2800)) et définition des catégories de consommation pour Veli ([#2798](https://github.com/MTES-MCT/ecobalyse/issues/2798)).
    - Amélioration de la précision et de la gestion des données : mise à jour des types de matériaux et des processus de recyclage des batteries ([#2825](https://github.com/MTES-MCT/ecobalyse/issues/2825)), ajout de la masse par unité pour l'eau ([#2799](https://github.com/MTES-MCT/ecobalyse/issues/2799)) et reclassification des ingrédients ([#2764](https://github.com/MTES-MCT/ecobalyse/issues/2764)).
    - Optimisation des rapports : amélioration du rapport de hiérarchie des ingrédients ([#2787](https://github.com/MTES-MCT/ecobalyse/issues/2787)) et gestion des anomalies de hiérarchie ([#2652](https://github.com/MTES-MCT/ecobalyse/issues/2652)).
- **Améliorations de l'interface et du simulateur :**
    - Nouvelles fonctionnalités de simulation : chargement d'exemples par défaut ([#2782](https://github.com/MTES-MCT/ecobalyse/issues/2782)), affichage de la masse unitaire des articles de production ([#2766](https://github.com/MTES-MCT/ecobalyse/issues/2766)) et rendu des éléments de partage des composants ([#2772](https://github.com/MTES-MCT/ecobalyse/issues/2772)).
    - Corrections d'interface : masquage des détails des étapes désactivées pour le textile ([#2812](https://github.com/MTES-MCT/ecobalyse/issues/2812)) et réinitialisation systématique des processus ([#2785](https://github.com/MTES-MCT/ecobalyse/issues/2785)).

### Évolutions techniques
- **Architecture et données :**
    - Refonte de la gestion des données : introduction d'un système de taxonomie (`taxonomy.json`) remplaçant les anciens fichiers d'ingrédients ([#2746](https://github.com/MTES-MCT/ecobalyse/issues/2746)) et automatisation de l'inférence des types de matériaux ([#2779](https://github.com/MTES-MCT/ecobalyse/issues/2779)).
    - Introduction d'une nouvelle API générique ([#2792](https://github.com/MTES-MCT/ecobalyse/issues/2792)).
- **Performance et infrastructure :**
    - Optimisation des performances : utilisation de l'insertion par lots (batch) pour les bases de données ([#2790](https://github.com/MTES-MCT/ecobalyse/issues/2790)).
    - Maintenance et compatibilité : mise à jour de la compatibilité avec Scalingo ([#2801](https://github.com/MTES-MCT/ecobalyse/issues/2801), [#2776](https://github.com/MTES-MCT/ecobalyse/issues/2776)), mise à jour de sécurité de Maildev ([#2771](https://github.com/MTES-MCT/ecobalyse/issues/2771)) et mise à jour de l'outil `uv` ([#2794](https://github.com/MTES-MCT/ecobalyse/issues/2794)).
    - Ajout d'un script de comparaison Volca ([#2783](https://github.com/MTES-MCT/ecobalyse/issues/2783)).

### Autres changements
- Nettoyage des fichiers de métadonnées obsolètes ([#2831](https://github.com/MTES-MCT/ecobalyse/issues/2831)).
- Mise à jour du snippet de suivi Plausible ([#2819](https://github.com/MTES-MCT/ecobalyse/issues/2819)).
- Ajout d'un flag `betauser` pour le contrôle des fonctionnalités ([#2832](https://github.com/MTES-MCT/ecobalyse/issues/2832)).
