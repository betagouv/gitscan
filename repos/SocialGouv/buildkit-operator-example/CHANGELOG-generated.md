## Changelog : buildkit-operator-example (30 derniers jours, au 27 juin 2026)

### Résumé
Ce dépôt a connu des améliorations significatives concernant la sécurité de la chaîne d'approvisionnement logicielle (supply chain security) et la flexibilité de l'intégration continue (CI). L'ajout de la signature cosign, de la génération de SBOM et de provenance, ainsi que l'utilisation d'une action réutilisable, renforcent la confiance dans les images construites. De plus, la configuration CI a été simplifiée et rendue plus portable.

### Évolutions fonctionnelles
- **Sécurité de la chaîne d'approvisionnement :** Implémentation de la signature cosign, de la génération de SBOM (Software Bill of Materials) et de provenance pour renforcer la sécurité et la traçabilité des images Docker construites.
- **Cache S3 optionnel :** Ajout de la possibilité d'utiliser un cache S3 distant pour accélérer les builds via les variables d'environnement `BUILDCAT_S3_*` [#8a10c13](https://github.com/SocialGouv/buildkit-operator-example/commit/8a10c13).
- **Authentification OIDC :** Amélioration de l'authentification OIDC avec l'utilisation du SHA complet de la référence de l'action et la validation de l'authentification sur `/route` [#97a4dee](https://github.com/SocialGouv/buildkit-operator-example/commit/97a4dee).

### Évolutions techniques
- **Action réutilisable :** Remplacement du script `build.sh` local par l'action réutilisable `socialgouv/buildkit-operator@v1` pour simplifier et standardiser le processus de build [#4f539b3](https://github.com/SocialGouv/buildkit-operator-example/commit/4f539b3).
- **CI portable :** Refonte du script `build.sh` pour le rendre portable et compatible avec différents systèmes CI, notamment GitLab [#02be867](https://github.com/SocialGouv/buildkit-operator-example/commit/02be867).
- **Utilisation de runners GitHub par défaut :** Configuration du workflow CI pour utiliser les runners GitHub hébergés par défaut (ubuntu-latest) [#11a4441](https://github.com/SocialGouv/buildkit-operator-example/commit/11a4441).
- **Amélioration de la gestion des certificats :** Utilisation de chemins absolus pour les certificats dans le script `build.sh` et affichage des erreurs lors de la création de `buildx` [#e14e185](https://github.com/SocialGouv/buildkit-operator-example/commit/e14e185).
- **Passage du token bearer :** Transmission du token bearer au buildkit-operator exposé sur internet [#0d43a08](https://github.com/SocialGouv/buildkit-operator-example/commit/0d43a08).
- **Expression régulière insensible à la casse :** Modification de l'expression régulière pour l'identité cosign afin de prendre en compte les organisations en majuscules (SocialGouv) [#eb1f573](https://github.com/SocialGouv/buildkit-operator-example/commit/eb1f573).

### Autres changements
- **Tests :** Utilisation de `gateway-host` pour les tests avec un DNS réel et configuration de l'action avec l'entrée `gateway-host` [#7d1585b](https://github.com/SocialGouv/buildkit-operator-example/commit/7d1585b).
- **Pinning des actions :** Épinglage des actions utilisées dans le workflow CI à des versions spécifiques pour garantir la reproductibilité des builds [#3ff40e7](https://github.com/SocialGouv/buildkit-operator-example/commit/3ff40e7) et [#e83d67f](https://github.com/SocialGouv/buildkit-operator-example/commit/e83d67f).
- **Suppression du script local :** Suppression du script `build.sh` local car il est maintenant remplacé par l'action réutilisable [#80dd4a7](https://github.com/SocialGouv/buildkit-operator-example/commit/80dd4a7).
