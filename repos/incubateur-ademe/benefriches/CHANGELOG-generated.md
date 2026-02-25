## Changelog : benefriches (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur la refonte du processus de création de projets urbains, en améliorant l'expérience utilisateur et en optimisant le code. Des améliorations ont également été apportées aux tests automatisés et à l'infrastructure de développement. Plusieurs corrections de bugs et ajustements de texte ont été effectués pour améliorer la clarté et la précision de l'application.

### Évolutions fonctionnelles

- Amélioration du flux de création de projets urbains : ajout de nouveaux types d'usages, simplification des étapes et amélioration de la sélection des espaces. (#20aa39c, #44a3f28, #dd0d369, #945ee20, #0d865db)
- Ajout de pictogrammes pour les nouveaux usages urbains. (#9c399c9)
- Possibilité de supprimer des projets depuis la page "Mes évaluations". (#bef2355)
- Ajout de menus d'actions sur les tuiles de projets et de sites. (#08f10e2)
- Affichage du séparateur de milliers pour les montants monétaires. (#032146a)
- Amélioration de la gestion des espaces naturels et des types de sols dans le formulaire de création de projet. (#17cdc68, #4964b57, #95b6e9d, #bbf788e, #69e588d)
- Correction de l'étiquetage des sols imperméables et perméables. (#95b6e9d)
- Suppression du lien vers le DVF dans le formulaire de revenus de la revente de site. (#4bfffc8)
- Ajout de dialogues de blocage de navigation sur les formulaires de création de site et de projet. (#7f91806)
- Mise à jour des libellés du stepper de création de projet. (#fea9805)

### Évolutions techniques

- Refactorisation importante du code lié à la création de projets urbains, avec une meilleure organisation des fichiers et une simplification de la logique. (#3e6f6ed, #a5521dc, #8b886a6, #9b55666, #f5f5d45, #bcc84f4, #c305a91, #24f13a1, #7735097, #4bfffc8, #09288e0, #c20f527, #ff311a4, #f84ecef, #7698b54, #880fc09, #649e03c, #e02a866, #20aa39c, #dd0d369, #945ee20, #0d865db)
- Amélioration de l'installation des dépendances dans le script `create-worktree.sh`. (#9d2d66d)
- Simplification du build Scalingo. (#1d47c9d)
- Mise à jour des dépendances (oxlint, prettier, etc.). (#5fe1745, #e4254ff, #d6a54f7, #dc4dc76)
- Refactorisation de l'authentification avec l'utilisation de DTOs partagés. (#fc015f1, #a6a2f98)
- Amélioration de la gestion des tests E2E avec la création d'un client API et l'ajout de tests initiaux. (#eb9b03c, #c355aa6, #2716d6d, #b639a32)
- Ajout de skills et d'agents pour l'automatisation de la revue de code et des migrations de base de données avec Claude. (#c20f527, #ff311a4, #4c72e0f, #b058552)

### Autres changements

- Mise à jour de la documentation pour refléter les changements apportés. (#c68670b, #69e588d)
- Suppression de code mort. (#53b3b80)
- Correction de typos et amélioration de la formulation. (#4dcf4cf, #efbee4d, #7cc190f, #4eac594)
- Mise à jour de la commande pour démarrer le serveur API en développement. (#65abc2c)
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
