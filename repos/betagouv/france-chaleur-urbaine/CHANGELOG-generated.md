## Changelog : france-chaleur-urbaine (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page de résultat et le formulaire de demande, avec un focus particulier sur l'intégration de nouvelles sources de données (BRGM, BDNB, RNB) et l'optimisation du parcours pour les demandes de chaleur renouvelable. Des améliorations techniques ont également été apportées pour la gestion des données, la performance et la maintenance du code.

### Évolutions fonctionnelles
- **Chaleur Renouvelable :** Amélioration du parcours utilisateur pour les demandes de chaleur renouvelable, incluant la pré-sélection de bâtiments via le RNB, l'ajout de commentaires, et la gestion des statuts de demande.
- **Formulaire de contact :** Personnalisation du formulaire de contact en fonction du profil de l'utilisateur et alternative proposée en cas d'inéligibilité au réseau de chaleur.
- **Comparateur PAC :** Intégration et refactorisation de l'API du comparateur de pompes à chaleur.
- **Interface utilisateur :**
    - Redesign du bloc FranceRenov.
    - Amélioration de l'affichage mobile de diverses sections.
    - Ajout d'effets visuels (survol) sur les bâtiments et les éléments interactifs.
    - Amélioration de la qualité des images et de l'affichage des tooltips.
    - Ajout d'icônes et d'améliorations graphiques diverses.
- **Tableau de bord administrateur :**
    - Ajout d'un méga-menu pour une meilleure organisation.
    - Réorganisation du dashboard avec toutes les pages administratives.
    - Possibilité de filtrer et trier les données dans les tableaux.
    - Gestion des étiquettes utilisateurs (tags) pour faciliter l'organisation et la recherche.
    - Ajout de la gestion des organisations et de l'API v2 associée.
- **Autres :**
    - Ajout de la gestion du maitre d'ouvrage pour les réseaux en construction.
    - Amélioration de la gestion des accès aux demandes pour les administrateurs.

### Évolutions techniques
- **API :** Refactorisation de l'API PAC et initialisation de l'API IFPEN (maintenant PAC).
- **Base de données :** Ajout de nouvelles colonnes dans les tables `batenr` et `demands_chaleur_renouvelable` pour supporter les nouvelles fonctionnalités.
- **Tests :** Ajout et mise à jour de tests unitaires et d'intégration, incluant l'utilisation de Playwright et Cypress.
- **Performance :** Amélioration des performances du tableau des demandes.
- **Dépendances :** Mise à jour du package `publicodes`.
- **Architecture :**
    - Utilisation de Dialog au lieu de Modal.
    - Refactoring du code pour une meilleure séparation des responsabilités.
    - Utilisation de composants UI réutilisables.
- **CI/CD :** Configuration des MCP (machines configurées pour les tests) pour Playwright et PostgreSQL.

### Autres changements
- Nettoyage du code et suppression de code obsolète.
- Mise à jour de la documentation.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Suppression de l'intégration Pipedrive et des notifications emails pour l'équipe FCU.
- Gestion améliorée des cookies et des erreurs.
- Suppression de l'AB test pour la collecte de contacts utilisateurs.
