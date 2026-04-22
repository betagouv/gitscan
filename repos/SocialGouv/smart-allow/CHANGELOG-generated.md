## Changelog : smart-allow (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, smart-allow a connu une refonte majeure de son infrastructure et de son installation. L'outil est désormais distribué en tant que binaire autonome (Go) avec un installateur amélioré, offrant une meilleure expérience utilisateur et une plus grande flexibilité.  Des améliorations ont également été apportées à la compatibilité avec les dernières versions de Claude et à la gestion des erreurs lors de l'installation.

### Évolutions fonctionnelles
- **Installation simplifiée :** Un nouvel installateur basé sur des sous-commandes permet une installation globale ou spécifique à un projet. [#958108d](https://github.com/SocialGouv/smart-allow/commit/958108d)
- **Nom du binaire modifié :** Le binaire a été renommé en `smart-allow` et des alias `enable` et `disable` ont été ajoutés pour faciliter son utilisation. [#cc55982](https://github.com/SocialGouv/smart-allow/commit/cc55982)
- **Détection du binaire dans le PATH :** L'installateur détecte si le binaire est déjà dans le PATH de l'utilisateur. [#4b47183](https://github.com/SocialGouv/smart-allow/commit/4b47183)
- **Compatibilité Claude Code 2.1+ :** Amélioration de l'émission des sorties spécifiques aux hooks pour Claude Code 2.1 et versions ultérieures. [#9e37cfb](https://github.com/SocialGouv/smart-allow/commit/9e37cfb)
- **Installateur interactif :** L'installateur est désormais interactif lorsqu'il est utilisé via un pipe (ex: `curl|sh`). [#6fb75b3](https://github.com/SocialGouv/smart-allow/commit/6fb75b3)

### Évolutions techniques
- **Refonte de l'architecture :** Le classificateur a été porté en Go, ce qui permet de créer un binaire multiplateforme. [#0eedbe8](https://github.com/SocialGouv/smart-allow/commit/0eedbe8)
- **Nouvelle infrastructure de build :** Utilisation de `taskfile` et `release-it` pour la gestion des builds et du versionnage. [#a566bea](https://github.com/SocialGouv/smart-allow/commit/a566bea)
- **Workflow de release amélioré :** Mise en place d'un workflow de release basé sur une matrice pour supporter différentes plateformes. [#a566bea](https://github.com/SocialGouv/smart-allow/commit/a566bea)
- **Gestion des erreurs améliorée :** L'installateur affiche désormais des messages d'erreur plus clairs et guide l'utilisateur en cas de problèmes. [#ff162c0](https://github.com/SocialGouv/smart-allow/commit/ff162c0)
- **Utilisation de `token-bureau` :** Utilisation de `token-bureau` pour déclencher correctement les workflows de release lors de la création de tags de version. [#d8b0730](https://github.com/SocialGouv/smart-allow/commit/d8b0730)
- **Pinning des dépendances :** Les dépendances sont désormais épinglées via `devbox` et `pnpm-lock.yaml` pour assurer la reproductibilité des builds. [#6732afe](https://github.com/SocialGouv/smart-allow/commit/6732afe)

### Autres changements
- **Documentation mise à jour :** La documentation a été déplacée sous le dossier `docs/` et inclut maintenant un guide pour l'installation via pipe. [#383f3e0](https://github.com/SocialGouv/smart-allow/commit/383f3e0)
- **Correction de bugs dans l'installateur :** Plusieurs corrections de bugs ont été apportées à l'installateur pour améliorer sa fiabilité et sa convivialité. [#2489b43](https://github.com/SocialGouv/smart-allow/commit/2489b43), [#d8ce62a](https://github.com/SocialGouv/smart-allow/commit/d8ce62a)
- **Correction d'un problème avec `--all` :** Correction d'un bug empêchant la désactivation de toutes les règles. [#a85a1de](https://github.com/SocialGouv/smart-allow/commit/a85a1de)
