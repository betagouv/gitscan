## Changelog : mobilic (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période a été marquée par l'ajout de fonctionnalités clés telles que les notifications push et une nouvelle page dédiée au schéma pluriannuel. Nous avons également amélioré l'expérience utilisateur en fluidifiant la création de missions et en affinant la précision des statistiques et de l'historique des activités.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout d'une page dédiée au schéma pluriannuel, incluant des améliorations d'accessibilité [#955](https://github.com/MTES-MCT/mobilic/pull/955).
    - Implémentation des notifications push [#920](https://github.com/MTES-MCT/mobilic/pull/920).
    - Ajout du logo Rota dans la section des partenaires [#940](https://github.com/MTES-MCT/mobilic/pull/940).
- **Améliorations de l'expérience utilisateur** :
    - Optimisation du parcours de création de mission via un accès direct depuis le menu de navigation et une redirection améliorée [#938](https://github.com/MTES-MCT/mobilic/pull/938).
    - Amélioration de la gestion des activités (division d'activités et correction de l'affichage des labels dans l'historique) [#930](https://github.com/MTES-MCT/mobilic/pull/930).
    - Optimisation de la saisie des dates de naissance (gestion de l'auto-focus).
    - Désactivation automatique du bouton de sauvegarde si le texte de la bannière n'a pas été modifié.
- **Corrections de bugs** :
    - Amélioration de l'affichage et du comportement des notifications (largeur, langue de l'application et cohérence visuelle) [#932](https://github.com/MTES-MCT/mobilic/pull/932).
    - Correction du calcul des statistiques de mission pour exclure les activités rejetées [#927](https://github.com/MTES-MCT/mobilic/pull/927).
    - Rectification de la référence légale concernant la définition de la semaine civile [#939](https://github.com/MTES-MCT/mobilic/pull/939).

### Évolutions techniques
- **Robustesse de la PWA** : Résolution des problèmes d'écrans blancs lors du chargement ou après un déploiement (gestion du cache) et application des recommandations SonarCloud.
- **Architecture** : Refactorisation pour rendre le `ActionsContext` disponible globalement dans l'application [#949](https://github.com/MTES-MCT/mobilic/pull/949).
- **Observabilité** : Amélioration du suivi des erreurs avec la capture des jetons de rafraîchissement invalides dans Sentry [#914](https://github.com/MTES-MCT/mobilic/pull/914).
- **Stabilité** : Correction d'un problème d'écran blanc survenant lors du chargement initial de l'application [#926](https://github.com/MTES-MCT/mobilic/pull/926).

### Autres changements
- Réécriture de la déclaration d'accessibilité.
