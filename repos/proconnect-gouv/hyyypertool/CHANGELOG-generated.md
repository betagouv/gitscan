## Changelog : hyyypertool (30 derniers jours, au 2026-07-17)

### Résumé
Les dernières mises à jour de Hyyypertool améliorent l'expérience utilisateur en ajoutant des informations plus claires sur les organisations et les modérations, notamment avec des badges de comptage et des colonnes dédiées. Des restrictions d'accès ont également été mises en place pour renforcer la sécurité et adapter l'interface aux différents rôles utilisateurs. Enfin, des améliorations techniques et des mises à jour de dépendances ont été effectuées pour assurer la stabilité et la performance de l'outil.

### Évolutions fonctionnelles
- Ajout d'une colonne "Interne" avec un indicateur ✅/❌ dans le tableau des organisations de la page utilisateur.
- Ajout de badges avec des émojis affichant le nombre d'éléments (organisations, modérations, connexions) dans les sections de la page utilisateur.
- Ajout d'une colonne "Type de vérification" dans le tableau des organisations.
- Possibilité d'éditer le motif de refus dans la modale de refus.
- Masquage du bouton de retraitement pour les utilisateurs visiteurs.
- Masquage des actions d'édition pour les utilisateurs visiteurs.
- Masquage de la section commentaires si aucun commentaire n'est présent.
- Restriction des écritures en base de données aux rôles administrateur et modérateur.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `tailwindcss`, `@preact/signals`, `typescript`, `cypress`, `hono`, `oxc-parser`, `sentry`, `release-it`, `@types/node`, `rate-limiter-flexible`, `actions/checkout`, `@proconnect-gouv/proconnect.identite.database`.
- Extraction du composant `MemberRowActions` pour une meilleure réutilisabilité.
- Amélioration de la structure de la page utilisateur avec des sections repliables via `<details>` et `<summary>`.

### Autres changements
- Publication des versions 2026.7.2, 2026.7.1 et 2026.7.0.
- Documentation mise à jour.
