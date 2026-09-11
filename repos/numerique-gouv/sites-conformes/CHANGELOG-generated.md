## Changelog : sites-conformes (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, l'accent a été mis sur le renforcement de la sécurité avec l'introduction de l'authentification à deux facteurs (2FA) et sur l'amélioration de la flexibilité de gestion de contenu pour les blogs et événements. La documentation a également été largement restructurée pour offrir une meilleure expérience de consultation.

### Évolutions fonctionnelles
- **Sécurité** : Mise en place et amélioration de l'authentification à deux facteurs (2FA) pour sécuriser l'accès ([#516](https://github.com/numerique-gouv/sites-conformes/pull/516), [#592](https://github.com/numerique-gouv/sites-conformes/pull/592)).
- **Gestion de contenu** : Le bloc "Articles récents" pour les blogs et événements est désormais plus flexible, permettant de personnaliser le texte du bouton de redirection et de lier vers des listes filtrées ([#542](https://github.com/numerique-gouv/sites-conformes/pull/542)).
- **Corrections de bugs** : 
    - Résolution d'un problème sur les pages d'index de catalogue où la suppression du dernier filtre ne mettait pas à jour les résultats ([#578](https://github.com/numerique-gouv/sites-conformes/pull/578)).
    - Correction du rendu des classes CSS dans les formulaires ([#569](https://github.com/numerique-gouv/sites-conformes/pull/569)).

### Évolutions techniques
- **Expérience développeur** : Ajout de hooks simplifiés pour permettre la personnalisation des résultats de recherche ([#561](https://github.com/numerique-gouv/sites-conformes/pull/561)).
- **Qualité et Sécurité du code** : 
    - Intégration de nouveaux outils d'analyse statique et de cohérence : Bandit pour la sécurité ([#583](https://github.com/numerique-gouv/sites-conformes/pull/583)), Deptry pour la gestion des dépendances ([#582](https://github.com/numerique-gouv/sites-conformes/pull/582)) et vérification de malwares via `uv`.
- **Tests et CI/CD** : 
    - Optimisation de la vitesse d'exécution des tests ([#574](https://github.com/numerique-gouv/sites-conformes/pull/574)).
    - Ajout de nouveaux tests de couverture, notamment pour les tags de templates ([#546](https://github.com/numerique-gouv/sites-conformes/pull/546)).

### Autres changements
- **Documentation** : Centralisation et réorganisation complète de la documentation technique via le moteur Sphinx pour une meilleure navigation ([#558](https://github.com/numerique-gouv/sites-conformes/pull/558)).
