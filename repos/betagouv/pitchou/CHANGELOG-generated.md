## Changelog : pitchou (30 derniers jours, au 23 mai 2026)

### Résumé
Ce changelog présente des améliorations de sécurité significatives, notamment concernant le chiffrement et la gestion des accès. Des outils de développement ont également été ajoutés pour faciliter les tests et le développement local. Enfin, des améliorations de la qualité du code ont été apportées avec l'intégration de Prettier.

### Évolutions fonctionnelles
*   Aucune évolution fonctionnelle visible pour l'utilisateur n'a été apportée durant cette période.

### Évolutions techniques
*   **Sécurité :** Génération d'un vecteur d'initialisation (IV) aléatoire pour le chiffrement, renforçant la sécurité des données.  [#560](https://github.com/betagouv/pitchou/issues/560)
*   **Sécurité :** Durcissement de la connexion et du code d'accès pour une meilleure protection contre les accès non autorisés. [#557](https://github.com/betagouv/pitchou/issues/557)
*   **Tests :** Ajout de Vitest et de tests pour la manipulation de chaînes de caractères, améliorant la couverture et la fiabilité des tests. [#559](https://github.com/betagouv/pitchou/issues/559)
*   **Migrations :** Correction de l'utilisation de Knex dans les migrations, assurant une meilleure gestion de la base de données. [#556](https://github.com/betagouv/pitchou/issues/556)
*   **Développement :** Ajout d'un environnement de développement Nix et de Direnv pour faciliter la configuration et la reproductibilité de l'environnement de développement. [#558](https://github.com/betagouv/pitchou/issues/558)
*   **Qualité du code :** Intégration de Prettier pour formater automatiquement le code, améliorant la lisibilité et la cohérence. [#555](https://github.com/betagouv/pitchou/issues/555)

### Autres changements
*   Aucun autre changement significatif à signaler.
