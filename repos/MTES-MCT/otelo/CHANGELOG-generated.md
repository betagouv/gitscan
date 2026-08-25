## Changelog : otelo (30 derniers jours, au 23 août 2026)

### Résumé
Otelo renforce l'accompagnement de ses utilisateurs grâce à l'introduction d'un assistant de simulation pas-à-pas (wizard) et d'un nouveau mode tutoriel. Ces évolutions visent à simplifier la création de scénarios, de la configuration initiale jusqu'à l'analyse des résultats. Parallèlement, la plateforme améliore ses capacités de pilotage avec une refonte de l'administration et la mise en place d'outils de suivi d'usage.

### Évolutions fonctionnelles
- **Accompagnement utilisateur** : Mise en place d'un assistant (wizard) guidant l'utilisateur de la configuration jusqu'à l'obtention des résultats, incluant la gestion des documents d'urbanisme et la décomposition des estimations. [#55](https://github.com/MTES-MCT/otelo/pull/55), [#56](https://github.com/MTES-MCT/otelo/pull/56)
- **Aide à la prise en main** : Introduction d'un mode tutoriel interactif couvrant les six étapes clés de la création de scénarios. [#53](https://github.com/MTES-MCT/otelo/pull/53)
- **Planification et temporalité** : Ajout d'un volet (drawer) dédié à la planification territoriale et intégration du millésime dans le cadrage temporel. [#54](https://github.com/MTES-MCT/otelo/pull/54)
- **Corrections d'exports** : Résolution de problèmes concernant l'encodage des accents et la gestion des noms de fichiers lors des exports Excel.

### Évolutions techniques
- **Suivi et Administration** : Implémentation de la mesure d'usage (via base de données et Matomo) et refonte complète de l'interface d'administration. [#57](https://github.com/MTES-MCT/otelo/pull/57)
- **Architecture** : Refactorisation du parcours de scénario via la création d'un registre unique des étapes pour une meilleure gestion du flux utilisateur.

### Autres changements
- Corrections mineures d'interface (bouton de signalement, fautes de frappe) et renommage de certains éléments.
