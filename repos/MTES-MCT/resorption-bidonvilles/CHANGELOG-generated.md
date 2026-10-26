## Changelog : resorption-bidonvilles (30 derniers jours, au 24 octobre 2026)

### Résumé
Les récentes mises à jour se sont concentrées sur l'amélioration de la lisibilité des indicateurs et le nettoyage de l'interface utilisateur. Les agents bénéficient désormais d'un meilleur regroupement des erreurs par année et d'une navigation plus fluide dans les rapports. Par ailleurs, les alertes temporaires liées à la canicule ont été retirées des différents tableaux de bord.

### Évolutions fonctionnelles
- **Amélioration du suivi des indicateurs** : regroupement des erreurs par année et ajout de préfixes pour les messages scolaires afin de faciliter l'analyse [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- **Optimisation de l'ergonomie** : amélioration de la gestion du focus lors de la consultation des erreurs d'indicateurs [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- **Nettoyage de l'interface** : suppression du bandeau d'alerte "canicule" sur le tableau de bord, la liste des sites et les fiches sites.

### Évolutions techniques
- **Refactorisation de l'UI** : optimisation du composant `ErrorSummary` pour rendre la propriété de message optionnelle et permettre l'émission d'événements de sélection [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).

### Autres changements
- **Versions publiées** : déploiement des versions v2.60.2 et v2.60.3.
