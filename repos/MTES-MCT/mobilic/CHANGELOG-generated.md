## Changelog : mobilic (30 derniers jours, au 08/09/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'introduction des notifications push et l'amélioration du parcours de création de mission. Les outils de suivi des activités et des statistiques ont également été affinés pour garantir une meilleure précision des données et une expérience utilisateur plus fluide.

### Évolutions fonctionnelles
- **Notifications & PWA** : Mise en place des notifications push [#920](https://github.com/MTES-MCT/mobilic/pull/920) et optimisation de l'affichage (gestion de la langue française dans le manifeste, ajustement de la largeur des barres de notification et amélioration du défilement).
- **Gestion des missions** : Accès direct au tunnel de création de mission depuis le menu de navigation et amélioration de la redirection automatique après la création d'une mission.
- **Suivi des activités** : Introduction de la fonctionnalité de division d'activité (split) [#930](https://github.com/MTES-MCT/mobilic/pull/930) et correction de l'affichage des libellés d'activité dans l'historique.
- **Statistiques & Données** : Correction du calcul des statistiques de mission en excluant les activités rejetées [#927](https://github.com/MTES-MCT/mobilic/pull/927) et mise à jour des références légales concernant la définition de la semaine civile.
- **Expérience utilisateur (UX)** : Amélioration de la saisie des dates (auto-focus optimisé) et désactivation du bouton de sauvegarde lorsque le texte de la bannière n'a pas été modifié.

### Évolutions techniques
- **Architecture** : Généralisation du contexte d'actions (`ActionsContext`) pour assurer sa disponibilité sur l'ensemble de l'application et non plus seulement sur la partie `/app` [#949](https://github.com/MTES-MCT/mobilic/pull/949).
- **Fiabilité & Monitoring** : Amélioration de la capture des erreurs de jeton de rafraîchissement (refresh token) dans Sentry [#914](https://github.com/MTES-MCT/mobilic/pull/914) et résolution de problèmes d'écran blanc lors du chargement ou du déploiement de la PWA.
- **Qualité du code** : Traitement des alertes SonarCloud concernant la qualité du code (code smells) et l'accessibilité.
- **Infrastructure & CI/CD** : Optimisation des environnements de revue (review apps) et ajustement des permissions des workflows de déploiement [#919](https://github.com/MTES-MCT/mobilic/pull/919).
