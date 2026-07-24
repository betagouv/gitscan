## Changelog : hyyypertool (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'interface utilisateur de la page utilisateur, notamment en rendant les informations plus compactes et en ajoutant des indicateurs visuels. Des restrictions d'accès ont également été mises en place pour les utilisateurs visiteurs afin de renforcer la sécurité. Plusieurs mises à jour de dépendances ont été effectuées pour assurer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- Ajout d'une colonne "Externe" avec un indicateur visuel (✅/❌) dans le tableau des organisations de la page utilisateur.
- Ajout de badges avec des émojis affichant le nombre d'éléments (organisations, modérations, connexions) dans les sections de la page utilisateur.
- Ajout d'une colonne "Type de vérification" dans le tableau des organisations.
- Les sections d'organisations, de modérations et d'historique OIDC de la page utilisateur sont désormais repliables pour une meilleure lisibilité.
- Restriction de l'accès aux actions de modération et d'édition pour les utilisateurs visiteurs.
- Possibilité d'éditer le motif de refus dans la modale de refus.

### Évolutions techniques
- Extraction du composant d'actions sur les membres de la table d'une organisation pour une réutilisation accrue.
- Mise à jour de plusieurs dépendances, incluant TypeScript, Cypress, Hono, et divers paquets Sentry.
- Mises à jour des paquets de construction et de déploiement (actions GitHub).

### Autres changements
- Documentation mise à jour.
- Mises à jour mineures de configuration et de dépendances.
- Corrections de bugs mineurs.
