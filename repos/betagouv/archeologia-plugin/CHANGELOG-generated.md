## Changelog : archeologia-plugin (30 derniers jours, au 10 novembre 2026)

### Résumé
Cette période a été marquée par une refonte majeure de l'interface utilisateur, transformant l'expérience en un assistant guidé par étapes pour plus de clarté. Le plugin est devenu plus robuste face à des données géographiques variées (systèmes de coordonnées différents) et les capacités de détection par intelligence artificielle ont été affinées pour offrir des résultats plus précis et des rapports plus lisibles.

### Évolutions fonctionnelles

**Interface et expérience utilisateur**
- Refonte complète de l'interface : passage à un flux de travail structuré en quatre étapes claires (Assistant).
- Amélioration de l'accessibilité : intégration de contrastes AA, gestion du focus clavier et agrandissement des cibles de clic.
- Nouveau lexique unifié pour harmoniser le vocabulaire (relief, structures, dalles, etc.) et simplification de la navigation (suppression du panneau latéral au profit de fenêtres dédiées).
- Ajout d'un champ "Nom de l'analyse" permettant de personnaliser et de retrouver facilement ses travaux.

**Détection et précision**
- Amélioration de la fiabilité de la détection : meilleure gestion des seuils de fusion des polygones par classe et correction des erreurs de géométrie.
- Système d'avertissements enrichi : signalement des fenêtres d'analyse vides, des données trop grossières ou des problèmes d'échelle.
- Affichage plus précis des niveaux de confiance lors de la détection.

**Gestion des données et géoréférencement**
- Support étendu des systèmes de coordonnées (CRS) : acceptation des données projetées en mètres hors Lambert-93 et gestion automatique des conversions.
- Amélioration de la gestion des résolutions : blocage des lots présentant des résolutions trop hétérogènes pour garantir la qualité de l'analyse.
- Meilleure gestion des "halos" (zones de bordure) lors de l'utilisation de modèles numériques de terrain (MNT) existants.

**Rapports et livrables**
- Optimisation des rapports : inclusion du nom de l'analyse, de l'horodatage et de vignettes plus lisibles.
- Automatisation dans QGIS : les couches générées sont désormais nommées automatiquement selon le traitement effectué et peuvent être ajoutées directement au projet courant.

### Évolutions techniques

**Moteur d'intelligence artificielle**
- Optimisation du moteur de détection : multiples recompilations du binaire `cv_runner_onnx` pour corriger des problèmes de gestion de la mémoire, de précision des fenêtres et de traitement des géométries.
- Amélioration de l'export des modèles (notamment pour RF-DETR) pour assurer une compatibilité accrue.

**Tests et intégration continue**
- Accélération des cycles de validation : mise en place de tests en parallèle avec `pytest-xdist`.
- Extension de la couverture de test : ajout de nouveaux jobs de CI sur Windows et renforcement des hooks de pré-validation (`pre-push`).

### Autres changements
- Documentation : mise à jour complète du manuel utilisateur, du fichier README et des schémas d'aide.
- Nettoyage : suppression de fonctions obsolètes et optimisation des scripts de gestion des fichiers de traces.
