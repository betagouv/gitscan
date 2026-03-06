## Changelog : domifa (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à DomiFa, la plateforme de gestion de la domiciliation. Les mises à jour incluent des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur, l'ajout de nouvelles fonctionnalités comme l'envoi de SMS via Mondomifa, et des améliorations techniques pour la surveillance et la configuration du backend.

### Évolutions fonctionnelles
- Ajout de l'envoi de SMS via Mondomifa pour faciliter la communication avec les utilisateurs. [#c360ffd](https://github.com/SocialGouv/domifa/commit/c360ffdbe8b8dcb0c060e9a5eba51a6c03c23ac9)
- Amélioration de la documentation et ajout de popups pour une meilleure expérience utilisateur sur l'interface. [#e36a138](https://github.com/SocialGouv/domifa/commit/e36a138dfe8323c6cd9ba656ecee8af1400b0f37)
- Correction de bugs concernant l'affichage et la gestion des dates dans les formulaires. [#30f4218](https://github.com/SocialGouv/domifa/commit/30f421890113c18cbed22b9a51182cbfbb46ba6f), [#1a168fc](https://github.com/SocialGouv/domifa/commit/1a168fc93c05f291177984370619638a24d5f808)
- Correction d'un bug empêchant la vérification des doublons dans les formulaires. [#2b6f796](https://github.com/SocialGouv/domifa/commit/2b6f796e81290ff021e2084b101a2178abea8024)
- Correction d'un problème lié au suivi Matomo. [#4069](https://github.com/SocialGouv/domifa/issues/4069) [#bbd4c69](https://github.com/SocialGouv/domifa/commit/bbd4c694ad55483ebf558e8419775256de7bb456)
- Correction de bugs liés à l'affichage de la politique. [#5864aad](https://github.com/SocialGouv/domifa/commit/5864aad6ab9fb9603f3cc64e3f5402e44f3743ad), [#fd30c27](https://github.com/SocialGouv/domifa/commit/fd30c27ab63ef946371a41b99d22d4ff5441dd6a)

### Évolutions techniques
- Refactorisation du cron et ajout d'une surveillance via Sentry pour une meilleure gestion et détection des erreurs. [#adf9625](https://github.com/SocialGouv/domifa/commit/adf9625ea4261f5dd3b90bf39c2ebb6d22335005)
- Mise à jour de la configuration NestJS du backend. [#3d541c7](https://github.com/SocialGouv/domifa/commit/3d541c7415f9d9d4749b343109c7ff960733399c)
- Ajout du label "other" pour les cerfa. [#bb5734f](https://github.com/SocialGouv/domifa/commit/bb5734f927e5f26ce4a15582f973a0fedb06b054)
- Correction de problèmes de build et de migration du backend. [#c833b17](https://github.com/SocialGouv/domifa/commit/c833b173ee22a7517c7ca7d294fcc71ba6349e82), [#d097080](https://github.com/SocialGouv/domifa/commit/d097080282785d709e1fef203fef28ff01d9a9d6)
