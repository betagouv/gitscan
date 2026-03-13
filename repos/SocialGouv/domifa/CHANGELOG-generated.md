## Changelog : domifa (30 derniers jours)

### Résumé
Les dernières mises à jour de DomiFa incluent des corrections de bugs pour améliorer la stabilité de l'application, notamment au niveau des dates et de la gestion des formulaires. De nouvelles fonctionnalités ont été ajoutées, comme l'envoi de SMS via Mondomifa et l'intégration de données provenant de 'MSS', ainsi qu'une amélioration de la surveillance de l'application avec l'ajout de Sentry. Des améliorations de l'interface utilisateur ont également été apportées avec l'ajout de popups et la mise à jour de la documentation.

### Évolutions fonctionnelles
- Ajout de l'envoi de SMS via Mondomifa [#c360ffd](https://github.com/SocialGouv/domifa/commit/c360ffdbe8b8dcb0c060e9a5eba51a6c03c23ac9)
- Ajout de popups et mise à jour de la documentation pour améliorer l'expérience utilisateur [#e36a138](https://github.com/SocialGouv/domifa/commit/e36a138dfe8323c6cd9ba656ecee8af1400b0f37)
- Correction de bugs liés à la gestion des dates dans les formulaires [#30f4218](https://github.com/SocialGouv/domifa/commit/30f421890113c18cbed22b9a51182cbfbb46ba6f) et [#1a168fc](https://github.com/SocialGouv/domifa/commit/1a168fc93c05f291177984370619638a24d5f808)
- Correction de bugs liés à la gestion de la politique [#5864aad](https://github.com/SocialGouv/domifa/commit/5864aad6ab9fb9603f3cc64e3f5402e44f3743ad) et [#fd30c27](https://github.com/SocialGouv/domifa/commit/fd30c27ab63ef946371a41b99d22d4ff5441dd6a)
- Correction de la vérification des doublons dans les formulaires [#2b6f796](https://github.com/SocialGouv/domifa/commit/2b6f796e81290ff021e2084b101a2178abea8024)

### Évolutions techniques
- Refactorisation du cron et ajout de la surveillance avec Sentry pour une meilleure gestion et supervision de l'application [#adf9625](https://github.com/SocialGouv/domifa/commit/adf9625ea4261f5dd3b90bf39c2ebb6d22335005)
- Mise à jour de la configuration NestJS côté backend [#3d541c7](https://github.com/SocialGouv/domifa/commit/3d541c7415f9d9d4749b343109c7ff960733399c)
- Ajout du label "other" pour les cerfa [#bb5734f](https://github.com/SocialGouv/domifa/commit/bb5734f927e5f26ce4a15582f973a0fedb06b054)
- Correction de problèmes de build et de migration du backend [#d097080](https://github.com/SocialGouv/domifa/commit/d097080282785d709e1fef203fef28ff01d9a9d6) et [#c833b17](https://github.com/SocialGouv/domifa/commit/c833b173ee22a7517c7ca7d294fcc71ba6349e82)

### Autres changements
- Correction d'un problème de persistance [#d1793df](https://github.com/SocialGouv/domifa/commit/d1793dfca422305ba62e46241b020e7bcc16007d)
- Mise à jour des structures HTML des formulaires [#fac8996](https://github.com/SocialGouv/domifa/commit/fac89965445f77961f3866161f845f7f57462f62), [#fbfd718](https://github.com/SocialGouv/domifa/commit/fbfd718f76465b61825f8a99a874a87942719498) et [#1670154](https://github.com/SocialGouv/domifa/commit/1670154a4919328796198574c4a551987f39775b)
