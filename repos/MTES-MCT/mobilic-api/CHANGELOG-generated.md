## Changelog : mobilic-api (30 derniers jours, au 17/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la protection de la vie privée via l'amélioration des processus d'anonymisation, la précision des alertes réglementaires (notamment sur les temps de repos) et la sécurisation de l'API contre les tentatives de déni de service et les fuites de données. Des optimisations de performance ont également été apportées pour stabiliser le système.

### Évolutions fonctionnelles
- **Conformité et Alertes** : Ajout de la gestion des totaux et des seuils de repos hebdomadaire ([#785](https://github.com/MTES-MCT/mobilic-api/issues/785)) et amélioration de la pertinence des alertes réglementaires en les limitant aux entreprises ayant l'activité correspondante.
- **Anonymisation** : Renforcement de la confidentialité des données pour s'aligner sur les standards de protection (WP29) et meilleure gestion du détachement des données d'emploi lors de l'anonymisation ([#760](https://github.com/MTES-MCT/mobilic-api/issues/760)).
- **Administration** : Amélioration du tableau de bord de gestion pour détecter et identifier les utilisateurs inactifs ([#787](https://github.com/MTES-MCT/mobilic-api/issues/787)).
- **Nouvelles fonctionnalités** : Introduction du support pour les notifications push ([#762](https://github.com/MTES-MCT/mobilic-api/issues/762)).
- **Expérience utilisateur** : Corrections de textes dans l'historique des activités et améliorations de la clarté des emails d'activation de compte.

### Évolutions techniques
- **Sécurité** : Protection de l'API GraphQL contre les attaques par déni de service (DoS) basées sur la profondeur et le nombre de champs ([#788](https://github.com/MTES-MCT/mobilic-api/issues/788)) et correction d'une vulnérabilité de type BOLA permettant une fuite de données personnelles ([#788](https://github.com/MTES-MCT/mobilic-api/issues/788)). Sécurisation des modèles d'emails Mailjet ([#783](https://github.com/MTES-MCT/mobilic-api/issues/783)).
- **Performance** : Optimisation du tableau de bord via la mise en cache Redis et amélioration de l'efficacité des tâches de traitement par lots (batch) pour l'anonymisation ([#764](https://github.com/MTES-MCT/mobilic-api/issues/764), [#745](https://github.com/MTES-MCT/mobilic-api/issues/745)).
- **Stabilité** : Résolution de problèmes de saturation mémoire (OOM) sur les workers liés à la planification des alertes de pause ([#793](https://github.com/MTES-MCT/mobilic-api/issues/793)).
- **Refactoring** : Simplification de la logique d'inscription des entreprises et extraction du client Redis pour une meilleure structure de code.

### Autres changements
- Mise en conformité du style de code (Black) pour les fichiers de tests.
