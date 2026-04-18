## Changelog : b3desk (30 derniers jours, au 17 avril 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment la possibilité pour un utilisateur authentifié de modifier son nom lors de la page de connexion et une correction pour éviter que le logo ne soit masqué par le titre. Des corrections ont également été apportées pour améliorer la compatibilité avec Keycloak et éviter l'utilisation de liens statiques. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Un utilisateur authentifié peut maintenant modifier son nom sur la page de connexion. [#318](https://github.com/numerique-gouv/b3desk/issues/318)
- Le logo n'est plus masqué par le titre de la page. [#319](https://github.com/numerique-gouv/b3desk/issues/319)
- Délégation de réunion : implémentation de la fonctionnalité permettant de déléguer la gestion d'une réunion. [#241](https://github.com/numerique-gouv/b3desk/pull/241) via [#226](https://github.com/numerique-gouv/b3desk/issues/226)

### Évolutions techniques
- Correction de la compatibilité avec Keycloak. [#317](https://github.com/numerique-gouv/b3desk/issues/317)
- Suppression des liens statiques au profit de liens dynamiques.
- Mise à jour de la version principale vers 1.6.1dev et 1.5.9dev.

### Autres changements
- Mise à jour de plusieurs dépendances :
    - `authlib` de 1.6.9 à 1.6.11
    - `mako` de 1.3.10 à 1.3.11
    - `pytest` de 9.0.2 à 9.0.3
    - `uv` de 0.9.26 à 0.11.6
    - `cryptography` de 46.0.5 à 46.0.7
    - `pygments` de 2.19.2 à 2.20.0
    - `requests` de 2.32.5 à 2.33.0
