## Changelog : resorption-bidonvilles (30 derniers jours, au 15 septembre 2026)

### Résumé
Cette période a été marquée par une modernisation majeure de l'interface utilisateur grâce à l'intégration complète du Design System de l'État (DSFR), améliorant ainsi l'accessibilité et l'ergonomie de la plateforme. Des améliorations significatives ont également été apportées à l'outil de cartographie et à la fiabilité des exports de données, tout en renforçant la robustesse technique de l'application.

### Évolutions fonctionnelles
- **Modernisation de l'interface (DSFR) :** Intégration de nouveaux composants standards pour les filtres, le tri et les boutons, offrant une meilleure accessibilité (navigation au clavier) et une interface plus cohérente [#2745](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2745).
- **Amélioration de l'ergonomie :** Optimisation de la réactivité (responsiveness) de l'application sur différents formats d'écran et amélioration de l'affichage du défilement horizontal.
- **Évolutions cartographiques :** 
    - Remplacement du fond de carte CartoDB par OpenStreetMap pour une meilleure visibilité [#2758](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2758).
    - Activation du zoom à la molette lors de l'utilisation de la carte en plein écran [#2760](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2760).
- **Fiabilisation des données :**
    - Correction des erreurs d'affichage (dates NaN) et des filtres lors de l'export des phases de résorption [#2749](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2749) [#2746](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2746).
    - Suppression d'un doublon dans le filtre "Type de propriétaire" sur la carte [#2759](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2759).

### Évolutions techniques
- **Refonte du Frontend :** Migration de composants vers la syntaxe `<script setup>` de Vue 3 et nettoyage des exports du package UI pour une meilleure maintenance.
- **Robustesse de l'API :** 
    - Ajout de timeouts de connexion pour la base de données Majic et amélioration de la gestion des messages d'erreur en cas d'indisponibilité du service [#2750](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2750).
    - Correction de la gestion des timeouts réseau sur l'intercepteur Axios.
- **Qualité logicielle :** Réactivation et mise à jour massive des tests unitaires de l'API (utilisateurs, contacts, téléchargements, etc.) pour garantir la stabilité des fonctionnalités existantes.

### Autres changements
- Nettoyage du code (suppression de fichiers et d'imports inutilisés) et corrections de linting.
