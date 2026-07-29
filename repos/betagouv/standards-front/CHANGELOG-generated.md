## Changelog : standards-front (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives, notamment l'ajout d'une vue pour les incubateurs, une simplification de l'interface utilisateur et des mises à jour techniques pour améliorer la stabilité et la compatibilité avec les services externes. L'objectif est de faciliter l'audit des produits numériques selon les standards de beta.gouv.fr.

### Évolutions fonctionnelles
- **Incubateurs :** Ajout d'une nouvelle vue permettant de visualiser les incubateurs, avec le nombre de services et d'évaluations actives. [#185](https://github.com/betagouv/standards-front/pulls/185)
- **Tableaux :** Introduction d'un composant de tableau DSFR (DsfrTableComponent) pour améliorer l'affichage des données tabulaires et permettre la personnalisation des légendes.
- **Interface utilisateur :** Simplification du menu principal et amélioration de la présentation de la liste des incubateurs avec un affichage en tableau.
- **Informations de démarrage :** Amélioration de la page de résumé pour afficher des informations de démarrage plus claires et une liste des composants. [#190](https://github.com/betagouv/standards-front/pulls/190)

### Évolutions techniques
- **Dépendances :** Mises à jour de plusieurs dépendances, incluant `grape`, `solid_queue`, `actions/checkout`, `actions/cache`, `dsfr-view-components` et `espace_membre-ruby`.
- **Configuration :** Mise à jour des URLs de staging et configuration pour ignorer les messages Zeitwerk liés à `espace_membre-ruby`.
- **Espace Membre :** Intégration et mise à jour de la gem `espace_membre-ruby` pour supporter le code `user.teams` et améliorer la compatibilité avec la base de données.
- **Tests :** Mise à jour de la gem `betagouv-cucumber-steps` pour partager les étapes Cucumber.
- **Rack Mini Profiler :** Ajout de la gem `rack-mini-profiler` pour faciliter le profilage des performances.

### Autres changements
- **Locales :** Refactorisation des fichiers de localisation pour une meilleure organisation.
- **Nettoyage de code :** Suppression de texte superflu dans l'affichage des évaluations.
- **Documentation :** Amélioration de la documentation interne et des commentaires.
