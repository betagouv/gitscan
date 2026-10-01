## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 30 septembre 2026)

### Résumé
Cette période a été marquée par une refonte majeure de l'interface de consultation des réalisations, offrant désormais une navigation fluide entre une vue cartographique et une vue tableau. Parallèlement, un effort important a été consacré au renforcement de la sécurité de l'application et à l'extension du modèle de données pour permettre une gestion plus fine des projets.

### Évolutions fonctionnelles
- **Nouvelle interface de consultation des réalisations** : possibilité de basculer entre une vue carte et une vue tableau ([#52](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/52)).
- **Améliorations de la vue carte** : ajout de nouveaux marqueurs, affichage d'un panneau de détails au clic sur un point, et ajout d'un mode d'affichage en niveaux de gris.
- **Améliorations de la vue tableau** : intégration de la pagination, affichage des dates de réalisation et ajout d'info-bulles pour plus de clarté.
- **Navigation et filtrage** : amélioration de l'expérience de recherche (UX), ajout d'un bouton de réinitialisation des filtres et gestion des paramètres d'URL pour faciliter le partage de vues filtrées.
- **Gestion de projet** : possibilité de visualiser et de mettre à jour le périmètre directement depuis la page de présentation du projet.

### Évolutions techniques
- **Renforcement de la sécurité** :
    - Protection contre les failles de type IDOR (accès non autorisé à des données via l'ID) sur les réalisations et les mises à jour de périmètre.
    - Sécurisation des téléchargements (uploads) via l'utilisation de chemins aléatoires non prévisibles.
    - Restriction de l'accès à l'endpoint de cartographie (MAP) aux seuls utilisateurs authentifiés.
    - Durcissement des contrôles d'accès sur les vues de réalisations via un Mixin de sécurité commun.
- **Architecture et Modèle de données** :
    - Extension du modèle "Projet" par une relation 1-1, permettant d'ajouter des données spécifiques sans alourdir le modèle principal.
    - Automatisation de la création des instances de ce nouveau modèle lors de la création d'un projet.
    - Refactorisation de la gestion des composants (filtres, panneaux) et des flux de données.
- **Version** : Passage à la version 0.3.0.

### Autres changements
- Nettoyage du code et corrections de fautes de frappe.
- Optimisation des tests unitaires.
