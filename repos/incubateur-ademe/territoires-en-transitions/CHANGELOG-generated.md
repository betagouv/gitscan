## Changelog : territoires-en-transitions (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des fiches d'actions et des plans, ainsi que sur des corrections de bugs et des optimisations techniques. L'ajout de nouvelles fonctionnalités comme l'intégration avec le système des communs et la refonte de l'interface statistique apportent une valeur ajoutée significative.

### Évolutions fonctionnelles
- Amélioration de l'ergonomie de l'EDL (Environnement de travail) avec l'utilisation d'un side panel décorrelé du contenu principal.
- Correction de la pagination de la page Actualités [#bc04d44](https://github.com/incubateur-ademe/territoires-en-transitions/issues/bc04d44).
- Gestion plus fine des sous-types de collectivités pour l'arrivée d'un nouveau référentiel.
- Amélioration de l'affichage et de la gestion des scores indicatifs.
- Ajout d'une nouvelle page "Stats" intégrant un dashboard Streamlit via un iframe [#405d668](https://github.com/incubateur-ademe/territoires-en-transitions/issues/405d668).
- Possibilité d'envoyer les plans au système des communs.
- Amélioration de l'interface et des fonctionnalités de la page Programme (nouvelle bannière, vidéo de présentation, réorganisation des blocs d'information, restauration des témoignages).
- Affichage du prénom plutôt que du nom dans les notifications par email.
- Ajout d'un bloc "centralisez, pilotez, etc." sur la page d'accueil.
- Ajout du type de collectivité "service_public".
- Transformation des étapes d'une fiche en sous-actions [#1760794](https://github.com/incubateur-ademe/territoires-en-transitions/issues/1760794).

### Évolutions techniques
- Mise à jour de la gestion du side panel pour une meilleure performance et indépendance du scroll.
- Utilisation de transactions pour la sauvegarde de l'historique des statuts et commentaires des actions.
- Refactoring pour simplifier le flow et les types de données.
- Amélioration de la gestion des erreurs lors de la création de tickets depuis Crisp.
- Suppression de vues SQL obsolètes.
- Mise à jour de Next.js pour améliorer les performances en développement.
- Suppression de tests qui modifiaient le référentiel ECI.
- Correction de bugs liés à la sauvegarde du score détaillé et à la création de tags.
- Amélioration de la gestion des fichiers et des permissions d'accès.
- Ajout de vérifications des formules du référentiel.
- Correction de problèmes liés aux migrations de données.
- Ajout de scripts de backup et restore pour la base de données.
- Utilisation de fichiers CSV locaux pour l'import des indicateurs, référentiels et questions de personnalisation.
- Mise à jour des dépendances (Node.js, GitHub Actions).
- Amélioration de la gestion des dates dans le parsing de fichiers Excel.

### Autres changements
- Mise à jour des templates d'import de plan.
- Suppression de dividers inutiles.
- Mise à jour de la documentation et du wording de certains éléments de l'interface.
- Correction de typos et amélioration du linter.
- Bump de la version du spreadsheet.
- Ajout de paramètres additionnels au service de base de données pour la gestion des transactions.
- Ajout de configurations Claude pour l'IA.
- Ajout de règles de validation pour l'update des fiches.
- Suppression de champs inutilisés.
- Amélioration des tests E2E pour éviter les faux positifs.
