## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'importation de données depuis Lakaa, l'ajout de fonctionnalités de gestion des réalisations (création, édition, suppression, traçabilité), l'amélioration de l'interface utilisateur (notamment la gestion des photos et des cartes) et l'ajout de notifications pour les administrateurs. Des améliorations de sécurité et de performance ont également été apportées.

### Évolutions fonctionnelles
- **Import Lakaa :** Import initial des données depuis Lakaa (utilisateurs, projets, ressources, réalisations) avec gestion des images et des PDF. L'importation des projets (sites) a été améliorée pour une meilleure localisation et gestion des coordonnées.
- **Gestion des réalisations :**
    - Ajout de la possibilité de créer, éditer et supprimer des réalisations.
    - Restriction de la modification et de la suppression des réalisations à leur auteur.
    - Ajout d'un champ "créé par" pour suivre l'auteur de chaque réalisation.
    - Ajout d'une traçabilité des actions (création, suppression) sur les réalisations.
- **Interface utilisateur :**
    - Amélioration de l'affichage des cartes de réalisation avec une gestion de l'ellipses pour les textes longs.
    - Ajout d'une gestion de galerie de photos avec navigation et affichage modal.
    - Refonte de la présentation des formulaires de réalisation avec ajout d'éléments d'aide et de champs obligatoires.
    - Amélioration du style général des cartes et des formulaires.
- **Notifications :** Ajout de notifications pour les administrateurs lors de la création de nouvelles réalisations ou projets.
- **Fonctionnalités diverses :**
    - Ajout d'un sélecteur de recherche pour les ressources lors de la création d'une réalisation.
    - Ajout d'un bouton pour activer/désactiver des fonctionnalités via un "feature flag".
    - Amélioration de la gestion des onglets actifs.

### Évolutions techniques
- **Refactoring :**
    - Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
    - Utilisation de classes DSFR pour éviter la duplication de code.
    - Optimisation des requêtes SQL pour améliorer les performances (préchargement des relations).
- **Tests :**
    - Ajout de tests unitaires pour les nouvelles fonctionnalités.
    - Refactorisation des tests existants pour une meilleure organisation.
- **Sécurité :**
    - Nettoyage des champs de description pour éviter les failles XSS.
    - Mise en place de permissions pour restreindre l'accès aux réalisations.
- **Infrastructure :**
    - Mise à jour des dépendances.
    - Amélioration du processus de build.

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs.
- Amélioration de la gestion des erreurs.
- Suppression de code inutile.
- Renommage des migrations pour correspondre aux standards du projet.
- Ajout de commentaires dans le code.
- Utilisation de `marksafe` pour la gestion des données HTML.
