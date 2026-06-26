## Changelog : vizeau (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la gestion des projets, en particulier sur la création, l'édition et le suivi des étapes de ces projets. Des améliorations ont également été apportées à la gestion des territoires et des exploitations agricoles, ainsi qu'à l'infrastructure et aux tests du projet.

### Évolutions fonctionnelles
- **Gestion des projets :**
    - Implémentation des tags pour les étapes de projet [#457](https://github.com/MTES-MCT/vizeau/issues/457).
    - Ajout de la possibilité d'uploader des documents lors de la création de la première étape d'un projet [#456](https://github.com/MTES-MCT/vizeau/issues/456).
    - Refonte du formulaire de projet, simplification et suppression de l'étape "FIRST_ENTRY" en édition [#457](https://github.com/MTES-MCT/vizeau/issues/457).
    - Correction d'un bug où les étapes de projet étaient supprimées lors de l'édition du projet [#457](https://github.com/MTES-MCT/vizeau/issues/457).
    - Ajout de la gestion des documents pour chaque étape de projet [#453](https://github.com/MTES-MCT/vizeau/issues/453).
    - Ajout d'une étape de suivi de projet [#451](https://github.com/MTES-MCT/vizeau/issues/451).
    - Création d'une page "Mes territoires" pour visualiser les territoires de l'utilisateur [#445](https://github.com/MTES-MCT/vizeau/issues/445).
    - Création d'une page "Projets" avec une liste des projets [#426](https://github.com/MTES-MCT/vizeau/issues/426).
    - Création d'un formulaire de création de projet (front et back) [#436](https://github.com/MTES-MCT/vizeau/issues/436).
- **Exploitations agricoles :**
    - Ajout d'une étape d'assignation d'AAC (Autorisation d'Accès Communautaire) au tunnel de création d'exploitation [#440](https://github.com/MTES-MCT/vizeau/issues/440).
    - Correction de la recherche dans les AACs [#439](https://github.com/MTES-MCT/vizeau/issues/439).
- **Interface utilisateur :**
    - Ajout d'un bouton de navigation vers la sélection de parcelles [#452](https://github.com/MTES-MCT/vizeau/issues/452).
    - Amélioration de la réactivité de la mise en page des listes et des timelines [#452](https://github.com/MTES-MCT/vizeau/issues/452).
    - Correction du troncature des titres [#455](https://github.com/MTES-MCT/vizeau/issues/455).
    - Correction de l'affichage des couleurs dans la répartition des cultures [#431](https://github.com/MTES-MCT/vizeau/issues/431).
    - Correction de l'affichage des unités pour l'évolution des parcelles bio (passage de % à ha) [#428](https://github.com/MTES-MCT/vizeau/issues/428).

### Évolutions techniques
- **Infrastructure & CI/CD :**
    - Passage de la CI à Node 24.
    - Mise à jour des variables d'environnement de la CI.
- **Architecture & Code :**
    - Refactorisation des filtres de projet [#435](https://github.com/MTES-MCT/vizeau/issues/435).
    - Raccourcissement des imports relatifs des types.
    - Séparation de la gestion des étapes de projet dans un contrôleur dédié.
    - Migration des modèles et services de gestion des étapes de projet.
    - Utilisation du composant `CustomTag` dans `ProjetInfosCard`.
- **Tests :**
    - Amélioration des tests et correction de bugs dans les tests unitaires.
    - Correction des tests liés à l'assignation des territoires.
    - Correction des tests liés à la création de projet.
    - Ajout de tests pour le service AAC.
    - Amélioration de la gestion d'erreur lors de l'export CSV.

### Autres changements
- Ajout de la documentation pour la commande de réinitialisation du mot de passe.
- Mise à jour de la documentation de migration en production.
- Suppression des props inutiles dans certains composants.
- Centralisation de la gestion des flash messages.
- Corrections de linter et de style.
- Corrections orthographiques.
