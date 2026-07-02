## Changelog : audiodescription (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'infrastructure et l'ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur et la gestion du contenu. On note notamment le remplacement du service d'envoi d'emails Brevo par Sendethic, l'ajout d'une nouvelle section "Affiches parlantes", et des améliorations d'accessibilité sur le site.

### Évolutions fonctionnelles
- Ajout d'une nouvelle fonctionnalité "Affiches parlantes" permettant d'afficher des affiches parlantes. [#50482c5](https://github.com/betagouv/audiodescription/commit/50482c5)
- Remplacement du service d'envoi d'emails Brevo par Sendethic pour la gestion des newsletters et autres communications. [#9046633](https://github.com/betagouv/audiodescription/commit/9046633), [#00d1563](https://github.com/betagouv/audiodescription/commit/00d1563), [#1a56b26](https://github.com/betagouv/audiodescription/commit/1a56b26)
- Amélioration de la gestion des affiches parlantes : elles sont maintenant masquées si aucune n'est disponible. [#8a3a906](https://github.com/betagouv/audiodescription/commit/8a3a906)
- Intégration de Proconnect sur Drupal. [#25a570d](https://github.com/betagouv/audiodescription/commit/25a570d)

### Évolutions techniques
- Mise à jour de la configuration Docker pour la production. [#601ec70](https://github.com/betagouv/audiodescription/commit/601ec70)
- Ajout de Redis pour la mise en cache. [#1aaa767](https://github.com/betagouv/audiodescription/commit/1aaa767)
- Utilisation d'une nouvelle URL pour l'infrastructure. [#31837d1](https://github.com/betagouv/audiodescription/commit/31837d1)
- Ajout de S3 avec RustFS pour le stockage des fichiers. [#db1892c](https://github.com/betagouv/audiodescription/commit/db1892c)
- Séparation des commandes cron pour Patrimony et Drupal afin d'améliorer la gestion des tâches planifiées. [#fbce2b6](https://github.com/betagouv/audiodescription/commit/fbce2b6)
- Mise à jour de la configuration pour S3 en pré-production. [#66f1c58](https://github.com/betagouv/audiodescription/commit/66f1c58)
- Mise à jour de `compose.staging.yml`. [#8c5b1e9](https://github.com/betagouv/audiodescription/commit/8c5b1e9)

### Autres changements
- Correction de l'icône "affiches parlantes". [#a3804db](https://github.com/betagouv/audiodescription/commit/a3804db)
- Améliorations de l'accessibilité des formulaires d'inscription à la newsletter. [#b294eb2](https://github.com/betagouv/audiodescription/commit/b294eb2)
- Correction de bugs liés aux mots-clés de recherche et mise à jour des titres. [#68e8fee](https://github.com/betagouv/audiodescription/commit/68e8fee)
- Correction d'un bug lié au bouton de réinitialisation pour l'accessibilité. [#7be0f8b](https://github.com/betagouv/audiodescription/commit/7be0f8b)
- Suppression des messages Drupal sur la page d'inscription à la newsletter. [#ee4ef17](https://github.com/betagouv/audiodescription/commit/ee4ef17)
- Mise à jour de la documentation avec les versions actuelles. [#f3a926c](https://github.com/betagouv/audiodescription/commit/f3a926c)
- Ajout d'un exemple de configuration dans le répertoire de configuration Docker. [#35a78f3](https://github.com/betagouv/audiodescription/commit/35a78f3)
- Correction du `composer.lock`. [#3fa0c96](https://github.com/betagouv/audiodescription/commit/3fa0c96), [#ca6cd6d](https://github.com/betagouv/audiodescription/commit/ca6cd6d)
