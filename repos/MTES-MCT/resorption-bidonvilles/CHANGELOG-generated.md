## Changelog : resorption-bidonvilles (30 derniers jours, au 06 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment autour de la gestion des adresses des Établissements Temporaires d'Hébergement (ETI) et de l'historique des actions. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Enfin, l'intégration de nouveaux indicateurs de suivi de la résorption des bidonvilles a été initiée.

### Évolutions fonctionnelles
- **Gestion des ETI :**
    - Synchronisation des coordonnées lors du changement d'adresse d'une ETI.
    - Ajustement automatique du zoom de la carte pour afficher toutes les ETI.
    - Ajout d'un tag "En cours de résorption" sur la liste des sites existants.
    - Possibilité de saisir et d'afficher plusieurs adresses pour une même ETI.
    - Validation de l'adresse obligatoire lorsque le type de localisation est "ETI".
    - Amélioration de l'affichage de l'historique des adresses et des sites.
- **Historique des actions :**
    - Implémentation de l'historique des actions, incluant l'affichage des modifications et des informations contextuelles.
    - Affichage des thématiques sur plusieurs lignes dans l'historique.
    - Ajout de filtres par année de financement DIHAL.
    - Affichage de l'année de financement DIHAL dans un badge.
- **Indicateurs de suivi :**
    - Ajout d'indicateurs de mise à jour de la population sur 3 mois.
    - Intégration de ces indicateurs dans l'email récapitulatif hebdomadaire.
- **Améliorations générales :**
    - Correction de la formulation des taux de mises à jour.
    - Correction de l'affichage de plusieurs erreurs simultanées.

### Évolutions techniques
- **Refactoring :**
    - Simplification et nettoyage du code, notamment dans les composants liés à la gestion des adresses ETI et à l'historique des actions.
    - Suppression de code redondant et d'imports inutiles.
    - Utilisation de types plus précis et de fonctions utilitaires partagées.
- **Infrastructure :**
    - Pré-bundle des librairies nécessaires pour Nuxt 4.
    - Mise à jour de l'URL de Matomo pour utiliser un lien proxifié.
- **Tests :**
    - Ajout de tests unitaires pour certaines fonctionnalités.
- **Sécurité :**
    - Correction de potentielles failles d'injection.
    - Amélioration de la validation des données.

### Autres changements
- Correction de bugs mineurs et améliorations de la lisibilité du code.
- Mise à jour de la documentation.
- Correction de problèmes de linting.
- Amélioration de la gestion des erreurs.
- Suppression de logs inutiles.
- Renommage de certains filtres et composants pour une meilleure clarté.
