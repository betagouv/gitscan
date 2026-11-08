## Changelog : referentiel-applications (30 derniers jours, au 06 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction de la synchronisation GristSync en version bêta et le déploiement de nouveaux outils de communication, tels que les résumés quotidiens par email et les rappels de sécurité. L'accent a également été mis sur l'amélioration de l'accessibilité (RGAA) et la fiabilité des exports de données, tout en renforçant la sécurité globale de la plateforme.

### Évolutions fonctionnelles
- **Notifications et communication** : ajout de filtres par type d'événement [#3188], mise en place de rappels pour l'expiration des jetons [#3177] et amélioration de la visibilité des notifications non lues pour les lecteurs d'écran [#3045].
- **Exports de données** : amélioration de la fiabilité et du contenu des exports Excel (inclusion du statut actuel, gestion des sessions et des listes d'applications) [#3082, #3092, #3171, #3150] et introduction des exports HTML en version bêta [#3042].
- **Expérience utilisateur (UX)** : mise en place d'une protection contre la perte de données lors de la navigation (confirmation de sortie si des changements ne sont pas enregistrés) [#3195], gestion des logos pour les applications [#3086] et renommage des filtres personnels [#3104].
- **Accessibilité (A11y)** : mises à jour importantes pour la conformité RGAA, incluant une meilleure gestion du focus dans les tableaux et des annonces pour les lecteurs d'écran lors du chargement [#2875, #3037, #3007, #3081].
- **Nouvelles fonctionnalités** : lancement de la synchronisation GristSync en mode bêta [#2876, #3190] et mise en place d'un service de résumé quotidien par email [#3098].
- **Recherche et filtrage** : amélioration de la recherche globale (respect des permissions technologiques) [#3176] et restauration de la recherche par source de données [#3055].

### Évolutions techniques
- **Sécurité** : renforcement de la gestion des jetons (validation des claims JWT, jetons applicatifs) [#3039, #3199, #3043], masquage des jetons API dans les logs HTTP [#3018] et correction de plusieurs vulnérabilités sur les dépendances et les images Docker [#3102, #3088, #3080, #2898].
- **Architecture et Backend** : implémentation d'un service de verrouillage pour gérer les conflits lors des synchronisations GristSync [#3087], amélioration des filtres de relation [#3197] et gestion fine des capacités pour les fonctionnalités bêta [#3034].
- **CI/CD et Infrastructure** : optimisation de la publication des images lors de la création de releases [#3079].

### Autres changements
- **Documentation** : transfert des décisions d'architecture dans le dossier `docs` [#3089] et documentation des processus de corrélation [#2922].
