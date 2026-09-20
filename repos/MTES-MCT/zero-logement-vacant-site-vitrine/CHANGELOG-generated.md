## Changelog : zero-logement-vacant-site-vitrine (30 derniers jours, au 17 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité des accès via l'authentification à deux facteurs et sur l'amélioration de la flexibilité pour les éditeurs. Les capacités de personnalisation des contenus (blocs d'articles, résultats de recherche) ont été enrichies pour offrir une plus grande liberté de mise en page.

### Évolutions fonctionnelles
- **Sécurisation des accès** : Mise en place de l'authentification à deux facteurs (2FA) avec l'ajout d'une notification dans l'interface d'administration pour inciter les utilisateurs à l'activer [#516](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/516) et améliorations associées [#592](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/592).
- **Flexibilité éditoriale** : 
    - Personnalisation du bloc "Articles récents" (Blog/Événements) permettant de modifier le texte du bouton de redirection et de lier vers des listes d'articles filtrées [#542](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/542).
    - Introduction de nouveaux points d'ancrage (hooks) pour permettre la personnalisation des résultats de recherche [#561](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/561).
- **Corrections de bugs** :
    - Résolution d'un problème sur les pages d'index du catalogue où la suppression du dernier filtre ne mettait pas à jour les résultats [#578](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/578).
    - Correction de classes CSS sur les formulaires [#569](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/569).

### Évolutions techniques
- **Qualité et sécurité du code** : Intégration de nouveaux outils d'analyse automatique pour renforcer la sécurité et la cohérence du projet (Bandit, Deptry et vérification de malwares via `uv`) [#583](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/583), [#582](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/582).
- **Optimisation des tests** : 
    - Accélération de l'exécution de la suite de tests en supprimant les éléments superflus [#574](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/574).
    - Ajout de tests pour le composant `toggle_url_filter` [#546](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/546).
- **Infrastructure et configuration** : Mise à jour de la gestion des dépendances et ajout de nouvelles variables d'environnement.

### Autres changements
- **Documentation** : Centralisation et réorganisation de la documentation technique via le moteur Sphinx [#558](https://github.com/MTES-MCT/zero-logement-vacant-site-vitrine/issues/558).
- **Maintenance** : Ajustements mineurs de la rédaction et du formatage des textes.
