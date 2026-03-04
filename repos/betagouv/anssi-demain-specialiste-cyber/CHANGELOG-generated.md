## Changelog : anssi-demain-specialiste-cyber (30 derniers jours)

### Résumé
Ce changelog présente les récentes mises à jour du site web "DemainSpécialisteCyber". Les changements incluent des corrections de bugs, notamment concernant la gestion du cache et la soumission de jeux, ainsi que des mises à jour de sécurité pour corriger des vulnérabilités dans les dépendances du projet. Des améliorations techniques ont également été apportées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait le renvoi correct des résultats du cache en cas d'erreur avec Grist. [#62d1e8a](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/62d1e8a)
- Désactivation du bouton de soumission du formulaire de jeu pour éviter des soumissions involontaires ou incorrectes. [#459449e](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/459449e) et [#560b534](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/560b534)

### Évolutions techniques
- Mises à jour de sécurité de plusieurs dépendances pour corriger des vulnérabilités connues :
    - axios (version 1.13.5) [#8273d24](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/8273d24)
    - fast-xml-parser (versions 5.3.6 et 5.3.9) [#006d066](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/006d066) et [#291cad1](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/291cad1)
    - minimatch (version 3.1.4) [#ac190c9](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/ac190c9)
    - svelte (version 5.53.5) [#7508d77](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7508d77)
    - ajv (version 6.14.0) [#5cd8b58](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/5cd8b58)
    - qs (version 6.14.2) [#3cab849](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/3cab849)
    - rollup (version 4.59.0) [#200a496](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/200a496)
- Correction de vulnérabilités de dépendances. [#1090414](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/1090414)
- Utilisation de révisions précises pour les dépendances. [#511acf0](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/511acf0)
