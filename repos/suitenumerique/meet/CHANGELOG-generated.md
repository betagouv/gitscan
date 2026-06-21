## Changelog : meet (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout de fonctionnalités comme un sondage de satisfaction optionnel, des améliorations de l'accessibilité et la gestion des participants dans les grandes réunions. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment concernant la gestion des fichiers, la réduction du bruit et la sécurité. L'addon Outlook a été amélioré avec des fonctionnalités d'internationalisation et de feedback.

### Évolutions fonctionnelles
- Ajout d'un sondage de satisfaction optionnel en bas de la réunion. [#135b99a](https://github.com/suitenumerique/meet/commit/135b99a)
- Possibilité de masquer le bouton de connexion via un paramètre d'URL. [#70a296e](https://github.com/suitenumerique/meet/commit/70a296e)
- Possibilité de désactiver la connexion silencieuse via un paramètre d'URL. [#d4a7cf2](https://github.com/suitenumerique/meet/commit/d4a7cf2)
- Amélioration de la réduction du bruit avec un pipeline de traitement audio BBBA. [#13036f6](https://github.com/suitenumerique/meet/commit/13036f6)
- Mise en sourdine automatique des participants lors de l'entrée dans une grande réunion. [#040df0e](https://github.com/suitenumerique/meet/commit/040df0e)
- Désactivation du son de notification lors de l'entrée dans une grande salle. [#00e197b](https://github.com/suitenumerique/meet/commit/00e197b)
- Ajout d'une gestion spécifique des fichiers avec une interface d'administration dédiée. [#5602d25](https://github.com/suitenumerique/meet/commit/5602d25)
- Support étendu pour tous les types de fichiers vidéo/audio. [#ec688e7](https://github.com/suitenumerique/meet/commit/ec688e7)
- Ajout d'une fonctionnalité Picture-in-Picture (PiP) pour les réunions. [#4911a7c](https://github.com/suitenumerique/meet/commit/4911a7c)
- Amélioration de l'addon Outlook : support de l'internationalisation, lien de feedback, et amélioration de l'insertion de liens. [#85eff8a](https://github.com/suitenumerique/meet/commit/85eff8a)

### Évolutions techniques
- Mise à jour de `react-i18next` vers la version 17.0.8. [#16f4654](https://github.com/suitenumerique/meet/commit/16f4654)
- Optimisation du chargement de `@libreaudio/la-call` via un import dynamique. [#ac85a20](https://github.com/suitenumerique/meet/commit/ac85a20)
- Refactorisation de la gestion des variables d'environnement backend pour une meilleure organisation. [#cd19dea](https://github.com/suitenumerique/meet/commit/cd19dea)
- Amélioration de la robustesse du processus de suppression de fichiers. [#8d653b3](https://github.com/suitenumerique/meet/commit/8d653b3)
- Mise à jour des dépendances `idna`, `urllib3` et `core-js` pour corriger des failles de sécurité. [#f5a5fa9](https://github.com/suitenumerique/meet/commit/f5a5fa9), [#7b48537](https://github.com/suitenumerique/meet/commit/7b48537), [#13c7b9a](https://github.com/suitenumerique/meet/commit/13c7b9a)
- Amélioration de la configuration de la sécurité (CSP). [#53722ad](https://github.com/suitenumerique/meet/commit/53722ad)
- Utilisation de `uv.lock` pour la gestion des dépendances. [#b2d6d33](https://github.com/suitenumerique/meet/commit/b2d6d33)
- Amélioration de la gestion des erreurs et des états de fichiers. [#d13e3a8](https://github.com/suitenumerique/meet/commit/d13e3a8)
- Mise à jour de la version du chart Helm. [#dcfdd35](https://github.com/suitenumerique/meet/commit/dcfdd35), [#913d4f9](https://github.com/suitenumerique/meet/commit/913d4f9)

### Autres changements
- Améliorations de l'accessibilité des effets vidéo (aria labels, structure). [#fd1715b](https://github.com/suitenumerique/meet/commit/fd1715b), [#c9de7d0](https://github.com/suitenumerique/meet/commit/c9de7d0), [#6368b67](https://github.com/suitenumerique/meet/commit/6368b67), [#65789ef](https://github.com/suitenumerique/meet/commit/65789ef)
- Corrections de bugs mineurs et améliorations de la documentation.
- Mise à jour des dépendances JavaScript. [#553df50](https://github.com/suitenumerique/meet/commit/553df50)
- Ajout de tests pour la gestion des utilisateurs. [#22b2e6b](https://github.com/suitenumerique/meet/commit/22b2e6b)
- Ajout d'un job Kubernetes pour la fusion des utilisateurs en double. [#90f95ab](https://github.com/suitenumerique/meet/commit/90f95ab)
