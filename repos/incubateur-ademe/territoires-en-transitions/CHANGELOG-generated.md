## Changelog : territoires-en-transitions (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la gestion des fiches action, des plans et des indicateurs. Des corrections et des optimisations ont été apportées pour fluidifier les workflows, notamment lors de la création, modification et suppression d'éléments. L'interface utilisateur a également été revue pour une meilleure ergonomie, en particulier avec l'introduction d'un side panel et des améliorations sur l'édition en ligne.

### Évolutions fonctionnelles
- Les contributeurs pilotes peuvent désormais créer, modifier et supprimer des sous-actions dans les plans [#1234](https://github.com/incubateur-ademe/territoires-en-transitions/issues/1234).
- Il est maintenant possible d'ajouter la dernière note dans les rapports.
- Amélioration de l'ergonomie de l'édition en ligne (inline edit) avec un nouveau composant et des corrections de typage.
- Ajout d'un portail pour le menu d'édition des options d'un select dans la nouvelle fiche action.
- Les étapes d'une fiche sont désormais transformées en sous-actions.
- Ajout de la possibilité d'ajouter des tags et de les supprimer.
- Amélioration de l'affichage des scores indicatifs.
- Mise à jour de la page d'accueil avec une nouvelle bannière et une vidéo de présentation.
- Refonte de la page "Programme" avec réintégration des témoignages et amélioration de la navigation.
- Possibilité d'ajouter la dernière note dans les rapports.
- Amélioration de l'affichage de l'état d'avancement des sous-actions.
- Ajout d'un bloc "centralisez, pilotez, etc." sur la page d'accueil.

### Évolutions techniques
- Refactorisation du code pour mutualiser des composants et simplifier la gestion des données (use-get-fiche, hooks d'accès aux données).
- Suppression du code legacy et du feature flag associé.
- Mise à jour des dépendances (Node.js, GitHub Actions).
- Amélioration de la gestion des erreurs et des validations (dates, instances de gouvernance).
- Optimisation des requêtes pour la génération de rapports.
- Mise en place d'une stratégie de backup et restore de la base de données.
- Ajout de tests E2E pour vérifier l'ouverture de la modale de saisie des données d'indicateur.
- Ajout d'un endpoint backend pour créer un plan à partir d'un panier d'actions.
- Mise à jour du spreadsheet pour l'import de plans.
- Amélioration du healthcheck avec l'ajout du dashboard privé Streamlit.
- Correction de problèmes de performance liés au scroll et à la navigation entre les onglets.
- Suppression de vues SQL inutilisées.

### Autres changements
- Mise à jour de la documentation et du wording de l'application.
- Corrections de typos et améliorations de l'ergonomie générale.
- Ajout de vérifications des formules dans les référentiels.
- Amélioration de la gestion des types de collectivités.
- Correction de bugs mineurs et améliorations de la stabilité de l'application.
- Mise à jour des tests et des configurations CI/CD.
- Ajout de la gestion des erreurs pour la création de tickets depuis Crisp.
- Ajout de la possibilité d'importer des indicateurs, des référentiels et des questions de personnalisation via des fichiers CSV locaux.
