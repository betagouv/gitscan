## Changelog : archeologia-pipeline (30 derniers jours, au 01/11/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience utilisateur et une montée en puissance de la fiabilité des analyses. L'interface a été entièrement repensée pour être plus intuitive, et de nouveaux outils permettent désormais de mesurer précisément la qualité des détections archéologiques. Le plugin gère également de manière beaucoup plus robuste les données provenant de différents systèmes de coordonnées géographiques.

### Évolutions fonctionnelles
- **Refonte complète de l'interface (UI) :** Nouveau parcours utilisateur rationalisé en étapes claires, introduction d'un lexique unifié et d'un assistant plus fluide.
- **Évaluation de la fiabilité :** Ajout de métriques de performance (précision, rappel, score F1) directement dans les fiches de modèles et de classes pour mieux comprendre la confiance des détections.
- **Aide intégrée :** Remplacement de la notice externe par un manuel d'aide complet et contextuel, directement consultable dans l'interface avec recherche globale.
- **Amélioration des indices de relief :** Ajout et optimisation de nouveaux indices (VAT, PRISM, CVAT, CRIM, MSTP) avec des réglages de luminosité et de visualisation personnalisables.
- **Système d'alertes :** Mise en place d'avertissements explicites en cas de détection impossible, de fenêtres d'analyse vides ou de problèmes de résolution.
- **Gestion des résultats :** Amélioration de la présentation des rapports de traitement et des fiches de structures.

### Évolutions techniques
- **Gestion des systèmes de coordonnées (CRS) :** Amélioration majeure de la compatibilité avec les données non Lambert-93 ; conversion automatique des calculs et des sorties (MNT, indices) en mètres et en systèmes projetés [#31](https://github.com/betagouv/archeologia-pipeline/pull/31).
- **Optimisation du moteur de détection (IA) :** Support de l'accélération GPU via DirectML et optimisation de la gestion de la mémoire et des sessions ONNX pour accélérer les traitements.
- **Performances de calcul :** Optimisation des pipelines de fusion de nuages de points (PDAL) et des calculs d'indices de relief.
- **Fiabilité des détections :** Implémentation d'un algorithme de fusion en deux passes pour une meilleure précision des contours des structures [#23](https://github.com/betagouv/archeologia-pipeline/pull/23).
- **Qualité logicielle :** Renforcement de la chaîne de tests (CI/CD) avec un support étendu pour Windows et de nouveaux outils de validation automatique (recettes).

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique, du manuel d'utilisation et du README.
- **Sécurité et maintenance :** Nettoyage du code et audits de sécurité via Talisman.
- **Packaging :** Amélioration de la construction des binaires et du processus de génération des livrables.
