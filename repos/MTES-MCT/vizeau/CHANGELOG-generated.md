## Changelog : vizeau (30 derniers jours, au 25 juin 2026)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations concernant la gestion des projets, notamment l'ajout d'étapes de projet avec gestion de documents, une nouvelle page "Mes territoires" et des avancées sur la création et l'édition de projets. Des corrections et optimisations diverses ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Gestion des projets :**
    - Ajout de la gestion des étapes de projet, permettant de définir des jalons et d'y associer des documents. [#457](https://github.com/MTES-MCT/vizeau/issues/457), [#456](https://github.com/MTES-MCT/vizeau/issues/456), [#453](https://github.com/MTES-MCT/vizeau/issues/453), [#451](https://github.com/MTES-MCT/vizeau/issues/451)
    - Possibilité d'éditer les projets existants. [#447](https://github.com/MTES-MCT/vizeau/issues/447), [#441](https://github.com/MTES-MCT/vizeau/issues/441)
    - Création d'un formulaire de création de projet. [#436](https://github.com/MTES-MCT/vizeau/issues/436)
    - Ajout d'une page "Mes territoires" pour faciliter la gestion des territoires associés à l'utilisateur. [#426](https://github.com/MTES-MCT/vizeau/issues/426)
- **Exploitations agricoles :**
    - Possibilité d'assigner un AAC (Autorisation d'activité agricole) à une exploitation lors de sa création. [#439](https://github.com/MTES-MCT/vizeau/issues/439), [#440](https://github.com/MTES-MCT/vizeau/issues/440)
- **Interface utilisateur :**
    - Ajout d'un bouton de navigation vers la sélection de parcelles. [#452](https://github.com/MTES-MCT/vizeau/issues/452)
    - Amélioration de la gestion des titres tronqués. [#455](https://github.com/MTES-MCT/vizeau/issues/455)
    - Correction de l'affichage des couleurs dans la répartition des cultures. [#431](https://github.com/MTES-MCT/vizeau/issues/431)

### Évolutions techniques
- **Infrastructure :**
    - Mise à jour de la version de Node.js en CI à la version 24. [#432](https://github.com/MTES-MCT/vizeau/issues/432)
- **Codebase :**
    - Refactorisation des filtres de projets. [#435](https://github.com/MTES-MCT/vizeau/issues/435)
    - Raccourcissement des imports relatifs des types. [#442](https://github.com/MTES-MCT/vizeau/issues/442)
    - Amélioration de la gestion d'erreur lors de l'export CSV. [#434](https://github.com/MTES-MCT/vizeau/issues/434)
    - Séparation de la gestion des étapes de projet dans un contrôleur dédié.
    - Validation du payload dans le validateur des étapes de projet.
- **Tests :**
    - Corrections et améliorations des tests unitaires.

### Autres changements
- Ajout d'une commande CLI pour réinitialiser le mot de passe d'un utilisateur. [#433](https://github.com/MTES-MCT/vizeau/issues/433)
- Mise à jour de la documentation de migration en production. [#433](https://github.com/MTES-MCT/vizeau/issues/433)
- Suppression des flash messages inutiles.
- Corrections diverses et amélioration du code suite aux revues.
- Ajout de commentaires et documentation.
