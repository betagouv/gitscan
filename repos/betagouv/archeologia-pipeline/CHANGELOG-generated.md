## Changelog : archeologia-pipeline (30 derniers jours, au 17 septembre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance importante du plugin, avec le passage de la version 0.8.0 à la version 0.11.0. Les utilisateurs bénéficient désormais de nouvelles méthodes de visualisation des données LiDAR et d'une interface plus intuitive pour consulter les résultats de détection. La fiabilité des analyses a été renforcée par une meilleure gestion des limites de traitement et une présentation plus claire des niveaux de confiance des objets détectés.

### Évolutions fonctionnelles
- **Nouvelles visualisations** : Ajout de deux nouveaux produits de visualisation pour l'étape 2 : le relief coloré (CRIM) et l'ouverture prismatique (PRISM).
- **Amélioration de la lecture des résultats** : 
    - Remplacement des scores numériques de détection par une échelle de confiance textuelle plus compréhensible (Douteux, Possible, Probable, Très probable).
    - Amélioration de la présentation des fiches de structures (illustrations, provenance des données, etc.).
- **Gestion du catalogue d'entités** : 
    - Intégration de nouveaux modèles de détection (notamment pour les tranchées).
    - Nettoyage du catalogue avec le retrait de certaines classes obsolètes (talus, fosse, abri et axes linéaires de parcellaires).
- **Expérience utilisateur (UI)** : 
    - Correction des problèmes de défilement de la fenêtre et de l'affichage des libellés d'onglets.
    - Amélioration du cadrage des icônes et des vignettes de cartes.
- **Gestion de projet** : Ajout d'une bibliothèque de configurations permettant de sauvegarder et de recharger les réglages spécifiques d'un chantier.

### Évolutions techniques
- **Optimisation du traitement** : 
    - Parallélisation de la préparation des images pour le mode `existing_rvt`.
    - Mise en place d'une règle de centroïde : chaque dalle de traitement ne rapporte désormais que les objets centrés dans sa cellule, améliorant la précision de l'attribution.
- **Fiabilisation de la vision par ordinateur** : 
    - Implémentation d'un "halo inter-dalles" pour mieux traiter les objets situés aux limites des zones de calcul.
    - Durcissement de la chaîne de traitement (parité ONNX et gestion stricte des fichiers annexes) pour garantir la reproductibilité des résultats.
- **Automatisation** : Création d'un lanceur "headless" (sans interface graphique) pour permettre l'exécution automatisée du pipeline sur des jeux de données denses.
- **Robustesse** : Correction de l'orchestrateur pour une meilleure gestion des noms de modèles et des erreurs de processus.

### Autres changements
- **Intégrité des données** : Mise en place massive de sommes de contrôle (checksums) via Talisman pour garantir l'intégrité des fichiers de configuration, de documentation et de visualisation.
- **Documentation** : Mise à jour du README et des guides d'utilisation concernant les mesures parcellaires et la provenance des données.
