## Changelog : espace_membre-ruby (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, la gem `espace_membre-ruby` a bénéficié d'améliorations significatives, notamment l'ajout de la gestion des organisations et l'utilisation d'UUID comme clés primaires pour une meilleure robustesse et scalabilité. Des corrections ont également été apportées pour améliorer la stabilité du serveur de test et faciliter l'exploration de la gem.

### Évolutions fonctionnelles
- Ajout de la gestion des organisations via un nouveau modèle `Organization` [#14](https://github.com/betagouv/espace_membre-ruby/pull/14).
- Utilisation d'UUID comme clés primaires pour le modèle de base, améliorant la gestion des identifiants uniques [#13](https://github.com/betagouv/espace_membre-ruby/pull/13).

### Évolutions techniques
- Mise en place d'un serveur HTTP factice pour faciliter l'exploration et le test de la gem [#12](https://github.com/betagouv/espace_membre-ruby/pull/12).
- Corrections diverses concernant la configuration de la base de données dans l'environnement CI.

### Autres changements
- Refonte et clarification de la documentation README en français [#14](https://github.com/betagouv/espace_membre-ruby/commit/6cf3ff4).
