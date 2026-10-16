## Changelog : release-action (30 derniers jours, au 08/10/2026)

### Résumé
Le projet a connu une phase de développement intense avec l'ajout de nouvelles capacités de gestion de branches et une refonte complète de la manière dont les notes de mise à jour (changelogs) sont générées, les rendant beaucoup plus interactives et lisibles.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout d'une sous-action pour le nettoyage automatique des branches (`prune-branches`) [#9](https://github.com/proconnect-gouv/release-action/issues/9).
    - Introduction d'une action de release partagée [#1](https://github.com/proconnect-gouv/release-action/issues/1).
- **Amélioration de l'expérience utilisateur (Changelog)** :
    - Optimisation de la lisibilité du changelog généré avec le regroupement des commits liés aux dépendances [#2](https://github.com/proconnect-gouv/release-action/issues/2).
    - Ajout de liens cliquables vers les Pull Requests et les commits [#4](https://github.com/proconnect-gouv/release-action/issues/4).
    - Utilisation de liens basés sur le hash des commits pour une navigation plus fluide [#5](https://github.com/proconnect-gouv/release-action/issues/5).
- **Corrections** :
    - Résolution d'un problème garantissant le bon fonctionnement des commentaires de release GitHub lors de l'utilisation d'un changelog lié [#7](https://github.com/proconnect-gouv/release-action/issues/7).

### Évolutions techniques
- **CI/CD** : Amélioration de la lisibilité des logs de workflow en ajoutant des emojis aux noms des workflows, des jobs et des étapes [#6](https://github.com/proconnect-gouv/release-action/issues/6).

### Autres changements
- Formatage automatique du fichier `CHANGELOG.md` avec Prettier pour assurer une cohérence visuelle [#11](https://github.com/proconnect-gouv/release-action/issues/11).
