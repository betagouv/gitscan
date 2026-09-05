## Changelog : mobilic (30 derniers jours, au 4 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure avec l'introduction des notifications push et une gestion améliorée des campagnes de communication. L'expérience utilisateur a été fluidifiée, notamment lors de la création de missions et de la saisie des données personnelles, tandis que la stabilité de l'application (PWA) et la précision des statistiques ont été renforcées.

### Évolutions fonctionnelles
- **Notifications** : Mise en place des notifications push, gestion des campagnes de communication et ajout d'une bannière d'acceptation (opt-in) pour les utilisateurs. [#920](https://github.com/MTES-MCT/mobilic/pull/920)
- **Navigation & UX** : 
    - Simplification du parcours de création de mission, désormais accessible directement depuis le menu de navigation et avec une redirection optimisée. [#938](https://github.com/MTES-MCT/mobilic/pull/938)
    - Amélioration de la saisie des dates de naissance grâce à un système d'autofocus et une validation plus intuitive. [#924](https://github.com/MTES-MCT/mobilic/pull/924)
- **Historique & Activités** : 
    - Optimisation de l'affichage des libellés d'activité dans l'historique et meilleure gestion des activités fractionnées (split). [#944](https://github.com/MTES-MCT/mobilic/pull/944), [#930](https://github.com/MTES-MCT/mobilic/pull/930)
    - Correction de l'affichage du bouton "Conduite" en mode PWA lorsque des tâches alternatives sont autorisées. [#44b1af77](https://github.com/MTES-MCT/mobilic/commit/44b1af77)
- **Conformité & Partenaires** : 
    - Correction de la référence légale concernant la définition de la semaine civile. [#939](https://github.com/MTES-MCT/mobilic/pull/939)
    - Ajustement du calcul des statistiques de mission pour exclure les activités rejetées. [#927](https://github.com/MTES-MCT/mobilic/pull/927)
    - Ajout du logo Rota dans la section des partenaires (logiciels autorisés). [#940](https://github.com/MTES-MCT/mobilic/pull/940)

### Évolutions techniques
- **Architecture & PWA** : 
    - Rendre le contexte d'actions (`ActionsContext`) disponible globalement pour stabiliser l'application. [#949](https://github.com/MTES-MCT/mobilic/pull/949)
    - Résolution de problèmes d'écran blanc lors du chargement de l'application suite à un déploiement (gestion du cache PWA). [#12d012bc](https://github.com/MTES-MCT/mobilic/commit/12d012bc)
- **Observabilité & CI/CD** : 
    - Amélioration de la capture des erreurs de jeton de rafraîchissement (refresh token) dans Sentry. [#914](https://github.com/MTES-MCT/mobilic/pull/914)
    - Corrections sur les environnements de revue (review apps) et les permissions de workflow. [#3bdb6788](https://github.com/MTES-MCT/mobilic/commit/3bdb6788)
- **Qualité de code** : Intégration des recommandations SonarCloud et améliorations de l'accessibilité. [#b15cd3dd](https://github.com/MTES-MCT/mobilic/commit/b15cd3dd)
