## Changelog : domifa (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité et la performance de la plateforme DomiFa, notamment avec l'ajout d'une authentification à deux facteurs (OTP) et des mesures de limitation de débit. Des améliorations ont également été apportées à l'interface utilisateur et à l'administration, ainsi que des corrections de bugs et des mises à jour techniques.

### Évolutions fonctionnelles
- Ajout d'une authentification à deux facteurs (OTP) pour certains endpoints et pour l'administration, renforçant la sécurité des accès.
- Amélioration de l'interface utilisateur du portail administrateur avec l'ajout d'UUID, l'amélioration de l'UX des dropdowns et des titres de listes.
- Ajout d'une page de témoignages pour le frontend.
- Ajout d'une liste d'utilisateurs dans l'administration.
- Ajout d'un statut pour bloquer les comptes dans le backend.
- Ajout d'un panneau d'information avec des statistiques dans l'administration.
- Ajout d'un détail réseau dans le backend.
- Ajout d'un blocage de bots basé sur l'user-agent.
- Possibilité de débloquer les utilisateurs.
- Ajout d'un banner DSFR.

### Évolutions techniques
- Mise à jour de l'ensemble des frontends vers la version 19 d'Angular.
- Durcissement de la sécurité OTP avec ajout de limitations de débit et de contrôle d'accès.
- Refactoring du code pour l'intégration de statistiques Metabase.
- Amélioration des tests unitaires et correction de bugs associés.
- Ajout de fingerprint dans les sessions pour une meilleure sécurité.
- Force d'une seule session active par utilisateur.
- Ajout de tests pour le blocage d'utilisateurs.

### Autres changements
- Correction de problèmes de linting et de composants autonomes dans l'administration.
- Mise à jour des dépendances et des packages.
- Ajout de la documentation CLAude.md.
- Correction de problèmes liés à la configuration de l'environnement CI.
- Ajout de la directive `[skip ci]` aux messages de commit de semantic-release.
- Correction de bugs mineurs dans l'interface utilisateur et le backend.
- Suppression de Bootstrap dans l'administration.
- Correction de filtres dans le backend.
- Correction de problèmes avec les champs d'upload dans le frontend.
- Correction de problèmes avec les fiches pratiques et les formulaires dans le frontend.
- Ajout de champs requis dans les formulaires du frontend.
- Correction de problèmes DSFR dans le frontend.
- Ajout de tooltips dans l'interface de gestion.
- Ajout d'actualités dans le frontend.
