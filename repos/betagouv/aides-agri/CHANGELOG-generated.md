## Changelog : aides-agri (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de la plateforme d'aides agricoles. Les nouveautés incluent l'ajout d'une première version de la page de statistiques, des améliorations de l'interface d'administration pour la gestion des aides, et des ajustements au parcours utilisateur pour faciliter l'accès aux informations. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une première version de la page de statistiques, permettant de visualiser des données sur l'utilisation de la plateforme. [#387](https://github.com/betagouv/aides-agri/pull/387)
- Les bureaux valideurs peuvent désormais voir les aides avant leur publication, améliorant ainsi le processus de validation. [#371](https://github.com/betagouv/aides-agri/pull/371)
- Mise à jour de la page des fonds d'urgence DNC pour refléter les informations les plus récentes. [#370](https://github.com/betagouv/aides-agri/pull/370)
- Ajustement du parcours v1 pour améliorer l'expérience utilisateur. [#363](https://github.com/betagouv/aides-agri/pull/363)
- Amélioration mineure de l'interface d'administration des aides. [#372](https://github.com/betagouv/aides-agri/pull/372)

### Évolutions techniques
- Amélioration du script de mises à jour pour faciliter la maintenance de la plateforme. [#381](https://github.com/betagouv/aides-agri/pull/381)
- Configuration d'un délai de refroidissement pour les mises à jour Dependabot afin de limiter l'impact sur la stabilité. [#374](https://github.com/betagouv/aides-agri/pull/374)
- Mises à jour de plusieurs dépendances :
    - Gunicorn : 25.0.1 -> 25.0.3, puis 25.0.3 -> 25.1.0 [#367](https://github.com/betagouv/aides-agri/pull/367), [#386](https://github.com/betagouv/aides-agri/pull/386)
    - Ruff : 0.14.14 -> 0.15.0, puis 0.15.0 -> 0.15.1 [#362](https://github.com/betagouv/aides-agri/pull/362), [#385](https://github.com/betagouv/aides-agri/pull/385)
    - Coverage : 7.13.2 -> 7.13.3, puis 7.13.3 -> 7.13.4 [#359](https://github.com/betagouv/aides-agri/pull/359), [#383](https://github.com/betagouv/aides-agri/pull/383)
    - Sentry SDK : 10.36.0 -> 10.37.0, puis 10.37.0 -> 10.38.0 [#361](https://github.com/betagouv/aides-agri/pull/361), [#373](https://github.com/betagouv/aides-agri/pull/373)
    - Django-dsfr : 3.3.0 -> 3.3.1 [#355](https://github.com/betagouv/aides-agri/pull/355)
    - Faker : 40.1.2 -> 40.4.0 [#366](https://github.com/betagouv/aides-agri/pull/366)
    - Asgiref : 3.11.0 -> 3.11.1 [#358](https://github.com/betagouv/aides-agri/pull/358)
    - Django : 5.2.10 -> 5.2.11 [#357](https://github.com/betagouv/aides-agri/pull/357)
    - Diverses mises à jour mineures de dépendances de développement (js-yaml, lodash-es, lodash, tar-fs, esbuild, markdown, qs, express).

### Autres changements
- Aucun changement significatif à signaler dans cette catégorie.
