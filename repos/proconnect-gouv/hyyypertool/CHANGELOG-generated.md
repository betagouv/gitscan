## Changelog : hyyypertool (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'interface utilisateur de la page utilisateur, notamment en rendant les informations plus compactes et en ajoutant des indicateurs visuels. Des restrictions d'accès ont été mises en place pour protéger les données sensibles. Plusieurs mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une colonne "Externe" avec un indicateur visuel (✅/❌) dans le tableau des organisations de la page utilisateur.
- Les sections d'organisations, de modérations et d'historique OIDC de la page utilisateur sont désormais repliables pour une meilleure lisibilité.
- Ajout de badges avec des émojis indiquant le nombre d'éléments dans chaque section de la page utilisateur.
- Ajout d'une colonne "Type de vérification" dans le tableau des organisations.
- Le champ "motif de modération" est de nouveau éditable dans le modal de refus.
- Restriction de l'accès aux actions de modification et de traitement pour les utilisateurs non administrateurs ou modérateurs.
- Masquage de la section des commentaires si aucun commentaire n'est présent.

### Évolutions techniques
- Extraction du composant d'actions des membres de la table d'une organisation vers un composant réutilisable.
- Mise à jour de plusieurs dépendances : `tailwindcss`, `@csmith/release-it-calver-plugin`, `@types/node`, `oxc-parser`, `sentry`, `release-it`, `pg`, `docker/setup-compose-action`, `cypress-io/github-action`, `hono`, `@electric-sql/pglite`, `cypress`, `@preact/signals-core`, `@proconnect-gouv/proconnect.identite.database`, `rate-limiter-flexible`, `actions/checkout`.

### Autres changements
- Documentation mise à jour.
- Corrections mineures et améliorations de la maintenance du code.
