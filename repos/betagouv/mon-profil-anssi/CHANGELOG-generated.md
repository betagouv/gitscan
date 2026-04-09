## Changelog : mon-profil-anssi (30 derniers jours, au 19 mars 2026)

### Résumé
Cette mise à jour apporte une amélioration significative à la fonctionnalité de recherche de profils, permettant de retrouver plus facilement les informations souhaitées.  En parallèle, une revue de sécurité a été effectuée avec la mise à jour de plusieurs dépendances pour corriger des vulnérabilités potentielles et améliorer la stabilité de l'application. La documentation a également été mise à jour.

### Évolutions fonctionnelles
- Amélioration de la recherche de profils : la recherche de profils est désormais fonctionnelle et retourne les résultats attendus. [#5f3d706](https://github.com/betagouv/mon-profil-anssi/commit/5f3d706)
- Mise à jour de la documentation : la documentation a été revue et modifiée pour refléter les dernières évolutions. [#081e000](https://github.com/betagouv/mon-profil-anssi/commit/081e000)

### Évolutions techniques
- Mise à jour des dépendances de sécurité : plusieurs dépendances ont été mises à jour vers leurs dernières versions mineures pour corriger des vulnérabilités et améliorer la sécurité de l'application :
    - Axios : version 1.13.5 [#f4438b0](https://github.com/betagouv/mon-profil-anssi/commit/f4438b0)
    - qs : version 6.14.2 [#c25b288](https://github.com/betagouv/mon-profil-anssi/commit/c25b288)
    - diff : version 4.0.4 [#6dbf0ca](https://github.com/betagouv/mon-profil-anssi/commit/6dbf0ca)
    - minimatch : version 3.1.4 [#345c411](https://github.com/betagouv/mon-profil-anssi/commit/345c411)
    - lodash : version 4.17.23 [#157c686](https://github.com/betagouv/mon-profil-anssi/commit/157c686)
- Adaptation suite à la mise à jour d'Express :  l'application a été adaptée pour fonctionner correctement avec la dernière version d'Express. [#e5bdc47](https://github.com/betagouv/mon-profil-anssi/commit/e5bdc47)
- Utilisation de dépendances mineures :  l'application utilise désormais des dépendances mineures pour une meilleure stabilité. [#04726bb](https://github.com/betagouv/mon-profil-anssi/commit/04726bb)
