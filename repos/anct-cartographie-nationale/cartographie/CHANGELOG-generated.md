## Changelog : cartographie (30 derniers jours, au 2026-09-10)

### Résumé
Les récentes évolutions se concentrent sur la mise en conformité légale via l'accessibilité et sur la sécurisation ainsi que l'optimisation des processus de déploiement automatique.

### Évolutions fonctionnelles
- Mise en ligne de la déclaration d'accessibilité via la route `/accessibilite` ([a305368](https://github.com/anct-cartographie-nationale/cartographie/commit/a3053686f323391d51c5eb2ff2ca61d7fee25a80)).
- Mise à jour de la déclaration d'accessibilité et harmonisation de l'adresse e-mail de contact ([cf82496](https://github.com/anct-cartographie-nationale/cartographie/commit/cf82496242662822a29569d879e1afa82254f6c3)).

### Évolutions techniques
- **Infrastructure et CI/CD :**
    - Sécurisation du workflow de release par la suppression du jeton npm statique ([8bc7dd0](https://github.com/anct-cartographie-nationale/cartographie/commit/8bc7dd0)).
    - Amélioration de l'authentification pour le téléchargement du plugin Pulumi Scaleway ([a3d59db](https://github.com/anct-cartographie-nationale/cartographie/commit/a3d59db103ff19909ddf0e882c122590dad36f4e)).
    - Mise à jour des GitHub Actions et alignement de la version de Node.js ([497e577](https://github.com/anct-cartographie-nationale/cartographie/commit/497e577)).
    - Optimisation de l'organisation du workflow de release (renommage en `release.yml` et déclaration du dépôt dans `package.json`) ([c9c9ca4](https://github.com/anct-cartographie-nationale/cartographie/commit/c9c9ca4), [0c6ad7d](https://github.com/anct-cartographie-nationale/cartographie/commit/0c6ad7d)).
- **Code :**
    - Refactoring de l'injection de dépendances pour utiliser `keyFor` de la bibliothèque `piqure` ([c6c8403](https://github.com/anct-cartographie-nationale/cartographie/commit/c6c8403)).
