## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 14/10/2026)

### Résumé
Cette période a été marquée par une refonte majeure de l'interface de consultation des réalisations, permettant désormais de basculer facilement entre une vue cartographique et une vue tableau. L'expérience utilisateur a été enrichie par l'ajout de nouveaux filtres (notamment par périmètre) et une gestion simplifiée de la publication des brouillons. Parallèlement, des mesures importantes ont été prises pour renforcer la sécurité de l'application.

### Évolutions fonctionnelles
- **Nouvelle interface de consultation** : Ajout de la possibilité de basculer entre une vue carte et une vue tableau pour les réalisations [#52](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/52).
- **Amélioration de la cartographie** : 
    - Ajout d'un panneau de détails lors du clic sur un marqueur.
    - Ajout d'un sélecteur de nuances de gris pour la carte.
    - Intégration d'une liste de sites dans un panneau dédié.
- **Nouveaux outils de recherche** : 
    - Mise en place d'un filtre par périmètre [#56](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/56).
    - Ajout d'un bouton pour réinitialiser les filtres de recherche.
- **Optimisation du workflow** : Possibilité de publier un brouillon de réalisation directement depuis la liste des réalisations.
- **Améliorations de l'interface (UI/UX)** : 
    - Correction de l'affichage des en-têtes de tableaux.
    - Ajout de textes d'aide et amélioration de la clarté des libellés.
    - Harmonisation du design global de l'application.

### Évolutions techniques
- **Renforcement de la sécurité** : 
    - Protection contre les accès non autorisés aux données (correction de failles IDOR sur les réalisations).
    - Sécurisation des chemins de téléchargement de fichiers (chemins aléatoires).
    - Restriction de l'accès aux points de terminaison de la carte pour les utilisateurs anonymes.
- **Évolution de l'architecture** : Introduction d'un nouveau modèle en relation 1-1 avec les projets pour permettre l'extension de données spécifiques.
- **Optimisation du code** : 
    - Refonte du système de filtrage via l'utilisation de `django-filter`.
    - Amélioration de la gestion de la pagination.
    - Ajout du filtrage par périmètre au niveau de l'API.

### Autres changements
- **Maintenance** : Passage à la version 0.6.0 du plugin.
- **Rédaction** : Travail de réécriture des textes pour améliorer la compréhension de l'interface [#62](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/62).
