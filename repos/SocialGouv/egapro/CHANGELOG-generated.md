## Changelog : egapro (30 derniers jours, au 22 juillet 2026)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment la refonte de la déclaration de rémunération et l'ajout de fonctionnalités d'accessibilité. Des corrections ont également été apportées pour assurer la conformité et la stabilité de la plateforme, ainsi que des améliorations techniques pour faciliter le développement et le déploiement.

### Évolutions fonctionnelles
- Le bouton d'export est de nouveau disponible dans l'étape 5 du parcours de déclaration de rémunération ([#3968](https://github.com/SocialGouv/egapro/issues/3968)).
- Un bouton "Je donne mon avis" a été intégré à la fin du parcours de déclaration ([#3966](https://github.com/SocialGouv/egapro/issues/3966)).
- Refonte du design de la déclaration de rémunération (pages 1 à 5) ([#3935](https://github.com/SocialGouv/egapro/issues/3935)).
- Refonte multi-pages du template PDF de la déclaration de rémunération (basé sur les maquettes) ([#3973](https://github.com/SocialGouv/egapro/issues/2914)).
- Implémentation de règles pour l'envoi de notifications par email et contenu des emails de rappel ([#3857](https://github.com/SocialGouv/egapro/issues/3857), [#3671](https://github.com/SocialGouv/egapro/issues/3671)).
- Implémentation d'un système de purge des données des déclarations ([#3828](https://github.com/SocialGouv/egapro/issues/3828)).
- Amélioration de l'affichage de la proportion de bénéficiaires dans l'étape 6 et le PDF de la déclaration de rémunération ([#3869](https://github.com/SocialGouv/egapro/issues/3869)).
- Implémentation de règles de conformité pour les écarts salariaux par GIP ([#3868](https://github.com/SocialGouv/egapro/issues/3868)).

### Évolutions techniques
- Verrouillage du compilateur du moteur d'étapes FSM pour plus de stabilité ([#3979](https://github.com/SocialGouv/egapro/issues/3979)).
- Dérivation du vocabulaire de statut admin à partir de `DECLARATION_FSM_STATUSES` pour une meilleure cohérence ([#3983](https://github.com/SocialGouv/egapro/issues/3980)).
- Rationalisation de la suite de tests E2E, en se concentrant sur les parcours critiques et en remplaçant les tests détaillés par des tests unitaires ([#3928](https://github.com/SocialGouv/egapro/issues/3928)).
- Amélioration de l'accessibilité (RGAA) avec l'implémentation d'ultra11y et la correction de plusieurs problèmes d'accessibilité ([#3889](https://github.com/SocialGouv/egapro/issues/3800), [#3887](https://github.com/SocialGouv/egapro/issues/3817)).
- Mise en place d'un lock pour le parcours de déclaration afin d'éviter les conflits ([#3753](https://github.com/SocialGouv/egapro/issues/3556)).
- Mise en place d'un canal de prépublication alpha avec déclenchement automatique des releases ([#3858](https://github.com/SocialGouv/egapro/issues/3736)).
- Correction de problèmes liés aux permissions OIDC et à la signature GPG lors des releases ([#3908](https://github.com/SocialGouv/egapro/issues/3908), [#3906](https://github.com/SocialGouv/egapro/issues/3906)).
- Amélioration de la configuration des environnements de test persistants pour les tests RGAA et de performance ([#3904](https://github.com/SocialGouv/egapro/issues/3904)).
- Migration des builds d'images vers buildkit-operator ([#3844](https://github.com/SocialGouv/egapro/issues/3844)).
- Ajout d'un seed pour les données de démonstration des graphiques statistiques ([#3758](https://github.com/SocialGouv/egapro/issues/3569)).

### Autres changements
- Documentation du moteur d'étapes (FSM) et ajout d'un pointeur vers le document CLAUDE.md ([#3982](https://github.com/SocialGouv/egapro/issues/3976)).
- Ajout d'un changelog pour les releases alpha ([#3965](https://github.com/SocialGouv/egapro/issues/3853)).
- Discipline de fidélité Figma (mesure, thème clair, états, tableaux, espaces verticaux) documentée ([#3961](https://github.com/SocialGouv/egapro/issues/3861)).
- Correction du seed des données Matomo en local ([#3787](https://github.com/SocialGouv/egapro/issues/3787)).
- Mise à jour de la documentation pour refléter le workflow Figma sur le serveur MCP officiel ([#3881](https://github.com/SocialGouv/egapro/issues/3848)).
- Correction d'un revert de la demande du niveau Eidas2 sur ProConnect ([#3907](https://github.com/SocialGouv/egapro/issues/3907)).
