## Changelog : standards-front (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment une nouvelle vue pour les incubateurs avec des informations plus complètes et une présentation plus claire. Des optimisations techniques ont également été réalisées pour améliorer la stabilité et la maintenance du code.

### Évolutions fonctionnelles
- Ajout d'une vue dédiée aux incubateurs, affichant le nombre de services actifs et d'évaluations. [#185](https://github.com/betagouv/standards-front/pull/185)
- Amélioration de la présentation des incubateurs avec l'utilisation d'un tableau.
- Formatage amélioré de la date de la dernière phase d'un incubateur.
- Simplification du menu principal.
- Suppression de la formulation redondante dans les résumés d'évaluation.
- Amélioration de la page de résumé avec des informations de démarrage supplémentaires et une présentation plus concise.
- Introduction d'une liste de composants pour une meilleure organisation de l'information.

### Évolutions techniques
- Mise à jour de la gem `espace_membre-ruby` pour corriger des tests instables et intégrer le code `user.teams`.
- Mise à jour de la gem `dsfr-view-components` vers une version plus récente.
- Introduction du composant `DsfrTableComponent` pour faciliter la création de tableaux.
- Refactorisation des fichiers de locale pour une meilleure organisation.
- Ajout de la gem `rack-mini-profiler` pour le profilage des performances.
- Mise à jour de la gem `betagouv-cucumber-steps` pour partager les étapes Cucumber.
- Mise à jour de la configuration pour utiliser les nouvelles URLs de staging.
- Mise à jour du schéma de la base de données `espace membre`.
- Inclusion explicite de la gem `grape`.

### Autres changements
- Nettoyage du code et suppression de messages inutiles.
- Configuration pour ignorer les messages Zeitwerk liés à `espace_membre-ruby`.
- Mise à jour de la gem `espace_membre-ruby` pour éviter des tests aléatoires.
- Correction de bugs mineurs et améliorations de la stabilité.
