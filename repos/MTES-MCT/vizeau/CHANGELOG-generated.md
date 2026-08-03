## Changelog : vizeau (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment la possibilité de partager des projets entre territoires, une migration vers une version plus récente du framework AdonisJS, et des corrections d'autorisations et d'affichage pour une meilleure expérience utilisateur. L'interface utilisateur a également été améliorée avec des corrections de style et de messages d'erreur.

### Évolutions fonctionnelles
- Les projets sont désormais communs aux territoires, facilitant la collaboration et le partage d'informations. [#481](https://github.com/MTES-MCT/vizeau/pull/481)
- Affichage amélioré des messages d'erreur d'authentification pour une meilleure clarté. [#472](https://github.com/MTES-MCT/vizeau/pull/472)
- Correction d'une permission trop stricte empêchant le téléchargement de documents de journal de bord. [#477](https://github.com/MTES-MCT/vizeau/pull/477)
- Les commentaires sur les parcelles sont maintenant privés à chaque utilisateur. [#474](https://github.com/MTES-MCT/vizeau/pull/474)
- Ajout de l'affichage des projets sur la carte. [#467](https://github.com/MTES-MCT/vizeau/pull/467)

### Évolutions techniques
- Migration vers AdonisJS version 7, améliorant la performance et la sécurité de l'application. [#470](https://github.com/MTES-MCT/vizeau/pull/470)
- Utilisation de nouveaux imports de type pour corriger les erreurs de linter.
- Refonte de la structure des contrôleurs et des policies avec l'utilisation de "barrels". [#476](https://github.com/MTES-MCT/vizeau/pull/476)
- Simplification des modèles de données.
- Mise à jour du routeur pour une meilleure gestion des routes. [#478](https://github.com/MTES-MCT/vizeau/pull/478)

### Autres changements
- Amélioration du style de la page d'accueil avec de nouveaux composants UI et une réduction de la taille des illustrations. [#480](https://github.com/MTES-MCT/vizeau/pull/480) et [#479](https://github.com/MTES-MCT/vizeau/pull/479)
- Correction de divers problèmes de linter et de prettier. [#473](https://github.com/MTES-MCT/vizeau/pull/473)
- Amélioration du message d'erreur affiché à l'utilisateur. [#462](https://github.com/MTES-MCT/vizeau/pull/462)
- Mise à jour des dépendances (TailwindCSS, npm).
