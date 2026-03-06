## Changelog : st-deploycenter (30 derniers jours)

### Résumé
Les dernières mises à jour de st-deploycenter se concentrent sur l'amélioration de l'administration et de l'import de données, notamment pour les organisations et les rôles. Des améliorations ont également été apportées à l'interface utilisateur pour une meilleure expérience, ainsi que des corrections de bugs et des optimisations techniques. L'intégration avec ProConnect et Messages a été renforcée, offrant plus de flexibilité et de contrôle aux superutilisateurs.

### Évolutions fonctionnelles
- Ajout de boutons de synchronisation dans l'import pour supprimer les anciens rôles d'organisation d'opérateur. [#43](https://github.com/suitenumerique/st-deploycenter/issues/43)
- Possibilité de dupliquer un service dans l'interface d'administration.
- Amélioration de l'affichage de l'interface utilisateur avec correction de divers problèmes mineurs.
- Possibilité pour les superutilisateurs de modifier les domaines ProConnect.
- Possibilité pour les superadministrateurs de modifier les domaines pour Messages.
- Ajout de l'import en masse des rôles de compte.
- Ajout de la possibilité de supprimer des comptes via l'interface utilisateur et l'API. [#38](https://github.com/suitenumerique/st-deploycenter/issues/38)
- Affichage des services avec une priorité d'affichage inférieure à 0 dans l'interface utilisateur.
- Ajout d'une carte Messages et amélioration des droits d'accès. [#36](https://github.com/suitenumerique/st-deploycenter/issues/36)
- Mise en place d'un résolveur d'administration étendu et d'une adhésion automatique pour les organisations. [#33](https://github.com/suitenumerique/st-deploycenter/issues/33)
- Amélioration de l'affichage des filtres dans l'administration pour l'import en masse des SIRET pour les abonnements.

### Évolutions techniques
- Mise à jour de Django.
- Amélioration du filtrage des valeurs des webhooks en fonction des métadonnées des autres services.
- Correction d'un test Faker aléatoire instable.
- Mise à jour des étapes des workflows GitHub Actions vers les dernières versions. [#39](https://github.com/suitenumerique/st-deploycenter/issues/39)
- Implémentation de `can_admin_maildomains` pour Messages. [#40](https://github.com/suitenumerique/st-deploycenter/issues/40)
- Correction d'un contournement des vérifications frontend des domaines ProConnect pour les superutilisateurs.

### Autres changements
- Amélioration de la lisibilité des champs JSON dans l'administration.
- Correction de l'attribut `lang` en `html lang=fr`.
- Mise à jour de la terminologie dans le fichier README.
- Masquage de RPNT pour les organisations de type "autre".
- Correction du texte d'aide "pas de domaines" pour Messages.
