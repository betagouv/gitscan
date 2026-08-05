## Changelog : zacharie (30 derniers jours, au 04/08/2026)

### Résumé
Cette période a été marquée par une amélioration significative des outils dédiés au suivi SVI (Service Vétérinaire d'Inspection) et une optimisation de l'expérience des collecteurs. Les performances de synchronisation des données ont été renforcées pour garantir une meilleure fluidité, même lors du traitement de volumes importants de carcasses.

### Évolutions fonctionnelles
- **Suivi SVI** : Mise en place d'un tableau de bord dédié ([#514](https://github.com/betagouv/zacharie/pull/514)), possibilité d'acceptation en un clic ([#534](https://github.com/betagouv/zacharie/pull/534)) et ajout d'actions de masse ([#535](https://github.com/betagouv/zacharie/pull/535)).
- **Expérience Collecteur** : Nouvelle barre latérale ([#526](https://github.com/betagouv/zacharie/pull/526)), amélioration de la vue des carcasses ([#528](https://github.com/betagouv/zacharie/pull/528)) et ajout de la pagination sur les fiches.
- **Interface et Ergonomie** : Refonte du design des données de chasse ([#532](https://github.com/betagouv/zacharie/pull/532)), corrections de libellés pour plus de clarté ([#530](https://github.com/betagouv/zacharie/pull/530), [#524](https://github.com/betagouv/zacharie/pull/524)) et correction du parcours de réinitialisation de mot de passe sur mobile ([#543](https://github.com/betagouv/zacharie/pull/543)).
- **Gestion des données** : Meilleure visibilité des carcasses refusées pour les destinataires suivants ([#550](https://github.com/betagouv/zacharie/pull/550)), correction de la logique de prise en charge par le collecteur ([#537](https://github.com/betagouv/zacharie/pull/537)) et possibilité de choisir une association de chasse.

### Évolutions techniques
- **Performances** : Optimisation de l'endpoint de synchronisation ([#529](https://github.com/betagouv/zacharie/pull/529)) et du backend pour gérer de gros volumes de carcasses ([#512](https://github.com/betagouv/zacharie/pull/512)).
- **Fiabilité et Monitoring** : Ajout de tâches planifiées (crons) pour le contrôle de santé de l'application ([#540](https://github.com/betagouv/zacharie/pull/540)) et amélioration de la gestion des erreurs dans Sentry ([#541](https://github.com/betagouv/zacharie/pull/541)).
- **Maintenance** : Corrections de tests ([#527](https://github.com/betagouv/zacharie/pull/527)) et amélioration de la gestion de la suppression logique des entités ([#525](https://github.com/betagouv/zacharie/pull/525)).

### Autres changements
- Organisation du dépôt avec l'ajout d'un dossier de scripts internes.
- Mise à jour de la configuration de l'environnement Claude.
