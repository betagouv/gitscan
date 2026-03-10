## Changelog : espace_membre-ruby (30 derniers jours)

### Résumé
Cette nouvelle version apporte des améliorations à la détection de l'environnement Rails, notamment concernant l'utilisation de FactoryBot. Des corrections ont également été apportées pour une meilleure gestion des phases actives et une résolution de problèmes liés à la portée des tests. Enfin, la gem a été versionnée avec plusieurs mises à jour mineures.

### Évolutions fonctionnelles
- Correction de la détection de FactoryBot dans l'environnement Rails [#1234](https://github.com/betagouv/espace_membre-ruby/issues/1234).
- Amélioration de la découverte de la phase active au démarrage.
- Possibilité de passer plusieurs valeurs au scope `in_phase`.

### Évolutions techniques
- Refactorisation du scope FactoryBot pour une meilleure organisation.
- Déplacement des factories vers les consommateurs pour une plus grande flexibilité.
- Correction des tests pour assurer la cohérence et la fiabilité du code.

### Autres changements
- Mises à jour de version : 0.2, 0.2.1, 0.2.2 et 0.3.
