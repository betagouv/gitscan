## Changelog : sill-deploy (30 derniers jours, au 17 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion de la configuration de l'application, permettant une plus grande flexibilité et une meilleure propagation des paramètres. Des corrections ont également été apportées à l'interface web, notamment pour la gestion des systèmes d'exploitation et la résolution de problèmes liés à la politique de sécurité du contenu (CSP). Enfin, l'intégration de workflows de déploiement SILL a été ajoutée.

### Évolutions fonctionnelles
- Amélioration de la gestion des systèmes d'exploitation dans l'interface web : ajout d'options pour les systèmes mobiles et typage plus précis. [#500](https://github.com/codegouvfr/sill-deploy/issues/500)
- Possibilité de définir une configuration via des fichiers, permettant une gestion plus flexible des paramètres de l'application.
- Propagation de la nouvelle gestion de configuration à travers l'application.
- Correction du suivi des changements de route dans l'application monopage (SPA) pour l'analytics, précédemment bloqué par la CSP.

### Évolutions techniques
- Ajout des workflows de déploiement SILL et synchronisation avec l'upstream.
- Refactorisation de la gestion des fonctionnalités "gateway".
- Modification de l'ordre des migrations.
- Amélioration de la configuration de la CSP locale pour permettre l'affichage des images.
- Ajout de `worker-src` à la CSP par défaut pour les workers Sentry.

### Autres changements
- Mise à jour de la version de l'application.
- Correction des dépendances de test.
- Documentation améliorée concernant la configuration de la CSP.
