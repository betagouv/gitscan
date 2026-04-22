## Changelog : territoires-en-transitions (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la gestion des fiches d'actions, des plans et des référentiels. Des corrections et des optimisations ont été apportées pour fluidifier les workflows, notamment concernant l'import de données, la gestion des statuts et des scores, ainsi que la navigation et l'affichage des informations. Des améliorations techniques ont également été réalisées pour la gestion des backups, la robustesse des tests et l'infrastructure.

### Évolutions fonctionnelles
- **Fiches d'actions (FA) :**
    - Amélioration de l'ergonomie de l'éditeur de fiches d'actions avec l'utilisation d'un side panel pour une meilleure gestion de l'espace.
    - Correction d'un bug empêchant la mise à jour des budgets.
    - Refonte de l'interface pour une meilleure gestion des sous-actions, notamment lors de l'import de plans.
    - Amélioration du rendu et du wording des tags dans l'export PDF.
    - Suppression du champ calendrier des fiches d'actions.
    - Possibilité de modifier l'ordre des étapes legacy en sous-actions via un script de migration.
- **Plans :**
    - Ajout d'un endpoint backend pour créer un plan à partir d'un panier d'actions.
    - Amélioration de la génération de rapports, notamment en évitant certaines requêtes et en limitant la parallélisation.
    - Ajout des objectifs de la collectivité sur les graphes du PCAET dans les rapports.
    - Envoi des plans et du parentId au système des communs.
- **Référentiels :**
    - Ajout d'un nouveau référentiel et possibilité de l'afficher/cacher via les préférences de la collectivité.
    - Amélioration de la gestion des scores indicatifs et de leur affichage.
    - Recalcul du score courant si la version du référentiel a changé.
    - Possibilité de ne pas exporter les mesures désactivées.
    - Ajout de vérifications des formules du référentiel.
- **Interface utilisateur :**
    - Amélioration de l'affichage des instances de gouvernance.
    - Suppression du bouton d'accès à la collectivité en mode visite pour un utilisateur vérifié sans collectivité.
    - Limitation de la hauteur du sélecteur de pilotes d'une SA.
    - Affichage du prénom plutôt que du nom dans l'email de notification au pilote.
    - Amélioration de la pagination de la page Actualités.
    - Mise à jour de l'interface pour rendre le header des sous-actions cliquable.
- **Authentification :**
    - Amélioration de la gestion des erreurs lors de l'inscription.

### Évolutions techniques
- **Infrastructure :**
    - Finalisation de la stratégie de backup et de restore de la base de données.
    - Ajout de scripts de backup et de restore dans le CI/CD.
    - Ajout du dashboard privé Streamlit dans le healthcheck.
    - Reset des applications Streamlit keepalive.
    - Mise à jour de la version de Node.js dans les actions GitHub.
- **Tests :**
    - Ajout de tests unitaires.
    - Correction de tests flaky.
    - Augmentation du timeout par défaut des tests.
- **Code :**
    - Refactoring et mutualisation de code (hooks d'accès aux données, gestion du titre des fiches d'actions).
    - Suppression de code legacy et de feature flags obsolètes.
    - Amélioration de la gestion des transactions dans la sauvegarde de l'historique des statuts et commentaires des actions.
    - Utilisation d'une transaction pour sauvegarder l'historique des statuts et commentaires des actions.
    - Amélioration du scope des requêtes dans l'iframe Streamlit.
    - Correction de linter.

### Autres changements
- Mise à jour de la documentation.
- Ajout de configurations pour l'utilisation de Claude.
- Suppression de vues SQL inutilisées.
- Mise à jour du spreadsheet utilisé pour l'import de données.
- Amélioration de la page d'accueil et des pages du programme (bannière, vidéo, témoignages, navigation).
- Correction de la gestion des fichiers de preuve de labellisation.
- Ajout de la possibilité d'utiliser des fichiers CSV locaux pour importer les indicateurs, les référentiels et les questions de personnalisation.
