## Changelog : aplypro (30 derniers jours)

### Résumé
Les dernières mises à jour d'aplypro se concentrent sur l'amélioration de la gestion des paiements, notamment pour les allocations ENPR et MER, ainsi que sur la correction de bugs et l'amélioration de la robustesse du système. Des améliorations ont également été apportées à la gestion des rectifications et à la journalisation des erreurs.

### Évolutions fonctionnelles
- Réactivation des paiements ENPR [#1905](https://github.com/betagouv/aplypro/issues/1905).
- Activation des paiements MER [#1890](https://github.com/betagouv/aplypro/issues/1890).
- La date PFMP est maintenant stockée dans le `codeobjet`.
- Blocage des paiements de rectification sortants négatifs (OR) [#1896](https://github.com/betagouv/aplypro/issues/1896).
- Les rectifications négatives sont maintenant conservées dans l'état "en attente".

### Évolutions techniques
- Utilisation de `codeobjet` pour stocker la date PFMP.
- Remplacement du markup `codeobjet` par `codecheance` [#1892](https://github.com/betagouv/aplypro/issues/1892).
- Amélioration de la journalisation des erreurs lors de la lecture des rectifications [#1901](https://github.com/betagouv/aplypro/issues/1901).
- Correction de problèmes Rubocop.
- Mise à jour de la version à 2.8.7 et 2.8.8.

### Autres changements
- Mise à jour de plusieurs dépendances :
    - nokogiri (de 1.19.0 à 1.19.1) [#1898](https://github.com/betagouv/aplypro/issues/1898)
    - rack (de 3.2.4 à 3.2.5) [#1897](https://github.com/betagouv/aplypro/issues/1897)
    - faraday (de 2.14.0 à 2.14.1) [#1893](https://github.com/betagouv/aplypro/issues/1893)
- Ajout de tests unitaires pour `paid_amount` et le format `codeobjet`.
- Mise à jour du bundle.
