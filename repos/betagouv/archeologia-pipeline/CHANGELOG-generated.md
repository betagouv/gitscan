## Changelog : archeologia-pipeline (30 derniers jours, au 11 octobre 2026)

### Résumé
Cette période a été marquée par une amélioration majeure de l'accompagnement utilisateur et de la capacité d'analyse des résultats. L'introduction d'un manuel d'aide directement intégré à l'interface et d'un système de profilage des scores permet désormais aux utilisateurs de mieux comprendre et d'ajuster la fiabilité de la détection par intelligence artificielle. De nouveaux produits de visualisation et des rapports de traitement automatisés enrichissent également les livrables produits.

### Évolutions fonctionnelles
- **Aide et documentation intégrée** : Remplacement de la notice externe par un manuel intégré à l'interface, incluant une recherche globale (Ctrl+F), une aide contextuelle, et des captures d'écran interactives.
- **Analyse de performance (Profils)** : Création d'un nouvel outil de profilage des scores permettant de visualiser l'équilibre entre précision et rappel, de tester dynamiquement des seuils de détection et d'exporter ces métriques.
- **Nouveaux produits de visualisation** : Ajout de nouveaux produits de traitement, notamment l'ouverture (OPNS), le relief coloré (CRIM) et l'ouverture prismatique (PRISM).
- **Amélioration des rapports et fiches** : 
    - Génération d'un rapport de traitement complet au format HTML dans le dossier de sortie.
    - Distinction claire entre les fiches de "classe" et les fiches de "modèle".
    - Ajout de métriques de fiabilité observée directement dans les fiches de classe.
    - Amélioration de l'ergonomie des fiches avec des fonctions de survol croisé entre la carte et la liste.
- **Gestion des données** : Intégration de la grille IGN (via WFS Géoplateforme) et possibilité de sauvegarder/recharger les configurations de chantier.

### Évolutions techniques
- **Refonte de l'interface utilisateur (UI)** : 
    - Modernisation de la vue d'exécution (étape 4) avec une frise d'état et un journal de bord amélioré.
    - Restructuration de l'arborescence des fichiers de sortie pour séparer les livrables des fichiers techniques.
- **Optimisation du pipeline de données** : 
    - Amélioration de la gestion des fichiers LiDAR (écriture atomique des fichiers .laz et correction de compatibilité PDAL).
    - Optimisation du traitement des images pour le mode "existing_rvt" via une parallélisation.
- **Intelligence Artificielle** : Amélioration de la précision de l'inférence par un recentrage des objets détectés.
- **Packaging et déploiement** : Correction du processus de création des archives ZIP pour exclure les fichiers non essentiels (catalogues privés, sauvegardes horodatées).

### Autres changements
- **Intégrité et sécurité** : Renforcement de la vérification de l'intégrité des fichiers via l'ajout systématique de sommes de contrôle (checksums).
- **Maintenance** : Mise à jour de la documentation de recette et nettoyage des workflows de développement.
